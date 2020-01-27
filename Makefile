PANDOC=/usr/local/bin/pandoc
PYTHON=/usr/local/bin/python3

.PHONY: install
install:
	$(PYTHON) -m venv venv
	venv/bin/pip install -r requirements.txt

.PHONE: resume
resume:
	$(PANDOC) -f markdown -t html -o tribone/templates/_resume.html README.md
	$(PANDOC) -f markdown -t pdf -o tribone/static/resume.pdf -V geometry:"top=3.5cm" README.md

.PHONY: run
run:
	env FLASK_APP=tribone/app.py venv/bin/flask run
