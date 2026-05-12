# Kapitel 4 – Teamets frustration

Amir Rahman hann se Lenas meddelande tre gånger innan någon i teamet sa något.

Det låg längst ner i tråden, kortare än han hade väntat sig och därför svårare att avfärda.

> Jag håller med om att vi behöver ett annat arbetssätt för piloten. Det betyder inte lägre krav. Det betyder tydligare krav tidigare.

Han läste det först som en eftergift. Sedan som en korrigering. Tredje gången som något mer irriterande: en formulering han inte helt kunde säga emot.

Runt honom hade teamrummet återgått till sitt vanliga ljud. Tangentbord. Fläkten från projektorn som ingen använde längre men som ändå satt kvar i taket. En kort hostning från Jonas vid fönstret. Nayas stol som gnisslade när hon vred sig mellan sina två skärmar. På väggen satt deras Kanban-tavla, digitalt speglad men ändå utskriven varje måndag eftersom produktägaren tyckte att papper gjorde arbetet “mer synligt”.

Det såg nästan komiskt ut nu.

Kolumnen **Väntar på extern part** var bredare än de andra.

Inte för att någon hade designat den så. Den hade blivit bredare i praktiken. Varje gång teamet försökte göra något som rörde produktionsmiljö, integrationer, brandväggar, certifikat, databasbehörigheter eller loggindex hamnade arbetet där. Som om värdeflödet hade en sumpmark i mitten och alla låtsades att det var en bro.

“Sa hon nej igen?” frågade Jonas.

Amir låste skärmen av reflex, trots att alla ändå kunde se tråden i Teams.

“Hon sa inte bara nej.”

“Det är väl en utveckling.”

Naya tittade upp från sin skärm.

“Vad sa hon?”

Amir läste upp meddelandet. Han försökte hålla rösten neutral och hörde själv att han misslyckades vid ordet krav.

Naya lutade sig tillbaka. Hon var testare, men den sortens testare som fick utvecklare att skruva på sig eftersom hon sällan letade efter fel där de själva tyckte att felen borde finnas. Hon hade en förmåga att ställa enkla frågor som efteråt visade sig ha varit arkitekturfrågor.

“Det där är inte orimligt”, sa hon.

Jonas vände sig mot henne.

“Vi har väntat på miljöbeställningen i fyra veckor.”

“Det gör inte meningen orimlig.”

“Nej, men tajmingen.”

Amir sa inget. Han ville hålla fast vid sin irritation eftersom den gav honom riktning. Irritation var användbar. Den gjorde att han kunde formulera hinder, skriva eskaleringar, driva på. Den gjorde att han slapp känna den där andra saken som hade krupit fram under förmiddagen: att de faktiskt inte hade haft en riktig rollback för databasmigreringen.

Inte riktig på produktionsspråk.

På deras språk hade rollbacken varit självklar. Föregående image. Föregående konfiguration. Scriptet var idempotent, eller nästan. Migreringen var enkel, eller skulle vara det om datat såg ut som i test. Det var sådana ord man använde när man ännu inte föreställt sig någon från drift klockan två på natten med en chef i telefonen och en verksamhet som ville veta när meddelandestatusarna skulle gå att lita på igen.

Han hatade att Lena hade rätt på just den punkten.

“Vi behöver visa flödet”, sa han till slut.

“För Karin?” frågade Naya.

“För Karin. För Lena. För Elin om hon kommer. För vem som än tror att detta handlar om att vi inte gillar dokumentation.”

Jonas drog handen genom håret.

“Jag gillar inte dokumentation.”

“Nej”, sa Naya. “Men det är inte därför du blev utvecklare.”

“Jag blev utvecklare för att slippa fylla i Excelmallar som någon sedan kopierar in i ett ärende.”

“Där har du din livsfilosofi.”

