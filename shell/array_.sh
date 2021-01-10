#!/usr/bin/env bash
#

arr=("one" "two")

wrong_demo() {
    cnt=0
    for i in "${arr[*]}"; do
        ((cnt++))
        echo ${i}
        echo $cnt
    done
}

echo

right_demo() {
    cnt=0
    for i in "${arr[@]}"; do
        ((cnt++))
        echo ${i}
        echo $cnt
    done
}

# "${arr[@]}" leads to each element of the array being treated as a separate shell-word,
# while "${arr[*]}" results in a single shell-word with all of the elements of the array separated by spaces,