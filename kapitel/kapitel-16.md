# Kapitel 16 – Nattläget

Mats hade alltid tyckt att nattincidenter började innan någon ringde.

De började i en liten förskjutning, ett värde som långsamt rörde sig åt fel håll, en kö som växte utan att någon först ville kalla det tillväxt, ett certifikat som någon trodde var bytt, ett beroende som svarade tillräckligt ofta för att inte räknas som nere men för sällan för att vara friskt.

Det var därför han inte litade på tystnad.

Tystnad i drift betydde sällan lugn. Det betydde oftare att något inte hade larmat än.

Han satt hemma vid köksbordet med laptopen uppfälld och en kopp te som hunnit bli mörk och besk. Klockan var 22.41. På skärmen låg övervakningen för kvällens begränsade produktionssättning av Kundportal Meddelandehantering. Inte den stora lanseringen som Amir hade velat ha från början. Inte ens den lansering som styrgruppen först hade trott att de skulle få rapportera som bevis på framdrift.

En kontrollerad aktivering, hade Sofia kallat det.

Mats hade nästan svarat att kontrollerad aktivering lät som en brandskyddsövning i ett fyrverkerilager, men han hade låtit bli. Dels för att Sofia redan såg tillräckligt trött ut. Dels för att hon hade haft rätt.

Efter förproduktionsincidenten hade de gjort det mesta långsammare än någon utanför rummet hade önskat. Readiness kontrollerade nu inte bara om applikationen svarade, utan om den kunde verifiera grundläggande beroenden utan att överdriva sin egen hälsa. Konsumenten mot MQ kunde pausa när Oracle inte svarade. Runbooken hade fått en ny sektion som hette **När systemet är delvis friskt**, vilket Mats tyckte var den mest realistiska rubrik de hittills producerat.

Ändå satt han där.

Inte för att han officiellt var ensam jour. Det var han inte. Det fanns en bemanningslista. Amir var med. Naya var med. Sofia var med. Lena hade sagt att hon skulle vara tillgänglig men inte hålla i varje steg. Annika från MQ var sekundär kontakt. Peter från databassidan hade skrivit att han var nåbar “vid faktiskt Oracle-relaterat behov”, vilket Mats tolkade som att Peter hoppades intensivt på att behovet skulle visa sig vara någon annans.

Men Mats satt där ändå, för han kunde inte låta bli.

Han hade haft sådana här kvällar i kroppen längre än han ville erkänna. Först i serverrum med för kall luft och för höga golv, sedan i kontorslandskap, sedan på distans med övervakningen som ett blått sken mot köksfönstret. Varje ny teknik lovade att göra nätterna mer förutsägbara. Varje ny teknik hittade sedan sitt eget sätt att bli märklig efter klockan tio.

Teamskanalen plingade.

**Naya:** Backlogg på `KPM.IN` ökar långsamt. Inte över tröskel än.

Mats satte ner muggen.

Där var den. Den lilla förskjutningen.

Han klickade upp grafen. Naya hade rätt. Kön växte inte dramatiskt, men den växte med en jämnhet som inte kändes som en tillfällig puckel. Applikationen rapporterade ready. Liveness var grön. Verksamhetshälsan visade gul, vilket i sig var ett framsteg. Förr hade den visat grönt tills någon ringde och frågade varför medborgare inte fick besked.

**Amir:** Jag ser det. Konsumenterna processar, men långsammare än väntat.

Det tog nästan en minut innan nästa meddelande kom. Mats hann föreställa sig hur Amir satt någonstans, kanske hemma, kanske fortfarande på kontoret, med käkarna spända och fingrarna över tangentbordet. För två veckor sedan hade han troligen skrivit att plattformen såg grön ut och frågat om MQ verkligen mätte rätt. Nu skrev han:

**Amir:** Vi behöver anta att vår applikation inte hänger med tills vi vet annat.

Mats märkte att han log, kort och motvilligt.

Det var ett bra första antagande. Inte för att det nödvändigtvis var sant, utan för att det började på rätt sida av ansvaret.

