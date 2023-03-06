.PHONY: build deps clean

build:
	sphinx-build doc/ build/

clean:
	rm -rf build

deps:
	pip install sphinx sphinx_rtd_theme
