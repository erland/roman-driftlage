# Kapitel 13 – Självservice med räcken

När Lena kom in i rummet stod Sofia redan vid tavlan.

Det var i sig inget ovanligt. Sofia hade en vana att komma före möten, inte för att småprata eller muta in plats, utan för att ordna rummet så att det gick att tänka i det. Hon hade dragit undan två stolar som annars skulle ha skymt tavlan, lagt pennorna i en rad och skrivit fem ord högst upp:

**Bygg. Kontrollera. Släpp. Se. Ångra.**

Lena stannade i dörren.

“Det låter nästan poetiskt.”

Sofia vände sig om. Hon såg trött ut, men inte på samma sätt som driftpersonalen brukade se trött ut. Hennes trötthet var mer koncentrerad, som om hon hade tänkt för många tankar samtidigt och inte hunnit lägga ner någon av dem.

“Det är livscykeln jag vill att vi ska designa för”, sa hon. “Inte bara deploy.”

Lena hängde av sig jackan över stolsryggen. Hon hade egentligen tänkt säga något om att designa för verkligheten också, men orden fastnade. Det var för tidigt på morgonen för reflexmässigt motstånd, och Sofia hade varit tydlig de senaste dagarna på ett sätt Lena inte kunde avfärda.

På bordet låg utskrivna kopior av Oracle-beslutet, MQ-miniminivån och listan från standardforumet. Någon hade ringat in frasen **självservice inom beslutad väg** med blå penna.

Självservice. Lena hade fortfarande svårt för ordet. Det lät som en obemannad bensinstation, något där ansvaret försköts till den som råkade stå med slangen i handen. Men hon hade börjat förstå att det inte var ordet hon var emot. Det var bilden av självservice som en lucka där drift förväntades försvinna.

Dörren öppnades bakom henne. Amir kom in med sin dator under armen och telefonen i handen. Han såg först på tavlan, sedan på Sofia.

“Bygg, kontrollera, släpp, se, ångra”, läste han. “Ångra?”

“Rollback”, sa Lena.

“Eller kompensation”, sa Sofia. “Eller stopp innan skada uppstår. Men ja. Vi behöver kunna ångra utan att uppfinna processen under incidenten.”

Amir nickade. Inte snabbt, inte med den där otåliga rörelsen han hade haft i början, utan långsammare. Som om han lärt sig att ett nick ibland kunde bli ett löfte.

Karin kom sist. Hon bar på en kaffemugg, sin anteckningsbok och en bunt gula lappar som såg ut att ha följt henne genom halva myndigheten.

“Bra”, sa hon. “Alla här. Elin ansluter sista halvtimmen. Naya kommer efter testmötet. Mats är på patchgenomgång men har lovat att komma förbi när vi bråkar om körboken.”

“Han sa faktiskt så?” frågade Amir.

“Nej”, sa Karin. “Han sa att ni inte fick skriva något dumt utan honom.”

Lena kunde inte låta bli att le.

Karin slog sig ner, men öppnade inte datorn. Hon såg på orden på tavlan.

“Dagens mål är inte att lösa hela plattformen”, sa hon. “Det är att definiera första självservicevägen för piloten. Tillräckligt smal för att gå att använda. Tillräckligt tydlig för att drift inte ska behöva gissa. Tillräckligt automatiserad för att utveckling inte ska behöva vänta på manuell tolkning varje gång.”

Lena hörde sin egen invändning innan hon sa den.

“Och tillräckligt säker för produktion.”

Karin nickade.

“Ja. Men jag vill att vi pratar om säker som något vi bygger in, inte något du personligen måste upptäcka sist.”

Det träffade mer än Lena ville visa.

Hon hade ägnat år åt att upptäcka saker sist. Fel kontaktlistor. Saknade certifikat. Testfall som inte betydde vad de påstod. Beroenden som fanns i produktion men inte i arkitekturbilden. Hon hade blivit bra på att känna igen luckor, men skickligheten hade börjat likna ett straff. Ju mer hon såg, desto mer hamnade hos henne.

Sofia skrev under de fem orden:

**1. Template**  
**2. Pipeline**  
**3. Policy**  
**4. Observability**  
**5. Runbook**

“Det här är första versionen”, sa hon. “Inte en vision. En faktisk väg.”

Amir öppnade datorn.

“Vi har redan en Helm-chart från teamet. Den behöver putsas, men den kan bli basen.”

Sofia skakade på huvudet.

“Den kan bli input. Basen måste ägas av plattformen, inte av ert team.”

