# Tidslinje

## Före romanens början

- Myndigheten för samhällstjänster har länge använt en traditionell driftsmodell.
- Driftkoordinering har byggt upp manuella rutiner för att hantera risk.
- Utvecklingsteamen har blivit allt mer frustrerade över långsamma beställningsflöden.
- Ledningen har beslutat att containerteknik ska införas.
- En pilot har valts: Kundportal Meddelandehantering.
- Mandat, ansvar och arbetssätt för piloten är oklara.

## Under romanen

| Tidpunkt | Händelse | Berörda karaktärer | Kapitel |
|---|---|---|---|
| Dag 1 förmiddag | Lena granskar produktionssättningsärendet och stoppar kvällens fönster | Lena, Amir, Mats | 1 |
| Dag 1 förmiddag | Elin och Karin kallar in Lena för att förstå stoppet | Lena, Karin, Elin | 1 |
| Dag 1 förmiddag | Karin föreslår att rätt personer samlas för att definiera pilotens miniminivå | Lena, Karin, Elin, Sofia nämns | 1 |
| Dag 1 förmiddag | Lena skriver till Amir att ett annat arbetssätt behövs: tydligare krav tidigare, inte lägre krav | Lena, Amir | 1 |
| Dag 1 sen förmiddag | Karin reflekterar över sitt oklara uppdrag och ser att problemet handlar om ansvar, mandat och tid | Karin | 2 |
| Dag 1 sen förmiddag | Elin erkänner indirekt att förändringen saknar tillräckligt utrymme men vill inte tappa fart | Karin, Elin | 2 |
| Dag 1 sen förmiddag | Karin bokar möte om pilotens miniminivå och bjuder in Lena, Amir, Sofia, Mats, databas och MQ | Karin, Lena, Amir, Sofia, Mats, Elin | 2 |
| Dag 1 sen förmiddag | Karin och Amir pratar om skillnaden mellan imperfektion och otydligt ansvar | Karin, Amir | 2 |
| Dag 1 mitt på dagen | Drift hanterar P2-incident i Intygsbeställning orsakad av felaktigt reindex-jobb i produktion | Lena, Mats | 3 |
| Dag 1 mitt på dagen | Lena eskalerar certifikatsrisk och ser hur förbättringsarbete skjuts fram | Lena, Mats, Elin indirekt | 3 |
| Dag 1 lunch | Amir kommer till driftön och erkänner att rollbacken är för tunn; Lena och Amir når en första saklig skottpaus | Lena, Amir, Mats | 3 |
| Dag 1 efter lunch | Lena formulerar driftens miniminivå inför Karins möte | Lena | 3 |
| Dag 1 tidig eftermiddag | Amir och teamet kartlägger alla väntetider och omtag i pilotflödet | Amir, Naya, Jonas | 4 |
| Dag 1 tidig eftermiddag | Sara påminner teamet om verksamhetsnyttan och att självservice inte får bli ett tomt löfte uppåt | Amir, Sara, Naya, Jonas | 4 |
| Dag 1 inför mötet | Amir skickar ett mer sakligt meddelande till Lena och säger att teamet tar med både flödesbild och eget ansvar | Amir, Lena | 4 |
| Dag 1 eftermiddag | Sofia hjälper Amirs team med ett MQ-/readiness-problem och identifierar att felet pekar på bristande standarder och oklart ägarskap | Sofia, Jonas, Amir indirekt | 5 |
| Dag 1 eftermiddag | Karin håller mötet om pilotens miniminivå; driftens krav, teamets flödesbild och Sofias tekniska helhetssyn möts | Karin, Sofia, Lena, Amir, Mats | 5 |
| Dag 1 eftermiddag | Gruppen formulerar en första miniminivå för nästa produktionsförsök och Oracle behandlas som externt beroende i piloten | Sofia, Lena, Amir, Mats, Karin | 5 |
| Dag 1 eftermiddag | Karin signalerar att hon tänker prata med Elin om tekniskt ägarskap; Sofia kräver tid, mandat, folk och prioritering | Karin, Sofia | 5 |
| Dag 1 senare eftermiddag | Karin leder värdeflödeskartläggningen i Björken; väntetider, manuella kontroller och ansvarsglapp blir synliga på tavlan | Karin, Lena, Amir, Sofia, Mats, Elin, Naya, Jonas, Sara | 6 |
| Dag 1 senare eftermiddag | Sofia delar upp problemet i applikationsleverans, plattformens standardförmågor och externa beroenden; behovet av tekniskt ägarskap uttalas | Sofia, Karin, Elin, Lena, Amir, Mats | 6 |
| Dag 1 senare eftermiddag | Elin tar med sig tre saker: frigjord tid, beslutad miniminivå och förslag på tekniskt ägarskap | Elin, Karin, Sofia | 6 |
| Dag 1 senare eftermiddag | Lena och Amir enas om en konkret gemensam timme kring första deploymentmallen med Sofia, Mats vid behov och Naya | Lena, Amir, Sofia, Naya, Mats | 6 |
| Dag 2 förmiddag | Första deploymentmallen testas; pipelinen blir grön men podden blir inte ready på grund av JBoss-/JNDI-/datasource-antaganden | Amir, Sofia, Lena, Mats, Naya, Jonas | 7 |
| Dag 2 förmiddag | Gruppen identifierar fler gamla miljöantaganden kring filsystem, sessioner, konfigurationsfiler, loggar och Elasticsearch-index | Amir, Sofia, Lena, Mats, Naya | 7 |
| Dag 2 förmiddag | Sofia delar upp arbetet i applikation, plattform och externa beroenden; Mats lägger till frågan “Vem väcks?” | Sofia, Mats, Lena, Amir, Karin | 7 |
| Dag 2 förmiddag | Amir meddelar Sara att bakslaget är både en försening och ett viktigt fynd | Amir, Sara | 7 |

