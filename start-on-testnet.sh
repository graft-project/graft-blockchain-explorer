#!/bin/bash
# src/templates directory needs to be copied to current directory

xmrblocks --bc-path <path-to-node-data-dir>/lmdb \
    --testnet \
    --deamon-url=52.88.171.144:28981 \
    --enable-emission-monitor

