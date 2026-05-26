# Romanbibel

## Arbetstitel

**Driftläge**

Alternativa titlar:
- Självservice
- Produktionssättning
- När systemet startar om
- Paved Road

## Undertitel

En roman om kontroll, tillit och förändring

## Författare

Erland Lindmark

## Omslagsbild

Skapad och sparad som `omslag/omslag-driftlage.png`.

## Genre

Realistisk samtidsroman med inslag av arbetsplatsdrama, lågmäld spänning och romantik.

## Målgrupp

Vuxen.

## Ton och känsla

Realistisk, mänsklig, stundvis spänd, med hoppfull riktning. Berättelsen ska skildra teknisk förändring som mänsklig, organisatorisk och emotionell förändring.

## Premiss

På en statlig myndighets IT-avdelning ska containerteknik införas i en komplex driftsmiljö byggd kring JBoss EAP, Oracle, IBM MQ och Elasticsearch. Utvecklingsteamen vill ha självservice och snabbare väg till produktion. Driftkoordineringen vill säkra ordning, spårbarhet och stabilitet genom manuella kontroller som hittills hållit systemen vid liv.

När en pilot blir stoppad kallas en agil coach in för att “få samarbetet att fungera”. Men snart visar det sig att problemet inte bara är kommunikation. Ingen äger helheten, ingen har fått tid att förändra arbetet, och den person som bäst förstår den tekniska vägen framåt har ännu inget formellt mandat.

## Romanens kärna

En pressad driftkoordinator vill bevara kontrollen över en samhällsviktig IT-miljö, men hindras av utvecklingsteamens krav på självservice, ledningens moderniseringsmål och en containerplattform som avslöjar hur ohållbara de manuella arbetssätten har blivit.

Om förändringen misslyckas riskerar myndigheten driftstörningar, tappat förtroende, personalflykt och en intern kultur där drift och utveckling slutar lita på varandra.

## Huvudkonflikt

Hur kan en statlig IT-organisation gå från manuell kontroll till automatiserad tillit utan att tappa ansvar, säkerhet och driftstabilitet?

## Teman

- Tillit kontra kontroll
- Yrkesstolthet och förändringsrädsla
- Självservice med ansvar
- Osynligt arbete
- Teknisk skuld som mänsklig belastning
- Mandat, ansvar och otydlighet
- Att gå från hjälteinsatser till hållbara system
- Kärlek och närhet under professionell press

## Huvudperson

Lena Holm, driftkoordinator.

## Antagonist eller motkraft

Ingen enskild ond antagonist. Motkraften är ett arbetssystem av manuell kvalitetssäkring, incidenttryck, otydliga ansvar, teknisk skuld, ledningens krav på modernisering utan tillräcklig prioritering samt kulturkrock mellan drift och utveckling.

## Viktiga bifigurer

- Amir Rahman, utvecklingslead
- Karin Nyström, agil coach / uppdragsledare
- Sofia Berg, senior systemingenjör som senare får formellt plattformsansvar
- Mats Eklund, erfaren drifttekniker
- Elin Varga, sektionschef / sponsor

## Miljö och värld

En fiktiv svensk statlig myndighet: **Myndigheten för samhällstjänster**.

Miljön består av kontor, mötesrum, Teams-kanaler, ärendehanteringssystem, incidentkanaler, styrgrupper och produktionssättningsfönster. Den tekniska miljön omfattar JBoss EAP, Oracle, IBM MQ, Elasticsearch och en ny containerplattform.

## Centrala regler och begränsningar

- Containerplattformen är inte en magisk lösning.
- Allt ska inte containeriseras på en gång.
- Oracle blir en pragmatisk arkitekturfråga.
- IBM MQ kräver tydligt ansvar kring persistens, återstart, övervakning och incidenter.
- Självservice betyder frihet inom tydliga räcken, inte frånvaro av ansvar.
- Driftens manuella rutiner är både skydd och belastning.
- Utvecklingens frustration är legitim, men deras ansvar behöver växa.

## Viktiga återkommande motiv

- Kaffe som kallnar.
- Teams-pling och ärendeköer.
- Regn mot myndighetens grå byggnad.
- Affischer med förenklingsbudskap som kontrast mot intern komplexitet.
- Orden “pilot”, “samverkan”, “mandat”, “rollback” och “ordning”.

## Slutets riktning

Hoppfullt men realistiskt. Piloten lyckas som första steg, inte som färdig lösning. Lena går mot en ny roll där hon bygger in kvalitet i plattformen. Amir accepterar driftbarhet som del av leverans. Karin får verkligt förändringsmandat. Sofia blir formellt plattformsansvarig och vågar stå i rollen.