| Dag 2 förmiddag | Gruppen analyserar MQ-spåret och formulerar miniminivå för persistens, idempotens, dead-letter, backlogg, incidentansvar och självservicegränser | Mats, Lena, Amir, Sofia, Karin, Annika, Sara, Peter, Elin | 8 |
| Dag 2 förmiddag | Sofia säger att hennes tekniska samordning inte är hållbar informellt; Lena markerar att Sofia inte ska bli nästa informella nyckelperson | Sofia, Lena, Karin, Elin, Mats, Amir | 8 |
| Dag 2 förmiddag | Elin säger att tekniskt ägarskap tas till styrgruppen och att piloten inte får nytt produktionsdatum förrän miniminivån är beslutad och bemannad | Elin, Karin, Sofia, Lena, Amir, Mats | 8 |
| Dag 2 efter mötet | Amir ber Mats om historisk driftkunskap från en incident 2019 med dubblettmeddelanden | Amir, Mats | 8 |
| Dag 3 förmiddag | Karin och Sofia konkretiserar villkor för tekniskt ägarskap: mandat, tid, standardforum, tydliga gränser och flera bärare | Karin, Sofia | 10 |
| Dag 3 förmiddag | Elin ansluter och får ett beslutsunderlag inför styrgruppen; minst 50 procent av Sofias tid och minst två ytterligare personer blir centrala krav | Elin, Karin, Sofia | 10 |
| Dag 3 förmiddag | Lena ansluter och formulerar driftens villkor: forumet ska bygga bort sena manuella kontroller, inte skapa ännu en möteskö | Lena, Karin, Sofia, Elin | 10 |
| Dag 3 förmiddag | Karin lovar Sofia att säga ifrån om organisationen försöker ge henne rollen utan villkoren | Karin, Sofia | 10 |

| Dag 4 | Gruppen fattar Oracle-beslutet: databasen flyttas inte in i containerplattformen i första steget; datakontrakt, anslutningsmönster, schemaändringar, testdata och incidenttriage ska definieras och bekräftas | Sofia, Karin, Elin, Lena, Mats, Amir, Naya | 12 |

