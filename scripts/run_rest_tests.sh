#!/usr/bin/env bash
set -euo pipefail
base="${BASE_URL:-http://127.0.0.1:8000}"
mkdir -p evidence
run() { file="$1"; shift; { printf '$ '; printf '%q ' "$@"; printf '\n'; "$@"; } > "evidence/$file" 2>&1; }
run rest-create-done curl -i -X POST "$base/accounts" -H 'Content-Type: application/json' -d '{"name":"John Doe","email":"john@example.com","address":"Astana","phone_number":"+77000000000"}'
run rest-list-done curl -i "$base/accounts"
run rest-read-done curl -i "$base/accounts/1"
run rest-update-done curl -i -X PUT "$base/accounts/1" -H 'Content-Type: application/json' -d '{"name":"John Updated","email":"john.updated@example.com","address":"Astana","phone_number":"+77000000001"}'
run rest-delete-done curl -i -X DELETE "$base/accounts/1"
