#!/bin/bash

cd /{{ discos_sw_dir}}/sdtools/quicklook/page
exec /usr/bin/SDTmonitor -c ../conf/monitor_config.ini {% if quicklook_polling %}--polling {% endif %}-w {{ quicklook_workers }} {{ quicklook_directories | join(' ') }}