| Dag 3 förmiddag | Elin tar prioriteringsfrågan till styrgruppen och får beslut om två veckors prioriterad bemanning för Pilotväg 0.1 | Elin, Per, Henrik, Maria | 14 |
| Dag 3 förmiddag | Styrgruppen avgränsar beslutet till Kundportal Meddelandehantering och kräver dokumentation av vad som byggs bort respektive flyttas | Elin, styrgruppen | 14 |
| Dag 3 eftermiddag | Elin och Lena går igenom vilka driftaktiviteter som flyttas, skyddas eller kräver ersättare | Elin, Lena, Mats | 14 |
| Dag 3 eftermiddag | Lena etablerar regeln Inga sidodörrar för att skydda driftgruppen från informella extra uppdrag i piloten | Lena, Elin, Mats, driftgruppen | 14 |
| Dag 3 eftermiddag | Amir bekräftar att teamet pausar refaktorering och fokuserar på felvägar och runbook | Amir, Sofia, Karin, teamet | 14 |

| Dag 8 förmiddag | Förproduktionstest av Oracle timeout visar att readiness kan ljuga och att tjänsten fortsätter konsumera vid beroendefel | Naya, Amir, Sofia, Lena, Mats, Karin, Jonas | 15 |
| Dag 8 eftermiddag | Efter åtgärd upptäcks ett blockerande kompensationsfel där meddelanden hamnar i felkö; produktionsfönster flyttas | Naya, Amir, Sofia, Lena, Mats, Sara, Karin | 15 |
| Dag 8 eftermiddag | Amir ber Lena om ursäkt efter att ha fallit tillbaka i gammal frustration; gruppen formulerar stoppet som att den nya vägen fungerar före produktion | Amir, Lena, Karin, Sofia, Naya | 15 |

| Natt efter begränsad aktivering | MQ-backlogg växer och Oracle-latens ökar; gruppen pausar konsumenter enligt runbook, identifierar ett osynligt nattjobb och stabiliserar utan rollback | Mats, Sofia, Amir, Lena, Naya, Karin, Peter, Annika | 16 |

| Dag efter nattincident | Efterrapporten hålls utan syndabock; gruppen beslutar om Pilotväg 0.2, namngivna bärare och förstärkt verksamhetshälsa | Karin, Lena, Amir, Sofia, Mats, Elin, Peter, Annika, Naya | 17 |

| Efter efterrapporten | Pilotväg 0.2 godkänns för nästa begränsade produktionsfönster; ansvarstabell, verksamhetshälsa, MQ-larm och beroendekarta används som beslutsunderlag | Lena, Karin, Sofia, Amir, Mats, Annika, Peter, Naya, Elin | 18 |
| Styrgrupp efter Pilotväg 0.2 | Elin får fortsatt prioriterad bemanning och uppdrag att ta fram permanent plattformsförmåga; Lenas nya roll ska utredas med avsatt tid | Elin, styrgruppen, Karin, Sofia, Lena | 18 |
| Nästa produktionsfönster | Begränsad produktionsaktivering genomförs odramatiskt; gruppen hanterar en gul verksamhetshälsosignal utan panik och håller kvar begränsad nivå | Lena, Sofia, Amir, Mats, Naya, Annika, Peter | 18 |

## Efter romanens slut

- Containerplattformen är inte färdig, men Pilotväg 0.2 har visat en fungerande riktning.
- Lena går mot en konkret roll kring driftbarhet, governance/kvalitet och plattformsflöde, med krav på avsatt tid.
- Amir förändrar sitt teams syn på självservice: snabbhet måste bygga på driftbarhet, felvägar och ansvar.
- Karin får ett tydligare förändringsledningsmandat.
- Sofia fortsätter som tekniskt ansvarig för pilotens standardmönster och rör sig mot varaktigt plattformsansvar.
- Mats kan bli bärare av operativ driftkunskap i den nya modellen, om rollen inte läggs ovanpå ordinarie drift.
- Sofia och Amir har en försiktig romantisk öppning, med professionella gränser kvar.
