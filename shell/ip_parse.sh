#!/usr/bin/env bash

mask2cidr() {
  typeset -A octets=([255]=8 [254]=7 [252]=6 [248]=5 [240]=4 [224]=3 [192]=2 [128]=1 [0]=0)
  local nbits

  while read -rd '.' dec; do
    [[ -z ${octets[$dec]} ]] && echo "Error: $dec is not recognised" && exit 1
    ((nbits += ${octets[$dec]}))
    [[ $dec -lt 255 ]] && break
  done <<<"${1}."

  echo "$nbits"
}

cidr2mask() {
  local mask=""
  local n_octets=$(($1 / 8))
  local octet_partial=$(($1 % 8))
  for ((i = 0; i < 4; i++)); do
    if [ "$i" -lt $n_octets ]; then
      mask+=255
    elif [ "$i" -eq $n_octets ]; then
      mask+=$((256 - 2 ** (8 - octet_partial)))
    else
      mask+=0
    fi
    test "$i" -lt 3 && mask+=.
  done

  echo $mask
}

get_net() {
  local IFS='.' ip i
  local -a oct mask

  read -ra oct <<<"$1"
  read -ra mask <<<"$2"

  for i in ${!oct[@]}; do
    ip+=("$((oct[i] & mask[i]))")
  done

  echo "${ip[*]}"
}

get_broad() {
  local IFS='.' ip i
  local -a oct mask

  read -ra oct <<<"$1"
  read -ra mask <<<"$2"

  for i in ${!oct[@]}; do
    ip+=("$((oct[i] + (255 - (oct[i] | mask[i]))))")
  done

  echo "${ip[*]}"
}

mask2cidr_v2() {
  local x=${1##*255.}
  set -- "0^^^128^192^224^240^248^252^254^" $(((${#1} - ${#x}) * 2)) "${x%%.*}"
  local y=${1%%$3*}
  echo $(($2 + (${#y} / 4)))
}

mask2cidr_v3() {
  local m="$1"
  local mn=${m##*255.}
  local x=$(((${#m} - ${#mn}) * 2))

  local quods="0^^^^^^^128^^^^^192^^^^^224^^^^^240^^^^^248^^^^^252^^^^^254^^^^^"
  local mnn=${mn%%.*}
  local yy=${quods%%$mnn*}
  local y=$((${#yy} / 8))

  echo $((x + y))
}

cidr2mask_v2() {
  set -- $((5 - ($1 / 8))) 255 255 255 255 $(((255 << (8 - ($1 % 8))) & 255)) 0 0 0
  [ $1 -gt 1 ] && shift $1 || shift
  echo ${1-0}.${2-0}.${3-0}.${4-0}
}

cidr2mask_v3() {
  local IFS='.'
  local cidr=$1
  local n255=$((cidr / 8))
  local oct="$(((255 << (8 - ($((cidr % 8)) % 8))) & 255))"

  local -a octs
  while true; do
    [[ $((n255--)) -le 0 ]] && break
    octs+=("255")
  done

  octs+=("$oct")

  echo ${octs[0]-0}.${octs[1]-0}.${octs[2]-0}.${octs[3]-0}
}

#mask2cidr_v2 "255.255.192.0"
#mask2cidr_v3 "255.255.192.0"
#cidr2mask_v2 18
#cidr2mask_v3 18
