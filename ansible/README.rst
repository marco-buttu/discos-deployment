Examples
========

To deploy the whole Nuraghe's development infrastructure::

    $ ansible-playbook -i inventories/development site.yml -l nuraghe -e "cdb=SRT"

Here the switch ``-l`` means ``--limit`` and ``-e`` means ``--extra-vars``.

To deploy the whole Nuraghe's production infrastructure::

    $ ansible-playbook -i inventories/production site.yml -l nuraghe -e "cdb=SRT"

To deploy a particular play on Nuraghe, for instance `playfile.yml`::

    $ ansible-playbook -i inventories/development playfile.yml -l nuraghe
