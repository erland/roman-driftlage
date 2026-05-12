# Kontinuitetsanteckningar

## Fasta fakta

- Myndigheten heter **Myndigheten för samhällstjänster**.
- Romanens arbetstitel är **Driftläge**.
- Pilotens tjänst heter **Kundportal Meddelandehantering**.
- Den befintliga tekniska miljön omfattar JBoss EAP, Oracle, IBM MQ och Elasticsearch.
- Containerplattformen är under införande och har ännu inte ett moget arbetssätt.
- Driftön är driftpersonalens arbetsyta i kontorslandskapet.
- Sofia har inte formellt plattformsansvar från början.


- Sofia har en privat anteckningsfil `osorterat.md`.
- Ett konkret problem i piloten är att `MQ_CHANNEL` stavats `MQ_CHANEL`, men det större problemet är att applikationen faller tillbaka på defaultvärde och ändå får grön readiness.
- Karins miniminivåtavla får fyra ord: **frihet**, **räcken**, **ansvar** och **ägarskap**.
- För pilotens nästa produktionsförsök krävs bland annat rollback för image/konfiguration/datamigrering, åtkomlig MQ-dokumentation, definierad incidentbemanning, meningsfull readiness/liveness, loggning/spårbarhet och tydligt Oracle-beslut.
- Oracle ska i piloten behandlas som externt beroende med kontrakt; inget flyttbeslut tas nu.


- I Kapitel 6 leder Karin värdeflödeskartläggningen i Björken under rubriken **Från kodändring till trygg produktion**.
- Mats skriver lappen **HITTA NÅGON SOM VET**, som blir en symbol för personberoende och odokumenterad kunskap.
- Karin skriver **Grupp ≠ ägare** på tavlan när Elin föreslår att gruppen kan äga plattformens arbetssätt.
- Karin skriver i slutet **BYGG SÅ ATT FLER KAN VETA** som motbild till personberoendet.
- Sofia delar upp problemet i tre delar: applikationens leverans, plattformens standardförmågor och externa beroenden.
- Elin lovar inte allt, men tar med sig tre beslutspunkter: frigjord tid, beslutad miniminivå och förslag på tekniskt ägarskap.
- Peter från databassidan deltar digitalt och markerar att Oracle inte ska flyttas in i containerplattformen utan genomtänkt beslut.
- Nästa konkreta arbetssteg är en gemensam timme kring första deploymentmallen med Amir, Lena, Sofia, Mats vid behov och Naya.


- I Kapitel 7 testas första deploymentmallen i Aspen. Pipelinen blir grön men podden blir inte ready.
- Bakslaget beror på att JBoss-applikationen förväntar sig JNDI-/datasource-resurser som den gamla servermiljön tillhandahöll.
- Gruppen upptäcker fler gamla miljöantaganden: skrivbar temporär filsökväg, sessionsantaganden, extern konfigurationsfil, blandad loggstruktur och Elasticsearch-index som applikationen kan skapa vid start.
- Sofia delar upp arbetet i tre kolumner: **Applikation**, **Plattform** och **Externa beroenden**.
- Mats lägger till driftsfrågan **Vem väcks?**
- Ett nytt konkret arbetsobjekt är listan över gamla miljöantaganden som måste göras explicita.
- Amir formulerar till Sara att den gamla miljön dolde beroendet och att den nya mallen gjorde det synligt.


- I Kapitel 8 hålls ett MQ-möte i rummet Granen med Mats som huvudsakligt perspektiv.
- Annika Lind introduceras som MQ-specialist från integration.
- Gruppen identifierar att MQ-frågan inte bara gäller teknisk kökonfiguration utan också verksamhetsrisk, incidentansvar och användarstatus.
- Karins tavla delas in i **Tekniskt beteende**, **Operativt ansvar** och **Verksamhetsrisk**.
- Nya fasta MQ-punkter för piloten: meddelandetyper ska klassificeras, persistens beslutas per meddelandetyp, idempotens/dubbletthantering dokumenteras, dead-letter-hantering får ägare och larm, backloggtrösklar sätts, incidentbemanning anger vem som väcks och för vad, användarstatus får inte ge falsk trygghet och självservicegränser för MQ definieras.
- Peter ställer frågan om vilken komponent som bär sanningen när MQ, Oracle och mottagande system hamnar i olika tillstånd.
- Sofia säger tydligt att hon i praktiken börjat hålla ihop vissa tekniska delar, men att det inte är hållbart informellt.
- Lena säger att Sofia inte ska bli nästa **hitta någon som vet**.
- Elin säger att tekniskt ägarskap tas till styrgruppen och att piloten inte får nytt produktionsdatum förrän miniminivån är beslutad och bemannad.
- Mats nämner en incident från 2019 där meddelanden skickades om efter omstart och skapade dubbletter i mottagande system.

