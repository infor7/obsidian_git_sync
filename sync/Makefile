SHELL := /bin/bash
install:
	python3 -m virtualenv venv && source venv/bin/activate; pip install -r requirements.txt
sync:
	source venv/bin/activate && python sync.py || python3 sync.py
