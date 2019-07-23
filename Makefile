.PHONY: default
default: clean test build publish

.PHONY: clean
clean:
	@echo "Cleaning up..."
	rm -rf build/ dist/ distro_names.egg-info .pytest_cache || true
	find . -type d -name __pycache__ -exec rm -rf {} \; || true
	find . -type f -name '*.pyc' -exec rm -rf {} \; || true

.PHONY: test
test:
	@echo "Running tests..."
	@pytest

.PHONY: build
build: test clean
	@python setup.py sdist bdist bdist_egg

.PHONY: publish
publish: build
	@twine upload dist/distro_names-*.egg
