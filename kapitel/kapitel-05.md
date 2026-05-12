# Kapitel 5 – Sofia i utkanten

Sofia Berg hade lärt sig att läsa mötesinbjudningar som andra läste väder.

Det var inte rubriken som betydde mest. Rubriker var ofta fromma förhoppningar. “Avstämning” kunde betyda att någon ville ha beslut utan att säga beslut. “Kort synk” kunde vara fyrtiofem minuter av gemensam osäkerhet. “Workshop” betydde ibland att någon redan hade bestämt sig men ville att andra skulle känna sig delaktiga.

Karins inbjudan hette:

**Containerpilot – miniminivå för säker självservice**

Det var en ovanligt ärlig rubrik.

Sofia såg på den medan hon stod vid kaffemaskinen och väntade på att den skulle sluta låta som en gammal serverfläkt. Hon hade blivit inbjuden med den vaga rollen “plattform/middleware”. Inte plattform. Inte middleware. Båda, med ett snedstreck emellan. Det var en liten sak, men hon fastnade vid den.

Ett snedstreck kunde bära mycket ansvar.

Hon hade arbetat på Myndigheten för samhällstjänster i sju år. Tillräckligt länge för att veta var gamla beslut låg begravda, men inte så länge att hon hunnit bli helt cynisk. Hon hade börjat med integrationsnära utveckling, glidit in i middleware, blivit den som förstod JBoss-konfigurationerna bättre än de flesta och sedan, nästan av misstag, blivit någon som folk frågade när deras problem inte passade i någon ruta.

Det var inte en roll. Det var mer som en läcka i organisationskartan.

Hon hade inget emot att hjälpa. Det var kanske problemet. Hon tyckte om ögonblicket när ett trassligt fel plötsligt fick konturer. När en stacktrace slutade vara brus och blev riktning. När ett möte fullt av åsikter gick att reducera till tre antaganden, två risker och ett beslut som någon borde ha fattat tidigare.

Men hon tyckte mindre om vad som hände efteråt. När någon sa: “Bra, då håller du i det här?” Som om förståelse automatiskt betydde ägarskap. Som om den som kunde formulera problemet också hade fått tid, mandat och team att lösa det.

Kaffet blev klart. Hon tog muggen och gick tillbaka mot sin plats, men hann inte sätta sig innan Teams ringde.

Det var Jonas från Amirs team.

Hon övervägde att låta det gå till missat samtal. Inte av ovilja. Mer av självbevarelsedrift. Hennes förmiddag hade redan bestått av en trasig testpipeline, en diskussion om versionshantering av secrets och ett kort men intensivt samtal med en leverantör som tyckte att “Kubernetes-stöd” var ett acceptabelt svar på alla följdfrågor.

Hon svarade ändå.

“Hej, det är Sofia.”

“Hej. Jonas här. Har du två minuter?”

Det hade ingen någonsin. Två minuter var en social konstruktion.

“Vad gäller det?”

“Vi får inte upp meddelandetjänsten i containermiljön. Eller den går upp, men readiness blir grön fast den sedan inte kan läsa konfigurationen för MQ-kanalen. Amir sitter i ett annat möte och Naya säger att jag inte får kalla det plattformsfel förrän jag frågat någon som faktiskt kan plattformen.”

Sofia satte ner muggen mycket långsamt.

“Bra Naya.”

“Ja, hon är hemsk på det sättet.”

Sofia log trots sig själv.

“Skicka länken till podloggen och deploymentmanifestet.”

“Jag gör det nu.”

Hon fick länkarna, öppnade dem och kände hur arbetsdagen smalnade. Det hände när ett problem blev konkret. Resten av världen fanns kvar, men tappade volym. Hon läste loggen först, inte för att loggar alltid talade sanning utan för att de åtminstone brukade ljuga konsekvent.

Applikationen startade. JBoss initialiserade. Datasource mot Oracle såg ut att registreras, åtminstone på ytan. Sedan kom varningen:

`MQ_CHANNEL not found, using default.`

Hon stannade där.

