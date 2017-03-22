HOW TO MAKE THE SYSTEM
======================
To provision nuraghe, development environment, and deploy
DISCOS master branch::

  $ ./make nuraghe:development

To provision nuraghe, production environment, and deploy
DISCOS latest stable version::

  $ ./make nuraghe:production

.. note:: The option ``nuraghe:development`` will deploy
   the DISCOS *master* branch.  This is the default behavior
   for the development environment.  When in development,
   if you want to specify another DISCOS version, you have to
   use the ``--version`` switch, as you will see in a moment.
   The option ``nuraghe:production`` will deploy the DISCOS
   *latest stable* version.  This is the default behavior
   for the production environment.  When in production,
   if you want to specify another DISCOS version, you have to
   use the ``--version`` switch and also the ``--force``
   switch , as you will see later.

To provision escs, development environment, and deploy
DISCOS master branch::

  $ ./make escs:development

To provision discos-mng, development environment, and deploy
DISCOS master branch, for SRT::

  $ ./make discos-mng:development --station SRT

To provision nuraghe, development environment, and deploy
DISCOS version 0.6::

  $ ./make nuraghe:development --version 0.6

To provision nuraghe, development environment, and deploy
DISCOS latest stable version::

  $ ./make nuraghe:development --version latest

To deploy DISCOS latest stable version on nuraghe development
environment, without provisioning::

  $ ./make nuraghe:development --only deploying --version latest

To deploy DISCOS master version on nuraghe development
environment, without provisioning::

  $ ./make nuraghe:development --only deploying

To provision nuraghe development environment, without deploying
DISCOS::

  $ ./make nuraghe:development --only provisioning

The following configuration raises an error, because
only the latest stable version is allowed in production::

       $ ./make nuraghe:production --version master

When in production, if you want to force a version
different than the latest one, you have to use the ``--force``
switch::

  $ ./make nuraghe:production --version master --force
