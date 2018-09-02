#!/bin/bash

function discos-deploy()
{
    python $(dirname $BASH_SOURCE)/discos-deploy $@
}

function discos-login()
{
    bash $(dirname $BASH_SOURCE)/discos-login $@
}

function discos-vms()
{
    python $(dirname $BASH_SOURCE)/discos-vms $@
}

function discos-vnc()
{
    python $(dirname $BASH_SOURCE)/discos-vnc $@
}