## Efter Kapitel 11

Sofia har fått formellt men avgränsat ansvar för pilotens standardmönster. Standardforumet är etablerat och arbetar med tre ansvarsnivåer: applikation, plattform och externa beroenden. Lena rör sig från ren stoppfunktion mot att bygga räcken tidigare i flödet, medan Amir börjar acceptera att självservice kräver verifierbar driftbarhet innan nya datum sätts.


## Viktigt beslut efter Kapitel 12

Oracle-plattformen flyttas inte in i containerplattformen i pilotens första steg. Den befintliga Oracle-plattformen behandlas som externt beroende, men applikationens användning av Oracle ska standardiseras genom datakontrakt, anslutningsmönster, versionerade schemaändringar, testdata, behörigheter, rollback- eller kompensationsplan och körbok för incidenttriage. Beslutet ska bekräftas av databasteamet innan nytt produktionsfönster bokas.


## Nya centrala begrepp efter Kapitel 13

- **Pilotväg 0.1:** första konkreta självservicevägen för piloten.
- **Självservice inom beslutad väg:** romanens praktiska kompromiss mellan utvecklingens autonomi och driftens krav på ordning.
- **Tidigt nej > sent stopp:** princip som flyttar kvalitetssäkring tidigare.
- **Bygg. Kontrollera. Släpp. Se. Ångra.:** Sofias livscykel för plattformens första mönster.

## Nya organisatoriska principer efter Kapitel 14

- **Inga sidodörrar:** Informella extra uppdrag till drift eller experter ska inte gå runt Karin/Sofia och den beslutade pilotplanen.
- Prioriterad bemanning är tidsatt till två veckor och avgränsad till Pilotväg 0.1 för Kundportal Meddelandehantering.
- Återrapport ska skilja på arbete som faktiskt byggts bort och arbete som bara flyttats.

## Uppdatering efter Kapitel 15

Pilotväg 0.1 har nu visat sin första verkliga funktion: att stoppa ett produktionsförsök innan Lena ensam behöver bära stoppbeslutet. Förproduktionstestet visar att tekniska räcken inte bara är dokumentation utan praktiska kontrollpunkter som kan avslöja fel i readiness, meddelandekonsumtion och kompensation. Detta stärker temat att ordning kan byggas in i systemet, men bara om gruppen accepterar att ett stopp också kan vara framsteg.


## Efter Kapitel 16

Pilotväg 0.1 har prövats i skarpt nattläge. En växande MQ-backlogg och Oracle-låsning kopplad till ett befintligt nattjobb hanteras utan rollback genom konsumentpaus, reducerad återstart, tydlig beslutsordning och gemensam lägesbild. Detta stärker romanens tema: ordning kan byggas in i arbetssätt och system i stället för att bäras av enskilda personer.


## Efter Kapitel 17

Organisationen har tagit ett kulturellt steg: efterrapporten efter nattincidenten blev inte en syndabocksjakt utan ett lärande samtal om system, beroenden och ansvar. Pilotväg 0.2 är nästa konkreta steg. Lenas roll börjar röra sig mot att bygga in driftbarhet och förklarande stoppunkter i plattformen. Amir tar mer ansvar för att utvecklingsbarhet och användbarhet i mönstren ska bära teamens självservice. Sofia står tydligare i plattformsansvaret men bevakar risken att själv bli nästa personberoende. Karin har utvecklats mot en mer beslutsdrivande uppdragsledare.


## Efter Kapitel 18

Första romanversionen är komplett. Organisationen har inte löst all teknisk skuld, men den har gått från personburen kontroll till början på systemburen tillit. Pilotväg 0.2 är etablerad som nästa fungerande steg. Det hoppfulla slutet bygger på att:
- driftbarhet börjar flyttas tidigare i flödet,
- självservice definieras med räcken och ansvar,
- ledningen erkänner att förändring kostar bemanning och prioritering,
- Sofia, Lena, Amir, Karin, Mats, Naya, Annika och Peter får tydligare roller,
- relationen mellan Sofia och Amir öppnas varsamt utan att underminera professionella gränser.

Slutets centrala betydelse: **driftläge** betyder inte längre bara att hålla igång, utan att vara på väg med ett arbetssätt fler än en person kan bära.


## Exportmetadata

- Titel för export: Driftläge
- Författare: Erland Lindmark
- Språk: svenska
- Exportkälla: `kapitel/kapitel-01.md` till `kapitel/kapitel-18.md` i numerisk ordning.
- EPUB-status: Tillräcklig metadata finns för grundläggande EPUB-export.
