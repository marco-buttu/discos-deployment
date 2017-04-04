*****************
DISCOS Deployment
*****************

To provision a *large* system, that is a system composed
of three machines (``manager``, ``as`` and ``ms``), use
the following command::

  $ ./build large:development

This command will connect via SSH to all development machines
and provision the whole system (users, networking, yum
packages, ACS and its dependencies, utilities, and
enventually the DISCOS dependencies.  It does not deploy
DISCOS.

To deploy DISCOS using the ``build`` script::

  $ ./build large:development --deploy srt_0.1

This command clones the ``srt_0.1`` branch (from the
**public** DISCOS repository) into the ``discos`` home
directory of all machines of the system.  It also creates
and loads the environment.

You can deploy as many branches as you want::

  $ ./build large:development --deploy master --station srt

This command deploys the ``master`` branch and configures
it for the SRT station.

You can also provision or deploy a single machine. For instance,
in the following case you are only deploying the ``manager``
machine::

  $ ./build manager:development --deploy medicina-0.1

The development environment allows you to easily create branches
and move from one branch to another.  For instance, let's give
the following command::

  $ ./build manager:development

If we go to the ``manager`` machine, we see that its prompt is::

  (branch?) discos@manager ~ $

That is becouse there is no active branch yet.  To get and activate
a branch, we use the ``discos-get`` command::

    $ discos-get srt_0.1
    Cloning into 'srt_0.1'...
        ...
    Repository cloned into /home/discos/srt_0.1
    Introot created into /home/discos/srt_0.1
    (srt_0.1:telescope) discos@manager ~ $

As you can see, the ``branch?`` text is now replaced by
``srt_0.1:telescope``.  The first item (``srt_0.1``) indicates
that the active branch is ``srt_0.1``.  In fact we have::

    (srt_0.1:telescope) discos@manager ~ $ echo $ACS_CDB
    /home/discos/srt_0.1/SRT/Configuration
    (srt_0.1:telescope) discos@manager ~ $ echo $INTROOT
    /home/discos/srt_0.1/introot
    (srt_0.1:telescope) discos@manager ~ $ echo $STATION
    SRT

The second item, ``telescope``, means that the *telescope*
CDB is set.  The ``discos-set`` command allows us to change
the CDB from ``telescope`` to ``test`` and viceversa::

    (srt_0.1:telescope) discos@manager ~ $ discos-set srt_0.1 --cdb test
    (srt_0.1:test) discos@manager ~ $ echo $ACS_CDB
    /home/discos/srt_0.1/SRT
    (srt_0.1:test) discos@manager ~ $ discos-set srt_0.1 --cdb telescope
    (srt_0.1:telescope) discos@manager ~ $ echo $ACS_CDB
    /home/discos/srt_0.1/SRT/Configuration

We can also create other branches and move from one branch to another::

    $ discos-get medicina_0.1
    Cloning into 'medicina_0.1'...
        ...
    Repository cloned into /home/discos/medicina_0.1
    Introot created into /home/discos/medicina_0.1
    $ ls
    medicina_0.1  srt_0.1
    (medicina_0.1:telescope) discos@manager ~ $ discos-set srt_0.1
    (srt_0.1:telescope) discos@manager ~ $

When a branch is active but you are inside another branch,
you will see a warning message::

    (srt_0.1:telescope) discos@manager ~ $ cd medicina_0.1/
    WARNING: you are in 'medicina_0.1', but the active branch is 'srt_0.1'
    (srt_0.1:telescope) discos@manager ~/medicina_0.1 $
