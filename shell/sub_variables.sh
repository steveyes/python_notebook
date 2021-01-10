#!/usr/bin/env bash

HOST_PROD="1.1.1.1"
HOST_TEST="192.168.1.101"

read -p "input the MODE(PROD/TEST): " MODE

server_name="$(
    tmp=HOST_${MODE}
    echo -n ${!tmp}
)"
echo $server_name

server_name="$(eval echo \${HOST_${MODE}})"
echo $server_name