Default.

Det fanns få ord som hade orsakat mer produktionströtthet än default. Default betydde ofta att någon försökt vara hjälpsam i utveckling och därmed gjort fel osynliga i alla miljöer som inte borde tillåta hjälp.

Hon öppnade manifestet. Variabeln fanns. Eller nästan. `MQ_CHANEL`.

Ett n saknades.

Sofia lutade sig bakåt.

Det var frestande att skriva “stavfel” till Jonas och gå vidare. Men något skavde. Om ett saknat n kunde få readiness att bli grön, då var stavfelet inte problemet. Stavfelet var bara den vänligaste formen problemet hade valt att visa sig i.

Hon ringde upp Jonas igen.

“Ni har en felstavad miljövariabel.”

“Åh nej.”

“Det är inte det värsta.”

“Det där är en öppning jag inte gillar.”

“Applikationen faller tillbaka till defaultvärde när MQ-konfigurationen saknas. Readiness bryr sig inte om att den inte kan prata med MQ. Det betyder att podden kan se frisk ut utan att kunna göra sitt jobb.”

Det blev tyst på andra sidan. Sofia hörde tangentbordsljud och någon som pratade i bakgrunden.

“Så det är därför Lena reagerade på health checks”, sa Jonas till slut.

“Delvis. Ja.”

“Men readiness ska väl inte alltid testa alla beroenden? Om MQ ligger nere vill man kanske inte att allt restartar i panik.”

Sofia blev glad över frågan, vilket hon inte hade väntat sig. Den var bättre än försvar. Den innehöll åtminstone ett försök att förstå systemet.

“Precis. Readiness och liveness är inte samma sak. Liveness ska inte döda applikationen bara för att ett beroende har hosta. Men readiness ska säga om instansen är redo att ta trafik. För en tjänst som ska behandla meddelanden behöver ni definiera vad redo faktiskt betyder. Det behöver inte vara full end-to-end mot allt hela tiden, men det kan inte bara vara att JVM:en svarar.”

“Det låter som en sådan sak som borde finnas i en mall.”

“Ja.”

Hon sa det för snabbt.

Jonas hörde det också.

“Finns det en mall?”

Sofia såg på sin skärm där manifestet låg bredvid Karins mötesinbjudan. Plattform/middleware. Snedstrecket igen. Där, i det lilla mellanrummet, fanns svaret.

“Det finns exempel”, sa hon. “Inte en beslutad mall.”

“Ah.”

Det lilla ordet bar mer än han nog avsett. Ah: då är det därför alla bråkar. Ah: då trodde vi att någon annan hade gjort jobbet. Ah: då är piloten inte bara pilot, den är också verktyget som avslöjar att vägen dit inte finns.

Sofia drog handen genom håret.

“Jag kan hjälpa er justera det här inför mötet. Men jag vill att ni tar med frågan som princip, inte bara som buggrättning.”

“Vilken fråga?”

“Vad ska plattformen garantera? Vad ska applikationsteamet garantera? Och vad ska en standardmall för produktionsbar tjänst faktiskt innehålla?”

Jonas var tyst i två sekunder.

“Det låter större än ett n.”

“Det är större än ett n.”

När samtalet var slut satt hon kvar med headsetet på, trots att det inte längre fanns någon röst i det. Hon hade kaffet bredvid sig. Det hade redan svalnat.

Hon öppnade sin privata anteckningsfil. Den hette inte något professionellt. Bara `osorterat.md`, vilket var ironiskt med tanke på hur ofta hon använde den för att skapa ordning åt andra.

Hon skrev:

```text
Containerpilot:
- Saknar beslutad standard för readiness/liveness.
- Applikation faller tillbaka på default vid saknad MQ-konfig. Bör faila tydligt?
- Ingen gemensam mall för produktionsbar containeriserad JBoss-tjänst.
- Ansvarsglapp: team tror plattform ger väg, plattform är fortfarande exempel + god vilja.
- Fråga: vem äger paved road?
```

Hon stannade vid sista raden.

