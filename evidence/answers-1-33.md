# Готовые ответы для заданий 1–33

Этот файл предназначен для копирования ответов в Coursera. Текст в угловых скобках (`<...>`) заменяется реальными данными. Не вставляйте выдуманные логи или скриншоты.

## Task 1

**Ответ (URL):**

```text
https://github.com/n1tr0oo/assik1/blob/main/README.md
```

CI badge уже настроен на репозиторий `n1tr0oo/assik1`.

## Task 2

**Ответ (URL):**

```text
https://github.com/n1tr0oo/assik1/blob/main/.github/ISSUE_TEMPLATE/user-story.md
```

## Task 3

**Загрузить:** `planning-userstories-done.png`

На скриншоте: GitHub Project и созданные Sprint 1 stories — development environment, Read, List, Update, Delete и Create account. Должны читаться названия карточек.

## Task 4

**Загрузить:** `planning-productbacklog-done.png`

На скриншоте: колонка Product Backlog с упорядоченными историями, названиями и оценками.

## Task 5

**Загрузить:** `planning-labels-done.png`

На скриншоте: карточки или список issues с видимыми метками `enhancement` и `technical debt`.

## Task 6

**Загрузить:** `planning-kanban-done.png`

На скриншоте: название проекта и колонки New Issues, Ice Box, Product Backlog, Sprint Backlog и Done.

## Task 7

**Ответ (URL):**

```text
https://github.com/n1tr0oo/assik1/blob/main/setup.cfg
```

## Task 8

**Загрузить:** `rest-techdebt-done.png`

На скриншоте: карточка `Setting up the development environment` с меткой `technical debt`, оценкой 3, Sprint 1, в колонке Done.

## Task 9

**Загрузить:** `read-accounts.png`

На скриншоте: `Read an account from the service`, estimate 3, Sprint 1, колонка Done.

## Task 10

**Загрузить:** `list-accounts.png`

На скриншоте: `List all accounts in the service`, estimate 3, Sprint 1, колонка Done.

## Task 11

**Загрузить:** `update-accounts.png`

На скриншоте: `Update an account in the service`, estimate 5, Sprint 1, колонка Done.

## Task 12

**Загрузить:** `delete-accounts.png`

На скриншоте: `Delete an account from the service`, estimate 3, Sprint 1, колонка Done.

## Tasks 13–17: готовые ответы REST API

Все блоки ниже получены реальными запросами к локально запущенному сервису 31 августа 2026 года. Копируйте содержимое нужного блока целиком.

### Task 13 — готовый ответ

```text
$ curl -i -X POST http://127.0.0.1:8000/accounts -H "Content-Type: application/json" -d '{"name":"John-Doe","email":"john@example.com","address":"Astana","phone_number":"+77000000000"}'
HTTP/1.1 201 CREATED
Content-Type: application/json
Access-Control-Allow-Origin: *

{"address":"Astana","date_joined":"2026-08-31T12:39:39.452173","email":"john@example.com","id":1,"name":"John-Doe","phone_number":"+77000000000"}
```

### Task 14 — готовый ответ

```text
$ curl -i http://127.0.0.1:8000/accounts
HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *

[{"address":"Astana","date_joined":"2026-08-31T12:39:39.452173","email":"john@example.com","id":1,"name":"John-Doe","phone_number":"+77000000000"}]
```

### Task 15 — готовый ответ

```text
$ curl -i http://127.0.0.1:8000/accounts/1
HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *

{"address":"Astana","date_joined":"2026-08-31T12:39:39.452173","email":"john@example.com","id":1,"name":"John-Doe","phone_number":"+77000000000"}
```

### Task 16 — готовый ответ

```text
$ curl -i -X PUT http://127.0.0.1:8000/accounts/1 -H "Content-Type: application/json" -d '{"name":"John-Updated","email":"john.updated@example.com","address":"Astana","phone_number":"+77000000001"}'
HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *

{"address":"Astana","date_joined":"2026-08-31T12:39:39.452173","email":"john.updated@example.com","id":1,"name":"John-Updated","phone_number":"+77000000001"}
```

### Task 17 — готовый ответ

```text
$ curl -i -X DELETE http://127.0.0.1:8000/accounts/1
HTTP/1.1 204 NO CONTENT
Content-Type: text/html; charset=utf-8
Access-Control-Allow-Origin: *
```

## Task 18

**Загрузить:** `sprint2-plan.png`

В Sprint Backlog должны одновременно находиться:

- `Need the ability to automate continuous integration checks` — technical debt, 5, Sprint 2.
- `Need automated test coverage reporting` — enhancement, 3, Sprint 2.

## Task 19

**Готовый ответ (реальный успешный GitHub Actions run):**

