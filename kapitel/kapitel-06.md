# Kapitel 6 – Workshoppen

Karin kom tio minuter för tidigt till Björken och låste upp rummet med armbågen eftersom hon bar på en laptop, en bunt utskrivna lappar och två pennställ från materialskåpet.

Det var egentligen inte hennes rum. Det var ett sådant där projektrum som alla kunde boka men ingen riktigt tog hand om. Whiteboardpennorna var nästan alltid torra. Någon hade lämnat en kaffering på fönsterbrädan som ingen längre såg. På väggen satt fortfarande en tejpremsa efter en workshop om “digitalt kundmöte” som måste ha hållits långt innan containerplattformen hade blivit ett ord i ledningens månadsrapport.

Karin ställde ner sakerna och såg sig omkring.

Björken var för litet för konflikt och för stort för intimitet. Det var den sämsta möjliga storleken för ett möte där människor skulle våga erkänna att deras sätt att arbeta inte höll. Samtidigt fanns det något användbart i just det. Ingen kunde gömma sig längst bak. Ingen kunde låtsas att tavlan var någon annans.

Hon drog upp persiennen. Regnet gjorde innergården blank.

På whiteboarden skrev hon med blå penna:

**Från kodändring till trygg produktion**

Hon stod kvar med pennan i handen och betraktade orden. Trygg produktion. Hon hade först tänkt skriva “snabb produktion”, men det hade varit att välja sida innan mötet ens börjat. “Effektiv produktion” lät som styrgruppssvenska. “Trygg” var farligare. Det var ett ord både drift och utveckling skulle kunna vilja äga.

Under rubriken drog hon en lång horisontell linje och satte upp gula lappar längst till vänster:

**Kod klar**  
**Bygg image**  
**Testa**  
**Beställ miljö**  
**Konfigurera beroenden**  
**Driftgranska**  
**Produktionsfönster**  
**Verifiera**  
**Förvalta**

Hon visste redan att linjen var för enkel. Det var poängen. Ingen reagerade på en tavla som redan var sann. Människor behövde få upptäcka sanningen själva och helst också få bli lite irriterade över att deras verklighet inte syntes.

Hennes dator plingade. Ett nytt meddelande från Elin.

> Jag kommer första halvtimmen. Behöver sedan in i annan styrning. Försök få fram konkreta nästa steg.

Karin läste det två gånger.

Försök få fram konkreta nästa steg.

Det var en rimlig förväntan. Det var också precis den sortens förväntan som gjorde att organisationen gång på gång hoppade över frågan om vem som faktiskt skulle göra stegen, med vilken tid, på vems mandat och på bekostnad av vad.

Hon skrev inte det.

> Bra. Jag håller fokus på flöde, ansvar och stoppunkter.

Hon lät meddelandet vara oskickat en sekund, ändrade “stoppunkter” till “beslutspunkter” och skickade.

När hon såg upp stod Sofia i dörren.

Hon hade en svart kofta över en enkel skjorta, håret uppsatt utan att riktigt vara uppsatt och en laptop under armen. Hon såg inte trött ut på det sätt som Lena gjorde. Sofias trötthet var mer koncentrerad, som om den låg bakom ögonen och bara syntes när hon tänkte för snabbt.

“Är jag för tidig?” frågade Sofia.

“Det är jag som är för tidig. Då ser man alltid ambitiös ut.”

Sofia log svagt och kom in.

“Eller nervös.”

Karin skrattade kort. Hon tyckte om människor som hörde vad man inte sa, även om de gjorde hennes arbete svårare.

“Lite både och.”

Sofia ställde sin dator vid ena änden av bordet men satte sig inte. Hon gick fram till tavlan och läste lapparna från vänster till höger.

“Du saknar ‘förstå vad applikationen faktiskt behöver’.”

Karin tog en gul lapp och skrev exakt det.

**Förstå behov och beroenden**

“Var ska den sitta?”

Sofia pekade inte direkt. Hon funderade, och Karin såg hur hon inte bara tänkte på processen utan på alla gånger processen redan hade misslyckats.

“Före kod klar”, sa Sofia. “Egentligen före kod börjar. Men då blir det bråk.”

“Bra”, sa Karin och satte lappen längst till vänster. “Bråk är data.”

