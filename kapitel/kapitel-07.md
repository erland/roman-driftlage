# Kapitel 7 – Det första tekniska bakslaget

Amir hade börjat kalla mallen för den första riktiga leveransen, fast den ännu bara fanns som en gren i ett repository, tre sidor anteckningar och en rad kommentarer i en Teams-tråd som redan var för lång för att någon skulle läsa den från början.

Det var kanske dumt.

Men efter workshoppen hade han behövt något som kändes som rörelse.

Inte ännu en tavla. Inte ännu ett möte där någon med rimlig röst sa att de behövde förstå varandra. Han hade inget emot förståelse. Problemet var att förståelse ofta kom utan effekt. Folk förstod varandra och gick sedan tillbaka till sina köer, sina ärenden, sina mejl, sina väntande beroenden. Till slut var alla väldigt förstående och ingenting hade flyttat sig en centimeter.

Nu hade de åtminstone något konkret.

En enkel deploymentmall.

En minimal väg för Kundportal Meddelandehantering in i containerplattformens testmiljö: image, konfiguration, secrets, readiness, liveness, loggning, grundläggande metrics, anslutning mot Oracle i test, MQ-stub i första körningen och sedan riktig MQ-koppling när dokumentationen var åtkomlig för drift.

Amir hade sagt “minimal” tre gånger när de började på morgonen. Sofia hade efter tredje gången höjt blicken från sin dator och sagt:

“Minimal betyder inte tunn. Minimal betyder att varje del som är med faktiskt håller.”

Det hade blivit tyst runt bordet.

Inte obehagligt tyst. Mer som när någon lagt ett vattenpass över en mening och alla sett lutningen.

De satt i ett projektrum som hette Aspen, mindre än Björken och med sämre ventilation. På bordet stod pappersmuggar, två laddare, en halvt uppäten banan och en utskriven bild från Karins workshop där de gula lapparna nästan inte gick att läsa. Karin var inte där. Hon hade sagt att hon skulle låta dem arbeta utan facilitator den första timmen, vilket Amir först hade tolkat som förtroende och sedan som ett test.

Lena satt längst ut vid bordet, nära dörren. Inte som om hon ville fly, utan som om hon behövde kunna bli hämtad av nästa incident utan att störa möbleringen. Hon hade sin dator vinklad så att hon såg både skärmen och rummet. Hon hade sagt väldigt lite sedan de började, men varje gång Amir försökte gå förbi en detalj markerade hon med en anteckning i sitt block.

Mats var med “vid behov”, vilket i praktiken betydde att han hade slagit sig ner med kaffe och inte tänkte gå förrän någon tvingade honom. Naya satt bredvid Amir med testfallen uppe. Sofia hade tagit plats mitt emot honom, inte vid kortändan. Hon hade undvikit den platsen med sådan precision att Amir lagt märke till det. Hon ville inte se ut som den som ledde arbetet, trots att alla väntade på hennes frågor.

“Vi börjar med att deploya exakt som mallen säger”, sa Sofia. “Inga lokala småjusteringar. Inga ‘jag sätter den här variabeln manuellt så länge’. Om mallen är fel ska mallen visa att den är fel.”

Jonas, som satt med i videosamtal från en annan våning eftersom hans yngsta barn hade feber och han behövde kunna gå med kort varsel, suckade hörbart.

“Det här kommer göra ont.”

“Ja”, sa Sofia. “Det är lite poängen.”

Amir hade velat invända. Inte mot själva principen, utan mot tonen. Det fanns en sorts lugn självklarhet hos Sofia som gjorde honom både trygg och otålig. Hon kunde säga nej utan att låta som Lena. Hos Lena fanns stoppet ofta redan i röstens första konsonant. Hos Sofia kom stoppet som en konsekvens av något hon redan sett tre led tidigare.

Det gjorde det svårare att argumentera.

Han startade pipelinen.

På skärmen rullade stegen förbi. Checkout. Build. Unit tests. Image build. Push to registry. Deploy to test namespace.

Första gröna bocken kom. Sedan nästa.

Naya lutade sig fram.

“Om det här går igenom på första försöket blir jag orolig.”

