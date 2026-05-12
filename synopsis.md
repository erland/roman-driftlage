# Synopsis

## Kort baksidestext

När en statlig myndighet ska införa containerteknik blir det snabbt tydligt att tekniken är det minsta problemet.

Utvecklingsteamet vill slippa veckor av beställningar, väntan och manuella godkännanden. Driftkoordineringen vill skydda produktionen från ogenomtänkta förändringar. Ledningen vill ha modernisering, men utan att släppa något annat.

Efter ännu en stoppad produktionssättning får den agila coachen Karin Nyström uppdraget att hålla ihop arbetet. Hon tror först att konflikten handlar om missförstånd. Men ju djupare hon gräver, desto mer ser hon av ett system där alla gör sitt bästa — och ändå hindrar varandra.

I mitten står Lena, driftkoordinatorn som inte längre vet om hon skyddar ordningen eller bara håller kaoset borta med händerna. Amir, utvecklingsledaren som vill framåt men underskattar vad produktion kräver. Och Sofia, den lågmälda teknikern som ser vägen framåt innan någon vågar ge henne ansvaret.

## Sammanfattning av hela handlingen

Containerinförandet på Myndigheten för samhällstjänster har formellt startat, men ingen äger riktigt helheten. Amirs utvecklingsteam försöker få ut tjänsten Kundportal Meddelandehantering via den nya containerplattformen. Lena stoppar produktionssättningen eftersom rollback, MQ-dokumentation, incidentansvar, testning och health checks inte håller för produktion.

Karin, agil coach och uppdragsledare utan tydligt mandat, får uppgiften att få samarbetet att fungera. Hon tror först att problemet handlar om kommunikation, men upptäcker snart att drift, utveckling och ledning arbetar i ett system där ansvar, tid och beslut inte hänger ihop.

Sofia Berg introduceras först som senior tekniker i utkanten. Hon löser problem och ser mönster som andra missar, men har inget formellt ansvar. När projektet krisar inser Karin att organisationen saknar tekniskt ägarskap för plattformens väg framåt och driver frågan om att ge Sofia mandat.

Under romanen möter projektet tekniska och organisatoriska hinder: JBoss-applikationens gamla antaganden, MQ-frågor om persistens och incidentansvar, Oracle som inte bör flyttas för snabbt, Elasticsearch-beroenden, otydliga deploymentmönster och brist på prioriterad tid. Samtidigt växer relationerna: Lena och Amir går från konflikt till respekt, Karin och Mats från skepsis till förtroende, och Sofia och Amir från professionell kemi till en komplicerad romantisk möjlighet.

Efter ett större bakslag i förproduktion och en skarp nattincident tvingas drift och utveckling arbeta tillsammans. De lär sig att självservice måste ha räcken, att manuell kontroll inte skalar, och att ansvar måste byggas in i flöden, plattform och team.

Slutet är hoppfullt: piloten blir inte perfekt, men den blir första fungerande steget. Organisationen börjar förändras på riktigt.

## Början

Pilotens första produktionssättning stoppas. Konflikten mellan drift och utveckling etableras. Karin kopplas in. Sofia nämns som en möjlig teknisk nyckelperson, men har ännu inte formellt ansvar.

## Mitt

Karin kartlägger värdeflödet. Driftens osynliga manuella arbete blir synligt. Amirs team konfronteras med att containerisering inte bara är deployment av en image. Sofia får gradvis en mer central roll. Organisationen tvingas fatta pragmatiska beslut kring JBoss, MQ, Oracle och självservice.

## Slut

En skarp incident tvingar alla att använda både gammal driftkunskap och nya plattformsmönster. Efterrapporten fokuserar på lärande i stället för syndabockar. Lena, Amir, Karin och Sofia förändrar sina arbetssätt och roller. Slutet visar början på en hållbar plattformsmodell.


