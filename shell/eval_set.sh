#!/usr/bin/env bash

# Preserving Whitespace Using set and eval

items=
# append position args into $items and keep its double quotes
for i in "$@"
do
    items="$items \"$i\""
done

echo $items

set -x
set -- $items
set +x
echo $1
echo $2
echo $3
echo $4


echo '================================================='
set -x

# The set command takes any arguments after the options (here "--" signals the end of the options) and assigns them to the positional parameters ($0..$n).
# The eval command executes its arguments as a bash command.
# By passing the set command to eval bash will honor the embedded quotes in the string rather than assume they are part of the word.
eval set -- $items
set +x
echo $1
echo $2
echo $3
echo $4

echo '================================================='
# run this script with arguments: "1 2" "3 4", to see what will happen.
for i in "$@"
do
    echo $i
done