“Varför?” frågade Mats.

“För då testar vi inte rätt saker.”

Mats pekade mot henne med kaffemuggen.

“Henne gillar jag.”

Amir log, men han märkte att han höll andan när deploymentsteget började. Det var löjligt. Det här var testmiljö. Inget medborgarflöde, ingen skarp kö, ingen nattlig incident. Ändå hade han den där känslan i kroppen som han brukade få före en produktionssättning: som om alla beslut som tagits i små bitar under veckor plötsligt blev ett enda ja eller nej.

Pipelinen blev grön.

En sekund hann han känna lättnad.

Sedan såg Naya på sin skärm.

“Readiness är röd.”

Amir böjde sig mot henne.

“Pipelinen säger deploy klar.”

“Ja. Kubernetes säger att podden inte är ready.”

Sofia hade redan öppnat loggarna.

“Det är bra”, sa hon.

Jonas röst kom ur högtalaren.

“Jag vill bara notera att det är en speciell arbetsmiljö där rött betyder bra.”

“Rött betyder att systemet inte ljuger”, sa Sofia.

Lena lyfte blicken från sitt block.

“Det där vill jag nästan rama in.”

Amir ignorerade dem och scrollade i loggarna. Första raden såg normal ut. Applikationen startade. JBoss laddade moduler. Konfiguration lästes in. Sedan kom en varning om datasource. Sedan en till. Sedan en stacktrace som bredde ut sig över skärmen som en trasig karta.

`javax.naming.NameNotFoundException`

Han kände igen felet innan han ville erkänna det.

“Naming”, sa Sofia.

“JNDI”, sa Mats samtidigt.

De såg på varandra, och för ett ögonblick fanns där en sorts teknisk samförstånd som inte behövde översättas. Amir hade alltid tyckt om sådana ögonblick. De brukade betyda att problemet var begränsat. Någon visste var man skulle börja.

Nu betydde det också att problemet inte var containerns fel.

“Vi har ju datasource-konfigurationen i manifestet”, sa Amir.

“Ni har en miljövariabel som pekar på datasourcens namn”, sa Sofia. “Applikationen förväntar sig troligen att servern redan har bundit upp JNDI-namnet på det sätt den gamla JBoss-miljön gjorde.”

“Det är samma namn.”

“Är det samma plats?”

Amir svarade inte direkt.

Han visste vad hon menade. I den gamla miljön var mycket förberett utanför teamets kod. Datasources, drivrutiner, vissa system properties, certifikatvägar, loggformat, ibland till och med små skillnader mellan miljöer som ingen längre erkände som skillnader eftersom de hade funnits så länge att de blivit landskap.

I containern fanns bara det de byggt in eller skickat med.

Det var egentligen hela poängen.

Och ändå kändes det orättvist.

“Vi kan lägga in det i imagen”, sa Jonas från högtalaren.

“Nej”, sa Sofia och Lena samtidigt.

Amir sneglade på Lena. Hon hade sagt nej snabbare än han väntat sig. Inte argt. Nästan reflexmässigt.

Sofia fortsatte:

“Vi ska inte baka in miljöspecifik datasource-konfiguration i imagen. Då har vi bara flyttat den gamla servern in i en låda och kallat det modernisering.”

Jonas muttrade något som lät som “lådan startar i alla fall”, men han skrev samtidigt i chatten att han tittade på konfigurationsmönstret.

Naya klickade mellan testfallen.

“Betyder det här att våra tester inte fångade att applikationen kräver gammal serverkonfiguration?”

“Ja”, sa Amir, lite för snabbt. Sedan tog han om. “Det betyder att våra tester körde mot en miljö som redan hade samma antaganden.”

Han hörde själv hur det lät. Mindre som en ursäkt, mer som början på en obekväm sanning.

Mats lutade sig tillbaka.

“Välkommen till driftens museum. Alla utställningsföremål är fortfarande i produktion.”

Lena gav honom en kort blick, men hon log nästan.

