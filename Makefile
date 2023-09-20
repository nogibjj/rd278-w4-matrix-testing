# Makefile for Python Project requested a basic, readable makefile from chatGPT to understand how these funciton

# Variables
PYTHON := python3
VENV := env
SRC_DIR := pythonproject/src
TEST_DIR := pythonproject/tests
REQUIREMENTS := requirements.txt

# Default target

.PHONY: all env install test format lint clean

# Install project dependencies

env:
	$(PYTHON) -m venv $(VENV); . $(VENV)/bin/activate

install:
	$(VENV)/bin/pip install --upgrade pip -r  $(REQUIREMENTS)

# Run unit tests
test:
	$(VENV)/bin/pytest $(TEST_DIR); 
	$(VENV)/bin/py.test --nbval $(SRC_DIR)/Notebook.ipynb;
	

# Format code with Black
format:
	$(VENV)/bin/black $(SRC_DIR)

# Lint code with Flake8
lint:
	$(VENV)/bin/pylint $(SRC_DIR)

# Clean up generated files and virtual environment
clean:
	rm -rf $(VENV) __pycache__ .pytest_cache

all: 
	env install test format lint
