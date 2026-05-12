# Kapitel 12 – Oracle-beslutet

Sofia hade skrivit ordet **Oracle** högst upp på whiteboarden och sedan låtit pennan vila mot kanten av tavlan.

Det var ett enkelt ord. Sex bokstäver. Ändå förändrade det rummet.

JBoss hade varit svårt, men begripligt. MQ hade gjort människor vaksamma, men det hade funnits en konkret kö att prata om, med meddelanden som antingen fanns där eller inte. Oracle var något annat. Databasen låg under nästan allt, som ett fundament ingen längre riktigt såg förrän någon föreslog att huset skulle flyttas.

I mötesrummet Aspen satt de tätare än vanligt, som om själva ämnet krävde mindre luft. Lena hade valt stolen närmast dörren. Mats satt bredvid henne med armarna i kors och en anteckningsbok han ännu inte öppnat. Amir hade tagit med sin laptop men inte slagit upp den. Naya satt ett halvt steg bakom honom, med testfall utskrivna på papper. Annika från MQ var inte med i dag, men hade skickat tre rader i chatten som Sofia redan visste skulle citeras minst en gång. Karin satt vid kortsidan, inte som mötesledare den här gången utan som den som skulle hålla frågan kvar på marken om den började sväva. Elin hade kommit in sist och stängt dörren efter sig med en beslutsamhet som nästan blev för mycket.

Sofia såg på dem och kände den där välbekanta dragningen: att börja med lösningen.

Det hade varit enklast. Hon kunde säga att de inte skulle flytta Oracle till containerplattformen nu. Hon kunde säga att applikationen skulle containeriseras först, medan databasen låg kvar i befintlig drift med tydliga anslutningsmönster, behörigheter, testdata och ändringsrutiner. Hon kunde rita tre rutor, två pilar och ett antal begränsningar. Det skulle vara sant.

Men om hon började där skulle några höra att hon bromsade. Andra skulle höra att hon äntligen var rimlig. Och båda tolkningarna skulle vara fel på ett sätt som kunde bli dyrt senare.

Hon vände sig mot tavlan och skrev:

**Vad beslutar vi egentligen?**

Mats suckade så lågt att det nästan inte hördes. Nästan.

“Vi beslutar väl om vi ska stoppa in databasen i containervärlden eller inte”, sa Amir.

Sofia vände sig om.

“Det är en formulering.”

“En förenklad formulering.”

“En farlig förenkling.”

Amir drog efter andan för att svara, men hejdade sig. Hon såg att han ansträngde sig. Det syntes i käken, i blicken som först blev skarp och sedan avsiktligt lugnare. Efter deras samtal i Granen hade något förändrats mellan dem, inte till något enklare, men till något mer uppmärksamt. Han försökte inte vinna varje replik lika snabbt. Hon visste inte om hon skulle vara tacksam för det eller mer försiktig.

Karin lutade sig fram.

“Kan vi börja med varför formuleringen är farlig?”

Sofia nickade.

“För att den får det att låta som om valet är tekniskt och binärt. Antingen gammalt eller nytt. Antingen legacy eller modernt. Antingen bromsar vi eller så vågar vi.”

“Är det inte lite så?” frågade Amir.

Lena såg på honom, men sa inget. Sofia hann tänka att det i sig var en framgång.

“Nej”, sa Sofia. “Det verkliga beslutet är vilka delar av dataansvaret vi förändrar nu, vilka vi låter vara kvar, och hur vi gör gränsen så tydlig att applikationsteamet inte behöver gissa och drift inte behöver kontrollera allt manuellt i sista stund.”

Hon skrev på tavlan:

- Databasplattform
- Schemaändringar
- Behörigheter
- Anslutning
- Testdata
- Backup/restore
- Prestanda
- Incidentansvar
- Ägarskap för datakontrakt

När listan var klar blev rummet tystare.

Det var alltid något med listor, tänkte Sofia. När saker stod var för sig såg de mindre ut. När de stod tillsammans syntes vikten.

Mats öppnade sin anteckningsbok.

