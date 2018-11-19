#!/bin/bash

cd /{{ discos_sw_dir}}/sdtools/quicklook/page
exec /usr/bin/SDTmonitor -c ../conf/monitor_config.ini --polling --nosave {{ quicklook_directories | join(' ') }}
