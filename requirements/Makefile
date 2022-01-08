.PHONY: all
all: dev-requirements.txt

.PHONY: install
install: dev-requirements.txt
	pip-sync $^

%.txt: %.in
	pip-compile $<
