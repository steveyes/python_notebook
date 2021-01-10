#!/usr/bin/env bash

# Each single character stands for an option.
# Non colon stands for nothing followed.
# A single colon (:) stands for that the option has a required argument or value.
# A double colon (::) stands for that the option has an optional argument e.g. none or value followed without blank space, in any case "shift 2" is required.

# Option strings
SHORT=ag::u:
LONG=all,group::,user:

OPTS=$(getopt --options $SHORT --long $LONG --name "$0" -- "$@")

if [ $? != 0 ]; then
    echo "Failed to parse options...terminating..."
    exit 1
fi

eval set -- "${OPTS}"

while true; do
    case "$1" in
        -a|--all)
            echo "all groups and users will be created..."
            shift
            ;;
        -g|--group)
            case "$2" in
                "")
                    echo "all groups will be created..."
                    shift 2
                    ;;
                *)
                    echo "only specified group: $2, and it's users will be created..."
                    shift 2
                    ;;
            esac
            ;;
        -u|--user)
            echo "user: $2, will be created..."
            shift 2
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "Internal error!"
            exit 1
            ;;
    esac
done

for arg in "$@"
do
    echo "processing $arg"
done