## Karaktärsfakta

- Lena Holm är driftkoordinator och huvudperson i kapitel 1.
- Amir Rahman är utvecklingslead för teamet bakom pilotens tjänst.
- Naya är testare i Amirs team och vågar markera teamets egna brister.
- Jonas är utvecklare i Amirs team, snabb med humor och tydlig frustration över manuella processer.
- Sara är produktägare för teamets arbete och påminner om verksamhetsnyttan bakom tekniken.
- Karin Nyström är agil coach/uppdragsledare med oklart mandat.
- Sofia Berg är senior systemingenjör som senare kan få formellt plattformsansvar.
- Mats Eklund är erfaren drifttekniker och Lenas kollega.
- Elin Varga är sektionschef/sponsor.

## Relationsutveckling

- I Kapitel 6 börjar Lena och Amir göra konkreta åtaganden tillsammans utan att konflikten är löst.
- Karin blir tydligare och vågar synliggöra ledningens otydlighet genom att skriva **Grupp ≠ ägare**.
- Sofia blir mer synlig för gruppen som teknisk helhetstänkare, men markerar för Karin att hon inte har bett om rollen och att ansvar kräver mandat, tid, folk och prioritering.
- Elin ser tydligare att moderniseringen kräver faktiska val, inte bara förväntan om samarbete.


- Lena och Amir startar i konflikt.
- Lena uppfattar Amir som otålig men anar att han inte har helt fel.
- Amir uppfattar Lena som stoppande, men Lenas sista meddelande öppnar för sakligare samarbete.
- Karin börjar se Lena som någon som kan formulera det egentliga systemproblemet.
- Karin identifierar Sofia som möjlig teknisk nyckelperson.
- Sofia visar i Kapitel 5 att hon kan översätta tekniska detaljer till organisatoriskt ägarskap.
- Karin ser Lena som någon som formulerar systemproblemet snarare än bara bromsar.
- Elin erkänner för Karin att organisationen vill ha förändring utan att ha skapat tillräckligt utrymme.
- Amir börjar se att Karin kan hjälpa till att definiera verklig självservice, inte bara försvara stoppet.
- Lena vet vem Sofia är och respekterar henne indirekt.
- Lena och Amir får i Kapitel 3 en första kort skottpaus: Amir erkänner att rollbacken är för tunn och Lena erkänner att manuell granskning av allt inte är rimlig.
- I Kapitel 4 kontaktar Amir Lena mer sakligt inför mötet och erkänner att han förstår bättre varför stoppet kom.
- I Kapitel 5 använder Amir Lenas formulering “inte lägre krav, tydligare krav tidigare”, vilket visar en liten men viktig rörelse mot gemensamt språk.
- Naya fungerar som intern motkraft i teamet och hindrar självserviceargumentet från att bara bli klagomål.
- Sara påminner Amir om att verksamheten väntar på nyttan, inte på en intern arbetssättsdebatt.

- Sofia och Amir får första tydliga professionella kemi i Kapitel 5, men Sofia markerar avstånd när hon märker att Karin observerar dynamiken.
- Lena markerar att en framtida plattformsmodell inte får bli en “Sofia-checklista”, vilket Sofia uppskattar.


- I Kapitel 7 börjar Amir ta ansvar för teamets egna antaganden i stället för att lägga allt på drift.
- Lena ser att teamet faktiskt hittar ett produktionsproblem före produktion och inte pratar bort det.
- Sofia blir tydligare i att prioritering är ett villkor, inte en punkt.
- Amir känner ökande respekt och dragning till Sofia, men håller det professionellt och outtalat.

## Miljöfakta

