#!/bin/bash
set -e

DESIGN=$1

if [ -z "$DESIGN" ]; then
    echo "Usage: ./run_flow.sh <design>"
    exit 1
fi

docker run -it --rm \
    -v $(pwd):/workspace \
    -w /workspace \
    efabless/openlane:2023.02.23 \
    bash -c "
        cd designs/$DESIGN && \
        flow.tcl -design . -overwrite -config config.tcl
    "