Amir såg upp. Lena såg irritationen blixtra till, men den stannade inte lika länge som förr.

“För att andra team ska kunna använda samma mönster?”

“För att ni inte ska bli undantaget som alla sedan kopierar fel”, sa Sofia. “Och för att drift inte ska behöva förstå varje teams egen tolkning av samma problem.”

Lena lade till:

“Om det står Kundportal-special i alla fält har vi inte byggt självservice. Då har vi byggt ett nytt beroende till Amir.”

“Det finns värre beroenden”, sa Amir, men log svagt.

Det var ett annat sorts skämt än tidigare. Mindre försvar, mer försök.

De började med templaten.

Först gick det fort. Namnstandard. Resursgränser. Readiness och liveness. Miljövariabler. Secrets. Image-taggar. Namespace. Kontaktuppgifter. Klassning. Loggnivå. Sofia skrev, Amir fyllde i, Lena strök under sådant som behövde vara obligatoriskt.

Sedan fastnade de på health checks.

“Readiness ska kontrollera att tjänsten kan ta emot trafik”, sa Sofia. “Men inte nödvändigtvis att alla externa system är uppe, annars drar vi ner applikationen för beroenden den kanske kan hantera med kö eller degradering.”

“Så vad är rätt?” frågade Karin.

Det var en bra fråga eftersom den inte låtsades att tekniken hade ett rent svar.

Amir lutade sig bakåt.

“För vår tjänst behöver den kunna prata med Oracle för vissa läsningar, men inkommande meddelanden kan ligga kvar i MQ vid kortare störning. Elasticsearch påverkar sök, inte hela tjänsten.”

Lena hörde hur han resonerade högt snarare än argumenterade. Det gjorde honom lättare att lyssna på.

“Då behöver vi skilja på startbar, trafikredo och verksamhetsfrisk”, sa Sofia.

Hon skrev tre rader:

**Liveness: processen lever.**  
**Readiness: tjänsten kan ta emot trafik enligt definierad miniminivå.**  
**Verksamhetshälsa: beroenden och flöden fungerar, visas i dashboard/larm.**

Lena kände hur något lade sig på plats. Inte för att allt blev enkelt, utan för att orden skilde mellan saker som tidigare hade blandats ihop. En grön endpoint skulle inte längre få låtsas vara hela sanningen.

“Verksamhetshälsa måste synas för incidentledningen”, sa hon. “Inte bara för teamet.”

“Ja”, sa Amir. “Och för oss. Vi har haft för lite insyn när något händer efter deploy.”

Lena såg på honom. Det var en liten mening, men den betydde mer än han kanske visste. Den flyttade inte skuld. Den flyttade ansvar närmare dem båda.

Karin satte en gul lapp under tavlan.

**Grönt betyder vad vi har beslutat att grönt betyder.**

“Den där får inte bli en slogan”, sa Lena.

“Nej”, sa Karin. “Den får bli ett krav.”

När Naya kom in en halvtimme senare hade tavlan redan börjat se farlig ut. Inte farlig på det gamla sättet, där allt var otydligt, utan på det nya sättet där otydligheten inte längre kunde gömma sig.

Hon ställde datorn på bordet och såg på listan.

“Har ni skrivit felvägarna än?”

“Vi har precis kommit dit”, sa Amir.

“Bra. Då hann jag innan ni kallade dem edge cases.”

Lena uppskattade henne omedelbart lite mer.

Naya tog en penna och skrev utan att fråga:

**MQ nere**  
**Oracle timeout**  
**Elasticsearch långsam**  
**Fel secret**  
**Fel schema version**  
**Pod startar men kan inte behandla meddelande**  
**Dubbel leverans**  
**Rollback efter partiell migrering**

Rummet blev tystare för varje rad.

Amir såg på listan och drog handen över hakan.

“Det där är inte en testlista. Det är en domedagskalender.”

“Det är en testlista”, sa Naya. “Det är bara att vi brukar låtsas att den inte finns förrän efteråt.”

Sofia pekade på rollbackraden.

“Den behöver in i pipelinekravet. Inga schemaändringar utan klassning: reversibel, framåtkompatibel eller kräver kompensation.”

“Det kommer sakta ner oss”, sa Amir.

Han sa det utan skärpa, nästan som en konstaterad naturlag.

“Ja”, sa Lena. “Vissa saker ska sakta ner oss.”