Vem äger paved road?

Det lät som en fråga Karin skulle kunna skriva på en whiteboard. Sofia hade en blandad känsla inför sådana frågor. De kunde vara skarpa, men de kunde också bli en sorts teater där alla nickade åt komplexiteten och sedan gick tillbaka till sina ordinarie köer.

Hon visste redan några av svaren. Inte alla, men tillräckligt.

Utvecklingsteamet kunde äga sin kod, sina tester, sina beroenden och sin driftbarhet. Drift kunde äga produktionskrav, övervakningsprinciper, incidentvägar och operativ erfarenhet. Plattformen kunde äga mallar, policyer, standardiserade byggblock och automatiserade spärrar. Ledningen kunde äga prioriteringen.

Problemet var att “kunde” inte betydde “gjorde”.

Och just nu verkade mycket av det ägas av hopp.

Hon tog kaffemuggen och gick mot projektrummet Björken, där Karins möte skulle hållas. Hon var tidig. Hon tyckte om att vara tidig till rum där hon inte visste vilken roll hon förväntades ha. Det gav henne tid att välja plats.

I korridoren mötte hon Mats.

Han hade en pärm under armen. Sofia visste inte om det var en faktisk pärm med innehåll eller ett statement. Med Mats kunde det vara båda.

“Du är också inkallad till containermässan?” sa han.

“Miniminivåmötet.”

“Det sa jag.”

Sofia gick bredvid honom.

“Har du MQ-underlaget?”

“Jag har tre olika underlag. Ett från teamet, ett från drift och ett från verkligheten.”

“Vilket är pärmen?”

“Verkligheten.”

Hon skrattade kort. Mats såg nästan nöjd ut, men bara nästan.

De gick några steg utan att säga något. Sofia tyckte om tystnader med Mats. De krävde inte omedelbar utfyllnad. Han kunde vara cynisk, men hans cynism var sällan tom. Den kom från för många år av att se organisationen glömma varför gamla spärrar hade satts upp och sedan kalla spärrarna för hinder.

“Jag hörde att du hjälpte Amirs gäng med en MQ-variabel”, sa han.

“Det var ett stavfel.”

“Det brukar allt vara tills det står i incidentrapporten.”

“Det större problemet var att applikationen defaultade och ändå såg frisk ut.”

Mats stannade nästan, men fortsatte.

“Där har du piloten i en mening.”

Sofia såg på honom.

“Hur menar du?”

“Den ser frisk ut.”

Han sa inget mer. Det behövdes kanske inte.

Björken låg längst in i korridoren, bredvid ett förråd som någon hade försökt göra om till tyst arbetsrum utan att ta bort hyllorna. Karin var redan där. Hon stod vid whiteboarden och drog en rak linje över mitten. På bordet låg gula, blå och rosa lappar i prydliga staplar. Sofia kände igen uppställningen. En del av henne ville sucka. En annan del ville ordna lapparna efter färgnyans.

Karin vände sig om.

“Sofia. Vad bra att du kunde komma.”

Det var något i hennes röst som fick Sofia att bli vaksam. Inte falskhet. Snarare förväntan. Karin såg på henne som om hon redan hade placerat henne i en funktion som Sofia själv ännu inte hade godkänt.

“Jag kunde komma en stund”, sa Sofia.

“Jag har dig som plattform/middleware.”

“Det såg jag.”

Karin hörde det också. Den lilla markeringen.

“Är det fel?”

“Det är otydligt.”

Karin log svagt, men inte bortförklarande.

“Det är nog därför du är här.”

Mats hostade något som kunde ha varit skratt.

Sofia gick fram till whiteboarden. Karin hade skrivit tre rubriker:

**Frihet**  
**Räcken**  
**Ansvar**

Det var snyggt. Nästan för snyggt. Sofia misstrodde snygga modeller eftersom verkligheten brukade ha fler integrationer än rubriker. Ändå kände hon att de tre orden ringade in något viktigt.

“Får jag lägga till en fjärde?” frågade hon.

