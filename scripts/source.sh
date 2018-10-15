#!/bin/bash

function discos-deploy()
{
    $(dirname $BASH_SOURCE)/discos-deploy $@
}

function discos-login()
{
    $(dirname $BASH_SOURCE)/discos-login $@
}

function discos-vms()
{
    $(dirname $BASH_SOURCE)/discos-vms $@
}

function discos-vnc()
{
    $(dirname $BASH_SOURCE)/discos-vnc $@
}
