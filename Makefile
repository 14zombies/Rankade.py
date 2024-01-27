SPHINXOPTS    ?= -E -a
SPHINXBUILD   ?= sphinx-build
SOURCEDIR      = docs
BUILDDIR       = build/docs
SHELL 		   = /bin/bash
PREVIOUS_TAG   = `git describe --tags --abbrev=0`
PRETTY_OPTIONS = "- %s (%h)"
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

.PHONY: build
build:
	python3 -m build

.PHONY: docs
docs: spelling
	@$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

.PHONY: spelling
spelling:
	$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) -b spelling

.PHONY: doccoverage
doccoverage:
	$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) -b coverage

# Danger! Be careful with this.
.PHONY: cleandocs
cleandocs:

	[ -d "$(BUILDDIR)" ] && rm -r $(BUILDDIR)

.PHONY: coverage
coverage: tests
	coverage report

.PHONY: tests
tests:
	coverage run
	coverage lcov

all: coverage docs build
