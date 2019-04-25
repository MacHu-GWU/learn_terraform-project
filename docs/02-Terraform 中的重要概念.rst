Terraform 中的重要概念
==============================================================================




Dependencies (依赖关系)
------------------------------------------------------------------------------

Reference: https://learn.hashicorp.com/terraform/getting-started/dependencies

有些资源必须要等其他资源被创建后才能被创建. 例如 Elastic IP 需要被绑定到 EC2 上, 所以要先创建 EC2, 再创建 EIP. 删除时反之.

Terraform 支持 隐示定义 和 显示定义 两种模式.

用 ``${<resource-type>.<resource-name>}`` 的方式是 ``隐示定义``.

.. code-block:: javascript

    resource "aws_instance" "example" {
      ami = "ami-b374d5a5"
      instance_type = "t2.micro"
    }
    
    resource "aws_eip" "ip" {
      instance = "${aws_instance.example.id}"
    }

用 ``depends_one = ["<resource-type>.<resource-name>"]`` 的方式是 ``显示定义``.

.. code-block:: javascript

    resource "aws_instance" "example" {
      ami = "ami-b374d5a5"
      instance_type = "t2.micro"
    }

    resource "aws_eip" "ip" {
      instance = "${aws_instance.example.id}"
      depends_on = ["aws_instance.example"]
    }


Provision (预分配)
------------------------------------------------------------------------------

Reference:

- 基础: https://learn.hashicorp.com/terraform/getting-started/provision
- 详细: https://www.terraform.io/docs/provisioners/index.html

当你创建完毕一个资源之后, 你可能需要调用一些外部命令对这个资源的信息进行一些处理, 例如将该资源的信息存入数据库, 或写入本地文件.

1. provision 发生在 Create 和 Destroy 之后. Apply 其实是由一串 Create / Destroy / Update 组成, 而其中的 Create / Destroy 会触发 provision.
2. provision 在执行 ``terraform`` 命令的机器上运行.
3. 一个资源可以有多个名字相同的 provision, 按照定义的顺序执行.

一些技巧: 比如你可以写一个 Python Script, 创建完某些资源后运行这个脚本, 执行一些复杂的命令.

如果 Create 成功, 但是对应的 Provision 却失败了, 则该资源会被标记为 tainted (受污染的), 下次运行 ``terraform apply`` 的时候会删除该资源. 因为 Provision 失败可能导致该资源出于 Incomplete Configured 的状态. 我们不能信任它.



Variable (变量)
------------------------------------------------------------------------------

Reference: https://learn.hashicorp.com/terraform/getting-started/variables

为了更好的复用 tf 脚本, 我们应该将具体的 数据 / 变量 和 逻辑 分开.

数据应该被保存在 ``variables.tf`` 文件中.

在运行 ``terraform`` 命令时指定参数:

.. code-block:: bash

    $ terraform apply \
      -var 'access_key=foo' \
      -var 'secret_key=bar'


在运行 ``terraform`` 命令时, 指定从 ``*.tfvars`` 文件中读取参数, ``*.tfvars`` 必须在执行 ``terraform`` 命令的目录下:

.. code-block:: javascript

    # content of secret.tfvars
    access_key = "foo"
    secret_key = "bar"

``production.tfvars`` is similar.

.. code-block:: bash

    $ terraform apply \
        -var-file="secret.tfvars"
        -var-file="production.tfvars"

在运行 ``terraform`` 命令时, 如果有些变量以上两种方法都找不到值, 则会自动从环境变量中读取参数 (注意, 此方法只适用于字符串变量, 对于列表和字典类型的变量, 无法使用环境变量的方法). 例如: 如果找不到 ``access_key`` 变量, 则会去 ``TF_VAR_access_key`` 环境变量中寻找.



重要命令
------------------------------------------------------------------------------

Reference: https://www.terraform.io/docs/commands/index.html

- ``terraform init``: 初始化, 为你安装各个 provider 对应的插件. 例如你主要用的 AWS 服务, 安装完 terraform 后是没有 AWS 的插件的, 这个命令于是会为你自动安装.
- ``terraform plan``:
- ``terraform apply``:
- ``terraform show``:
- ``terraform destroy``:

Note: 在命令行中设置 ``$ alias tf="terraform"``, 然后你就可以 ``tf plan``, ``tf apply``, ``tf destroy`` 了.