- Kontoret är ett grått kontorskomplex nära järnvägen.
- Organisationen använder Teams, ärendehantering, incidentkanaler och styrgruppsformat.
- Det lilla projektrummet där Karin arbetar heter **Björken**.
- Teamskanalen för arbetet heter `container-pilot-samverkan`.
- Karin håller miniminivåmötet i projektrummet **Björken** med whiteboard och lappar.
- Amirs teamrum har en Kanban-tavla där kolumnen **Väntar på extern part** i praktiken dominerar.
- Affischer om digital förnyelse och medborgarnytta finns i kontorsmiljön.
- En separat e-tjänst heter **Intygsbeställning** och använder Elasticsearch/sökindex i sitt flöde.

## Ledtrådar och planteringar

- Rollbackplanen saknar databasskript och migrerade statusvärden.
- MQ-dokumentation är inte åtkomlig för driftkoordinering.
- Testprotokollet saknar verifiering med representativ MQ-belastning.
- Readiness-kontroll verifierar bara applikationssvar, inte kritiska beroenden.
- Kontakt- och ansvarsfördelning vid incident är otydlig.
- Karin nämner Sofia som någon som kan se vad andra inte formulerat.
- Karin formulerar pilotens miniminivå genom orden **frihet, räcken och ansvar**.
- Sofia frågar om hon representerar plattformsteknik eller middleware, vilket planterar hennes rolloklarhet.
- Databassidan försöker först hantera mötet asynkront, vilket visar ansvarsglapp kring databasfrågor.
- Ett felaktigt reindex-jobb i produktion startas 09.47 via tekniskt konto och orsakar långsamhet i Intygsbeställning.
- Lena har en privat anteckningsfil `drift_komihag.txt`, vilket visar att viktig driftkunskap inte är systematiserad.
- Ett certifikat för integration mot en extern myndighet riskerar att löpa ut söndag 17 maj, med oklar systemägarkontakt och bristande uppföljning.
- Frågan “vem äger paved road?” planteras via Sofias anteckningar.
redundant endpoint i konfiguration.
- Teamets flödesbild visar väntan kring testmiljö, brandvägg, Oracle-schema, tekniskt konto, MQ-flöde och Elasticsearch-index/retention.
- Teamet markerar sina egna brister med blå penna: bland annat tunn rollback, för svag readiness och otydligt incidentansvar.
- Amir formulerar: "Vi behöver inte mindre drift. Vi behöver drift tidigare, tydligare och mer automatiserat" samt att teamet måste äga mer av det som händer efter deployment.

## Öppna frågor

- Vilka minimikrav ska gälla för pilotens produktionssättning?
- Hur ska ett nytt arbetssätt för piloten se ut?
- Vilket mandat har Karin egentligen?
- Vem från databassidan kan delta med mandat?
- När och varför får Sofia formellt plattformsansvar?
- Kommer Elin frigöra tid och prioritet för förändringen?
- Kommer teamets flödesbild och driftens miniminivå kunna förenas i en gemensam modell?
- Hur påverkas Amir av Sofias närvaro när hon kommer in mer aktivt?

## Saker som måste följas upp

- Amirs svar på Lenas sista meddelande är nu delvis följt upp: han kontaktar Lena inför mötet och säger att han förstår bättre varför stoppet kom.
- Det gemensamma mötet om pilotens miniminivå med Lena, Amir, MQ-kompetens, databaskompetens, Mats, Sofia och Elin inledningsvis.
- Karins roll som coach kontra uppdragsledare.
- Driftens belastning av incidenter, certifikat, patchar och manuella kontroller.
- Lenas punkter inför mötet: krav ska komma före granskning, självservice kräver automatiska spärrar, drift måste kunna se beroenden, incidentansvar måste vara konkret och förändring kräver kapacitet.
- Utvecklingsteamets perspektiv på väntan och frustration.

## Saker som inte får motsägas

- Lena stoppar inte piloten av prestige, utan av verkliga produktionsrisker.
- Utvecklingsteamet är inte oansvarigt; de underskattar bara vissa produktionskrav.
- Sofia ska introduceras gradvis och få mandat senare.
- Självservice ska beskrivas som ansvar inom tydliga ramar.