Amir log trots sig själv. Han behövde deras skämt. De höll teamet rörligt när organisationen blev trög. Men han visste också att skämten ibland blev en vägg. Bakom den slapp de se att drift inte bara var ett hinder, utan människor som levde med konsekvenserna av teamets förenklingar.

Han reste sig och gick till tavlan.

“Vi tar Kundportal Meddelandehantering från början. Vad har vi väntat på?”

Jonas snurrade stolen mot honom.

“Hur långt tillbaka?”

“Från första miljöbehov.”

“Då behöver jag kaffe.”

“Då behöver du prata medan du hämtar kaffe.”

Jonas reste sig långsamt, som om han ville demonstrera vad administrativ friktion gjorde med människokroppen.

“Först behövde vi en testmiljö som liknade produktion tillräckligt mycket för att verifiera MQ-flödet. Det fanns ingen beställningsväg för containerbaserad testmiljö, så vi använde den gamla serverbeställningen och skrev i kommentarsfältet att det egentligen inte var en server.”

“Vilket gick till servergruppen”, sa Naya.

“Som frågade vilken virtuell maskin vi ville ha.”

“Som vi inte ville ha.”

“Som ledde till ett möte”, sa Jonas och pekade på Amir som om mötet var hans fel.

Amir skrev på whiteboarden.

**1. Testmiljö: fel beställningsväg → möte → omtag**

“Sedan behövde vi brandväggsöppning mot MQ i test”, fortsatte Naya. “Där var formuläret byggt för fasta servernamn. Poddar hade ingen ruta.”

“Det där är inte rättvist”, sa Jonas från dörröppningen. “Det fanns en ruta. Den hette Övrigt.”

“Övrigt är inte en arkitekturmodell.”

Amir skrev.

**2. Brandvägg: formulär antar statisk server → manuell tolkning**

Han kände hur något lättade när punkterna kom upp på tavlan. Det var inte bara irritation längre. Det blev synligt. Synligt gick att diskutera. Osynligt blev bara personlighet.

“Databasen”, sa han.

Naya gjorde en min som betydde att där fanns både fakta och uppgivenhet.

“Oracle-schemat tog åtta arbetsdagar att få. Inte för att databasteamet var långsamt, utan för att beställningen behövde systemägargodkännande, informationsklassning och sedan separat behörighetsärende för tekniskt konto. Tre ärenden. Ingen länk mellan dem.”

“Fyra”, sa Jonas och kom tillbaka med kaffe. “Du glömde att behörighetsärendet först avslogs eftersom kontonamnet inte följde standard.”

“För att standarden inte tillät prefixet för containerpiloten.”

“Just det. Innovationen dog på teckenposition tolv.”

Amir skrev.

**3. Oracle: schema + klassning + tekniskt konto + namnistandard → 8 dagar**

Han hörde sin egen penna gnissla mot tavlan. Det fanns en barnslig tillfredsställelse i att skriva ner siffran. Åtta dagar. Inte en känsla. Inte gnäll. Åtta dagar.

Men så tänkte han på Lena igen. På hur hon hade stått vid driftön tidigare, tröttare än han velat se. Han hade gått dit beredd att argumentera och kommit därifrån med något som inte gick att sortera som seger eller förlust.

Hon hade inte sagt att självservice var fel. Hon hade sagt att den behövde räcken.

Det var ett ord han ogillade. Räcken lät som något man satte upp för barn. Men om han bytte ut det mot kontrakt, standarder, guardrails — då var det samma sak som han själv brukade säga när någon ville ge produktägaren direktåtkomst till databasen “bara tillfälligt”.

“Nästa”, sa han.

“Loggindex”, sa Naya.

Jonas satte sig igen.

“Elasticsearch-miljön fanns, men indexmönstret behövde beställas separat eftersom vi inte fick skapa det själva. När vi fick det var namnet fel, för någon hade tolkat tjänstenamnet från ärenderubriken i stället för från vår deploymentfil.”

