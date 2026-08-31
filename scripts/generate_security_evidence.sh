#!/usr/bin/env bash
set -euo pipefail
nosetests --with-spec --spec-color > evidence/security-headers-done 2>&1