Efter styrgruppens beslut om två veckors prioriterad bemanning testas Pilotväg 0.1 i förproduktion. Naya leder felvägstestet för Oracle timeout. Testet hittar först att readiness fortfarande kan ljuga och att tjänsten fortsätter konsumera meddelanden vid kritiskt beroendefel. Efter snabb åtgärd avslöjas ett djupare kompensationsfel: pausad konsumtion feltolkas som avbruten behandling och meddelanden flyttas till felkö. Produktionsfönstret flyttas, men stoppet formuleras som ett tecken på att den nya vägen fungerar före produktion, inte som ett rent misslyckande.

## Viktiga vändpunkter

1. Lena stoppar piloten.
2. Karin inser att problemet inte bara är kommunikation.
3. Sofia identifieras som informell teknisk ledare.
4. Sofia får formellt plattformsansvar.
5. Oracle-beslutet visar att allt inte ska containeriseras direkt.
6. Förproduktionsincidenten avslöjar brister i det nya arbetssättet.
7. Nattincidenten tvingar fram verkligt samarbete.
8. Efterrapporten blir lärande i stället för skuld.

## Viktiga avslöjanden

- Driftens manuella kontroll är till stor del kompensation för otydliga ansvar.
- Utvecklingsteamets frustration döljer också rädsla för stagnation.
- Sofia har länge agerat arkitekt utan mandat.
- Ledningen har krävt förändring utan att frigöra kapacitet.
- Självservice kräver mer disciplin, inte mindre.

## Saker som måste planteras tidigt

- Lenas trötthet och ansvarskänsla.
- Amirs frustration och legitima argument.
- Karins osäkra mandat.
- Sofias tekniska helhetssyn.
- Mats historiska kunskap.
- Elins press från ledning/styrgrupp.
- Skillnaden mellan “pilot” som snabbspår och “pilot” som risk.


## Lägessammanfattning efter Kapitel 7

Efter workshoppen testas första deploymentmallen. Den tekniska körningen blir ett första verkligt bakslag: pipelinen blir grön men JBoss-applikationen blir inte ready eftersom den förväntar sig resurser från den gamla servermiljön, särskilt datasource/JNDI-konfiguration. Bakslaget blir samtidigt konstruktivt eftersom det synliggör gamla miljöantaganden innan produktion. Amir börjar formulera problemet som ett gemensamt fynd snarare än ett rent hinder från drift.


## Uppdatering efter Kapitel 8

Kapitel 8 fördjupar MQ-spåret och visar att “en kö” i praktiken rymmer beslut om persistens, dubbletter, dead-letter, backlogg, incidentansvar, verksamhetsstatus och självservicegränser. Mats blir mer aktivt delaktig, Amir börjar efterfråga gammal driftkunskap och Sofia synliggör att hennes informella tekniska samordning inte är hållbar utan mandat.


## Uppdatering efter Kapitel 9

Efter MQ-mötet får Sofia och Amir ett lågmält samtal som fördjupar både deras professionella respekt och den personliga laddningen mellan dem. Sofia formulerar att en framtida plattformsroll bara är hållbar om den får verkliga villkor: mandat, tid, tydliga gränser, forum för standarder och fler personer som kan bära förmågan.


## Aktuell fördjupning efter Kapitel 10

I Kapitel 10 konkretiseras Sofias möjliga mandat inför styrgruppen. Rollen avgränsas till pilotens standardmönster och villkoras med minst 50 procent frigjord tid, standardforum, mandat att säga nej inom godkända mönster, driftmedverkan för att bygga bort sena manuella kontroller och minst två ytterligare personer som bär plattformsförmågan. Karin tar ett tydligare uppdragsledande ansvar och Elin måste prövas i om hon kan stå kvar när förändringen börjar kosta verklig kapacitet.

## Lägesutveckling efter Kapitel 11

Styrgruppen ger Sofia formellt tekniskt ansvar för pilotens standardmönster och frigör 50 procent av hennes tid. Beslutet skapar reaktioner: Lena och Mats oroar sig för att drift får ännu ett lager ansvar, Amir vill fortfarande skapa framdrift och Sofia måste börja använda mandat i stället för att bara hjälpa till informellt. Första standardforumet etablerar ansvarsnivåerna applikation, plattform och externa beroenden samt beslutar att inget nytt produktionsfönster bokas innan miniminivån är verifierad.


