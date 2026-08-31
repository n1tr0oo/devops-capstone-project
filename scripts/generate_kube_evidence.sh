#!/usr/bin/env bash
set -euo pipefail
docker images accounts:1 --format $'Name: {{.Repository}}\nTag: {{.Tag}}\nImage ID: {{.ID}}\nCreated Time: {{.CreatedSince}}\nSize: {{.Size}}' > evidence/kube-images
{
  echo '=== DEPLOYMENTS ==='; kubectl get deployments; echo
  echo '=== PODS ==='; kubectl get pods; echo
  echo '=== REPLICA SETS ==='; kubectl get rs; echo
  echo '=== SERVICES ==='; kubectl get services
} > evidence/kube-deploy-accounts
