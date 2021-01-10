#!/usr/bin/env bash


token='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3d3cuY2hla2F3YS5jb20iLCJpYXQiOjE1NDE4NDkwNDQsImV4cCI6MTU0MjQ1Mzg0NCwicGhvbmUiOiIxMjMzMjEwMTI3OCIsInVpZCI6IjEyNzgifQ.D7TXnE7o9ugG-4KjxQZYKxfBupKSx9vTBkDsaZcssjA'


curl -X POST \
--header "Content-Type: multipart/form-data" \
--header "Accept: application/json" \
--header "Authorization: ${token}" \
-d "{
  \"name_bo\": \"དང་ལེན་དགོན་པ\",
  \"manager_phone\": \"12345678900\",
  \"operator_name\": \"alice\",
  \"operator_phone\": \"12345678901\",
  \"password\": \"123456\",
  \"history\": \" 甘川交界的群山峻岭之间，有着一座凡间净土热尔寺，这座藏传佛教格鲁派寺院创建于1712年，是当时热尔部落首领热·绰甲为邀请第二世卓仓喇嘛罗让丹贝坚参来热尔地区讲经说法而修建。热尔寺是纳木格尔登寺院的第一子寺，极具特色的建筑风格与蓝天、草原和谐呼应在一起，在这里浓郁的藏地风情、优美的自然风光让人不禁有走近它的冲动。\"
}" "http://192.168.1.104/api/temple/json/1278"
