#!/bin/bash
# src/templates directory needs to be copied to current directory

grfblocks --bc-path <path-to-node-data-dir>/lmdb \
    --testnet \
    --deamon-url=localhost:28981 \
    --enable-emission-monitor

