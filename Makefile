PYTEST_FLAGS=

# Clean rules
.PHONY: clean
clean :
	git clean -dX --force
# -------------------

# Setup rules for the dev environment
.PHONY: setup-dev
setup-dev :
	tox --develop --workdir .tox -e py
	.tox/py/bin/pre-commit install
#	.tox/py/bin/python setup.py develop
# -------------------

# Test rules
.PHONY: pytest
pytest :
	pytest -vvvv \
           --strict-markers \
           --basetemp=./.pytest_tmp/ \
           --cov tests/ \
           --cov fake_uwsgi \
           --no-cov-on-fail \
           --cov-fail-under 100 \
		   --cov-report=xml:coverage_reports/coverage.xml \
		   $(PYTEST_FLAGS)

.PHONY: safety
safety :
	safety check

.PHONY: test
test : pytest lint
	which python
	python --version
# -------------------

# Lint Check rules
.PHONY: lint
lint : flake8_check pylint_check black_check

.PHONY: flake8_check
flake8_check :
	flake8 --max-line-length=88 --count --statistics src/ tests/

.PHONY: pylint_check
pylint_check :
	pylint --jobs 0 src/ tests/

.PHONY: black_check
black_check :
	black --check --diff --verbose .
# -------------------

# Formatting related rules
.PHONY: black
black :
	black --verbose .
# -------------------

# Deploy rules
.PHONY: deploy
deploy : setup-dev
	python setup.py sdist
	twine upload dist/*
