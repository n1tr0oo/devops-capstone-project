# DevOps Capstone: Customer Accounts Microservice

![CI Build](https://github.com/n1tr0oo/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)

Flask REST microservice for creating, listing, reading, updating, and deleting customer accounts.

## Features and API

- SQLite locally; optional PostgreSQL through `DATABASE_URI` (PostgreSQL default port: `5432`).
- CORS and Flask-Talisman security headers.
- `POST /accounts` (201), `GET /accounts` (200), `GET /accounts/<id>` (200/404), `PUT /accounts/<id>` (200), `DELETE /accounts/<id>` (204), and `GET /health`.

## Install, run, and test

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
curl http://127.0.0.1:8000/accounts
flake8 service tests --show-source
nosetests --with-spec --spec-color
```

The server listens on `0.0.0.0:8000`. `make install`, `make lint`, `make test`, and `make run` provide shortcuts. GitHub Actions runs lint and tests on every push and pull request. The badge points to this repository's CI workflow. Save real CI logs with `gh run view RUN_ID --log > evidence/ci-workflow-done`.

Local HTTP is enabled by default; set `FORCE_HTTPS=true` behind a TLS-aware production proxy.

## Docker and IBM Container Registry

```bash
docker build -t accounts:1 .
docker images
docker tag accounts:1 us.icr.io/$SN_ICR_NAMESPACE/accounts:1
docker push us.icr.io/$SN_ICR_NAMESPACE/accounts:1  # only after authentication
```

## Kubernetes

Replace `YOUR_NAMESPACE` in `deploy/deployment.yaml`, then run:

```bash
kubectl apply -f deploy/deployment.yaml
kubectl apply -f deploy/service.yaml
kubectl port-forward service/accounts 8080:8080
curl http://127.0.0.1:8080/accounts | tee evidence/kube-app-output
oc describe secret postgresql
```

Use `scripts/generate_kube_evidence.sh` for real image and cluster evidence.

## Tekton CD

Install compatible Catalog tasks listed in `tekton/tasks/README.md`, replace pipeline-run placeholders, then:

```bash
kubectl apply -f tekton/pipeline.yaml
kubectl create -f tekton/pipeline-run.yaml
tkn pipeline start accounts-cd --showlog \
  -p repo-url=https://github.com/n1tr0oo/devops-capstone-project.git -p branch=main \
  -p app-name=accounts -p build-image=us.icr.io/YOUR_NAMESPACE/accounts:1 \
  -w name=source,claimName=YOUR_PVC
bash scripts/generate_pipeline_evidence.sh
```

The pipeline sequence is clone → lint → tests → build → deploy.

## Git and evidence

This checkout uses repository-local author `n1tr0oo`. To publish:

```bash
git add .
git commit -m "Initial Customer Accounts capstone implementation"
git remote add origin https://github.com/n1tr0oo/devops-capstone-project.git
git push -u origin main
# Assignment branch example: git push --set-upstream origin add-kubernetes
```

Do not commit invented evidence. See `evidence/` for the exact 33-task mapping and screenshot guidance.
