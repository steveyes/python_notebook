#!/bin/bash

eth=$1

echo -e "$(date +%k:%M:%S)\trx_diff\ttx_diff" | column -t

while true; do
  rx_prev=$(cat /proc/net/dev | grep $eth | awk '{print $2}')
  tx_prev=$(cat /proc/net/dev | grep $eth | awk '{print $10}')
  sleep 1
  rx_next=$(cat /proc/net/dev | grep $eth | awk '{print $2}')
  tx_next=$(cat /proc/net/dev | grep $eth | awk '{print $10}')

  rx_diff=$((${rx_next} - ${rx_prev}))
  tx_diff=$((${tx_next} - ${tx_prev}))

  if [[ $rx_diff -le 1024 ]]; then
    rx_diff="${rx_diff}B/s"
  elif [[ $rx_diff -ge 1048576 ]]; then
    rx_diff=$(printf "%0.2f" $((rx_diff / 1048576)))"MB/s"
  else
    rx_diff=$(printf "%0.2f" $((rx_diff / 1024)))"KB/s"
  fi

  if [[ $tx_diff -le 1024 ]]; then
    tx_diff="${tx_diff}B/s"
  elif [[ $tx_diff -ge 1048576 ]]; then
    tx_diff=$(printf "%0.2f" $(($tx_diff / 1048576)))"MB/s"
  else
    tx_diff=$(printf "%0.2f" $(($tx_diff / 1024)))"KB/s"
  fi

  echo -e "$eth\t$rx_diff\t$tx_diff" | column -t
done