Sofia gav henne en blick.

“Säg inte så när Mats kommer.”

“Nej. Jag har överlevnadsinstinkt.”

Amir kom två minuter senare med Naya och Jonas bakom sig. Sara kom strax efter, med mobiltelefonen mot örat och en rynka mellan ögonbrynen. Hon avslutade samtalet i dörren med orden “nej, jag lovar inte datum förrän vi vet vad drift säger, och det är inte samma sak som att drift bestämmer vår roadmap”.

Karin lade märke till att Amir hörde det. Hans ansikte rörde sig nästan inte, men något i axlarna sjönk en aning. Han bar på teamets frustration, men också på trycket från dem som väntade på nyttan. Det gjorde honom mer komplicerad än rollen “otålig utvecklingslead”. Det var bra för mötet, tänkte Karin. Dåligt för Amir.

Lena och Mats kom sist av de centrala deltagarna. Inte för sent, men så nära starttid att det tydligt inte fanns en sekund över att ge bort. Lena hade en anteckningsbok i handen och telefonen vänd med skärmen neråt, som om hon redan hade bestämt sig för att inte låta den vinna. Mats bar ingen dator alls.

“Databassidan?” frågade Lena och såg på Karin.

“Peter kommer digitalt om fem minuter”, sa Karin. “MQ representeras av Mats tills vidare, om det är okej?”

Mats drog ut en stol.

“Jag älskar när ‘tills vidare’ betyder ‘för alltid’.”

Karin skrev upp **MQ – Mats tills vidare** på en lapp och satte den i hörnet av tavlan.

“Jag hör att det är en risk.”

Mats satte sig långsamt.

“Det var inte en komplimang.”

“Jag vet.”

Elin kom in precis när mötet skulle börja. Hon bar med sig sin chefsnärvaro som andra bar nyckelkort: synligt, nödvändigt, lite skavande. Alla noterade henne, även de som inte tittade upp.

Karin ställde sig vid tavlan.

“Syftet med det här mötet är inte att rädda ett produktionsfönster”, sa hon. “Det är inte heller att avgöra vem som hade rätt i går. Syftet är att synliggöra vägen från kodändring till trygg produktion för pilotens tjänst och hitta vilka krav som behöver komma tidigare, vilka steg som kan automatiseras och vilka ansvar som saknar ägare.”

Hon såg på Lena när hon sa “krav som behöver komma tidigare”. Lena gav ingen synlig reaktion, men Karin anade att formuleringen hade landat på rätt sida av hennes försvar.

“Vi börjar med flödet”, fortsatte Karin. “Inte idealflödet. Det faktiska.”

Jonas lutade sig bakåt.

“Hur många väggar har vi?”

“Vi börjar med en”, sa Karin.

Det kom några låga skratt. Till och med Mats drog lite på munnen.

Karin bad Amir beskriva teamets väg från kodändring till produktionssättning. Han reste sig inte först. Det var som om han behövde avgöra om han stod inför en domstol eller en verkstad. Sedan gick han fram till tavlan och tog pennan.

“Vi utvecklar ändringen, bygger image, kör våra automatiska tester, deployar i test. Sedan behöver vi beroenden. Oracle-behörigheter, MQ-kö, konfiguration, brandvägg, certifikat, loggning, miljövariabler, secrets.”

Han sa orden snabbt, som någon som hade räknat upp dem för många gånger.

Karin märkte att Lena skrev något. Inte protesterade, bara skrev.

“Vad händer efter att ni behöver beroenden?” frågade Karin.

“Vi skapar ärenden.”

“Ett ärende?”

Amir log utan glädje.

“Det hade varit fint.”

Naya reste sig och gick fram bredvid honom. Hon tog en grön penna och började sätta små streck under flödet.

“Ett för miljö. Ett för brandvägg. Ett för databas. Ett för MQ. Ibland ett för certifikat, beroende på om någon tycker att det ingår i miljö eller inte. Ett för loggning om indexet inte redan finns. Sedan kommentarer i ärenden, Teams, ibland mejl.”

“Varför mejl?” frågade Karin.

Naya såg nästan generad ut.

“För att någon inte är med i Teamskanalen. Eller för att ärendet inte går att använda för diskussion. Eller för att vi behöver få tag på en person.”

