#!/bin/bash

cd /{{ discos_sw_dir}}/sdtools/quicklook/page
exec /usr/bin/SDTmonitor -c ../conf/monitor_config.ini {% if quicklook_polling %}--polling {% endif %}--nosave -w {{ quicklook_workers }} --http-server-port {{ quicklook_server_port }} {{ quicklook_directories | join(' ') }}