“Det där”, sa han och pekade med pennan mot tavlan, “är anledningen till att folk som säger ‘bara en databas’ inte ska få kaffe.”

Amir log inte, men Naya gjorde det.

Elin sköt fram stolen lite.

“Jag behöver förstå konsekvensen för piloten. Styrgruppen kommer fråga varför vi inte tar hela steget när vi ändå håller på.”

Sofia hade väntat på den meningen. Hon hade till och med skrivit den i sina egna anteckningar kvällen innan, inte som citat utan som risk.

“För att hela steget inte är ett steg”, sa hon. “Det är ett program.”

Elin såg inte nöjd ut, men hon såg inte heller avvisande ut.

“Utveckla.”

Sofia vände sig mot tavlan igen och ritade tre lager.

Överst skrev hon: **Applikation i container**  
I mitten: **Datakontrakt och anslutning**  
Nederst: **Oracle-plattform**

“Piloten handlar primärt om att få applikationen att fungera i ett nytt deployment- och driftmönster. Vi behöver standardisera hur den får konfiguration, hur den kontrolleras, hur den loggar, hur den rullas tillbaka, hur den larmar och hur teamet tar ansvar för den i produktion.”

Hon pekade på nedersta lagret.

“Oracle-plattformen har egna frågor: licens, patchning, backup, restore, övervakning, prestanda, HA, behörighetsmodell, lagring och driftkompetens. Om vi försöker göra båda förändringarna samtidigt i piloten får vi inte en modig pilot. Vi får en oklar riskklump.”

Lena antecknade något. Det var litet, men Sofia såg det ändå. Lena antecknade när någon sa något som gick att använda.

Amir lutade sig tillbaka.

“Så vi låter databasen vara kvar där den är.”

“Ja”, sa Sofia. “I första steget.”

“Men då sitter vi fortfarande fast i beställningar.”

“Inte nödvändigtvis.”

“Behörigheter, schemascript, testdata, anslutningar. Allt det där går genom ärenden i dag.”

“Därför är beslutet inte ‘Oracle stannar, allt annat som vanligt’. Beslutet måste vara: Oracle stannar som plattform i första steget, men applikationens sätt att använda Oracle standardiseras och görs beställningsbart tidigare, tydligare och delvis automatiserat där det är rimligt.”

Hon hörde själv hur meningen lät. Den var inte vacker. Den skulle aldrig hamna på en affisch om digital förnyelse. Men den kunde kanske överleva kontakt med verkligheten.

Naya bläddrade i sina papper.

“Vad betyder det för test?”

Sofia såg på henne med tacksamhet. Testfrågor kom ofta för sent. Naya hade börjat flytta dem framåt.

“Att testmiljöerna måste ha representativa datakontrakt. Inte produktionsdata, inte full kopia, men tillräckligt realistiska scheman, behörigheter och felvägar. Om applikationen saknar rätt behörighet ska vi veta hur den beter sig innan produktion.”

“Så testfallen ska inte bara visa att frågan fungerar när databasen svarar.”

“Precis.”

Naya nickade långsamt.

“De ska visa vad som händer när den inte svarar. Eller svarar långsamt. Eller när migrationen redan delvis körts.”

Mats tittade på henne.

“Du får gärna komma och säga det där på nästa incidentgenomgång också.”

“Om jag får överleva den första.”

“Det är ingen som överlever sin första incidentgenomgång”, sa Mats. “Man får bara behörighet till nästa.”

Karin log kort, men skrev samtidigt något i sin bok. Sofia undrade om Karin samlade repliker eller risker. Kanske båda.

Elin harklade sig.

“Jag hör riktningen. Men jag behöver ett beslutsförslag. Inte bara resonemang.”

Det var därför Elin var nyttig, tänkte Sofia. Irriterande ibland, men nyttig. Hon lät inte gruppen stanna i välformulerade insikter.

Sofia tog upp ett utskrivet papper från bordet. Hon hade kallat det **Oracle-beslut för pilot – arbetsversion**. Orden kändes för stora och för små samtidigt.

