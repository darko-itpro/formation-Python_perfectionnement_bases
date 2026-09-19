.PHONY: clean doc-build

clean:
	rm -rf site

doc-build:
	mkdocs build
