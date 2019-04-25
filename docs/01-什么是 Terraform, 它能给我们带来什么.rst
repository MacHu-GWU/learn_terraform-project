什么是 Terraform, 它能给我们带来什么
==============================================================================

Terraform 是 Hashicorp 公司的一款软件, 也是 H 公司开发的一套跟 Json 很相似的配置语言. 用纯文本的 Terraform Script 可以定义云设施系统中所有用到的资源, 例如虚拟机, 数据库, 云存储, 消息队列, 日志服务器等等. 也可以用来定义这些资源的详细配置, 以及相互依赖关系. 有了 tf 脚本, 我们就可以方便地一键, 或者自动化云系统的创建, 更新, 销毁. tf 当然算是 Infrastructure as Code (IAC) 语言的一种.

现在的的云服务提供商非常多, 比较大的有 亚马逊的 AWS, 微软的 Azure, 谷歌的 Google Cloud Platform. 各家用于定义云设置的脚本语言标准都不一样, 例如 AWS 用的 Cloudformation, Azure 用的 Azure Resource Manager (ARM) Template. 而 Terraform 则是建立在这些之上的更高层的抽象. 只需要掌握 Terraform, 就不用学各个云服务提供商的专用 IAC 语言了.
