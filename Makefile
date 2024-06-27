PYTHON_DEPS_FILE = python_deps.txt
VENV_DIR = .venv
ACTIVATE_VENV = $(VENV_DIR)/bin/activate
PYTHON = python3

.PHONY: venv
venv:
	$(PYTHON) -m venv $(VENV_DIR) && \
	source $(ACTIVATE_VENV) && \
	$(PYTHON) -m pip install -r $(PYTHON_DEPS_FILE)

.PHONY: clean
clean:
	$(RM) -r $(VENV_DIR)
	$(RM) -r src/__pycache__
