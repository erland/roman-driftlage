# Kapitelplan

## Översikt

| Kapitel | Titel | Syfte | Viktiga händelser | Status |
|---|---|---|---|---|
| 1 | Stopp i kön | Etablera huvudkonflikten | Lena stoppar pilotens produktionssättning; Karin kopplas in; Sofia nämns | Sparat utkast |
| 2 | Någon måste hålla ihop det | Introducera Karin och mandatproblemet | Karin försöker förstå uppdraget; Elin vill ha samarbete, tempo och trygghet | Sparat utkast |
| 3 | Driftens vardag | Skapa empati för drift | Lena och Mats hanterar P2-incident, certifikatsrisk och manuella kontroller; Amir ser driftens belastning | Sparat utkast |
| 4 | Teamets frustration | Skapa empati för utveckling | Amir och teamet kartlägger väntetider, manuella beställningar och sitt eget ansvar inför mötet | Sparat utkast |
| 5 | Sofia i utkanten | Introducera Sofia som informell nyckelperson | Sofia löser MQ-/readiness-problem, synliggör oklart ägarskap och bidrar till gemensam miniminivå | Sparat utkast |
| 6 | Workshoppen | Synliggöra systemproblemet | Karin håller värdeflödeskartläggning; flaskhalsar, ansvarsglapp och behovet av tekniskt ägarskap blir synliga | Sparat utkast |
| 7 | Det första tekniska bakslaget | Visa att teknikskiftet kräver anpassning | Första deploymentmallen avslöjar dolda JBoss-/datasource-antaganden, bristande tester och behov av tydliga plattformsstandarder | Sparat utkast |
| 8 | Mer än en kö | Visa att självservice kräver ansvar för beroenden | IBM MQ blir konfliktpunkt kring persistens, återstart, övervakning och ansvar | Sparat utkast |
| 9 | Efter mötet | Starta romantisk och idéburen spänning | Sofia och Amir får ett lågmält samtal om ansvar, mandat och framtida rollgränser | Sparat utkast |
| 10 | Mandatet som saknas | Konkretisera villkor för tekniskt ägarskap | Karin, Sofia, Elin och Lena formulerar styrgruppens beslutspunkter: mandat, tid, standardforum, driftens roll och flera bärare | Sparat utkast |
| 11 | Reaktionen | Visa att mandat skapar konflikt | Styrgruppsbeslutet om Sofia kommuniceras; Lena kräver att driftens tid frigörs; Amir accepterar verifierad miniminivå före datum; första standardforumet hålls | Sparat utkast |
| 12 | Oracle-beslutet | Visa mogen teknisk kompromiss | Oracle flyttas inte in i piloten; datakontrakt, anslutningsmönster, schemaändringar, testdata och incidenttriage definieras | Sparat utkast |
| 13 | Självservice med räcken | Visa romanens konstruktiva centrum | Pilotväg 0.1 formas med template, pipeline, policy, observability, runbook, blockerande krav, felvägstester och prioriteringsbeslut | Sparat utkast |
| 14 | Det som kostar | Visa att förändring kräver prioritering | Elin får styrgruppen att besluta om två veckors prioriterad bemanning, avgränsning och dokumentation av flyttade aktiviteter | Sparat utkast |
| 15 | Förproduktionsincidenten | Stort bakslag | Förproduktionstest hittar blockerande readiness- och kompensationsfel; produktionsfönstret flyttas; gamla konfliktmönster återkommer men hanteras | Sparat utkast |
| 16 | Nattläget | Klimax med praktiskt samarbete | Skarp nattincident kräver samarbete mellan gammal driftkunskap, ny runbook och tydlig beslutsordning | Sparat utkast |
| 17 | Utan syndabock | Kulturell förändring | Efterrapporten fokuserar på systemlärande, tydliggör dolda beroenden och etablerar Pilotväg 0.2 utan syndabock | Sparat utkast |
| 18 | Driftläge | Hoppfull upplösning | Pilotväg 0.2 godkänns och prövas; styrgruppen ger fortsatt mandat; roller och relationer landar hoppfullt utan att allt är färdigt | Sparat utkast |

## Kapitelanteckningar