“Det var inte bara namnet”, sa Naya. “Retention var fel också. Trettio dagar i stället för nittio.”

“För att standarden var trettio.”

“För att ingen visste att verksamhetskravet var nittio.”

“För att verksamhetskravet låg i en PDF i SharePoint”, sa Jonas.

Amir skrev.

**4. Logg/sök: index och retention manuell tolkning → fel standard**

Han stannade med pennan mot tavlan. Varje punkt var verklig. Varje punkt kunde användas som bevis för deras sak. Men varje punkt visade också att deras egen information inte alltid hade varit där den borde. Det var inte bara att någon annan hade tolkat fel. De hade placerat sanningen i dokument, chattar, kommentarer och muntliga genomgångar och sedan blivit irriterade när den inte förvandlades till fungerande drift.

Han önskade att insikten hade känts mer upplyftande.

“Vad är poängen?” frågade Jonas. “Att vi har bevis för att allt tar för lång tid? Det visste vi.”

“Poängen är att självservice inte kan betyda att vi skickar färre ärenden och hoppas mer”, sa Amir.

Naya tittade på honom med ett nästan omärkligt höjt ögonbryn.

“Det där lät som Lena.”

“Ta tillbaka det.”

“Nej.”

Han kunde inte låta bli att skratta. Men skrattet fastnade halvvägs, för hon hade rätt. Inte i tonen, men i saken. Om han skulle stå framför Karin och Lena i eftermiddag och säga att teamet behövde självservice, behövde han också säga vad de själva var beredda att äga.

Inte bara vad de ville slippa.

Han öppnade sin laptop igen och drog upp en ny sida i teamets arbetsyta.

**Teamets bild av självservice**

Han skrev underrubriker:

- Miljöer
- Deployment
- Beroenden
- Databas
- MQ
- Loggning och övervakning
- Incidentansvar
- Rollback

Orden såg torra ut. Men under dem fanns allt de hade bråkat om i månader. Väntan. Misstro. Brist på åtkomst. Brist på standarder. Frågan om vem som egentligen skulle behöva ligga vaken när något gick fel.

“Vi behöver en demo”, sa han.

Jonas höjde sin kaffemugg.

“Äntligen ett ord jag tycker om.”

“Inte en teknisk säljdemo. En flödesdemo.”

“Det där var ett fruktansvärt sätt att ta tillbaka ordet demo.”

Amir ignorerade honom.

“Vi visar hur det borde fungera. Kod in, pipeline kör, image byggs, tester, policykontroller, deployment till testmiljö, automatiskt skapade standardresurser, loggning kopplad, health checks verifierade, beroenden deklarerade. Och sedan visar vi var det faller i dag.”

Naya nickade långsamt.

“Bra. Men då måste vi visa vad vi inte har löst också.”

“Som?”

“Databasmigreringar. MQ-belastning. Incidentbemanning. Och att vår readiness faktiskt är för tunn.”

Jonas suckade.

“Kan vi inte bara vara övertygande utan att vara självskadliga?”

“Det är exakt den frågan som gör att drift inte litar på oss”, sa Naya.

Det blev tystare än Amir hade väntat sig. Inte obehagligt, men skarpt. Som när ett fönster öppnas i ett rum där luften blivit dålig utan att någon märkt det.

Jonas såg ner i kaffet.

“Jag vet.”

Hans röst var låg nu. Utan skämtets skydd.

“Jag vet att det finns saker vi missar. Men jag orkar inte fler gånger där vi gör nittio procent rätt och sedan stoppas av något som ingen berättade förrän sista dagen.”

Amir kände hur meningen landade. Där var teamets verkliga frustration, renare än hans egen argumentation. Det var inte att de ville ha frihet från krav. Det var att kraven kom sent, i olika format, från olika personer, med olika konsekvenser, och alltid när energin redan var slut.

