#! /usr/bin/env bash

CHECK_OUTPUT=$(/usr/bin/_discos-check-branch)
if [ -n "${CHECK_OUTPUT}" ]
then
    echo -e "${pur}WARNING:${txtrst} $CHECK_OUTPUT"
fi

source ~/.bashrc
