# Driftläge

**Författare:** Erland Lindmark
**Undertitel:** En roman om kontroll, tillit och förändring
**Omslagsbild:** `omslag/omslag-driftlage.png`

Detta är projektarkivet för romanprojektet **Driftläge**.

## Arbetsflöde

1. Planera romankärnan: huvudperson, mål, hinder, insats och förändring.
2. Utveckla synopsis, kapitelplan, romanbibel och stilguide.
3. Skriv ett kapitel i taget i chatten.
4. Justera kapitlet tills det känns rätt.
5. Uppdatera projektfilerna och fortsätt med nästa kapitel.

## Viktiga filer

- `projektstatus.md` visar nuvarande fas och nästa steg.
- `roman-bibel.md` innehåller projektets centrala fakta.
- `synopsis.md` sammanfattar handlingen.
- `kapitelplan.md` är romanens färdplan.
- `stilguide.md` håller språk, ton och perspektiv konsekvent.
- `tidslinje.md` håller ordning på händelser.
- `kontinuitetsanteckningar.md` fångar fakta som inte får motsägas.
- `karaktarer/` innehåller karaktärsblad.
- `kapitel/` innehåller godkända eller sparade kapitelutkast.
- `omslag/` innehåller skapad omslagsbild.


## GitHub Actions och publicering

Projektet innehåller ett anpassat GitHub Actions-upplägg för validering och reproducerbar EPUB/PDF-generering.

- `.github/workflows/01-validate.yml` kör snabb projektvalidering vid pull request och push till `main`.
- `.github/workflows/02-build-preview.yml` kan startas manuellt och bygger EPUB + PDF som ett gemensamt preview-artifact.
- `.github/workflows/03-release.yml` körs på `v*`-taggar och publicerar EPUB och PDF som separata release-assets.
- `scripts/validate_project.py` kontrollerar projektstruktur, kapitelserie, metadata och omslag.
- `scripts/build_book.py` bygger EPUB/PDF från `kapitel/kapitel-XX.md` i numerisk ordning.
- `publishing/metadata.yaml` innehåller metadata för titel, undertitel, författare, språk och omslag.

Pandoc-versionen i GitHub Actions är låst till `3.1.11.1`. PDF-bygget använder XeLaTeX.