Sofia ringde upp incidentmötet innan någon bad henne. Mats anslöt. Kamerorna var av i början, som de ofta var när människor ville låtsas att natten inte riktigt räknades som arbetstid. Sedan slog Karin på sin kamera, sittande i en svagt upplyst hall eller kanske ett arbetsrum med en bokhylla bakom sig. Håret var uppsatt hastigt. Hon såg inte pigg ut, men hon såg närvarande ut.

“Vi håller oss till runbooken”, sa Sofia. Hennes röst var lugn på det där sättet som inte dolde allvar utan gav det form. “Mats, kan du börja med MQ-bilden?”

Han skulle ha kunnat svara att Annika borde göra det, att han inte längre var den enda som visste, att de faktiskt hade byggt för att fler skulle kunna veta. Men Annika var ännu inte inne i samtalet och kön växte nu snabbare.

“Backloggen ökar på inkommande kö”, sa han. “Inte katastrof. Inte normal. Dead-letter ser ren ut än så länge. Ingen massflytt. Konsumtion sker, men genomströmningen är lägre än den borde vara.”

“Naya?” frågade Sofia.

“Verksamhetsflödet gulmarkerar efter första tröskeln”, sa Naya. “Inga användarfel i portalen än, men statusuppdateringar tar längre tid. Vi har femton ärenden som väntar på slutstatus längre än normalspannet.”

“Oracle?” frågade Sofia.

Peter hade anslutit utan kamera. Hans initialer lyste i en cirkel.

“Databasen är inte nere”, sa han. “Men vi har långsammare svar på vissa skrivningar. Jag ser låsningstendenser på tabellen för meddelandestatus.”

Amir drog in luft, hörbart.

“Det är vår nya tabell.”

“Inte bara er”, sa Peter, och Mats hörde hur han försökte låta mindre spetsig än han kunde ha gjort. “Den skriver mot ett befintligt flöde ni delar historik med.”

“Vi har testat det.”

“Ni har testat det med testdata.”

Det blev tyst en halv sekund. Den sortens tystnad där alla valde mellan att vinna en poäng och att lösa problemet.

Karin hann före.

“Vi parkerar skuld. Vad behöver vi veta för beslut?”

Sofia tog över utan paus.

“Ett: kan vi fortsätta konsumera utan att skapa felaktiga tillstånd? Två: behöver vi pausa konsumenterna enligt runbook? Tre: är rollback eller kompensation aktuell? Amir?”

Mats såg på deltagarlistan medan Amir svarade. Lena hade anslutit. Ingen kamera. Inget meddelande. Bara namnet där i listan, som en hand på en broms hon ännu inte tryckt ner.

“Vi behöver pausa innan backloggen skapar fler halvfärdiga statusar”, sa Amir. “Men jag vill verifiera att paus inte triggar kompensationsjobbet fel igen.”

Naya svarade direkt.

“Den kontrollen finns i nya versionen. Jag kan köra läsverifieringen nu.”

“Gör det”, sa Sofia. “Mats, vad händer MQ-mässigt om vi pausar konsumenten femton minuter?”

Mats tittade på graferna. Det gamla svaret låg redo i honom: Det beror på. Det var alltid sant och nästan aldrig användbart. Det var ett svar man kunde gömma sig bakom när man var rädd att ha fel.

Han öppnade runbooken i stället.

“Enligt de trösklar vi satte klarar verksamheten femton minuter utan användarsynlig påverkan om portalen visar fördröjd status efter två minuter. Vi har inte nått högsta backloggtröskeln. Dead-letter är tom. Jag säger att vi kan pausa, men vi behöver meddela Sara eller jourhavande verksamhetskontakt om statusfördröjning.”

“Jag gör det”, sa Karin.

Mats reagerade på att hon inte frågade om hon borde. Hon bara tog den relationella delen av incidenten, som om den också hörde till systemet. Kanske gjorde den det.

Lena slog på mikrofonen.

