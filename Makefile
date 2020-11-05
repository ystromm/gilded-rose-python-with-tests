export PYTHON_VERSION = python3.7

venv:
	virtualenv venv --python=$$PYTHON_VERSION

.PHONY: test
test: venv 
	@ . venv/bin/activate && pip install nose && nosetests  --cover-branches --with-coverage --rednose --with-watch --cover-erase --cover-html

## Cleaning

.PHONY: clean
clean:
	rm -rf venv
	find . -name "*.pyc" -delete
