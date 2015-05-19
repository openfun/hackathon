all: pdf
pdf:
	pandoc -V lang=french --table-of-contents -o static/hackathon.pdf 0*.md
publish:
	git push origin master:gh-pages
publish-force:
	git push --force origin master:gh-pages