Amir försökte fokusera på skärmen. Stacktracen fortsatte, men det var inte den som störde honom mest. Det var känslan av att problemet inte bara var tekniskt. Teamet hade pratat om containerisering som om de flyttade applikationen från en plats till en annan. Men kanske var applikationen inte en sak. Kanske var den ett samarbete mellan kod, serverkonfiguration, manuella rutiner, driftkunskap och historiska beslut som ingen längre ägde.

Han ogillade den tanken.

Den gjorde allt långsammare.

Sofia öppnade deploymentmallen och pekade på ett avsnitt.

“Här behöver vi skilja på applikationens artefakt, miljökonfiguration och plattformens standardkonfiguration. Just nu blandar ni ihop dem.”

“Vi blandar inte ihop dem”, sa Amir.

Han ångrade sig nästan innan meningen var slut. Inte för att den var helt fel, utan för att den kom från fel plats i honom. Stolthet, inte analys.

Sofia såg på honom. Hon svarade inte direkt, och den pausen var värre än ett mothugg.

“Då formulerar jag om”, sa hon. “Mallen blandar ihop dem. Och eftersom teamet följer mallen visar det att mallen inte är tillräckligt tydlig.”

Det var generöst. Hon gav honom en väg ut utan att backa från sakfrågan.

Lena skrev något i sitt block.

Amir undrade vad. Kanske “utveckling defensiva”. Kanske “Sofia räddar samtalet”. Kanske bara “datasource”.

Han andades ut.

“Okej”, sa han. “Vad behöver ändras?”

Det var en liten mening. Han visste det. Ändå märkte han att Lena tittade upp när han sa den.

Sofia vred datorn en aning så att alla såg.

“Först behöver vi beskriva vilka resurser applikationen förväntar sig att plattformen tillhandahåller. Datasource, MQ-anslutning, certifikat, loggformat, health check-beteende. Sedan behöver vi definiera vad som är teamets ansvar och vad som är plattformens standard.”

“Det låter som en hel produkt”, sa Jonas.

“Ja”, sa Sofia.

“Vi skulle ju bara få upp vår tjänst.”

“Ja”, sa Sofia igen. “Det är därför det gör ont.”

Amir såg mot Lena. Han väntade sig att hon skulle säga något om att det här var precis vad drift försökt förklara. Det gjorde hon inte. Hon satt tyst med pennan mellan fingrarna och såg på stacktracen på skärmen med ett ansikte som var mer trött än triumferande.

Det var nästan värre.

Han hade lättare att försvara sig mot misstänksamhet än mot någon som bara såg konsekvenserna.

Naya markerade tre testfall.

“Vi behöver ett test som startar applikationen utan förpreparerad servermiljö. Alltså så som containern faktiskt gör.”

“Ja”, sa Amir.

“Vi behöver också ett test som verifierar att readiness inte blir grön om datasource saknas.”

“Ja.”

“Och MQ.”

“Ja.”

Hon vände sig mot Lena.

“Skulle drift lita mer på det?”

Lena såg först ut som om frågan var riktad till fel person. Sedan lade hon ner pennan.

“Jag skulle lita mer på att ni visste när det inte fungerade.”

Det blev tyst.

Amir lät meningen sjunka in. Den var inte samma sak som tillit. Inte än. Men den var kanske mer användbar.

Sofia nickade.

“Det är en bra miniminivå. Inte att allt alltid fungerar. Att systemet tydligt visar när det inte gör det.”

Mats pekade på skärmen.

“Och att det visar det för rätt människor innan medborgarna gör det.”

“Ja”, sa Lena.

Amir kände hur irritationen i honom bytte form. Den försvann inte. Han var fortfarande frustrerad. Fortfarande medveten om kalendern, styrgruppen, Saras förväntningar, teamets energi som alltid tappade kraft när något fastnade i beroenden. Men irritationen var inte längre riktad lika tydligt mot drift. Den hade börjat vända sig mot deras egen förenkling av problemet, och det tyckte han inte om. Det var bekvämare när hindret hade ett namn och satt vid andra sidan bordet.

Hans telefon vibrerade. Ett meddelande från Sara.

> Hur går det? Behöver veta om jag ska börja förbereda verksamheten på ny försening.

Han stirrade på meddelandet.