“Person”, upprepade Karin och satte upp en orange lapp: **Hitta rätt person**.

Mats tittade på lappen.

“Den där borde vara större.”

Karin gav honom en penna.

“Gör den större.”

Han tog pennan, lite motvilligt, och skrev på en ny lapp med blockiga bokstäver:

**HITTA NÅGON SOM VET**

Han satte den mitt på linjen, inte i början eller slutet utan ovanpå nästan allting.

Det blev tystare än Karin hade väntat sig.

För en sekund försvann humorn ur rummet. Där satt den, enkel och ful, som en sammanfattning av halva myndighetens IT-styrning.

Lena såg på lappen länge. Karin försökte läsa hennes ansikte men kom bara halvvägs. Där fanns något som liknade igenkänning, men också skam. Inte personlig skam, kanske. Snarare den sortens skam som uppstod när ett fungerande nödläge blev synligt som normalprocess.

Elin rörde sig i stolen.

“Det där är väl också en kunskapsdelningsfråga.”

Mats såg på henne.

“Det är en tid-fråga. Och en ansvar-fråga. Kunskap delar sig inte själv mellan incidenter.”

Elin öppnade munnen men stängde den igen. Karin noterade det. Inte som seger, utan som ett litet ögonblick av verklighet som inte direkt polerades bort.

“Vi markerar väntan”, sa Karin. “Var uppstår väntan?”

Jonas skrattade till.

“Får jag bara hälla ut lapparna?”

“Gör det strukturerat.”

“Det är inte så väntan fungerar.”

Ändå gick han fram. Han började sätta röda lappar mellan nästan varje steg.

**Väntar på godkännande**  
**Väntar på åtkomst**  
**Väntar på svar i ärende**  
**Väntar på driftgranskning**  
**Väntar på nästa produktionsfönster**  
**Väntar på någon som kan tolka gammal konfiguration**

När han var klar såg tavlan mindre ut som ett flöde och mer som ett utslag.

Amir stod kvar bredvid tavlan, men hans energi hade förändrats. Han såg inte triumferande ut. Karin hade väntat sig att han skulle använda bilden som bevis mot drift. I stället såg han nästan besvärad ut, som om tavlan bekräftade hans frustration men också gjorde den svårare att använda som vapen.

“Det här är vårt problem”, sa han till slut. “Vi kan inte leverera i den här takten.”

Lena lyfte blicken från sina anteckningar.

“Och vi kan inte granska allt manuellt i den här takten.”

“Det är ju det vi säger.”

“Nej”, sa Lena. Hennes röst var lugn, men Karin hörde hur hon valde varje ord med omsorg. “Ni säger ofta att vi ska sluta stoppa er. Jag säger att vi måste sluta bygga ett system där stoppet kommer sist.”

Amir såg ut som om han först tänkte svara snabbt. Sedan lät han bli.

Karin kände igen det där ögonblicket. Det var inte samsyn, men det var en mikroskopisk paus i försvarsmekanismen. Ofta var det allt man fick.

Sofia hade varit tyst länge. Hon stod nära fönstret, en bit från tavlan, och Karin såg hur hon inte följde samtalet som en vanlig deltagare. Hon sorterade det. I huvudet måste hon redan ha ritat om tavlan i lager: applikation, plattform, beroenden, ansvar, runtime, data, integration.

Karin vände sig mot henne.

“Sofia. Vad ser du?”

Sofia ryckte nästan till, inte för att hon var oförberedd utan för att hon hade hoppats få vara det lite till.

“Jag ser att vi blandar tre saker och kallar allt produktionssättning.”

Hon gick fram till tavlan. Amir flyttade sig utan att hon bad om det.

“Första saken är applikationens leverans. Image, kod, tester, versionshantering. Det kan teamet äga mer av än i dag.”

Hon ritade en tunn ruta runt de första lapparna.

“Andra saken är plattformens standardförmågor. Deploymönster, konfigurationssätt, secrets, loggning, metrics, health checks, policykontroller. Det borde inte uppfinnas per applikation.”

Hon ritade en andra ruta, större och mer osymmetrisk.