```text
CI Build — completed successfully
Run ID: 33393070627
Run URL: https://github.com/n1tr0oo/assik1/actions/runs/33393070627
Branch: main
Event: push
Lint: passed
Unit tests and coverage: passed
Ran 5 tests in 0.097s
TOTAL: 97 statements, 3 missing, 97% coverage
Result: OK
```

Полный реальный лог: https://github.com/n1tr0oo/assik1/blob/main/evidence/ci-workflow-done

## Task 20

**Загрузить:** `ci-kanban-done.png`

На скриншоте обе Sprint 2 истории должны быть в Done после успешного CI.

## Task 21

**Ответ (URL):**

```text
https://github.com/n1tr0oo/assik1/blob/main/.github/workflows/ci-build.yaml
```

## Task 22

**Ответ (URL):**

```text
https://github.com/n1tr0oo/assik1/blob/main/service/__init__.py
```

## Task 23

**Готовый ответ:**

```text
Account model
- create and serialize account
- update from

Account routes
- create list read update delete
- health and security headers
- validation conflict and missing

Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
service/__init__.py      24      0   100%
service/config.py         6      0   100%
service/models.py        15      0   100%
service/routes.py        52      3    94%   53-55
---------------------------------------------------
TOTAL                    97      3    97%
Ran 5 tests in 0.117s
OK
```

Полный результат: https://github.com/n1tr0oo/assik1/blob/main/evidence/security-headers-done

## Task 24

**Загрузить:** `security-kanban-done.png`

На скриншоте `Need to add security headers and CORS policies`, estimate 3, Sprint 3, в Done.

## Task 25

**Загрузить:** `sprint3-plan.png`

В Sprint Backlog должны быть видны Security/CORS, Docker и Kubernetes stories с оценками 3, 5 и 5.

## Task 26

В одном терминале:

```bash
kubectl port-forward service/accounts 8080:8080
```

В другом:

```bash
curl http://127.0.0.1:8080/accounts | tee evidence/kube-app-output
cat evidence/kube-app-output
```

**Ответ:** вставить реальный JSON из `evidence/kube-app-output`.

## Task 27

**Загрузить:** `kube-docker-done.png`

На скриншоте `Containerize your microservice using Docker`, estimate 5, Sprint 3, в Done.

## Task 28

**Загрузить:** `kube-kubernetes-done.png`

На скриншоте `Deploy your Docker image to Kubernetes`, estimate 5, Sprint 3, в Done.

## Task 29

**Ответ (URL):**

```text
https://github.com/n1tr0oo/assik1/blob/main/Dockerfile
```

## Task 30

**Готовый ответ (реальный локально собранный Docker image):**

```text
Name: accounts
Tag: 1
Image ID: 19db4a3c4a80
Created Time: 22 seconds ago
Size: 277MB
```

Полный результат: https://github.com/n1tr0oo/assik1/blob/main/evidence/kube-images

## Task 31

После замены `YOUR_NAMESPACE` и настоящего deployment:

```bash
kubectl apply -f deploy/deployment.yaml
kubectl apply -f deploy/service.yaml
bash scripts/generate_kube_evidence.sh
cat evidence/kube-deploy-accounts
```

**Ответ:** вставить реальное содержимое `evidence/kube-deploy-accounts`. В нём должны быть deployments, pods, replica sets и services.

## Task 32

После установки Tekton Catalog tasks и запуска pipeline:

```bash
kubectl apply -f tekton/pipeline.yaml
kubectl create -f tekton/pipeline-run.yaml
tkn pipelinerun logs --last > pipelinerun.txt
cat pipelinerun.txt
```

**Ответ:** вставить реальные логи `pipelinerun.txt`, показывающие clone, lint, tests, build и deploy.

## Task 33

**Загрузить:** `cd-pipeline-done.png`

На скриншоте `Create a CD pipeline to automate deployment to Kubernetes`, estimate 5, Sprint 3, в Done.

## Команды публикации от аккаунта n1tr0oo

```bash
git add .
git commit -m "Initial Customer Accounts capstone implementation"
git remote add origin https://github.com/n1tr0oo/assik1.git
git push -u origin main
```

Перед push убедитесь, что автор коммита правильный:

```bash
git config user.name
git config user.email
```

Ожидается:

```text
n1tr0oo
n1tr0oo@users.noreply.github.com
```

## Статус скриншотов

Скриншоты Tasks 3–6, 8–12, 18, 20, 24, 25, 27, 28 и 33 нельзя создавать до появления настоящего GitHub Project. После его создания сохраняйте изображения с точными именами в `evidence/`. На каждом изображении должны быть видны название проекта, нужная колонка и полное название карточки; не используйте макеты или поддельные изображения.