Där var den gamla Lena, tänkte hon. Men när hon hörde meningen i rummet kändes den inte som ett nej. Den kändes som en gräns som gick att förstå.

Amir mötte hennes blick.

“Så länge det saktar ner oss tidigt, inte klockan fem dagen före produktionsfönstret.”

“Det är hela poängen”, sa Lena.

Karin skrev på en ny lapp:

**Tidigt nej > sent stopp.**

Den här gången protesterade ingen mot sloganrisken.

De gick vidare till pipelinen.

Sofia ville ha automatiska kontroller för obligatoriska fält, image-sårbarheter, resursgränser, godkända base images, secrets-referenser, loggformat och deploymentstrategi. Amir ville att pipelinefel skulle vara begripliga nog att teamet kunde rätta dem utan att skapa ett ärende. Lena ville att vissa kontroller skulle vara blockerande och andra bara varna.

Det var där konflikten återvände.

“Om för många kontroller blockerar”, sa Amir, “kommer teamen börja leta vägar runt pipelinen.”

“Om för få blockerar”, sa Lena, “kommer drift få leta fel i produktion.”

“Då behöver vi definiera vad som är blockerande i piloten”, sa Sofia. “Inte utifrån vad som vore perfekt, utan utifrån vad som är miniminivå för skarp drift.”

Hon ritade två kolumner.

**Blockerande** och **Varning**

De fyllde dem långsamt.

Blockerande:
- saknad rollback- eller kompensationsplan
- saknad incidentkontakt och bemanning
- otillgänglig beroendedokumentation
- inga resursgränser
- ej godkänd imagekälla
- avsaknad av logsökbar korrelationsnyckel
- schemaändring utan klassning
- MQ-flöde utan dead-letter-hantering

Varning:
- icke-optimal loggnivå i test
- saknad prestandabaslinje om volymen är låg och beslut finns
- teknisk skuld dokumenterad med åtgärdsdatum
- dashboard saknar verksamhetsvy men tekniskt larm finns

När de var klara kände Lena både lättnad och oro. Lättnad för att mycket av det hon brukade bära i huvudet nu stod på tavlan. Oro för att det därmed också kunde ifrågasättas. Ett krav i hennes huvud var säkert på ett särskilt sätt. Det behövde ingen kompromiss. Ett krav på tavlan kunde förhandlas, tolkas, prioriteras.

Men kanske var det just därför det kunde bli hållbart.

Mats dök upp strax före lunch. Han ställde sig i dörren med en kaffekopp och såg på tavlan som om någon hade monterat isär hans verktygslåda och sorterat skruvarna efter färg.

“Ni har haft roligt.”

“Vi har sparat körboken åt dig”, sa Karin.

“Det var omtänksamt. Eller hotfullt.”

Han gick fram till tavlan och läste de blockerande kraven. Vid dead-letter-hantering nickade han kort. Vid incidentkontakt gjorde han en min som kunde betyda godkänt eller magsår.

Sedan pekade han på “runbook”.

“Om den här ska vara användbar klockan tre på natten ska den inte börja med bakgrund och syfte.”

“Vad ska den börja med?” frågade Amir.

Mats såg på honom.

“Hur vet jag att det är den här tjänsten som bråkar? Vad är farligt att göra? Vem får fatta beslut? Hur stoppar jag inflödet utan att tappa meddelanden? Hur ser jag om kön växer? Hur ser jag om Oracle är orsak eller symptom? Hur backar vi utan att skapa dubbletter?”

Naya skrev medan han pratade.

Lena såg Amir lyssna. Inte försvara sig, inte förklara hur teamet hade tänkt, utan faktiskt lyssna. Hon undrade om hon hade missat sådana ögonblick tidigare för att hon varit så upptagen med att vänta på nästa invändning.

“Vi kan skriva första versionen tillsammans”, sa Amir.

Mats höjde ögonbrynen.

“Tillsammans som i att du skickar ett dokument till mig för granskning fredag 16.12?”

“Tillsammans som i att vi sitter en timme efter lunch.”

Mats såg nästan besviken ut över att inte kunna avfärda svaret.

“Jag har patchplanering.”

Lena öppnade munnen, men Karin hann före.

“Är patchplaneringen blockerande för dig personligen, eller kan Elin hjälpa till att prioritera om?”

Mats skrattade till.

“Du frågar som om svaret inte är ‘både och’.”

“Jag frågar för att om det här alltid görs i mellanrummen kommer det aldrig bli klart.”

Rummet blev stilla igen.

