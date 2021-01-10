#!/usr/bin/env bash

echo $IFS

YELLOW_COLOR='\E[1;33m'
RED_COLOR='\E[1;31m'
RES='\E[0m'

echo -e "${YELLOW_COLOR}choose the option which you want to ssh: ${RES}"
echo -e "${RED_COLOR}or <Ctrl-D> to exit ${RES}"

select var in $(awk '/^Host / {print $2}' ~/.ssh/config); do
    ssh "$var"
done
