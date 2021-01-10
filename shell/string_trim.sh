#!/usr/bin/env bash

file="t_dict_city.sql.bak.2100-01-01"

## trim from left to right

# trim only one times
file_suffixes=${file#*.}
echo $file_suffixes

# trim as many times as possible
date=${file##*.}
echo $date

## trim from right to left

# trim only one times
file_without_date=${file%.*}
echo $file_without_date

# trim as many times as possible
table=${file%%.*}
echo $table
