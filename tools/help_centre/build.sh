#!/usr/bin/env bash
# Builds an app's help centre in a Python container, for a computer without pip. Run from the app's folder:
#   <design-system>/tools/help_centre/build.sh [out folder, default _site]
set -euo pipefail
ds="$(cd "$(dirname "$0")/../.." && pwd)"
out="$(realpath -m "${1:-_site}")"; mkdir -p "$out"
docker run --rm -u "$(id -u):$(id -g)" -e HOME=/tmp -v "$ds:/ds:ro" -v "$PWD:/app:ro" -v "$out:/out" -w /app python:3.12-slim \
  sh -c "pip install -q --no-warn-script-location --user markdown==3.7 pymdown-extensions==10.9 2>/dev/null && python /ds/tools/help_centre/build.py --out /out"
