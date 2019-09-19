VERSION = 2.1.2

PACKAGE = python-ew
#======================================================================


clean:
	rm -rf *.tar.gz dist *.egg-info *.rpm build
	find . -name "*.pyc" -exec rm '{}' ';'

version:
	@echo $(VERSION)

dist: clean
	@python setup.py sdist

pypi: dist
	@twine upload dist/*

build:
	docker build -t ${PACKAGE}:${VERSION} .
	docker tag ${PACKAGE}:${VERSION} ${PACKAGE}:latest
	docker image prune -f

docker-clean:
	docker stop $(shell docker ps -a -q)
	docker rm $(shell docker ps -a -q)
