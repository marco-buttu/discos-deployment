#!/bin/bash

cd /{{ discos_sw_dir }}/sdtools/quicklook
SDTmonitor -c monitor_config.ini --polling --nosave /archive/data/
