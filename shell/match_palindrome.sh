#!/usr/bin/env bash
# file: match_palindrome.sh

arg1=$1

hello

string=${arg1:-"malayalam"}

if [[ "$string" == "$(echo $string | rev)" ]]; then
    echo "Palindrome"
else
    echo "Not Palindrome"
fi