Karin räckte henne pennan utan att tveka.

Det var en liten sak. Ändå noterade Sofia den. Många som ledde möten höll hårt i pennan, som om den var mandatet.

Sofia skrev:

**Ägarskap**

Hon satte tillbaka korken på pennan.

“Annars kommer alla tre ovanför bli tolkningar.”

Karin såg på ordet en stund.

“Bra.”

Mats lade pärmen på bordet med en duns.

“Då är vi klara. Kan någon bara tala om vem som äger vad?”

“Det är mötets ambition”, sa Karin.

“Ambition”, sa Mats. “Det mest riskabla av alla styrord.”

Dörren öppnades innan Karin hann svara. Amir kom in med datorn under armen, telefonen i handen och en energi i kroppen som gjorde att rummet kändes mindre. Han stannade till när han såg Sofia vid whiteboarden.

“Hej”, sa han.

“Hej.”

Det var inget särskilt i ordet. Ändå märkte Sofia att Karin såg mellan dem. Inte nyfiket, mer registrerande. Som om varje relation i rummet var en möjlig beroendekarta.

Amir såg på ordet Sofia hade skrivit.

“Ägarskap”, läste han. “Det kan bli ett kort möte om alla får välja själva.”

“Det är därför du inte får välja själv”, sa Mats.

Amir log, men det fanns spänning i käken. Han var inte här för att vara charmig. Han var här med en flödesbild, ett stoppat produktionsfönster och ett team som väntade på att han skulle komma tillbaka med något som liknade väg framåt.

Lena kom sist.

Hon kom inte sent, bara sist. Det var skillnad. Hon hade blocket i handen och en blick som först gick till tavlan, sedan till personerna, sedan till dörren, som om hon redan planerade sin flyktväg om mötet blev för fluffigt.

När hon såg Sofia mjuknade något, knappt märkbart.

“Sofia”, sa hon.

“Lena.”

De hade arbetat i samma organisation länge utan att egentligen känna varandra. Deras relation bestod av korta sakliga utbyten i ärenden, några sena kvällar där Sofia förklarat ett JBoss-beteende och Lena ställt precis de följdfrågor som visade att hon faktiskt lyssnade. Det räckte för en sorts respekt.

Karin stängde dörren.

“Tack för att ni kom. Jag vill börja med att vara tydlig: syftet är inte att rädda kvällens produktionsfönster.”

Amir såg ner i bordet. Han visste det redan, men kroppen hann reagera ändå.

“Syftet”, fortsatte Karin, “är att definiera vad som måste vara sant för att en pilot i containerplattformen ska kunna gå mot produktion utan att varje steg blir en förhandling.”

Sofia satte sig vid sidan, inte längst bak men inte heller vid bordets kortända. Hon hade valt sådana platser i flera år. Nära nog för att bidra. Inte så nära att någon trodde att hon ledde.

Karin bad först Lena beskriva driftens miniminivå. Lena gjorde det utan att läsa innantill, men Sofia såg att hon hade ordnat punkterna noga.

Rollback som omfattade dataförändringar.  
Åtkomlig dokumentation.  
Tydligt incidentansvar.  
Verifierade beroenden.  
Health checks som betydde något.  
Tidsatt granskning, inte sista-minuten-godkännande.

Lena talade sakligt, men Sofia hörde tröttheten under. Inte trötthet på förändring. Trötthet på att behöva formulera självklarheter som om de vore hinder.

När Amir sedan visade teamets flödesbild blev rummet annorlunda. Det var inte en presentation med snygga pilar. Det var en karta över väntan. Miljöbeställning. Behörigheter. Brandvägg. Certifikat. Loggindex. Databas. MQ. Granskning. Omtag. Ny granskning.

“Det här”, sa Amir, och pekade på tre röda markeringar, “är inte kvalitetssäkring. Det är kötid med otydlig återkoppling.”

Lena rörde sig i stolen.

“En del av kötiden beror på att underlaget kommer ofullständigt.”

“Ja”, sa Amir.

Det enkla erkännandet fick rummet att stanna upp.

