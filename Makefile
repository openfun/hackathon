all: pdf html
pdf: html
	pandoc -V lang=french --table-of-contents -o static/hackathon.pdf --from=html README.md
html:
	pandoc -V lang=french  --table-of-contents -o README.md --to=html 0*.md
