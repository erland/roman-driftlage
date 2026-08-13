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