Amir såg inte nöjd ut när han sa det. Snarare som någon som betalat för en sak han inte ville köpa.

“Och en del”, fortsatte han, “beror på att vi inte vet vad fullständigt betyder förrän någon säger nej.”

Sofia skrev ner det.

Inte för att det var nytt. För att det var användbart.

Karin lät tystnaden ligga kvar en stund. Det var skickligt. Många hade fyllt den med sammanfattning. Karin lät dem känna den.

Sedan vände hon sig mot Sofia.

“Du tittade på en teknisk fråga från teamet före mötet. Kan du beskriva den?”

Sofia kände hur rummet flyttade sig mot henne.

Hon hade vetat att det kunde hända. Ändå störde det henne att Karin gjorde det så smidigt. Som om hon bara öppnade en dörr och förutsatte att Sofia skulle gå igenom den.

“Det var en felstavad MQ-variabel”, sa Sofia.

Jonas, som inte var där, skulle ha älskat att få skulden reducerad till ett n inför denna publik.

“Applikationen hittade inte rätt kanal och föll tillbaka på ett defaultvärde. Samtidigt blev readiness grön eftersom kontrollen bara verifierade att applikationen svarade.”

Lena slöt ögonen i en sekund. Inte triumferande. Mer som någon som hade fått sin oro bekräftad och inte blev glad av det.

Amir sa:

“Vi har redan rättat variabeln.”

“Det är bra”, sa Sofia. “Men det är inte huvudpoängen.”

Han såg på henne. Där fanns något i blicken som hon kände igen från tidigare samtal: en vilja att springa före mot lösning. Hon tyckte om den energin mer än hon ville erkänna. Hon litade bara inte på den ensam.

“Huvudpoängen”, fortsatte hon, “är att plattformen just nu tillåter att en tjänst ser produktionsbar ut utan att vara det. Teamet har ansvar för sin konfiguration. Absolut. Men om pilotens mål är självservice måste självservicevägen hjälpa teamet att göra rätt och stoppa dem när något är för riskabelt.”

Mats lutade sig bakåt.

“Automatiserad Lena”, sa han.

Lena gav honom en blick.

Sofia skakade på huvudet.

“Nej. Inte automatiserad Lena. Det vore att bygga in nuvarande flaskhals i YAML.”

Karin log med pennan mot läpparna. Amir såg ut att vilja le men lät bli. Lena däremot såg direkt på Sofia nu.

“Vad är alternativet?” frågade Lena.

Det var en verklig fråga. Inte en utmaning.

Sofia kände hur svaret i henne redan fanns, men hon visste också vad det kunde leda till. Svar blev förväntningar. Förväntningar blev uppdrag. Uppdrag blev kalenderbokningar utan slutdatum.

Hon svarade ändå.

“En miniminivå som är byggd som produkt, inte som checklista. Standardmallar för vanliga tjänstetyper. Tydliga krav på health checks, loggning, metrics, secrets, rollback och beroenden. Policykontroller i pipeline där det går. Dokumentation som ägs och versionshanteras. Och ett gemensamt beslut om vilka saker som är teamets ansvar, plattformens ansvar och driftens ansvar.”

Hon hörde själv hur orden blev många. Det lät nästan som en plan.

Det var farligt.

Amir lutade sig framåt.

“Det är ungefär det vi har bett om.”

Lena svarade innan Sofia hann.

“Nej. Ni har bett om att slippa vänta.”

Amir drog efter andan, men Lena höjde handen lite. Inte för att tysta honom, mer för att be om tre sekunder att göra meningen färdig.

“Jag säger inte att det är fel. Jag säger att det inte är samma sak.”

Sofia såg hur Amir tog emot det. För ett ögonblick såg han yngre ut, inte i ålder utan i försvar. Sedan sjönk det undan.

“Okej”, sa han. “Då ber jag om fel sak på rätt grund.”

Det var en bra formulering. Sofia skrev ner den också.

Karin gick fram till tavlan och drog streck mellan orden.