### Kapitel 1
- Mål: Etablera Lena, myndigheten, pilotstoppet och konflikten mellan drift och utveckling.
- Konflikt: Utveckling vill köra i produktionsfönster; Lena stoppar på grund av bristande produktionsbarhet.
- Slutpunkt: Lena öppnar för annat arbetssätt: tydligare krav tidigare, inte lägre krav.

### Kapitel 2
- Mål: Introducera Karins perspektiv och visa hennes oklara uppdrag.
- Konflikt: Hon ska “hålla ihop arbetet” utan att någon kan säga vad hon får besluta.
- Slutpunkt: Karin bokar mötet om pilotens miniminivå och inser att vägen framåt går genom konflikten, inte runt den.

### Kapitel 3
- Mål: Skapa empati för driftens vardag genom Lena och Mats.
- Konflikt: Operativ drift, incidenter, certifikatsrisker och manuella kontroller tränger undan förbättringsarbete.
- Slutpunkt: Lena formulerar driftens miniminivå inför Karins möte: förändring kräver kapacitet, automatiska spärrar och krav som kommer tidigare.

### Kapitel 4
- Mål: Skapa empati för utvecklingsteamets vardag och frustration.
- Konflikt: Amir och teamet försöker visa att manuella beställningar, gamla formulär och otydliga krav bromsar leverans, samtidigt som de måste erkänna egna brister i rollback, readiness och ansvar.
- Slutpunkt: Amir kontaktar Lena sakligt inför Karins möte och ser att självservice behöver förtjänas genom ansvar.

### Kapitel 5
- Mål: Introducera Sofia som informell teknisk nyckelperson utan formellt mandat.
- Konflikt: Ett konkret MQ-/readiness-fel visar att teamets problem inte bara är ett stavfel utan ett symptom på bristande standarder, oklart ägarskap och en plattform som ännu inte är en produkt.
- Slutpunkt: Karin tänker ta frågan om tekniskt ägarskap till Elin, medan Sofia markerar att hon inte får bli ensam lösning utan tid, mandat, folk och prioritering.
ansvar, inte bara krävas.


### Kapitel 6
- Mål: Synliggöra hela flödet från kodändring till trygg produktion och visa att problemet är systemiskt.
- Konflikt: Utveckling vill visa väntan och omtag; drift vill visa risk och sen granskning; ledningen vill ha konkreta steg utan att fullt ut ha valt kostnaden.
- Slutpunkt: Elin tar med sig behovet av frigjord tid, beslutad miniminivå och tekniskt ägarskap; Karin signalerar att Sofias informella roll behöver tas på allvar.

### Kapitel 7
- Mål: Visa att containerisering kräver mer än att flytta applikationen till en image.
- Konflikt: Teamet vill se framdrift, men första körningen avslöjar gamla beroenden och falsk trygghet.
- Slutpunkt: Amir börjar acceptera att självservice kräver att teamet synliggör och äger gamla miljöantaganden.

### Kapitel 8
- Mål: Fördjupa IBM MQ som tekniskt och organisatoriskt beroende.
- Konflikt: Utveckling vill att MQ ska vara ett standardiserat stöd, medan drift och integration visar att köer kräver tydliga beslut om persistens, dubbletter, backlogg, incidentansvar och verksamhetsstatus.
- Slutpunkt: Elin säger att piloten inte får nytt produktionsdatum förrän miniminivån är beslutad och bemannad, och att tekniskt ägarskap tas till styrgruppen.


### Kapitel 9
- Mål: Starta den romantiska och idéburna spänningen mellan Sofia och Amir utan att förlora den professionella konflikten.
- Konflikt: Sofia ser att hon kan behöva ta en formell roll, men att mandatet skulle göra hennes relation till Amir och andra mer komplicerad.
- Slutpunkt: Sofia svarar Karin att de kan prata om tekniskt ägarskap, men bara om villkor och inte bara rollnamn.


