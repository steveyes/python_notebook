#!/usr/bin/env bash
# word frequency count

if [ $# -ne 1 ]; then
    echo "Usage: $0 filename"

    exit 1
fi

filename=$1

grep -E -o "\b[[:alpha:]]+\>" "$filename" | awk '{count[$0]++} END {
    printf("%-20s%s\n","word","count");
    for(word in count) {
        printf("%-20s%d\n", word, count[word]);
    }
}'
