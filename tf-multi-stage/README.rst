**Setup**:

1. store your terraform variable data in ``${HOME}/<config-filename>.json``:

.. code-block:: javascript

    {
        "dev": {
            "profile": "test",
            ...
        },
        "test": {
            ...
        },
        "qa": {
            ...
        },
        "stage": {
            ...
        },
        "prod": {
            ...
        }
    }

2. Edit the ``switch-stage.py`` file change this line:

.. code-block:: python

    CONFIG_JSON_FILENAME_AT_HOME = "<config-filename>.json"

3. Put following code in your shell initiation script ``~/.bashrc``, ``~/.bash_profile``, ``~/.zshrc``, etc ...

.. code-block:: bash

    alias tf='terraform'
    alias tfplan='terraform plan -var-file=var.json'
    alias tfapply='terraform apply -var-file=var.json'
    alias tfdestroy='terraform destroy -var-file=var.json'

then you can use the shortcut ``tfplan``, ``tfapply``, ``tfdestroy``.

**Usage**:

1. Switch to the stage:

.. code-block:: bash

    python switch-stage.py dev|test|qa|stage|prod

2. Run terraform command:

    $ tfplan ... other option expect -var-file
    $ tfapply ...
    $ tfdestroy ...