Frihet. Räcken. Ansvar. Ägarskap.

“Kan vi testa något?” sa hon. “Inte lösa hela plattformen. Bara beskriva vad som måste vara sant för Kundportal Meddelandehantering innan nästa produktionsförsök.”

Mats öppnade pärmen.

“Då börjar verkligheten.”

Nästa timme blev rörigare än Sofia först hade hoppats och bättre än hon hade väntat sig.

De gick igenom rollbacken. Amir erkände att databasskriptet behövde en separat plan och att migreringen av statusvärden inte kunde behandlas som en detalj. Lena beskrev vad drift behövde veta för att kunna stå bakom ett nytt fönster. Mats lade till att MQ inte bara var “en anslutning” utan ett beteende över tid: ködjup, persistens, återstart, felmeddelanden, övervakning.

Sofia ritade en enkel bild på tavlan: applikationspod, MQ, Oracle, Elasticsearch, pipeline, loggning, övervakning. Hon skrev inte alla detaljer. Hon ritade bara tillräckligt för att visa var antaganden korsade varandra.

När hon satte pennan mot Oracle-rutan blev rummet stillare.

Inte mycket. Men tillräckligt.

Oracle var inte dagens huvudfråga, och därför var det förstås där framtiden låg och väntade. Alla visste att vissa ville diskutera databasen i containrar. Alla visste också att ingen ville vara den som öppnade licens-, backup-, prestanda- och ansvarsdiskussionen just nu.

Sofia skrev bara:

**Oracle: externt beroende i pilot. Kontrakt krävs. Ej flyttbeslut nu.**

Det var en försiktig mening, men hon kände hur den landade.

Amir tittade på den.

“Du stänger dörren.”

“Nej”, sa Sofia. “Jag hindrar oss från att låtsas att dörren redan är öppen.”

Lena såg nästan nöjd ut. Inte för att Sofia bromsade, utan för att någon äntligen skiljde på steg och dröm.

Karin fångade upp det.

“Så pilotens princip är: containerisera applikationslagret först, men definiera beroenden tydligt.”

“Ja”, sa Sofia.

Hon hörde hur enkelt det lät när Karin sa det. Nästan självklart. Det hade inte varit självklart för en timme sedan.

Mot slutet av mötet fanns en lista. Inte en färdig plattformsmodell, men något mer användbart än en diskussion om attityder.

För nästa produktionsförsök behövdes:

- rollbackplan för både image, konfiguration och databasmigrering
- tillgänglig MQ-dokumentation med ägare
- definierad incidentbemanning för pilotfönstret
- readiness-kontroll som speglade tjänstens faktiska förmåga att ta emot arbete
- liveness-kontroll som inte skapade onödiga omstarter vid beroendestörning
- loggning och spårbarhet enligt driftens miniminivå
- tydligt beslut att Oracle ligger utanför containerplattformen i denna pilot
- en kort gemensam genomgång senast dagen före nytt fönster, inte samma eftermiddag

Karin skrev listan rent på tavlan.

“Är det här lägre krav?” frågade hon.

“Inte för mig”, sa Lena.

“Är det här omöjligt för teamet?” frågade Karin.

Amir såg på listan länge.

“Nej. Men vi behöver hjälp med mallar och tolkningar. Annars kommer varje team uppfinna det här själva.”

Karin vände sig inte mot Sofia direkt. Det var nästan värre. Hon lät rummet göra det.

Sofia kände blickarna innan hon mötte dem.

Där var Mats, skeptisk men inte avvisande. Lena, prövande. Amir, förhoppningsfull på ett sätt som gjorde henne både varm och irriterad. Karin, lugn, som om hon redan visste vilken punkt hon själv skulle ta med sig till Elin.

Sofia lade ner pennan.

“Jag kan ta fram ett första tekniskt förslag tillsammans med rätt personer”, sa hon. “Förslag. Inte beslutad standard. Och inte ensam.”

Det sista kom hårdare än hon tänkt.

Karin nickade.

“Noterat.”