- I Kapitel 9 blir Sofia och Amir kvar i Granen efter MQ-mötet och får ett lågmält samtal om självservice, ansvar och den möjliga plattformsrollen.
- Amir formulerar att utvecklingsteam ofta ritar den glada vägen och blir irriterade när drift frågar om den olyckliga vägen.
- Sofia säger att teamen vill runt väntan och otydlighet, men att det kan se ut som att de vill runt driftansvaret eftersom ansvaret idag ligger inbakat i manuella steg.
- Sofia tänker att en formell roll inte bara är en titel: ansvar utan mandat gör henne till eskaleringspunkt, mandat utan tid gör henne till flaskhals, och mandat utan accepterade nej gör rollen till dekoration.
- Sofias villkor för formellt tekniskt ägarskap: mandat att säga nej, frigjord tid från löpande ärenden, tydliga gränser mot drift/utveckling/integration, beslutat forum för standarder och minst två personer till som kan bära plattformsförmågan.
- Sofia svarar Karin att hon kan prata om tekniskt ägarskap, men att samtalet måste handla om villkor och inte bara rollnamn.
- Sofia och Amir får en tydligare personlig laddning; de konstaterar indirekt att ett framtida mandat kan komplicera relationen.


## Efter Kapitel 10

- Sofias möjliga formella ansvar avgränsas först till **pilotens standardmönster**, inte hela framtida plattformen.
- Fem beslutspunkter tas fram till styrgruppen:
  1. Sofia får tekniskt plattformsansvar för pilotens standardmönster.
  2. Minst 50 procent av Sofias tid frigörs under pilotfasen.
  3. Ett standardforum för piloten etableras med mandat att besluta godkända mönster och hantera avvikelser öppet.
  4. Driftens deltagande ska bygga bort sena manuella kontroller genom automation, mallar och tidigare krav, inte skapa fler manuella grindar.
  5. Minst två ytterligare personer ska utses för att bära och dokumentera plattformsförmågan tillsammans med Sofia.
- Nytt produktionsdatum ska inte sättas förrän miniminivån är beslutad, bemannad och verifierad i förproduktion.
- En viktig kommunikationsprincip inför Kapitel 11: Sofias roll ska presenteras som **en tydligare väg, inte en genväg**.
- Karin tar ett tydligt steg från neutral facilitator till uppdragsledare som vågar hålla emot.
- Sofia börjar lita på att Karin kan hjälpa henne skydda villkoren, inte bara rollen.
- Lena visar försiktig respekt för Sofia och formulerar plattformsforumets syfte på ett praktiskt sätt.
- Elin visar tidigare erfarenhet av införanden som såg bra ut i styrgruppen men inte höll i produktion; detta kan fördjupas senare.


- I Kapitel 11 kommuniceras styrgruppsbeslutet: Sofia blir tekniskt ansvarig för pilotens standardmönster, inte för hela framtida containerplattformen.
- Sofia får 50 procent frigjord tid under fyra veckor för pilotens standardmönster.
- Första standardforumets princip är: **Inte allt. Tillräckligt. Beslutat. Dokumenterat. Verifierat.**
- Standardforumet delar ansvar i tre nivåer: **applikation**, **plattform** och **externa beroenden**.
- Inget nytt produktionsfönster får bokas innan miniminivån är beslutad, dokumenterad och verifierad.
- Mats kan bidra till driftbarhetsmönster om patchplanering flyttas och arbetet inte hamnar på övertid.
- Naya föreslås som bärare av testbarhet och felvägar i standardmönstret.
- Elin visar konkret sponsring genom att flytta uppgraderingsmöte och ta ansvar för resurskonflikter.
- Sofia och Amir har fortsatt personlig laddning, men Sofias nya mandat gör relationen professionellt mer komplicerad.


## Kapitel 12 – Oracle-beslutet

- Oracle-plattformen flyttas inte in i containerplattformen inom pilotens första scope.
- Applikationen får ansluta till befintlig Oracle-plattform via ett beslutat standardmönster.
- Standardmönstret ska omfatta secrets, connection pools, timeouts, eventuella certifikat, nätverksöppningar och felsökningsansvar.
- Schemaändringar ska ha versionerade scripts, framåtplan och rollback- eller kompensationsplan.
- Testdata och databasbehörigheter ska definieras som del av pilotens datakontrakt och tas upp i standardforumet.
- Oracle-plattformens framtid ska utredas separat och är inte villkor för pilotens första produktionssättning.
- Beslutet kräver bekräftelse från databasteamet senast fredag.
- Nytt produktionsfönster får inte bokas innan Oracle-punkterna är bekräftade.
- Incidenttriage ska beskrivas som körbok: podd, secret, nätverk, behörighet, databasrespons och connection pool ska kunna kontrolleras tidigt.
- Naya driver frågan om felvägstester och realistiska testfall.
- Amir accepterar att teamet ska rita felvägar, inte bara den glada vägen.
- Lena formulerar skillnaden mellan att fastna och att synliggöra beroenden.


