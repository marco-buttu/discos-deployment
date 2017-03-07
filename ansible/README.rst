Examples
========

To deploy the whole Nuraghe's development infrastructure::

    $ ansible-playbook -i inventories/development site.yml --limit nuraghe

To deploy the whole Nuraghe's production infrastructure::

    $ ansible-playbook -i inventories/production site.yml --limit nuraghe

To deploy a particular play on Nuraghe, for instance `playfile.yml`::

    $ ansible-playbook -i inventories/development playfile.yml --limit nuraghe
