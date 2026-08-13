# Build-noteringar

Detta projekt kan byggas automatiskt med GitHub Actions eller lokalt med Pandoc.

## Struktur

- Kapitelkällor: `kapitel/kapitel-XX.md`
- Omslag: `omslag/omslag-driftlage.png`
- Metadata: `publishing/metadata.yaml`
- Byggscript: `scripts/build_book.py`

## Lokalt bygge

```bash
python3 scripts/validate_project.py .
python3 scripts/build_book.py --output-dir dist --allow-pandoc-version-mismatch
```

Standardbygget skapar både EPUB och PDF. PDF kräver XeLaTeX och TeX Gyre Pagella.

## 2026-08-13 – Fix för PDF-bygge i GitHub Actions

Preview-bygget föll i PDF-steget när Pandoc/XeLaTeX genererade LaTeX-kommandot `\tightlist`
och senare markerad kodmiljö (`Shaded`) utan motsvarande definitioner i den anpassade PDF-mallen.

Åtgärder:
- `publishing/pdf-template.tex` innehåller nu en Pandoc-kompatibel definition av `\tightlist`.
- `scripts/build_book.py` skickar `--no-highlight` till Pandoc vid PDF-bygge, eftersom romanexporten inte behöver syntaxmarkering och det undviker beroenden till Pandocs standard highlight-miljöer.
- Lokal testkörning av `scripts/build_book.py --formats epub,pdf` är verifierad med Pandoc 3.1.11.1.


## 2026-08-13 – PDF-titelsida efter TOC borttagen

PDF-bygget använder nu endast kapitelmarkdown som Pandoc-input i PDF-steget. Den manuella titelsidan i `00-title.md` används fortsatt för EPUB, men skickas inte längre in till PDF-bygget eftersom PDF-mallen redan skapar omslag och titelsida före innehållsförteckningen. Detta tar bort den extra titelsidan som tidigare hamnade efter innehållsförteckningen före kapitel 1.
