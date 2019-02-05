#! /usr/bin/env bash

if [ -f $HOME/bin/_discos-check-branch ]; then
	CHECK_OUTPUT=$($HOME/bin/_discos-check-branch)
	if [ -n "${CHECK_OUTPUT}" ]; then
		echo -e "${pur}WARNING:${txtrst} $CHECK_OUTPUT"
	fi
fi

# Load DISCOS environment
# =======================
if [ -f /{{ discos_sw_dir }}/config/misc/load_branch ]; then
    source /{{ discos_sw_dir }}/config/misc/load_branch
fi

# Load ACS definitions
# ====================
if [ -f /{{ discos_sw_dir }}/config/acs/.bash_profile.acs ]; then
    source /{{ discos_sw_dir }}/config/acs/.bash_profile.acs
fi

export ACS_TMP=/service/acstmp/{{ inventory_hostname_short }}

if [ -n "${DISCOS_BRANCH}" ]; then
    if [ -z "${STATION}" ]; then
        if [ -f $INTROOT/.station ]; then
            source $INTROOT/.station
        else
            echo -e "${pur}WARNING:${txtrst} STATION is unset, cannot set the ACS_CDB!"
            unset ACS_CDB
            return
        fi
    fi

    if [ $CDB = "test" ]; then
        export ACS_CDB=/{{ discos_sw_dir }}/{{ user.name }}/$DISCOS_BRANCH/$STATION
    else
        export ACS_CDB=/{{ discos_sw_dir }}/{{ user.name }}/$DISCOS_BRANCH/$STATION/Configuration
    fi
fi

# Set the prompt
# ==============
red='\e[1;31m'  # Red
grn='\e[1;32m'  # Green
cyn='\e[1;36m'  # Cyan
pur='\e[1;35m'  # Purple
txtrst='\e[0m'  # Text Reset
if [ -n "${DISCOS_BRANCH}" ]; then
    PS1="(\[$grn\]$DISCOS_BRANCH\[$txtrst\]:\[$cyn\]$CDB\[$txtrst\]) \u@\h \w $ "
else
    PS1="(\[$red\]branch?\[$txtrst\]) \u@\h \w $ "
fi