Ny försening.

Det var det alla skulle se. Inte att de hittat ett grundantagande i applikationen. Inte att mallen för första gången avslöjade en falsk trygghet. Inte att readiness faktiskt gjorde sitt jobb genom att vägra bli grön. Bara ännu en försening.

Han skrev:

> Vi har hittat ett faktiskt containeriseringsproblem i JBoss-konfigurationen. Inte redo att ge ny tid än. Det är bra att vi hittade det nu.

Han läste sista meningen och hörde hur tunn den skulle låta för någon som väntade på funktionalitet.

Han skickade ändå.

Sofia hade under tiden ritat tre kolumner på whiteboarden.

**Applikation**  
**Plattform**  
**Externa beroenden**

Under Applikation skrev hon:

- Förväntade resurser
- Startbeteende
- Felhantering
- Health semantics

Under Plattform:

- Standardkonfiguration
- Secrets
- Logging
- Metrics
- Deploymentmönster

Under Externa beroenden:

- Oracle
- MQ
- Elasticsearch
- Certifikat

“Det här är inte hela kartan”, sa hon. “Men det är tillräckligt för att inte låtsas att allt ligger i samma hink.”

Mats reste sig och gick fram till tavlan.

“Får jag?”

Sofia gav honom pennan.

Han skrev under Externa beroenden:

- Vem väcks?

Sedan gick han tillbaka till kaffet.

“Tekniskt begrepp”, sa han. “Mycket underskattat.”

Lena såg på orden. Amir såg att något rörde sig i hennes ansikte, en blandning av irritation och erkännande. Kanske tänkte hon på alla gånger svaret hade varit hon. Eller Mats. Eller någon som råkade ha varit med 2014 när ett val gjordes som nu fanns kvar som en osynlig regel.

“Det borde stå i ansvarsmatrisen”, sa hon.

“Det borde stå i systemet”, sa Sofia.

Lena vände sig mot henne.

“Håller du på att göra mig överflödig?”

Det var sagt torrt, men inte skämtsamt nog för att bara vara ett skämt.

Sofia mötte hennes blick.

“Nej. Jag försöker göra det möjligt för dig att göra något annat än att minnas åt alla.”

Rummet blev stilla på ett sätt som inte hade med tekniken att göra.

Amir såg på Lena. Hon tittade ner i sitt block igen, men hon skrev inte. För första gången sedan han lärt känna henne såg hon inte främst sträng ut. Hon såg träffad ut, och det gjorde honom försiktig.

Han hade tänkt på driftkoordinering som en grind. En kö. En funktion. En plats där ärenden blev liggande tills någon ställde en fråga som borde ha ställts tidigare. Han hade sällan tänkt på vad det gjorde med en människa att vara den platsen år efter år.

Hans telefon vibrerade igen.

Sara:

> Jag förstår. Men verksamheten kommer fråga varför det här inte var känt tidigare.

Amir höll nästan på att skriva “för att drift inte gett oss rätt mallar tidigare”. Det var en reflex så stark att fingrarna hann börja forma svaret innan han stoppade sig.

Han raderade.

Skrev i stället:

> För att gamla miljön dolde beroendet. Nya mallen gör det synligt. Vi behöver förklara det så.

Han skickade och lade telefonen med skärmen nedåt.

“Vi behöver en plan för vad vi gör nu”, sa han.

Kanske sa han det för gruppen. Kanske mest för sig själv.

Naya tog ordet.

“Jag kan skriva testfallen för start utan förpreparerad serverkonfiguration och readiness vid saknad datasource. Men jag behöver någon som hjälper mig definiera vad som räknas som korrekt fel.”

“Jag kan ta det”, sa Sofia.

Jonas röst kom genom högtalaren.

“Jag tittar på hur vi läser in datasource-konfigurationen utan att baka in miljöspecifika värden i imagen. Men jag behöver veta vilket mönster vi faktiskt vill använda.”

“Vi definierar ett första mönster”, sa Sofia. “Inte det perfekta. Ett som går att förstå, upprepa och granska.”

Mats grymtade.

“Det låter misstänkt mycket som drift.”

