all: pdf html
pdf: html
	pandoc --table-of-contents -o static/hackathon.pdf README.md
html:
	pandoc --table-of-contents -o README.md --to=html 0*.md
