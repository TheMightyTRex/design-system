#!/usr/bin/env bash
# Tests penpot/plugin.js in SES, the sandbox Penpot runs plugins in, against a stand-in for Penpot:
# penpot/test.sh. Run it after penpot/make.py and before every push. Needs Docker.
set -euo pipefail
cd "$(dirname "$0")/.."
docker run --rm -u "$(id -u):$(id -g)" -e HOME=/tmp -v "$PWD:/w:ro" mcr.microsoft.com/playwright:v1.63.0-noble \
  sh -c "npm i --silent --prefix /tmp/ses ses@1.10.0 >/dev/null 2>&1 && node /w/penpot/test-sandbox.mjs" 2>&1 | grep -v "Removing intrinsics"