“Förslag”, sa hon. “Ett: Oracle-databasen flyttas inte in i containerplattformen inom pilotens scope.”

Amir såg ner på bordet, men protesterade inte.

“Två: Applikationen får ansluta till befintlig Oracle-plattform via ett beslutat standardmönster. Det ska beskriva secrets, connection pools, timeouts, certifikat om relevant, nätverksöppningar och vem som äger felsökning i respektive del.”

Lena höjde blicken vid “vem som äger felsökning”.

“Tre: Alla schemaändringar för piloten ska ha versionerade scripts, framåtplan, rollback- eller kompensationsplan och verifierade testfall.”

Mats skakade lite på huvudet.

“Rollback för databaser är inte alltid rollback.”

“Nej”, sa Sofia. “Därför står det rollback- eller kompensationsplan. Om vi inte kan backa måste vi veta hur vi tar oss framåt till ett säkert läge.”

Lena nickade en gång. Inte mycket, men tillräckligt.

“Fyra: Testdata och databasbehörigheter beställs inte som fria textärenden i slutet av flödet. De definieras som del av pilotens datakontrakt och tas in i standardforumet innan nästa produktionsfönster bokas.”

Amir lyfte blicken.

“Det där hjälper faktiskt.”

“Det var tanken.”

“Det lät nästan som självservice.”

“Det är självservice med räcken.”

Han såg på henne, och i en sekund fanns Granen där igen, det tysta mötesrummet efter arbetstid, hans fråga om hon skulle kunna säga nej till honom, hennes svar att hon måste kunna det. Hon vände tillbaka blicken mot pappret innan det hann bli synligt för någon annan.

“Fem: Oracle-plattformens framtid utreds separat. Inte som villkor för pilotens första produktionssättning.”

Elin tog pappret när Sofia sköt det över bordet.

“Vad saknas?”

Det var en ovanligt bra fråga. Inte “är vi överens”, inte “kan vi gå vidare”, utan vad saknas.

Lena svarade först.

“Databasteamet.”

Alla såg mot henne.

“Vi kan inte fatta ett Oracle-beslut utan någon som faktiskt äger Oracle-driften.”

Elin drog med pennan längs marginalen på pappret.

“Jag har pratat med deras chef. De kunde inte komma.”

Mats gjorde ett ljud som kanske var ett skratt och kanske inte.

“Då kan de inte heller säga att de inte var med när konsekvenserna kommer.”

Lena gav honom en blick, men den saknade kraft. Hon tyckte samma sak, det såg Sofia.

Karin lade pennan på bordet.

“Det här är viktigt. Är beslutet giltigt om databasteamet inte är representerat?”

Elin blev stilla. Sofia såg hur chefens ansikte ändrades, från framdrift till risk.

“Formellt kan jag ta det vidare”, sa Elin. “Men praktiskt... nej. Inte helt.”

Amir drog handen över hakan.

“Så vi fastnar igen.”

Lena svarade snabbare än Sofia väntat.

“Nej. Vi gör det synligt.”

Amir såg på henne.

“Skillnaden är?”

“Att fastna är när vi väntar på någon utan att säga vad vi väntar på. Synligt är när vi skriver: beslutet kräver databasteamets bekräftelse på de här punkterna senast fredag. Om de inte kan ge det lyfts det som kapacitetsrisk, inte som att drift eller utveckling är långsamma.”

Karin pekade på Lena med pennan.

“Det där vill jag fånga ordagrant.”

Lena såg nästan besvärad ut.

“Gör inte det.”

“Jag gör det ändå, men med bättre kommatering.”

Sofia kände något oväntat i bröstet. Inte lättnad, riktigt. Mer som när en låst mekanism gav ifrån sig ett första litet klick. Lena hade inte bara sagt nej. Hon hade beskrivit ett sätt att hålla beslutet levande utan att låtsas att osäkerheten var borta.

Det var kanske så förändringen skulle se ut, tänkte Sofia. Inte som ett genombrott. Som små formuleringar människor inte hade kunnat säga veckan innan.

Naya höjde handen lite, trots att de inte var i skolan och ingen hade bett om det.