“Vem tar beslutet att pausa?”

Frågan var enkel. Den var också allt som de hade bråkat om i femton kapitel av sina arbetsliv, även om ingen av dem skulle ha uttryckt det så.

Förut hade svaret blivit en röra. Drift kunde stoppa. Utveckling kunde åtgärda. Någon chef kunde vilja bli informerad. Någon annan kunde säga att det var tekniskt. Alla kunde efteråt hävda att någon borde ha förstått.

Sofia svarade.

“Jag tar beslutet inom pilotens standardmönster. Amir verkställer i applikationen. Mats och Annika bevakar MQ. Peter bevakar Oracle. Lena, du håller driftens samlade lägesbild och stoppar om du ser risk utanför mönstret.”

Det var nästan exakt så de hade skrivit det. Men skriven text och uttalade ord i skarpt läge var inte samma sak. Mats tittade på Lenas namn i listan och väntade på invändningen.

Den kom inte.

“Bra”, sa Lena. “Säg beslutet tydligt i kanalen också.”

Sofia gjorde det. Inte långt. Inte elegant. Bara tydligt.

**Sofia:** Beslut 22.53: paus av KPM-konsumenter i max 15 min enligt runbook “Delvis friskt system”. Syfte: stoppa ökande halvfärdiga statusar medan Oracle-låsning verifieras. Amir verkställer. Mats/Annika bevakar MQ. Peter bevakar Oracle. Naya verifierar kompensation. Lena håller driftlägesbild. Karin informerar verksamhetskontakt.

Mats läste meddelandet två gånger. Det såg nästan tråkigt ut.

Han hade aldrig älskat tråkiga meddelanden mer.

Amir verkställde pausen. Backloggen började växa snabbare, vilket den skulle. Skillnaden var att de nu visste varför. Det fanns något märkligt lugnande i ett fel som följde den plan man gjort för fel.

Annika anslöt och bekräftade att MQ betedde sig förväntat. Naya rapporterade att kompensationsjobbet inte felklassade pausade meddelanden. Peter hittade två låsande transaktioner och började spåra dem mot en batchkörning som ingen i pilotgruppen hade pratat om.

“Batch?” sa Amir.

Peter lät trött.

“Ja. Befintligt nattjobb. Kör statusstädning. Det brukar inte märkas.”

“Det märks nu”, sa Mats.

Han hade tänkt att det skulle låta syrligt, men orden kom ut mer konstaterande än anklagande. Det brukade inte märkas. Det var halva myndighetens tekniska skuld sammanfattad i fyra ord. Gamla jobb, gamla antaganden, gamla tider på dygnet där system fick vara ifred eftersom människor sov och flöden var lägre. Sedan kom nya tjänster och nya förväntningar och plötsligt gick historiken genom väggen som fukt.

“Finns det dokumenterat som beroende?” frågade Sofia.

Peter suckade.

“Inte i pilotens underlag. I databasens driftkalender, ja. Men inte kopplat till den här tabellen.”

Mats tänkte att det var nu någon skulle säga: Varför visste vi inte det? Och någon annan skulle svara: För att ni inte frågade. Sedan skulle samtalet lägga tio minuter på gamla försvarslinjer.

Det hände inte.

Lena sa:

“Då har vi hittat ett beroende som inte fanns i pilotens karta. Lägg det i incidentloggen. Inte som avvikelse mot person. Som saknat beroende mellan ny tabell och nattjobb.”

Karin skrev något. Mats såg det inte, men han kunde nästan höra pennan.

Sofia bad Peter bedöma om batchen kunde pausas. Peter försvann från samtalet i tre minuter som kändes längre än femton. Under tiden bevakade de backloggen. Den steg. Inte panikartat. Inte ofarligt. Precis i zonen där människor gärna började prata för mycket.

Amir var tyst. Mats undrade vad som rörde sig i honom. Förmodligen allt på en gång: viljan att fixa, rädslan att piloten skulle få skulden, irritationen över ett nattjobb han inte kände till, skammen över att själv ha missat det, och den där envisa kraften som gjorde honom bra när han lyckades rikta den mot problemet i stället för mot rummet.

