HOW TO MAKE THE SYSTEM
======================
To provision discos_srt, development environment, and deploy
DISCOS master branch::

  $ ./make discos_srt:development

To provision discos_srt, production environment, and deploy
DISCOS latest stable version::

  $ ./make discos_srt:production

.. note:: The option ``discos_srt:development`` will deploy
   the DISCOS *master* branch.  This is the default behavior
   for the development environment.  When in development,
   if you want to specify another DISCOS version, you have to
   use the ``--version`` switch, as you will see in a moment.
   The option ``discos_srt:production`` will deploy the DISCOS
   *latest stable* version.  This is the default behavior
   for the production environment.  When in production,
   if you want to specify another DISCOS version, you have to
   use the ``--version`` switch and also the ``--force``
   switch , as you will see later.

To provision discos_medicina, development environment, and deploy
DISCOS master branch::

  $ ./make discos_medicina:development

To provision manager, development environment, and deploy
DISCOS master branch, for SRT::

  $ ./make manager:development --station SRT

To provision discos_srt, development environment, and deploy
DISCOS version 0.6::

  $ ./make discos_srt:development --version 0.6

To provision discos_srt, development environment, and deploy
DISCOS latest stable version::

  $ ./make discos_srt:development --version latest

To deploy DISCOS latest stable version on discos_srt development
environment, without provisioning::

  $ ./make discos_srt:development --only deploying --version latest

To deploy DISCOS master version on discos_srt development
environment, without provisioning::

  $ ./make discos_srt:development --only deploying

To provision discos_srt development environment, without deploying
DISCOS::

  $ ./make discos_srt:development --only provisioning

The following configuration raises an error, because
only the latest stable version is allowed in production::

       $ ./make discos_srt:production --version master

When in production, if you want to force a version
different than the latest one, you have to use the ``--force``
switch::

  $ ./make discos_srt:production --version master --force