Han tänkte på sitt första år på myndigheten. Då hade han kommit från konsultvärlden med övertygelsen att långsamhet främst var ett kompetensproblem. Smarta människor kunde lösa saker snabbt. Efter sex månader hade han förstått att långsamheten hade arkitektur. Den satt i ärenden, behörigheter, ansvarslinjer, budgetkoder, styrgrupper, miljöskillnader och en ständig rädsla för att bli den person vars beslut hamnade i en avvikelserapport.

Ändå hade han inte riktigt förlåtit organisationen för det.

Kanske för att han var rädd att om han förlät den skulle han börja anpassa sig.

“Vi ska inte låtsas att allt är klart”, sa han. “Men vi ska visa vad som skulle kunna bli klart tidigare om vi byggde det som en produkt. Inte som en tjänst drift gör åt oss när de hinner.”

Naya lutade sig fram.

“Då behöver vi namnge vad vi vill ha av drift också.”

“Ja.”

“Inte ‘sluta stoppa oss’.”

“Nej.”

“Utan?”

Amir tittade på tavlan.

“Standarder. Tydliga kontroller. API:er eller beställningsmallar som faktiskt passar containrar. Tidig granskning av driftbarhet. Och någon form av gemensam katalog för godkända mönster.”

Jonas gjorde en gest mot honom med muggen.

“Där. Säg så i mötet. Inte det där du brukar säga.”

“Vad brukar jag säga?”

“Att vi inte kan vänta på manuella grindvakter från 2007.”

“Jag säger inte 2007 varje gång.”

“Nej. Ibland säger du 2009.”

Naya log, men Amir kände värmen i ansiktet. Det var pinsamt eftersom det var sant. Han hade använt drift som symbol lika mycket som drift hade använt utveckling som riskkategori.

Hans telefon vibrerade. Ett meddelande från Karin i kanalen `container-pilot-samverkan`.

> Inför eftermiddagens möte: jag vill att varje grupp tar med sig en konkret bild av vad ni behöver för att piloten ska kunna gå vidare, samt vad ni själva kan ta ansvar för. Målet är inte att rädda gårdagens plan, utan att definiera miniminivån för nästa steg.

Amir visade meddelandet för de andra.

Jonas läste och nickade mot Naya.

“Hon är farlig.”

“För att hon ber oss tänka?” sa Naya.

“Ja.”

Amir svarade inte i kanalen än. Han behövde formulera sig utan att låta som om han redan stod på en scen.

Han skrev först i sina anteckningar:

**Vi behöver inte mindre drift. Vi behöver drift tidigare, tydligare och mer automatiserat.**

Han såg på meningen. Den var nästan bra.

Sedan lade han till:

**Och vi behöver själva äga mer av det som händer efter deployment.**

Det gjorde lite ont att skriva. Bra. Då var det kanske användbart.

“Vi behöver ta med Sara också”, sa Naya.

“Sara från produkt?”

“Ja. Hon måste höra att självservice inte betyder att vi kan lova snabbare leveranser utan att prioritera teknisk skuld.”

Amir kände en impuls att protestera. Produktägaren Sara hade redan press på sig från verksamheten, och han ville inte ge henne fler skäl att säga att teamet var för försiktigt. Men Naya hade rätt igen. Självservice skulle annars bli ännu ett ord som användes uppåt för att lova tid, och nedåt för att kräva kvällar.

“Bjud in henne”, sa han.

Jonas pekade på tavlan.

“Och Sofia?”

Amir vände sig om.

“Vad menar du?”

“Hon är inbjuden, eller hur? Sofia Berg.”

“Ja.”

“Bra. Då kanske någon kan översätta mellan driftens nej och våra varför.”

Naya såg på Jonas.

“Det där är inte hennes jobb.”

“Nej, men hon gör det ändå.”

Amir låtsades skriva något på datorn för att slippa möta Nayas blick. Han visste att hon såg mer än han ville. Sofia hade funnits i periferin av plattformsarbetet i månader. Inte som ansvarig, inte som beslutsfattare, men som den person vars frågor fick rummet att ändra temperatur.