När Amir till slut talade lät han annorlunda.

“Vi borde ha frågat efter nattjobb kopplade till tabellen.”

Peter hann inte svara.

“Ja”, sa Lena. “Och databassidan borde ha kopplat tabellen till kalendern när schemaändringen granskades. Båda sakerna är sanna.”

Det var så rakt sagt att Mats nästan skrattade. Inte för att det var roligt, utan för att Lena just hade gjort det hon brukade kräva av andra: hållit två ansvar i huvudet samtidigt utan att förenkla bort något.

Peter kom tillbaka.

“Batchen kan pausas efter nuvarande transaktion. Två minuter.”

“Sofia?” sa Lena.

“Vi håller konsumenterna pausade tills Peter bekräftat. Sedan startar vi med reducerad konsumtion i fem minuter och följer backlogg och skrivlatens. Om det stabiliseras fortsätter vi. Om inte går vi till rollbackbeslut.”

“Rollback av vad?” frågade Karin, inte som invändning utan för att få det sagt.

“Applikationsversion och konfiguration”, sa Sofia. “Inte databasen, om vi inte ser felaktiga data. Naya verifierar status innan.”

“Bra”, sa Karin. “Säg det i kanalen.”

Sofia gjorde det.

Mats satt med ena handen över munnen och läste. Han kände något i bröstet som nästan var obehagligt. Inte oro. Inte lättnad. Snarare den ovana känslan av att ett rum faktiskt använde det de hade byggt tillsammans.

Det var inte perfekt. De hade missat nattjobbet. De hade en växande kö. De hade en verksamhetskontakt som snart skulle vilja veta om medborgare påverkades. Men de famlade inte blint efter någon som visste. De gjorde inte Lena till ensam grind. De gjorde inte Amir till ensam fixare. De lät inte Sofia bli informell trollkarl i ett hörn. De följde ett ansvarsmönster som fortfarande var skört men verkligt.

Peter bekräftade pausad batch. Amir startade konsumenterna med reducerad takt. Backloggen planade först ut, sedan började den sjunka långsamt. Oracle-latensen gick ner. Verksamhetshälsan låg kvar gul i ytterligare sju minuter, sedan grön med varning om tidigare fördröjning.

Naya lät nästan förvånad när hon sa:

“Statusarna är konsekventa. Inga felaktiga kompensationer. Inget i felkö.”

“MQ bekräftar”, sa Annika. “Backloggen minskar kontrollerat.”

Mats såg på grafen. Den var inte vacker, men den gjorde rätt sak. Han hade sett många vackra grafer ljuga och många fula grafer tala sanning. Den här var ful nog att lita på.

Lena slog på kameran.

Hon satt inte på kontoret. Hon satt hemma, i ett rum med mörkt fönster bakom sig och en lampa som gav ansiktet skarpa skuggor. Hon såg äldre ut än på dagen, eller kanske bara mindre skyddad.

“Jag vill säga en sak innan vi rundar av”, sa hon.

Ingen avbröt.

“Det här är inte ett bevis på att piloten är riskfri. Det är den inte. Vi hittade ett beroende vi borde ha hittat tidigare.”

Amir nickade, långsamt.

“Men”, fortsatte Lena, “det här är första gången på länge som jag inte behövde välja mellan att stoppa allt eller hoppas att någon hade koll. Systemet gav oss ett mellanläge. Det är viktigt.”

Mats såg ner på sina händer. Han visste inte varför just den meningen tog. Kanske för att han hade byggt så mycket av sitt yrkesliv på frånvaron av mellanlägen. Antingen var det grönt eller så brann det. Antingen litade man eller så kontrollerade man. Antingen var man med på förändringen eller så var man ett hinder.

Mellanlägen krävde mer arbete. Men de kanske också var mer sanna.

Amir slog på sin kamera. Han såg trött ut på ett yngre sätt än Lena, som om tröttheten ännu gjorde honom rastlös i stället för tung.