## Kapitel 13 – Självservice med räcken

### Fasta fakta
- Första självservicevägen kallas **Pilotväg 0.1**.
- Självservice definieras som **självservice inom beslutad väg**.
- Pilotväg 0.1 består av template, pipeline, policy, observability och runbook.
- Health checks delas upp i:
  - liveness: processen lever
  - readiness: tjänsten kan ta emot trafik enligt definierad miniminivå
  - verksamhetshälsa: beroenden och flöden fungerar och visas i dashboard/larm
- Blockerande krav inkluderar saknad rollback/kompensationsplan, saknad incidentkontakt, otillgänglig beroendedokumentation, saknade resursgränser, ej godkänd imagekälla, avsaknad av logsökbar korrelationsnyckel, schemaändring utan klassning och MQ-flöde utan dead-letter-hantering.
- Felvägstester som måste följas upp: Oracle timeout, MQ-stopp och rollback/kompensation.
- Mats och Amir ska skriva första versionen av runbook tillsammans.
- Elins beslutsunderlag: en vecka med prioriterad bemanning, annars tre veckor med högre risk.

### Relationsutveckling
- Lena börjar se att krav kan byggas in och delas, inte bara bäras av henne i sen granskning.
- Amir accepterar tydligare att tidiga krav kan ersätta sena stopp.
- Karin visar större skärpa och kräver prioritering snarare än bara samverkan.
- Sofia agerar praktiskt som teknisk samordnare för Pilotväg 0.1.
- Naya blir tydligare bärare av felvägstänkande och testbarhet.

### Öppna frågor
- Kommer styrgruppen att frigöra rätt personer?
- Kommer Pilotväg 0.1 fungera i förproduktion?
- Kan runbooken bli användbar för nattincidenter?


## Kapitel 14 – Det som kostar

- Styrgruppen beslutar om **två veckors prioriterad bemanning** för Pilotväg 0.1, med första avstämning efter en vecka.
- Beslutet avgränsas till **Kundportal Meddelandehantering** och pilotens standardmönster; det gäller inte generell containerplattform, databasplattform, MQ-strategi eller full målarkitektur.
- Flyttade aktiviteter ska dokumenteras; återrapporten ska visa **vad som byggts bort**, **vad som bara flyttats** och vad det betyder för kommande leveranser.
- Elin äger prioriteringen, Sofia får tekniskt mandat inom standardmönstret och Karin håller ihop uppdraget.
- Driftaktiviteter delas upp i **Flyttas**, **Skyddas** och **Behöver ersättare**.
- Certifikatinventeringen får skjutas **en vecka, inte mer**.
- En ny regel etableras: **Inga sidodörrar**. Inga informella “kan du bara”-uppdrag får läggas direkt på drift eller Mats vid sidan av Karin/Sofia.
- Lena kommunicerar till driftgruppen att pilottiden ska bygga bort sena manuella kontroller, inte göra containerplattformen viktigare än drift.
- Amir bekräftar att teamet pausar refaktorering och fokuserar på felvägar och runbook samt verkliga beroenden, inte bara den glada vägen.

## Kapitel 15 – Förproduktionsincidenten

- Förproduktionstestet leds praktiskt av Naya och fokuserar först på **Oracle timeout**.
- Första körningen visar blockerande avvikelse: readiness är grön trots kritiskt beroendefel och tjänsten fortsätter konsumera meddelanden.
- Efter snabb åtgärd fungerar konsumentpaus, röd readiness och larm bättre, men ett nytt blockerande fel upptäcks.
- Kompensationsjobbet tolkar pausad konsumtion som avbruten behandling och flyttar meddelanden till felkö trots att behandlingen inte är korrekt etablerad.
- Produktionsfönstret den aktuella veckan flyttas.
- Sara formulerar att testet visar att den nya vägen fungerar genom att stoppa före produktion.
- Amir ber Lena om ursäkt efter en orättvis kommentar om att hon inte behöver förklara förseningar för verksamheten.
- Sofia säger att det är första gången plattformen säger nej innan Lena behöver göra det ensam.
- MQ-stopp-testet återstår.