“Bra”, sa Sofia. “Då kanske vi kan automatisera delar av det.”

Lena tog upp pennan igen.

“Jag kan skriva vilka delar drift behöver kunna se innan nästa körning. Inte för att godkänna varje rad manuellt, utan för att veta vad som finns.”

Amir noterade formuleringen. Inte godkänna varje rad manuellt. Veta vad som finns. Den skillnaden hade funnits i diskussionen hela tiden, men först nu lät den som något de kunde bygga på.

“Och jag”, sa han, “tar ansvar för att teamet dokumenterar vilka gamla miljöantaganden vi hittar. Inte som efterhandsförsvar. Som en lista vi faktiskt betar av.”

Lena såg upp.

“Det kommer bli en lång lista.”

“Ja.”

“Den kommer göra ont.”

“Det har jag hört är poängen.”

Det var första gången Lena log mot honom utan att det kändes som en olycka.

Sofia såg mellan dem, och Amir kunde inte avgöra om hon var nöjd, lättad eller bara redan tre problem längre fram. Han tyckte om det hos henne. Han tyckte om det mer än han borde i ett rum där de just hade misslyckats.

Pipelinen stod fortfarande röd.

Det märkliga var att rött nu inte kändes som stopp. Det kändes som information.

De arbetade vidare i nästan två timmar. Den första timmen försvann in i detaljer: var drivrutinen skulle ligga, hur datasource skulle definieras, hur secrets skulle refereras, om health endpointen skulle kontrollera beroenden direkt eller via en intern komponent, vad som riskerade att skapa falska negativa larm. Den andra timmen blev mer obekväm, eftersom de började hitta fler antaganden.

Applikationen skrev temporära filer till en sökväg som inte var garanterad skrivbar i containern.

Sessioner hanterades på ett sätt som antog stabil nodtillhörighet.

En konfigurationsfil hämtades från en plats som i gamla miljön monterats av drift utan att teamet längre tänkte på den.

Loggarna var delvis strukturerade, delvis inte.

Elasticsearch-indexet skapades av applikationen vid start om det saknades, vilket lät praktiskt tills Mats frågade vad som hände om applikationen hade fel behörighet i fel miljö.

Till slut satt ingen rak i ryggen längre.

Amir kände samma trötthet som efter en incident, trots att ingenting skarpt hade hänt. Kanske var det just därför. De hade grävt i framtida incidenter innan de inträffade, och det fanns ingen adrenalinkick i förebyggande arbete. Bara en växande lista och en obehaglig respekt för allt de inte visste.

Karin kom in när mötet egentligen borde ha varit slut. Hon stannade i dörren med handen kvar på handtaget.

“Jag skulle fråga hur det går”, sa hon, “men ni ser ut som om ni antingen har löst något eller förstört något.”

“Ja”, sa Mats.

Karin såg på tavlan. Hennes blick fastnade på kolumnerna och sedan på Mats tillägg.

“Vem väcks”, läste hon.

“Vi förfinar terminologin”, sa Mats.

Karin gick närmare.

“Vad hände?”

Amir väntade på att någon annan skulle svara. Det var barnsligt, men han ville inte vara den som sammanfattade ett misslyckande. Sedan insåg han att det var precis vad han brukade anklaga organisationen för: att ingen ägde det obekväma.

“Deploymenten gick igenom”, sa han. “Men podden blev inte ready. JBoss-konfigurationen utgår från resurser som den gamla servermiljön tillhandahöll. Våra tester fångade inte det eftersom testmiljön hade samma antaganden.”

Karin nickade långsamt.

“Så mallen avslöjade ett dolt beroende.”

Amir såg på henne.

“Ja.”

“Det är väl bra?”

Han skrattade, men utan glädje.

“Du får gärna säga det till Sara och styrgruppen.”

“Det kan jag”, sa Karin. “Men då måste vi vara ärliga med vad det betyder. Är det en försening, ett fynd eller båda?”

Amir ville säga fynd. Lena skulle kanske säga försening. Sofia skulle säga något mer exakt och därmed jobbigare.

“Båda”, sa han.

Karin log svagt.

“Det brukar vara där verkligheten börjar.”

