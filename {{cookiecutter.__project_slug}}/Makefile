SOURCES := $(wildcard ./src/*.py)
NOTEBOOKS := $(patsubst ./src/%.py,./build/%.ipynb,$(SOURCES))


.PHONY: default
default: help

.PHONY: help
help:
	@echo
	@echo "{{ cookiecutter.project_name }}"
	@echo "{{ '='*cookiecutter.project_name|length }}"
	@echo "Below are the available \`make\` targets for the {{ cookiecutter.project_name }} package."
	@echo
	@echo "Build:"
	@echo "  install-requirements"
	@echo "    install the requirements in the current Python environment"
	@echo "  notebooks"
	@echo "    build the notebooks"
	@echo
	@echo "Development:"
	@echo "  start-dev"
	@echo "    watch Python source files and convert to IPython notebooks"
	@echo "    run Voila server"
	@echo "  stop-dev"
	@echo "    terminate the background processes initiated by \`start-dev\`"
	@echo

.PHONY: install-requirements
install-requirements:
	$(MAKE) -C ./requirements/ install

.PHONY: all
all: notebooks

.PHONY: notebooks
notebooks: $(NOTEBOOKS)

.PHONY: check
check: notebooks
	pytest --nbmake ./build/

.PHONY: start-dev
start-dev: stop-dev notebooks
	watchmedo shell-command ./src/ --patterns="*.py" --command='make notebooks' \
	  & echo "$$!" >> watchmedo.pid
	voila --debug ./build/ \
	  & echo "$$!" >> voila.pid

.PHONY: stop-dev
stop-dev:
	- pkill -F watchmedo.pid
	- pkill -F voila.pid
	- rm watchmedo.pid
	- rm voila.pid

.PHONY: clean
clean:
	- rm -rf ./build/*

.PHONY: clean-all
clean-all: clean

./build:
	mkdir -p ./build

./build/%.ipynb: ./src/%.py | ./build
	jupytext --from py:percent --to notebook --output $@ $<