## Kapitel 16 – Nattläget

- Begränsad skarp aktivering av Kundportal Meddelandehantering genomförs kväll/natt.
- MQ-backlogg på `KPM.IN` växer långsamt men tydligt.
- Oracle-skrivningar blir långsammare på grund av låsningstendenser kopplade till ett befintligt nattjobb för statusstädning.
- Gruppen använder runbooken för **delvis friskt system** och pausar konsumenter i max 15 minuter enligt beslutad ordning.
- Sofia tar beslut inom pilotens standardmönster, Amir verkställer, Mats/Annika bevakar MQ, Peter bevakar Oracle, Naya verifierar kompensation, Lena håller driftlägesbild och Karin informerar verksamhetskontakt.
- Konsumentpausen triggar inte längre felaktigt kompensationsjobb.
- Efter pausat nattjobb startas konsumenterna med reducerad takt; backlogg sjunker och Oracle-latens normaliseras.
- Ingen rollback krävs i nuläget.
- Nattjobbet ska in i beroendekarta och runbook.
- Lena säger att systemet gav henne ett mellanläge mellan att stoppa allt och att hoppas.
- Amir erkänner teamets del i missad beroendekartläggning; Peter/databassidan tar sin del.
- Mats upplever att hans gamla driftkunskap blir del av räcket, inte ett hinder.


## Kapitel 17 – Utan syndabock

- Efterrapporten efter nattincidenten hålls i rummet Tallen.
- Karin ramar in mötet med tre frågor: **Vad gjorde systemet svårt?**, **Vad gjorde vi rätt trots det?**, **Vad ändrar vi innan nästa gång?**
- Nattjobbet mot Oracle saknades i pilotens beroendekarta.
- Gruppen formulerar lärpunkten att dold produktions- och beroendekunskap aktiveras för sent.
- Verksamhetshälsa ska bli förstaklassignal, inte efterhandsanalys.
- Begränsad aktivering räknas som kontrollerad framdrift, inte full pilotgodkänning.
- Pilotväg 0.2 ska innehålla beroendekarta för schemalagda jobb, förstärkt verksamhetshälsa, separata MQ-larm, tydligare beredskapströsklar och namngivna bärare med avsatt tid.
- Namngivna roller: Amir för utvecklingsbarhet/användbarhet i mönstren, Mats för driftbarhet/gamla miljökanter, Annika för MQ-mönster, Naya för testbarhet/felvägar.
- Oracle i containerplattformen är parkerat för piloten.
- Formuleringen **stoppunkten förklarade sig** blir central för framtida driftkrav.
- Lena lägger till tavelfrågan: **Vad kan systemet bära nästa gång, så att människor slipper bära det ensamma?**


## Efter Kapitel 18

- Pilotväg 0.2 godkänns för nästa begränsade produktionsfönster och prövas odramatiskt.
- Verksamhetshälsa, MQ-larm, Oracle-nattjobb, beroendekarta och tydliga beredskaps-/ansvarströsklar används som praktisk styrning.
- Styrgruppen beslutar om fortsatt prioriterad bemanning och uppdrag att ta fram permanent plattformsförmåga.
- Lenas möjliga nya roll formuleras som att flytta driftbarhet och kvalitet tidigare i plattformsflödet; rollen kräver avsatt tid och får inte bli ett tillägg ovanpå allt annat.
- Karin har tydligt utvecklats från coach/facilitator till förändringsledare som håller i kostnad, mandat och svåra beslut.
- Sofia fortsätter som tekniskt ansvarig för pilotens standardmönster och står mer självklart i sitt mandat.
- Amir och Sofia får en försiktig romantisk öppning med professionella gränser: “inte stillastående”, men varsamt.
- Mats börjar se sin gamla driftkunskap som något som kan byggas in i den nya modellen, inte bara försvaras.
- Slutbilden: ärendekön, systemen och riskerna finns kvar, men arbetet har fått en form fler än Lena kan bära.