### Kapitel 10
- Mål: Konkretisera vad tekniskt ägarskap måste innebära innan Sofia kan få en formell roll.
- Konflikt: Elin behöver ett säljbart styrgruppsunderlag, medan Sofia och Karin kräver att mandat, tid och fler bärare beslutas på riktigt. Lena bevakar att driftens medverkan inte blir ännu en manuell grind.
- Slutpunkt: Elin går mot styrgruppen med fem beslutspunkter och Karin lovar Sofia att säga ifrån om villkoren försvinner.


### Kapitel 11
- Mål: Visa att Sofias formella pilotansvar skapar reaktioner och tvingar rollerna att förändras i praktiken.
- Konflikt: Lena och Mats oroar sig för att drift får ännu ett ansvarslager; Amir vill skapa nytt produktionsdatum men måste acceptera verifieringar först; Sofia måste börja tala som ansvarig snarare än hjälpsam tekniker.
- Slutpunkt: Första standardforumet genomförs med tydliga ansvarsnivåer, kapacitetsbeslut och verifieringar innan nytt produktionsfönster.


### Kapitel 12
- Mål: Fatta ett pragmatiskt Oracle-beslut som visar teknisk mognad och organisatorisk tydlighet.
- Konflikt: Utveckling vill undvika nya beställningsflaskhalsar; drift vill inte bära risker kring databas, rollback och incidenter; ledningen behöver ett beslut som kan försvaras.
- Slutpunkt: Gruppen beslutar att Oracle-plattformen inte flyttas in i containerplattformen i första steget, men att anslutning, datakontrakt, schemaändringar, testdata och incidenttriage måste standardiseras och bekräftas av databasteamet innan nytt produktionsfönster bokas.


### Kapitel 13
- Mål: Visa hur självservice konkretiseras som frihet inom beslutad, verifierad väg.
- Konflikt: Utveckling vill undvika tung process, drift vill undvika sena stopp och Sofia/Karin måste göra kraven användbara utan att de blir en ny möteskö.
- Slutpunkt: Pilotväg 0.1 finns som synligt, delbart arbetssätt och Elin får ett beslutsunderlag om prioriterad bemanning.

### Kapitel 14
- Mål: Visa att förändring kostar faktisk kapacitet och kräver att ledningen väljer bort annat.
- Konflikt: Styrgruppen vill ha både snabbhet, säkerhet och oförändrad ordinarie leverans; Elin måste synliggöra riskerna och kostnaden.
- Slutpunkt: Två veckors prioriterad bemanning beslutas, med första avstämning efter en vecka och tydlig regel om inga sidodörrar.

### Kapitel 15
- Mål: Visa att Pilotväg 0.1 prövas praktiskt och hittar fel innan produktion.
- Konflikt: Readiness, meddelandekonsumtion och kompensation fungerar inte tillräckligt; Lena vill stoppa, Amir vill behålla fart.
- Slutpunkt: Produktionsfönstret flyttas och gruppen formulerar bakslaget som ett bevis på att den nya vägen faktiskt kan säga nej före produktion.

### Kapitel 16
- Mål: Pröva Pilotväg 0.1 i skarpt läge och visa praktiskt samarbete.
- Konflikt: MQ-backlogg och Oracle-låsningar hotar meddelandeflödet under nattlig aktivering.
- Slutpunkt: Gruppen undviker rollback genom tydligt ansvar, konsumentpaus, identifierat nattjobb och gemensam lägesbild.


### Kapitel 17
- Mål: Göra efterrapporten till kulturell vändpunkt där gruppen väljer systemlärande framför skuld.
- Konflikt: Nattjobbet saknades i beroendekartan och skulle kunna skapa syndabocksjakt mellan utveckling, databas och drift.
- Slutpunkt: Gruppen beslutar om Pilotväg 0.2, namngivna bärare och en ny princip: stoppunkter ska förklara sig och systemet ska bära mer så människor slipper bära allt ensamma.


### Kapitel 18
- Mål: Ge romanen en hoppfull upplösning där piloten blir första steg, inte färdig transformation.
- Konflikt: Gruppen måste fatta beslut utan att göra Pilotväg 0.2 till en falsk slutlösning; ledningen måste fortsatt betala för förändringen.
- Slutpunkt: Begränsad produktionsaktivering genomförs odramatiskt, Lenas nya roll börjar formuleras och organisationen har fått en väg fler än en person kan bära.