Första gången Amir hade lagt märke till henne på riktigt hade varit under ett tekniskt avstämningsmöte om JBoss-konfigurationen. En arkitekt hade pratat länge om målbilden. En driftrepresentant hade pratat ännu längre om risker. Amir hade varit nära att stänga av mentalt när Sofia frågade:

“Vilken konfiguration ska kunna ändras utan ny image, och vem äger beslutet att ändra den?”

Ingen hade svarat. Inte direkt.

Det var då han hade förstått att hon inte bara kunde tekniken. Hon kunde hitta tomrummen mellan människors ansvarsområden.

Det var en farlig sorts intelligens. Den drog honom till sig och gjorde honom samtidigt försiktigare med sina egna formuleringar.

“Hon kommer säkert inte säga så mycket”, sa han.

Naya gav honom en blick.

“Det brukar vara då folk lyssnar.”

Jonas reste sig igen och gick fram till tavlan.

“Okej. Om vi ska visa flödet behöver vi en riktig tidslinje. Inte bara känslor.”

Han drog ett streck under punkterna Amir hade skrivit.

“Första beställning när?”

“Tre veckor innan sprint 18 slutade”, sa Naya.

“Datum.”

Hon letade i Jira.

“Den 14 april.”

Jonas skrev datumet.

Amir såg på dem medan de arbetade. Det var så här teamet var som bäst: snabbt, vasst, ibland respektlöst, men med en gemensam vilja att göra det krångliga begripligt. Han önskade att drift fick se det oftare. Inte bara deras krav, inte bara deras otålighet, utan deras hantverk.

Sedan insåg han att drift antagligen önskade samma sak.

Att utveckling skulle se driftens hantverk. Inte bara stoppen.

Vid lunch hade de byggt en tidslinje som täckte nästan hela väggen. Den började med behovet av en testmiljö och slutade med Lenas stoppade produktionssättning. Mellan punkterna fanns väntetider, omtag, oklarheter, felaktiga antaganden och små segrar som ingen utanför teamet hade sett.

Naya hade markerat sådant de själva borde ha gjort bättre med blå penna. Jonas hade muttrat men inte hindrat henne.

Blått fanns på fler ställen än Amir hade hoppats.

“Det här gör ont att visa”, sa Jonas.

“Bra”, sa Naya. “Då kanske det inte bara ser ut som klagomål.”

Amir tog ett foto av tavlan och laddade upp det i arbetsytan. Sedan skrev han ett svar till Karin.

> Vi tar med en konkret flödesbild från teamets sida: väntetider, omtag, manuella beställningar och sådant vi själva behöver äga bättre. Vi vill också visa hur ett självserviceflöde skulle kunna se ut med tydliga kontroller tidigare i kedjan.

Han tvekade innan han skickade. Det fanns en formulering han ville lägga till. Något om att drift behövde möta dem halvvägs. Något om att de inte kunde fortsätta bli bedömda med rutiner som inte passade tekniken.

Men han lät bli.

Inte för att det var fel.

För att det skulle höras ändå.

Han skickade.

Några minuter senare kom Karins svar.

> Bra. Ta gärna med både målbild och friktion. Vi behöver båda.

Amir stirrade på ordet friktion.

Det var ett av de där orden coacher älskade. Men den här gången kändes det inte helt tomt. Friktion var exakt vad det var. Inte stopp, inte motstånd, inte illvilja. Ytor som gneds mot varandra för att de inte var formade för samma rörelse.

Sara, produktägaren, kom in strax efter tolv med en matlåda i handen och ett uttryck som sa att hon redan visste att hon inte skulle få äta i fred.

“Jag hör att ni vill dra in mig i plattformspolitik.”

“Vi vill dra in dig i verkligheten”, sa Naya.

