.PHONY: install lint test run rest-evidence security-evidence docker-build docker-evidence kube-deploy kube-evidence
install:
	pip install -r requirements.txt
lint:
	flake8 service tests
test:
	nosetests --with-spec --spec-color
run:
	python app.py
rest-evidence:
	bash scripts/run_rest_tests.sh
security-evidence:
	bash scripts/generate_security_evidence.sh
docker-build:
	docker build -t accounts:1 .
docker-evidence:
	docker images accounts:1
kube-deploy:
	kubectl apply -f deploy/
kube-evidence:
	bash scripts/generate_kube_evidence.sh
