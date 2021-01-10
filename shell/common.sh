#!/usr/bin/env bash

alert() {
  # usage: alert <$?> <MESSAGE>
  if [[ -z "$DEBUG" ]] || [[ "$DEBUG" -eq 0 ]]; then
    return
  fi
  local RET_CODE="$1"
  local MESSAGE="$2"
  if [[ "$RET_CODE" -ne 0 ]]; then
    echo "WARNING: $MESSAGE failed with a return code of $RET_CODE." >&2
    [[ "$DEBUG" -gt 9 ]] && {
      echo "$DEBUG greater than 9"
      exit "$RET_CODE"
    }
  else
    echo "INFO: $MESSAGE successful." >&2
  fi
}

evenodd() {
  local LAST
  LAST=$(echo $1 | sed 's/^.*\(.\)$/\1/')
  case $LAST in
  0 | 2 | 4 | 6 | 8)
    return 0
    ;;
  1 | 3 | 5 | 7 | 9)
    return 1
    ''
    ;;
  *)
    echo "not digit, exiting..."
    exit 1
    ;;
  esac
}

is_root() {
  [[ $(id -u) -eq 0 ]] && return || {
    echo "must be run as root"
    return 1
  }
}

is_alive() {
  local NODE="$1"
  ping -c 3 $NODE >/dev/null 2>&1
  [[ $? -eq 0 ]] && return 1 && return 0
}

main() {
  local REAL_NAME
  local RUNTIME_NAME
  local BASE_NAME
  REAL_NAME="common.sh"
  RUNTIME_NAME="$(realpath $0)"
  BASE_NAME="$(basename $RUNTIME_NAME)"

  if [[ "$BASE_NAME" == '-bash' ]]; then
    return
  elif [[ "$BASE_NAME" == "$REAL_NAME" ]]; then
    echo "WARNING: this library should be sourced rather than executed directly"
    return 1
  else
    echo "ERROR: ambiguous name: '$BASE_NAME'"
  fi
}

main