Efter att Sofia fått ansvar för pilotens standardmönster tvingas gruppen fatta ett pragmatiskt Oracle-beslut. I stället för att flytta in Oracle-plattformen i containerplattformen inom pilotens scope beslutar de att behandla databasen som ett externt beroende med tydliga kontrakt. Beslutet omfattar anslutningsmönster, schemaändringar, testdata, rollback- eller kompensationsplan, incidenttriage och bekräftelse från databasteamet. Det blir ett viktigt steg från symbolisk modernisering till genomförbar förändring.


## Uppdatering efter Kapitel 13

Efter Oracle-beslutet konkretiserar gruppen första självservicevägen, **Pilotväg 0.1**. Sofia leder den tekniska struktureringen med template, pipeline, policy, observability och runbook. Lena ser för första gången hur krav hon tidigare burit manuellt kan byggas in tidigare i flödet. Amir accepterar att tidiga blockerande krav kan vara bättre än sena stopp. Karin pressar fram ett tydligt beslutsunderlag: med prioriterade personer kan piloten gå vidare på ungefär en vecka, annars tar det betydligt längre tid och risken ökar. Kapitel 14 ska visa vad detta kostar organisatoriskt när Elin måste prioritera på riktigt.

Efter att Pilotväg 0.1 formulerats tvingas Elin ta den verkliga kostnaden till styrgruppen. Hon får beslut om två veckors prioriterad bemanning, tydlig avgränsning och krav på att dokumentera vad som byggs bort jämfört med vad som bara flyttas. Lena etablerar regeln Inga sidodörrar för att skydda driftgruppen från informella extrauppdrag, och Amir accepterar att teamet pausar annan förbättring för att fokusera på felvägar och runbook.


## Uppdatering efter Kapitel 16

Under en begränsad skarp aktivering uppstår en nattincident där MQ-backlogg och Oracle-latens hotar meddelandeflödet. Pilotväg 0.1 prövas i praktiken: gruppen pausar konsumenter enligt runbook, identifierar ett osynligt nattjobb och stabiliserar utan rollback. Händelsen visar att den nya arbetssättet inte eliminerar fel, men skapar tydliga mellanlägen, ansvar och lärande.


## Uppdatering efter Kapitel 17

Efter nattincidenten hålls en efterrapport där Karin styr samtalet bort från syndabockar och mot systemlärande. Gruppen ser att nattjobbet mot Oracle saknades i beroendekartan och att verksamhetshälsa måste bli en förstaklassignal. Begränsad aktivering räknas som kontrollerad framdrift, inte full pilotgodkänning. Pilotväg 0.2 definieras med förstärkt beroendekarta, separata MQ-larm, tydliga beredskapströsklar och namngivna bärare. Lena och Amir formulerar tillsammans en ny syn på stoppunkter: de ska förklara sig, inte bara bromsa.


## Uppdatering efter Kapitel 18

Avslutningen visar att Pilotväg 0.2 godkänns och används som nästa begränsade produktionsväg. Gruppen fattar beslut med tydligare ansvar, synlig verksamhetshälsa, beroendekarta och namngivna roller. Elin får styrgruppen att fortsätta prioritera bemanning och arbete mot permanent plattformsförmåga. Produktionsfönstret blir odramatiskt men meningsfullt: en gul signal hanteras utan panik, utan överreaktion och utan att Lena ensam behöver bära beslutet.

Lenas nya riktning formuleras som en roll där driftbarhet och kvalitet flyttas tidigare i plattformsflödet. Karin har blivit en förändringsledare som står kvar i kostnaden. Sofia står i sitt tekniska mandat. Amir har accepterat att självservice kräver ansvar och driftbarhet. Mats ser att hans gamla kunskap kan bli byggsten i den nya modellen. Sofia och Amir får en försiktig romantisk öppning utan att relationen löser allt. Romanen slutar hoppfullt: inte med färdig transformation, utan med en väg som fler kan bära tillsammans.
