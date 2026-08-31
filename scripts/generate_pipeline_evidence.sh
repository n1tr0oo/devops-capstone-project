#!/usr/bin/env bash
set -euo pipefail
tkn pipelinerun logs --last > pipelinerun.txt