Sofia var inte säker på det. Noterat kunde betyda mycket. Men hon såg att Lena också nickade, och det betydde mer.

“Det ska inte bli en Sofia-checklista”, sa Lena.

Sofia såg på henne.

“Nej.”

“För då är vi bara tillbaka där vi började. Fast med dig i vägen i stället för mig.”

Det var krasst. Och sant.

Amir drog handen över nacken.

“Det är inte det vi vill.”

Lena tittade på honom.

“Vet ni det?”

Han svarade inte direkt. Sofia uppskattade att han inte gjorde det. Snabba svar var ibland bara ett sätt att slippa förstå frågan.

“Vi vill ha en väg som inte kräver att någon enskild person räddar oss varje gång”, sa han till slut. “Men jag tror inte vi har betett oss som om vi förstår vad det kräver.”

Karin skrev något i sin anteckningsbok. Sofia hade en känsla av att just den meningen skulle dyka upp i en sammanfattning senare, möjligen med ordet “insikt” framför.

Mötet avslutades utan applåder, utan energiövning och utan att någon sa att de hade haft en jättebra dialog. Det gjorde Sofia mer optimistisk än motsatsen. Riktiga steg kändes sällan som genombrott i stunden. De kändes oftare som att någon hade flyttat en tung möbel tio centimeter och alla låtsades att de inte var svettiga.

När de andra började samla ihop sina saker stannade Amir vid tavlan.

Sofia torkade inte bort bilden. Hon ville fotografera den först, men det kändes fånigt att göra det medan alla såg på. Hon tog ändå upp mobilen.

“Jag kan ta en bättre bild och lägga i kanalen”, sa Amir.

“Gör det.”

De stod bredvid varandra några sekunder. För nära för att vara helt neutralt, men inte så nära att någon annan skulle kunna säga något. Sofia var medveten om Karin vid bordet, Mats vid dörren, Lena som stoppade ner blocket i väskan. Arbetsplatser hade tunna väggar även när väggarna var av glas.

“Det där med defaultvärdet”, sa Amir lågt. “Vi borde ha fångat det.”

“Ja.”

Han log snett.

“Du kunde ha sagt ‘det händer’.”

“Det händer.”

“Lite sent.”

“Det händer, men ni borde ha fångat det.”

Nu skrattade han, tystare än vanligt.

Hon tyckte om ljudet. Det var opraktiskt.

“Du har en hemsk pedagogisk stil”, sa han.

“Jag har ingen pedagogisk stil. Jag har produktionsrädsla med struktur.”

“Det borde stå på en mugg.”

“Det kanske redan gör det hos drift.”

De log båda två, och för ett ögonblick fanns det något i rummet som inte handlade om MQ, rollback eller mandat. Något enklare. Sedan såg Sofia Karins blick i periferin och klev ett halvt steg åt sidan, som om hon just kommit på att tavlan behövde mer luft.

Amir märkte det. Det var det värsta. Eller kanske det bästa. Han märkte saker när han inte sprang.

“Vi ses i kanalen”, sa han.

“Ja.”

När han gick ut stannade Sofia kvar. Karin var den enda som fortfarande samlade ihop sina papper, långsamt nog för att det inte skulle vara en slump.

“Sofia”, sa hon.

“Mm?”

“Det du gjorde i dag var viktigt.”

Sofia tog bilden av tavlan och kontrollerade att texten gick att läsa.

“Jag beskrev ett stavfel som organisationsproblem. Det brukar vara uppskattat i lagom dos.”

Karin log inte den här gången.

“Jag menar det.”

Sofia stoppade ner mobilen i fickan.

“Var försiktig med vad du menar.”

“Varför?”

“För att nästa steg brukar vara att någon tycker att jag ska äga det.”

Karin höll hennes blick.

“Borde någon annan göra det?”

Frågan var enkel. För enkel. Sofia kände hur något i henne ville svara tekniskt: plattformsteam, arkitekturforum, driftrepresentanter, utvecklingsteam, produktägarskap, governance. Hon kunde rita modellen. Hon kunde namnge forumen. Hon kunde till och med skriva ett förslag som skulle se moget ut i ett beslutsunderlag.

