# Tekton task prerequisites

Install compatible `git-clone`, `flake8`, `buildah`, and `kubernetes-actions` Catalog tasks before starting the pipeline. The assignment's example is:
`kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/main/task/flake8/0.1/flake8.yaml`.
Catalog versions can change, so verify workspace and parameter names against the installed versions.