“Tredje saken är externa beroenden: Oracle, MQ, Elasticsearch, nät, certifikat, behörigheter. De kan inte bara trollas bort för att applikationen kör i container.”

Mats nickade innan han hann stoppa sig själv.

Sofia fortsatte, nu mer säker.

“Problemet med piloten är att vi låtsas att första rutan kan springa fortare medan andra och tredje rutan fortfarande fungerar som förr. Då får teamet vänta, drift får granska sent, och plattformen blir bara en ny plats där gamla oklarheter hamnar.”

Det blev stilla.

Karin såg på Elin. Hon hade slutat titta på telefonen.

“Vad skulle behöva finnas i andra rutan?” frågade Karin.

Sofia tog en svart penna.

“En standard för readiness och liveness som betyder något. Inte bara att processen svarar. En mall för hur beroenden deklareras. En miniminivå för loggning och spårbarhet. En modell för rollback som skiljer på image, konfiguration och data. Godkända sätt att hantera secrets. Och en tydlig lista över vad teamet får göra själv när det följer mallen.”

“När det följer mallen”, upprepade Lena.

Sofia såg på henne.

“Ja. Annars är det inte självservice. Då är det bara att flytta handpåläggningen till ett annat ställe.”

Amir korsade armarna, men inte aggressivt. Mer som om han behövde hålla fast något i sig själv.

“Men om mallen tar tre månader att ta fram har vi inte löst någonting.”

“Nej”, sa Sofia. “Därför behöver vi en tunn första version. Men den måste ägas av någon.”

Karin lät meningen hänga. Hon ville inte fylla i den för snabbt. Organisationer kunde bli märkligt skickliga på att gå förbi ordet ägare när det blev konkret.

Elin bröt tystnaden.

“Vad menar du med ägas?”

Sofia såg ut som om hon ångrade att hon sagt det, men hon backade inte.

“Jag menar att någon behöver kunna säga: så här ser den godkända vägen ut nu, det här ingår, det här ingår inte, det här måste teamen uppfylla, det här måste plattformen leverera, och det här ligger fortfarande hos externa beroendeägare. Annars kommer varje pilot bli en förhandling.”

“Kan inte det vara den här gruppen?” frågade Elin.

Karin kände hur rummet drog efter andan utan att någon hörbart gjorde det. “Gruppen” var en vacker plats att lägga ansvar på om man inte ville välja person, tid eller konflikt.

Lena hann före henne.

“En grupp kan bidra. Den kan inte vara ansvarig klockan 22.40 när något inte fungerar.”

Mats tittade på henne med något som kunde vara stolthet om han hade varit en annan sorts människa.

Karin skrev på tavlan:

**Grupp ≠ ägare**

Elin såg på orden. Karin visste att hon tog en risk. Det var en sak att facilitera; en annan att skriva chefens otydlighet på väggen. Men hon hade kommit till en punkt där mjukare formuleringar bara skulle skapa ännu en röd lapp längre fram.

Peter från databassidan anslöt till mötet via skärm fem minuter för sent och med ljudet på för högt. Hans första bidrag var att Oracle absolut inte skulle in i någon containerplattform “bara för att någon varit på konferens”. Det kunde ha förstört energin i rummet, men i stället blev det nästan användbart. Frågan behövde sägas rakt.

“Vi pratar inte om att flytta Oracle nu”, sa Sofia.

Peter såg misstänksam ut, vilket var rimligt. Organisationer hade en tendens att säga “inte nu” när de menade “så snart du slutar bevaka frågan”.

“Vad pratar vi om då?”

“Kontrakt”, sa Sofia. “Vilka schemaändringar kräver granskning. Hur migrering testas. Hur rollback hanteras när data ändrats. Vilka kopplingar teamet får beställa själv och vilka som kräver DBA. Och hur vi får det synligt tidigare än veckan för produktionssättning.”

Peter tystnade. Sedan sa han:

“Det kan jag prata om.”

Karin skrev **Oracle som kontrakt, inte flyttbeslut** på tavlan.

Hon märkte att Amir såg på orden. Det var inte vad han ville ha, men det var något han kunde arbeta med. För Karin var det där ett viktigt tecken. Alla bra kompromisser var först lite otillfredsställande.

