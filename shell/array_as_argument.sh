#!/usr/bin/env bash

function f1() {
    a=("$@")
    ((last_idx = ${#a[@]} - 1))
    b=${a[last_idx]}
    unset a[last_idx]

    for i in "${a[@]}"; do
        echo "$i"
    done
    echo "b: $b"
}

x=("one two" "LAST")
b='even more'

f1 "${x[@]}" "$b"
echo ===============

f1 "${x[*]}" "$b"
echo ---------------

function f2() {
    name=$1[@]
    a=("${!name}")
    b=$2

    for i in "${a[@]}"; do
        echo "$i"
    done
    echo "b: $b"
}

x=("one two" "LAST")
b='even more'

f2 x "$b"
