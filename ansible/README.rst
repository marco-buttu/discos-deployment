Examples
========

To deploy the whole Nuraghe's development infrastructure::

    $ ansible-playbook -i inventories/development all.yml -l nuraghe -e "cdb=SRT"

Here the switch ``-l`` means ``--limit`` and ``-e`` means ``--extra-vars``.
To deploy one single machine, just give the machine name to the limit switch.
For instance, to deploy discos-mng for SRT::

    $ ansible-playbook -i inventories/development all.yml -l discos-mng -e "cdb=SRT"

To deploy the whole Nuraghe's production infrastructure::

    $ ansible-playbook -i inventories/production all.yml -l nuraghe -e "cdb=SRT"

To deploy a particular play on Nuraghe, for instance `playfile.yml`::

    $ ansible-playbook -i inventories/development playfile.yml -l nuraghe

To provision only, withoud taking care of discos::

    $ ansible-playbook -i inventories/development all.yml -l nuraghe -e "cdb=SRT" -t provisioning

deploy a particular play on Nuraghe, for instance `playfile.yml`::