Mötet fortsatte. MQ blev nästa strid. Mats förklarade varför persistenta meddelanden, återstartsbeteenden och felköer inte kunde behandlas som en rad i en miljövariabell. Jonas försökte först skämta om att “kö är ju bara asynkron väntan med bättre självbild”, men när Mats beskrev vad som hände om ett meddelande tappades mellan två system slutade han.

Lena antecknade inte längre lika mycket. Hon lyssnade. Det slog Karin att Lena kanske var ovan vid möten där driftens invändningar inte omedelbart tolkades som broms, men också ovan vid att deras egna rutiner ritades upp som problem. Varje gång någon sa “driftgranskning” som om det var en svart låda blev hennes ansikte en aning stängdare.

Karin gick fram till tavlan och ritade en cirkel runt alla lappar som hade ordet “granska”, “kontrollera”, “godkänna” eller “verifiera”.

“Vad av det här behöver vara mänsklig bedömning?” frågade hon. “Och vad kan vara automatisk kontroll?”

Lena svarade inte först. Amir gjorde det inte heller.

Det var Naya som bröt tystnaden.

“Testresultat borde kunna vara automatiskt. Men någon måste bestämma vilka tester som räcker.”

“Policy för obligatoriska fält i deploymentunderlag kan vara automatisk”, sa Amir. “Åtminstone så att ärendet inte ens går vidare om rollback saknas.”

Lena tittade på honom. Karin såg att hon inte hade väntat sig det från honom.

“Readinesskrav kan valideras delvis”, sa Sofia. “Inte att allt är rätt, men att teamet deklarerat beroenden och att endpointen inte bara svarar lokalt.”

Mats lade till:

“MQ-dokumentation ska inte ligga i en wiki där halva rummet saknar behörighet.”

“Automatisk åtkomst?” frågade Karin.

“Nej”, sa Mats. “Men gemensam plats. Och ägare.”

Ordet ägare återkom hela tiden nu. Karin skrev det i mitten av tavlan, större än hon först tänkt.

**ÄGARE**

Det såg nästan brutalt ut.

Elin tittade på klockan. Hennes halvtimme hade blivit femtio minuter. Karin såg att hon borde gå, men också att hon inte ville lämna innan hon visste vad hon lämnade.

“Jag behöver snart vidare”, sa Elin. “Vad behöver ni från mig?”

Rummet blev tyst på ett annat sätt. Inte osäkert. Mer hungrigt.

Karin kände impulsen att rädda Elin med en sammanfattning. Hon lät bli.

Lena talade först.

“Tid. Om drift ska bidra till att bygga automatiska kontroller och tydliga krav kan det inte ske mellan incidenter.”

Amir fortsatte, oväntat snabbt.

“Och om teamet ska ta mer produktionsansvar behöver det stå i vårt uppdrag. Inte bara som en förväntan när något går fel.”

Sofia sa:

“Någon behöver äga den tekniska vägen. Inte allt, men tillräckligt för att beslut inte ska förhandlas om varje gång.”

Mats lutade sig bakåt.

“Och sluta kalla saker pilot om ni menar produktion med sämre underlag.”

Det gick ett kort skratt genom rummet, men det bar mer allvar än skämt.

Elin såg på tavlan. Karin undrade vad hon såg: lappar, kostnader, risker, en hotad tidsplan, eller kanske för första gången en karta över det ansvar som hittills hade gömt sig mellan kolumnerna.

“Jag kan inte lova allt här och nu”, sa Elin.

Karin noterade hur flera ansikten stängdes, för de hade hört den meningen förr.

Elin fortsatte:

“Men jag kan ta med mig tre saker. Ett: vi behöver frigöra tid för drift och plattformsarbete, inte bara lägga det ovanpå. Två: pilotens miniminivå ska beslutas innan nästa produktionsfönster bokas. Tre: jag vill ha ett förslag på tekniskt ägarskap för plattformens arbetssätt.”

Hon såg på Karin när hon sa det sista, men Karin såg att orden träffade Sofia.

Sofia tittade ner i bordet. Inte blygt. Snarare för att dölja att hon redan visste vad alla andra började förstå.

Karin kände en blandning av lättnad och oro. Det var ett bra steg. Det var också början på nästa konflikt.

