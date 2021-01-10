#!/usr/bin/env bash


curl -X POST \
--header "Content-Type: application/json" \
--header "Accept: application/json" \
"http://192.168.1.104/api/authentication/login?phone=12332101278&smscode=123456"