Det var något med Karins röst när hon sa det. Inte den mjuka workshoprösten, inte den avväpnande. Den hade en kant nu, en tydlighet som fick Lena att förstå att Karin också höll på att förändras. Hon faciliterade inte längre bara andras insikter. Hon började kräva konsekvenser av dem.

När Elin anslöt efter lunch hade tavlan blivit full, och Sofia hade flyttat över delar till ett dokument med rubriken **Pilotväg 0.1**.

Elin läste sammanfattningen i tystnad. Hon ställde några frågor om tid, bemanning och vad som krävdes för att boka nytt produktionsfönster.

Sofia svarade utan att titta på Amir.

“Vi behöver tre saker innan datum sätts. Ett: pipelinekontrollerna för blockerande krav ska vara implementerade eller manuellt verifierade enligt beslutad checklista. Två: runbook ska vara genomgången av drift och team. Tre: felvägstesterna för Oracle timeout, MQ-stopp och rollback/kompensation ska vara körda i förproduktion.”

“Hur lång tid?” frågade Elin.

Ingen svarade direkt.

Lena kände den gamla impulsen: säg inget som kan bli ett löfte. Amir såg ut som om han räknade. Sofia såg på listan, inte på människorna. Karin väntade.

“En vecka om vi får rätt personer”, sa Amir till slut. “Tre om vi ska göra det mellan allt annat.”

Elin såg på honom, sedan på Lena.

“Stämmer det?”

Lena ville säga att det var optimistiskt. Hon ville säga att allt alltid tog längre tid. Men hon hörde också skillnaden i Amirs svar. Han hade inte sagt “en vecka”. Han hade sagt “om vi får rätt personer”.

“Ja”, sa hon. “Det är rimligt.”

Elin skrev något.

“Då tar jag det som beslutsunderlag. En vecka med prioriterad bemanning, annars tre och ökad risk.”

Karin nickade.

“Det behöver sägas så i styrgruppen. Inte som att teamet eller drift är långsamma.”

Elin tittade upp.

“Du tänker säga det åt mig om jag inte gör det?”

“Ja”, sa Karin.

Det blev tyst.

Sedan log Elin, trött men äkta.

“Bra.”

När mötet upplöstes satt Lena kvar en stund. Tavlan var fortfarande full av krav, pilar och lappar. Det borde ha känts som mer arbete. På ett sätt gjorde det det. Men det var en annan sorts arbete än det som brukade vänta på henne i ärendekön.

Det här arbetet gick att peka på.

Det gick att dela.

Det gick kanske till och med att bygga bort.

Amir samlade ihop sina saker men stannade vid stolen bredvid henne.

“Det där du sa”, började han.

Hon såg på honom.

“Jag sa ganska mycket.”

“Att vissa saker ska sakta ner oss. Jag hatade den meningen i ungefär tre sekunder.”

“Bara tre?”

“Sedan insåg jag att jag hatade mest att det brukade hända sent.”

Lena lutade sig tillbaka. Hon hade inget färdigt svar, och för första gången kändes det inte nödvändigt.

“Sent stopp är dyrt”, sa hon.

“Tidigt nej är också irriterande.”

“Det är inte samma sak som dyrt.”

Han log lite.

“Nej.”

Sofia kom fram till dem med datorn under armen.

“Jag skickar ut Pilotväg 0.1 om en timme. Inga sidodiskussioner i Teams innan dess, tack.”

Amir lade handen över hjärtat.

“Jag skulle aldrig.”

Sofia såg på honom tills han sänkte handen.

“Jag ska försöka att aldrig”, sa han.

Lena reste sig.

“Det är ett bättre krav.”

På väg tillbaka till sin plats plingade det i hennes telefon. Ett nytt incidentärende. En integration som börjat svara långsamt. Hon kände den välbekanta tyngden landa i kroppen, men den fyllde inte hela henne.

Bakom henne hörde hon Mats säga till Amir:

“Om vi ska skriva körbok börjar vi med vad man inte får göra.”

“Är det en driftgrej?” frågade Amir.

“Det är en överlevnadsgrej.”

Lena gick vidare genom korridoren.

På väggen satt fortfarande affischen med texten:

**Vi förenklar vardagen för alla.**

Hon hade sett den hundra gånger och blivit irriterad nästan lika många. Nu stannade hon inte, men hon saktade in tillräckligt för att läsa den igen.

För första gången tänkte hon inte att den ljög.

Hon tänkte bara att någon borde ha börjat med att fråga vems vardag som skulle bära förenklingen.