“Jag har en sak till.”

“Ja?” sa Karin.

“Om vi ska ha datakontrakt behöver vi veta vem som får ändra dem. Annars blir det bara ett nytt dokument som ligger efter verkligheten.”

Amir log svagt, stolt på ett sätt han försökte dölja. Sofia såg det och tyckte om honom för det, vilket var opraktiskt.

“Bra”, sa Sofia. “Då lägger vi till datakontraktägare. För piloten borde det vara applikationsteamet för sin användning, databasteamet för plattform och behörighetsmodell, och standardforumet för mönstret mellan dem.”

“Tre ägare?” frågade Mats.

“Tre ansvar, inte tre ägare av samma sak.”

“Det där måste stå väldigt tydligt.”

“Ja.”

Lena lutade sig fram.

“Och incidentvägen?”

Sofia skrev på tavlan: **Incident: var felsöker vi först?**

“Om applikationen inte får kontakt med Oracle behöver vi en första triage. Är podden frisk? Finns secret? Har nätverket öppning? Är behörigheten korrekt? Svarar databasen? Finns connection pool-problem? Vem tittar på vad inom första femton minuterna?”

“Det där är inte ett dokument”, sa Mats. “Det är en körbok.”

“Då gör vi en körbok.”

“Som någon övar.”

Naya nickade direkt.

“Vi kan simulera fel i test.”

Amir såg på henne.

“Hinner vi det?”

Naya mötte hans blick.

“Vill du veta svaret före eller efter produktion?”

Han höjde händerna lite.

“Okej. Poäng.”

Sofia märkte att hon log, och dolde det genom att skriva vidare. Inte för att leendet var fel, utan för att hon behövde hålla rummet i arbete. Det fanns något skört i den här sortens samförstånd. Om någon lutade sig tillbaka för tidigt skulle allt stelna till ord igen.

Elin läste igenom pappret.

“Det här blir ett större beslut än jag hade tänkt.”

Karin svarade mjukt.

“Eller så var beslutet alltid så här stort. Vi har bara slutat kalla det en teknisk detalj.”

Elin såg på henne. För ett ögonblick såg hon tröttare ut än hon brukade tillåta sig.

“Styrgruppen kommer fråga vad det kostar.”

Lena sa ingenting. Mats bläddrade i sin tomma anteckningsbok. Amir tittade på Sofia, men den här gången som om han inte bad henne trolla fram ett svar.

Sofia hörde sig själv säga:

“Det kostar mindre att fatta beslutet nu än att upptäcka gränsen under en incident.”

Det var en sådan mening som kunde missbrukas i en presentation. Men den var sann.

Elin skrev ner den.

“Jag kommer använda det där.”

“Gör det inte till en slogan.”

“Jag lovar inget.”

Mötet närmade sig slutet, men ingen reste sig. Det var ett gott tecken och ett dåligt. Gott, för att de faktiskt arbetade. Dåligt, för att allas kalendrar redan blödde.

Karin sammanfattade med blicken på tavlan.

“Så. Vi har ett preliminärt beslut: Oracle-plattformen flyttas inte in i containerplattformen för pilotens första steg. Vi definierar i stället standardmönster för anslutning, datakontrakt, schemaändringar, testdata, incidenttriage och ansvar. Beslutet kräver bekräftelse från databasteamet senast fredag. Om det inte sker lyfts det som kapacitets- och mandatfråga till Elin, inte som ett vanligt väntande ärende.”

“Lägg till att produktionsfönster inte bokas innan de punkterna är bekräftade”, sa Lena.

Amir öppnade munnen.

Sofia hann se kampen i honom. Den gamla impulsen: invända mot ännu en villkorsrad. Den nya insikten: villkorsraden kanske var det som hindrade dem från att upptäcka bristen för sent.

Han stängde munnen igen.

“Ja”, sa han. “Lägg till det.”

Lena såg på honom. Inte länge, men tillräckligt.

Karin skrev.

Sofia märkte att hennes händer var kalla. Det hände ibland efter möten där hon hållit sig lugn längre än kroppen egentligen orkade. Hon lade pennan på bordet och pressade handflatorna mot varandra under kanten, där ingen såg.