“Det låter värre.”

Amir förklarade. Först snabbt, sedan långsammare när han såg hur Saras ansikte förändrades från försvar till oro.

“Betyder det här att vi tappar releasen även nästa vecka?” frågade hon.

“Det beror på.”

“Det där är inte ett svar jag kan ta till verksamheten.”

“Nej”, sa Amir. “Men ett falskt ja är sämre.”

Han hade tänkt att meningen skulle låta stabil. I stället lät den som något han själv behövde öva på att tro.

Sara satte sig på kanten av bordet.

“De väntar på den här funktionen. Handläggarna gör delar manuellt nu. Det är inte bara en intern teknikövning.”

“Jag vet.”

“Gör du?” Hennes röst var inte hård, men trött. “För ibland låter det som att både ni och drift pratar om plattformen som om det viktigaste är vem som har rätt om arbetssättet. Verksamheten bryr sig om att meddelandena går fram.”

Amir tog emot det utan att svara direkt. Han ville säga att det var just därför de behövde självservice. Att handläggarna fick vänta eftersom organisationen byggt en leveransmodell där varje beroende blev en kö. Men han hörde också den dolda anklagelsen: att även han kunde bli så upptagen av förändringen att nyttan blev abstrakt.

“Då behöver du vara med i eftermiddag”, sa han. “Inte för att pressa fram datum. För att hjälpa oss säga vad risken kostar på båda sidor.”

Sara såg på tavlan. På alla pilar, datum och blå markeringar.

“Ni har markerat era egna missar.”

“Naya gjorde det.”

“Naturligtvis.”

Naya log kort.

Sara gick närmare väggen.

“Det här borde ledningen se.”

“De vill se gröna statusrapporter”, sa Jonas.

“Då får vi visa varför de är gula.”

Amir såg på Sara och kände något i honom justeras. Teamet var inte ensamt i sin frustration. Verksamheten väntade också. Drift bar också. Karin försökte hålla ihop. Elin pressades uppifrån. Sofia såg något ingen gett henne mandat att göra något åt.

Det gjorde inte hindren mindre irriterande.

Men det gjorde bilden svårare att förenkla.

Klockan 13.42, arton minuter före Karins möte, stod Amir ensam kvar framför tavlan. De andra hade gått för att hämta kaffe, svara på meddelanden eller i Saras fall ringa ett samtal till verksamheten och formulera en försening utan att kalla den försening.

Han läste igenom deras rubriker en gång till.

Miljö.  
Brandvägg.  
Oracle.  
MQ.  
Elasticsearch.  
Rollback.  
Incidentansvar.

Det kunde se ut som teknik. Men varje ord betydde egentligen: vem får göra vad, vem behöver veta vad, vem litar på vem, och vem blir väckt när antagandet visar sig fel.

Han öppnade Teams och klickade på Lenas namn.

Markören blinkade i meddelanderutan.

Han skrev:

> Vi har tagit fram vår bild av flödet och även markerat saker vi själva behöver ta ansvar för. Jag tror det kan hjälpa mötet.

Han läste meningen. För artig? För svag? För mycket som att han bad om godkännande?

Han lade till:

> Jag står fast vid att dagens ledtider inte fungerar, men jag förstår bättre varför stoppet kom.

Det tog emot att skriva. Därför skickade han.

Svaret dröjde.

Han hann ångra sig två gånger, skriva en mental version där han var skarpare och en annan där han inte hade hört av sig alls.

Sedan kom Lenas svar.

> Bra. Ta med konkreta exempel. Jag tar med driftens miniminivå.

Inget tack. Ingen smiley. Ingen värme.

Men inte heller någon sköld.

Amir lade ner telefonen och såg på tavlan igen.

För första gången sedan stoppet kände han inte att eftermiddagens möte bara var något att vinna.

Det var mer obekvämt än så.

Det kunde bli något de behövde förtjäna.