“Jag vill lägga till att teamet tar nattjobbet som en miss i vår beroendekartläggning”, sa han. “Inte bara databasens. Vi bad om kontrakt, men vi frågade inte tillräckligt om tidssatta jobb.”

Peter hummade.

“Databassidan tar sin del. Vi borde ha flaggat vid schemaändringen.”

Karin lutade sig framåt.

“Då har vi två lärpunkter utan syndabock. Bra. Skriv dem så innan ni hinner bli mer defensiva.”

Det fick till och med Peter att skratta till.

Sofia sammanfattade nästa steg. Batchberoendet skulle in i runbook och beroendekarta. Produktionssättningen skulle fortsätta i begränsat läge över natten med extra bevakning till 01.00. Om backlogg och latens höll sig inom trösklar skulle de inte rulla tillbaka. Om någon av de definierade gränserna bröts skulle rollbackbeslut tas utan ny diskussion om principen.

“Alla okej?” frågade hon.

Det var en märklig fråga, tänkte Mats. Inte “är alla glada”, inte “är alla överens om att detta är optimalt”, utan “är detta tillräckligt beslutat för att vi ska kunna agera”.

En efter en svarade de.

Ja.  
Okej.  
Bekräftar.  
Jag följer MQ.  
Jag följer Oracle.  
Jag stannar i kanalen.

När mötet slutade var klockan 23.38. Mats satt kvar vid köksbordet. Han borde resa sig, sträcka på ryggen, hälla ut det kalla teet. I stället öppnade han runbookens redigeringsläge och började skriva in nattjobbet under beroenden.

Han kom på sig själv med att formulera sig för någon annan.

Inte som en minneslapp till sig själv. Inte som en varning till den som redan visste. Utan som om en människa han aldrig träffat skulle kunna läsa texten klockan två en annan natt och förstå tillräckligt för att inte behöva gissa.

Det tog längre tid.

Det blev bättre.

Teams plingade igen, privat den här gången.

**Amir:** Tack för MQ-lugnet. Och för att du inte sa “vad var det jag sa”.

Mats tittade på meddelandet.

Det fanns många svar han kunde skriva. Några var roliga. Några var sanna. Några var skydd.

Han skrev:

**Mats:** Jag tänkte det bara tre gånger.

Amir svarade med en skrattreaktion.

Efter några sekunder kom ett nytt meddelande.

**Amir:** Seriöst. Det hjälpte.

Mats lät fingrarna vila över tangentbordet. Han var ovan vid att ta emot sådant utan att göra det mindre. Det var lättare att svara med skämt. Skämt höll avståndet lagom stort. Men något med natten, med grafen som långsamt sjönk och runbooken som inte längre bara var ord, fick honom att låta bli.

**Mats:** Ni höll er till planen fast det tog emot. Det hjälpte också.

Han skickade innan han hann ändra sig.

Sedan öppnade han incidentkanalen igen. Sofia hade lagt ut en kort status:

**Sofia:** 23.47: Begränsat läge stabilt. Backlogg sjunker. Oracle-latens normaliserad efter pausat nattjobb. Ingen rollback i nuläget. Nästa kontroll 00.15.

Lena reagerade med en bock.

Det var allt.

Men Mats såg den där bocken och tänkte att Lena kanske också satt kvar någonstans och inte riktigt visste vad hon skulle göra med ett system som för en gångs skull inte krävde att hon bar det ensam.

Han reste sig till slut och hällde ut teet. I fönstret såg han sin egen spegelbild mot mörkret: grått hår, trötta ögon, t-shirt från en konferens om middleware som inte längre fanns. Han hade ibland känt sig som en kvarleva från en äldre driftvärld, en sådan som yngre kollegor lyssnade på av artighet när han berättade om varför saker var farliga.

Men i kväll hade hans kunskap inte varit ett hinder. Den hade varit en del av räcket.

Det var en liten skillnad.

Kanske tillräckligt stor.