Men Karin frågade inte efter modellen. Inte egentligen.

“Jag kan inte vara plattformen”, sa Sofia.

“Nej.”

“Jag kan inte vara genvägen runt att organisationen prioriterar.”

“Nej.”

“Jag kan inte vara den som alla frågar i stället för att vi bygger ett arbetssätt.”

“Nej.”

“Då ska du inte sälja in mig som lösningen.”

Karin tog emot det utan att backa.

“Jag vill sälja in behovet av tekniskt ägarskap. Inte dig som ensam lösning.”

Sofia såg på henne och försökte avgöra om hon trodde henne. Karin hade den där sortens lugn som kunde vara antingen integritet eller yrkesvana. Sofia hade ännu inte bestämt vilket.

“Det är en tunn skillnad i praktiken”, sa hon.

“Då får vi göra den tjockare.”

Sofia skrattade till, kort.

“Är det där coachspråk?”

“Förmodligen.”

“Det behöver översättas innan du säger det till Mats.”

“Jag märkte det.”

De stod tysta en stund. Ute i korridoren gick Lena och Mats sida vid sida. Mats sa något som fick Lena att skaka på huvudet, men inte som när hon var arg. Mer som när hon inte ville visa att hon blivit road.

Karin följde också dem med blicken.

“Lena litade på dig i rummet”, sa hon.

Sofia blev obekväm.

“Lena litar på tydlighet.”

“Hon litar inte på många personers tydlighet.”

Det var kanske sant. Sofia ville inte veta hur mycket.

Hon tog sin dator från bordet.

“Vad tänker du göra nu?”

Karin stängde anteckningsboken.

“Prata med Elin.”

“Om?”

“Att piloten saknar ett formellt tekniskt ägarskap för vägen till produktion.”

Sofia kände hur kaffet, som hon knappt druckit, plötsligt blev surt i magen.

“Karin.”

“Jag kommer inte föreslå att du ensam ska bära det.”

“Men du kommer säga mitt namn.”

Karin svarade inte direkt.

Det var svar nog.

Sofia nickade långsamt. Inte ja. Bara ett erkännande av riktning.

“Då ska du också säga att om organisationen vill ha en plattformsansvarig, eller teknisk ledare, eller vad de nu kallar det, så måste rollen ha tid, mandat och folk. Inte bara mötesinbjudningar med snedstreck.”

Karin tog upp pennan igen och skrev ner det.

“Tid, mandat och folk.”

“Lägg till prioritering. Annars får jag folk på papper och ingen i praktiken.”

“Tid, mandat, folk och prioritering.”

“Bra.”

Sofia gick mot dörren men stannade innan hon lämnade rummet. Hon såg tillbaka på tavlan. Frihet. Räcken. Ansvar. Ägarskap. Under orden fanns hennes enkla systembild och listan över nästa produktionsförsök.

Det såg inte ut som en revolution.

Det såg ut som en början.

Hon tänkte på stavfelet. Ett saknat n i en miljövariabel. En pod som log och låtsades vara frisk. En organisation som gjorde ungefär samma sak.

I korridoren plingade Teams.

Amir hade lagt upp bilden av tavlan i kanalen.

Under den hade han skrivit:

> Förslag till gemensam miniminivå inför nästa produktionsförsök. Inte lägre krav. Tydligare krav tidigare.

Sofia stod stilla med telefonen i handen.

Lenas formulering.

Amir hade använt Lenas formulering.

Det var en liten sak, men små saker kunde vara tecken på att något rörde sig under ytan. Inte tillräckligt för att lita på. Inte än. Men tillräckligt för att inte avfärda.

Hon stoppade ner telefonen och gick tillbaka mot sin plats.

På vägen passerade hon kaffemaskinen igen. Den hostade till när någon tryckte på cappuccino. Sofia tänkte att även maskiner kunde se friska ut tills någon faktiskt bad dem leverera.
