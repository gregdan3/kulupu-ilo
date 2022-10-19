OUTDIR=downloads
PYDIR=tputils


download: $(OUTDIR)/nimi_pu.txt $(OUTDIR)/nimi_pi_pu_ala.txt $(OUTDIR)/compounds.txt $(OUTDIR)/nimi_ku.txt $(OUTDIR)/data.json

py: $(PYDIR)/steps.py

run:
	echo "No run behavior"

deps:
	$(info This is only needed for the nltk tokenizer.)
	pdm run python -c "import nltk; nltk.download('punkt')"

test:
	pdm run pytest -rP ./tests

$(OUTDIR)/nimi_pu.txt:
	curl -s https://tokipona.org/nimi_pu.txt > $@
$(OUTDIR)/nimi_pi_pu_ala.txt:
	curl -s https://tokipona.org/nimi_pi_pu_ala.txt > $@
$(OUTDIR)/compounds.txt:
	curl -s https://tokipona.org/compounds.txt > $@
$(OUTDIR)/data.json:
	curl -s https://raw.githubusercontent.com/lipu-linku/jasima/master/data.json > $@

$(OUTDIR)/tlds-alpha-by-domain.txt:
	curl -s https://data.iana.org/TLD/tlds-alpha-by-domain.txt > $@

$(PYDIR)/steps.py:
	pdm run python ./tputils/toys.py > $@
