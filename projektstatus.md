# Projektstatus

## Nuvarande fas

Första romanversion komplett / utkastrevision.

## Senast godkända kapitel eller del

- Senast sparade: Kapitel 18 – Driftläge
- Status: Sparat utkast i projektzipen.
- Senast ändrad: 2026-08-13
- Romanens kapitelutkast: Kapitel 1–18 finns sparade.

## Nästa rekommenderade steg

Granska hela romanen som sammanhängande utkast. Börja inte med språkputs i varje kapitel, utan gör först en helhetsrevision: tempo, perspektivbalans, teknisk tydlighet, relationsbågar och om slutet känns hoppfullt utan att bli för perfekt.

## Viktiga öppna beslut

- Om Kapitel 18 ska göras mer känslomässigt, mer tekniskt konkret eller behållas i nuvarande lågmälda ton.
- Om Sofia och Amirs romantiska öppning ska vara tydligare eller mer antydd.
- Om Lenas nya roll ska namnges mer exakt i slutet, till exempel driftbarhetsansvarig, governance lead eller plattformskoordinator.
- Om romanen ska ha epilog eller sluta här.
- Om titeln **Driftläge** ska behållas.

## Risker att bevaka i revision

- Att mittendelen blir för mötestung; vissa kapitel kan behöva mer scenisk handling.
- Att tekniska begrepp blir för täta för läsare utanför IT; lägg till mänsklig konsekvens där det behövs.
- Att konfliktens upplösning känns för smidig; bevara att mycket återstår.
- Att Karin, Elin eller Naya kan behöva förstärkas tidigare för att slutets rollförändringar ska kännas helt förtjänade.
- Att romantikspåret mellan Sofia och Amir behöver doseras så det stödjer temat utan att ta över.

## Kontinuitet som måste följas upp i eventuell revision

- Pilotväg 0.2 är nästa arbetsform, inte slutgiltig modell.
- Containerplattformen är fortfarande under införande.
- Oracle är fortsatt externt beroende i pilotens första steg.
- MQ, Oracle, nattjobb och verksamhetshälsa är nu synliga i beroendekarta och larm.
- Lena rör sig mot en roll där driftbarhet och kvalitet byggs in tidigare.
- Karin har gått från coach till tydligare förändringsledare.
- Sofia har formellt tekniskt ansvar för pilotens standardmönster och fortsätter mot plattformsansvar.
- Amir accepterar att självservice kräver ägande, felvägar och driftbarhet.
- Mats kan bli bärare av operativ driftkunskap om tid avsätts.
- Styrgruppen har beslutat om fortsatt prioriterad bemanning och arbete mot permanent plattformsförmåga.

## Användarens aktuella önskemål

- Realistisk vuxenroman med spänning och lågmäld romantik.
- Utförligare inre tankar och perspektiv, inte bara korta dialogfraser.
- Projektzipen ska fungera som kontinuitetskälla för fortsatt skrivande och revision.


## Omslagsstatus

- Omslagsbild: Skapad och sparad i projektet som `omslag/omslag-driftlage.png`.
- Titel på omslag: Driftläge
- Undertitel på omslag: En roman om kontroll, tillit och förändring
- Författare på omslag: Erland Lindmark

## EPUB-metadata

- Titel: Driftläge
- Författare: Erland Lindmark
- Språk: svenska
- Kapitelkälla: `kapitel/kapitel-01.md` till `kapitel/kapitel-18.md`
- Status: Tillräcklig information finns för att skapa en grundläggande EPUB.
- Valfria kompletteringar inför senare export: baksidestext för metadata, förlagsnamn, ISBN och eventuell dedikation.
## Exportstatus

- EPUB-underlag: Kapitel 1–18 är rensade från kapitelnoteringar.
- Senaste EPUB-export: `driftlage-erland-lindmark-ren.epub`.
- Författare: Erland Lindmark.



## GitHub Actions och publiceringsstatus

- Status: Infört i projektzipen 2026-08-13.
- `.github/` ligger på samma nivå som `README.md`.
- Validate kör `scripts/validate_project.py`.
- Build Preview bygger EPUB och PDF med Pandoc och laddar upp ett gemensamt preview-artifact.
- Release körs på `v*`-taggar och publicerar EPUB/PDF som separata GitHub Release assets.
- Pandoc-version i Actions: `3.1.11.1`.
- Omslagsfil för automatiserad export: `omslag/omslag-driftlage.png`.
