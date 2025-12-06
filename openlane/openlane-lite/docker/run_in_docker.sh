#!/bin/bash
docker run -it --rm \
    -v $(pwd):/workspace \
    -w /workspace \
    efabless/openlane:2023.02.23 \
    /bin/bash
