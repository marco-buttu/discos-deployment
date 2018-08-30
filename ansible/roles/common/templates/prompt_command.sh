#! /usr/bin/env bash

if [ -f $HOME/bin/_discos-check-branch ]; then
	CHECK_OUTPUT=$($HOME/bin/_discos-check-branch)
	if [ -n "${CHECK_OUTPUT}" ]; then
		echo -e "${pur}WARNING:${txtrst} $CHECK_OUTPUT"
	fi
fi

source ~/.bashrc
