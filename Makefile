.PHONY: setup clean doc-build

setup:
	mkdir data

clean:
	rm -rf site
	rm -rf data
	rm -f file.log

doc-build:
	mkdocs build
