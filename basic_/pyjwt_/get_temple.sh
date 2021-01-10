#!/usr/bin/env bash


token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3d3cuY2hla2F3YS5jb20iLCJpYXQiOjE1NDE4NDkwNDQsImV4cCI6MTU0MjQ1Mzg0NCwicGhvbmUiOiIxMjMzMjEwMTI3OCIsInVpZCI6IjEyNzgifQ.D7TXnE7o9ugG-4KjxQZYKxfBupKSx9vTBkDsaZcssjA'
#token='Bearer AiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3d3cuY2hla2F3YS5jb20iLCJpYXQiOjE1NDE4NDkwNDQsImV4cCI6MTU0MjQ1Mzg0NCwicGhvbmUiOiIxMjMzMjEwMTI3OCIsInVpZCI6IjEyNzgifQ.D7TXnE7o9ugG-4KjxQZYKxfBupKSx9vTBkDsaZcssjA'

curl -X GET \
    --header "Authorization: ${token}" \
    --header "Accept: application/json" \
    "http://192.168.1.104/api/temple/1278"