Elin reste sig först.

“Jag tar detta vidare med databasteamets chef och styrgruppen. Sofia, jag vill att du skickar underlaget innan klockan tre. Karin, kan du hjälpa till med beslutsdelen?”

“Ja.”

“Lena, jag behöver att du avsätter någon från drift till körboken.”

Lena hann bli hård i ansiktet innan Elin fortsatte.

“Jag vet. Inte ovanpå allt annat. Jag tar det med din chef.”

Det var kanske första gången Sofia hörde Elin förekomma invändningen innan Lena behövde bära den. Lena verkade också märka det. Hon nickade bara.

“Mats är rätt person”, sa hon. “Men inte om han samtidigt ska hålla ihop patchplanen ensam.”

Mats såg upp.

“Jag uppskattar att bli erbjuden som resurs med tillhörande varningstext.”

“Det är så du ska användas.”

“Som farligt gods.”

“Som specialist.”

Han såg på henne, och något i hans ansikte mjuknade.

“Okej.”

När mötet löstes upp blev Amir kvar vid bordet och stoppade långsamt ner sin laptop i väskan. Sofia torkade tavlan delvis men lät de tre lagren stå kvar. Applikation. Datakontrakt. Oracle-plattform. Det kändes som en karta de skulle behöva igen.

“Du fick igenom mer än jag trodde”, sa Amir.

Hon fortsatte sudda.

“Jag fick inte igenom något. Vi formulerade ett beslut.”

“Det där är en väldigt Sofia-mening.”

Hon vände sig mot honom.

“Är det bra eller dåligt?”

“Det är... användbart.”

Hon borde inte ha tyckt att det var roligt, men det gjorde hon.

Han blev allvarligare.

“Jag ville att du skulle säga att databasen också skulle in. Inte för att jag egentligen visste hur, utan för att jag ville att riktningen skulle vara tydlig.”

“Jag vet.”

“Det stör mig lite att du vet.”

“Det stör mig ibland också.”

Han såg mot tavlan.

“Men det här är bättre.”

“Ja.”

“Långsammare.”

“Ja.”

“Mer verkligt.”

Hon mötte hans blick.

“Ja.”

Det fanns ett ögonblick där. Inte stort. Inte dramatiskt. Bara en liten öppning i en dag fylld av ansvar, där två människor stod kvar efter ett beslut och såg samma kompromiss från varsitt håll.

Sedan stack Karin in huvudet genom dörren.

“Sofia, förlåt. Databasteamets chef kan ta femton minuter nu om du och Elin hinner.”

Ögonblicket stängdes inte hårt. Det lades bara åt sidan.

Sofia tog upp sitt papper.

“Jag kommer.”

Amir drog väskan över axeln.

“Lycka till.”

Hon gick mot dörren men stannade när han sa hennes namn.

“Sofia.”

Hon vände sig om.

“Det där med felvägarna”, sa han. “Vi börjar rita dem i teamet i eftermiddag. Inte bara glada vägen.”

Hon kände hur tröttheten och hoppet, de två mest envisa krafterna i huset, drog åt varsitt håll.

“Bra”, sa hon. “Då har vi något att bygga på.”

När hon gick ut i korridoren stod Karin och väntade med telefonen i handen. Elin var redan halvvägs mot nästa möte.

Karin såg på Sofia.

“Hur känns det?”

Sofia tänkte säga “bra”. Hon tänkte säga “mycket”. Hon tänkte säga att hon inte visste hur länge hon kunde fortsätta vara den som höll isär lager, ansvar och människors förhoppningar utan att själv gå sönder i skarvarna.

I stället sa hon sanningen som gick att använda.

“Som att vi just bestämde oss för att inte låtsas.”

Karin stoppade ner telefonen i fickan.

“Det är ett rätt stort beslut.”

Sofia såg tillbaka mot mötesrummet. På tavlan stod fortfarande de tre lagren kvar, svarta mot vitt.

“Ja”, sa hon. “Det är nog det.”