När Elin hade gått förändrades rummet. Inte mycket, men tillräckligt. Chefsnärvaron hade hållit vissa formuleringar på plats. Nu blev människor lite mer sig själva.

Jonas sträckte på sig.

“Så vi löste inte allt på två timmar?”

“Jag beklagar”, sa Karin. “Jag borde ha haft fler färger.”

Mats pekade på tavlan.

“Du har rött. Det räcker.”

Amir gick närmare tavlan och stod bredvid Lena utan att de tittade på varandra.

“Om vi tar fram en första version av deploymentmallen”, sa han, “kan drift titta på den innan vi bygger om allt?”

Lena dröjde med svaret. Karin såg hur hon vägde kalendern, tröttheten, principen och möjligheten. Det var mycket som fick plats i en tystnad om man lät den vara.

“Ja”, sa Lena. “Men inte som fristående dokument på fredag eftermiddag. Vi sitter tillsammans en timme. Du, jag, Sofia, Mats om han behövs. Naya också, om test ska bli verkligt.”

Naya såg nästan överraskad ut över att bli nämnd.

“Jag kan.”

Amir nickade.

“Bra.”

Det var inget varmt ögonblick. Ingen log stort. Ingen sa att de äntligen förstod varandra. Men Karin kände igen det som mer värdefullt än samförstånd: ett konkret åtagande som inte byggde på att någon låtsades vara mindre bekymrad än de var.

Sofia samlade ihop sina saker när de andra började lämna rummet, men Karin hann fram till henne innan hon försvann.

“Har du fem minuter?”

Sofia såg mot dörren där Amir just gick ut. Han vände sig inte om, men Karin kunde inte avgöra om Sofia hade hoppats att han skulle göra det.

“Fem”, sa Sofia.

De stod kvar vid tavlan. Rummet var plötsligt fullt av kvarlämnade stolar, torra pennor och beslut som ännu inte var beslut.

Karin pekade på Sofias tre rutor.

“Det där var tydligt.”

“Det var inte färdigt.”

“Det behöver inte vara färdigt för att vara sant.”

Sofia suckade.

“Karin.”

Det var första gången hon sa hennes namn så. Inte som tilltal, mer som varning.

“Jag tänker prata med Elin om tekniskt ägarskap”, sa Karin.

“Det förstod jag.”

“Jag tänker säga att det inte räcker med en grupp.”

“Det förstod jag också.”

“Och att du redan gör delar av jobbet informellt.”

Sofia såg länge på tavlan.

Där fanns allt hon hade sagt, fast förenklat till rutor och lappar. Karin undrade om det kändes som att bli sedd eller få sin flyktväg blockerad.

“Det är skillnad på att hjälpa till och att äga”, sa Sofia.

“Ja.”

“Om de vill att någon ska äga behöver de ge mandat, tid, folk och prioritering. Inte bara ett nytt ansvar i ett möte.”

“Det tänker jag också säga.”

Sofia vände sig mot henne.

“Och om de inte gör det?”

Karin hade inget färdigt svar. För en gångs skull lät hon bli att låtsas.

“Då kommer vi fortsätta ha workshoppar om samma problem tills nästa incident bestämmer åt oss.”

Sofia log inte. Men hon såg mindre ensam ut än en minut tidigare.

“Då säger du det till Elin”, sa hon.

“Ja.”

“Och du säger inte att jag har bett om rollen.”

“Nej.”

“För det har jag inte.”

“Nej.”

Sofia tog sin laptop.

“Men säg att om de vill ha rollen, då får de ta den på allvar.”

När hon gick stod Karin kvar en stund framför tavlan.

Hon borde fotografera den, renskriva, skicka ut anteckningar, formulera åtgärder, boka uppföljning, skapa struktur. Allt det skulle hon göra. Det var hennes arbete. Hennes sätt att ge kaoset form.

Men först lät hon blicken vila på Mats stora lapp mitt i flödet.

**HITTA NÅGON SOM VET**

Det var en sorglig lapp. Och en ärlig.

Karin tog en svart penna och skrev en ny bredvid den:

**BYGG SÅ ATT FLER KAN VETA**

Hon visste inte om det var ett mål, en strategi eller bara en önskan.

Men för första gången den dagen kändes det som en början.