Hon vände sig mot Lena.

“Och från driftens sida?”

Lena såg på tavlan innan hon svarade.

“Det här är första gången jag har sett teamet hitta ett produktionsproblem innan produktion och inte försöka prata bort det som miljöstrul.”

Amir kände att kommentaren borde irritera honom. Den gjorde det också, lite. Men under irritationen fanns något annat, något oväntat nära lättnad.

“Jag tänker ta det som beröm”, sa han.

“Gör inte det till en vana.”

“För sent.”

Karin skrev inte ner deras replikskifte, vilket Amir var tacksam för. Vissa små fredsavtal dog om de dokumenterades.

Sofia stängde sin laptop till hälften.

“Vi behöver kommunicera det här rätt. Inte som att containerplattformen fallerat. Inte som att teamet misslyckats. Och inte som att drift hade rätt hela tiden.”

“Fast drift hade lite rätt”, sa Mats.

“Särskilt inte som att drift hade rätt hela tiden”, sa Sofia.

Lena såg på Mats.

“Vi kan nöja oss med att ha rätt i tysthet.”

“Det låter inte hälsosamt.”

“Det har hållit oss vid liv sedan WebSphere.”

Mats pekade på henne med pennan.

“Nu stjäl du mitt material.”

Amir märkte hur rummet andades ut. Inte mycket. Inte så att problemet blev mindre. Men tillräckligt för att människor skulle börja tänka igen i stället för att försvara sig.

Karin satte sig på den enda lediga stolen.

“Vad är nästa konkreta steg?”

Sofia svarade först.

“Vi skapar en lista över gamla miljöantaganden som måste göras explicita. Teamet äger applikationsdelarna. Plattformen behöver äga standardmönster för datasource, secrets, loggning och health. Drift behöver beskriva vilken insyn och vilka larm som krävs. Och någon måste prioritera arbetet, annars gör vi det på kvällar mellan incidenter.”

Det sista var riktat mot Karin, eller kanske genom Karin till Elin.

Karin tog emot det utan att försvara sig.

“Jag tar den med Elin.”

“Ta den inte som en punkt”, sa Sofia. “Ta den som villkor.”

Karin såg på henne.

“Det där är en annan typ av mening från dig.”

Sofia sänkte blicken mot datorn.

“Det är samma mening. Bara mindre inlindad.”

Amir såg henne då, inte som den person som löste detaljerna utan som någon som stod på kanten till något större och inte riktigt visste om hon ville bli knuffad eller hålla emot. Han ville säga något efter mötet. Något som inte var arbetsmässigt. Men bara tanken gjorde honom medveten om Lena, Karin, Mats, Naya och alla de osynliga linjer som gick mellan roller och ansvar.

Så han sa inget.

Inte än.

När de bröt upp stod pipelinen fortfarande röd i historiken. Den senaste körningen hade misslyckats på exakt samma sätt som den första, men nu fanns det kommentarer, uppgifter och ägare kopplade till felet. Rött, men inte längre anonymt.

Amir gick sist ut tillsammans med Naya. I korridoren stannade hon och såg på honom.

“Du var nära att börja försvara allt där inne.”

“Jag vet.”

“Men du gjorde inte det hela vägen.”

“Är det här min utvecklingssamtalsfeedback?”

“Ja. Jag ger den agilt och kontinuerligt.”

Han skrattade.

Hon log, men blev sedan allvarlig.

“Det här kommer bli större än vi tänkt.”

“Ja.”

“Du behöver säga det till Sara innan någon annan säger det som ett misslyckande.”

Han nickade. Han visste det.

När Naya gick vidare stod han kvar en stund utanför Aspen. På andra sidan glaset suddade Sofia ut tavlan men lämnade tre ord kvar längst upp:

**Applikation. Plattform. Beroenden.**

Hon tog en bild innan hon suddade även dem.

Amir såg på henne genom glaset, och för första gången sedan containerplattformen blivit teamets stora löfte kände han inte att vägen framåt låg i att trycka hårdare.

Den låg kanske i att se tydligare.

Det var mindre tillfredsställande.

Men troligen mer sant.
