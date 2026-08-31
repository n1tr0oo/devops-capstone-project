# Evidence

Only real command output and genuine screenshots belong here. Scripts in `scripts/` generate local evidence. For CI use `gh run list`, then `gh run view RUN_ID --log > evidence/ci-workflow-done`. For the Kubernetes response, run `kubectl port-forward service/accounts 8080:8080`, then `curl http://127.0.0.1:8080/accounts | tee evidence/kube-app-output`.
