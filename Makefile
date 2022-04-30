PANDOC=$(shell brew --prefix pandoc)/bin/pandoc
PYTHON=$(shell brew --prefix python)/bin/python

.PHONY: install
install:
	$(PYTHON) -m venv venv
	venv/bin/pip install -r requirements.txt

.PHONY: pandoc
pandoc:
	$(PANDOC) --katex \
	          --section-divs \
	          --filter pandoc-sidenote \
	          --from markdown+tex_math_single_backslash \
	          --to html5+smart \
	          --template tribone/templates/pandoc/resume \
	          --css static/css/tufte.css \
	          --css static/css/pandoc.css \
	          --css static/css/resume.css \
	          --output tribone/templates/resume.html \
	          tribone/templates/markdown/resume.md
	$(PANDOC) --from markdown \
	          --to pdf \
	          --output tribone/static/resume.pdf \
	          --variable geometry:margin=1.5cm \
	          tribone/templates/markdown/resume-pdf.md
	$(PANDOC) --katex \
	          --section-divs \
	          --from markdown+tex_math_single_backslash \
	          --to html5+smart \
	          --template tribone/templates/pandoc/index \
	          --css static/css/tufte.css \
	          --css static/css/pandoc.css \
	          --css static/css/index.css \
	          --output tribone/templates/index.html \
	          tribone/templates/markdown/index.md

.PHONY: run
run:
	env FLASK_APP=tribone/app.py venv/bin/flask run --host='0.0.0.0' --port=9876

.PHONY: debug
debug:
	env DEBUG=1 SECRET_KEY=1234asdf FLASK_APP=tribone/app.py venv/bin/python -m tribone.app
