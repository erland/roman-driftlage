# Kapitel 15 – Förproduktionsincidenten

Naya hade börjat ogilla ordet verifierad.

Inte för att det var ett dåligt ord. Tvärtom. Det var ett av de ord hon själv brukade försvara när andra ville kalla något klart för att det gick att klicka sig igenom den glada vägen tre gånger i rad. Verifierad betydde prövad. Visad. Inte önskad.

Men den här veckan hade ordet fått något nästan religiöst över sig.

Verifierad miniminivå. Verifierad runbook. Verifierade felvägar. Verifierad readiness. Verifierad kompensation.

Allt skulle verifieras, och varje gång någon sa det tittade de på henne som om testning var en plats där osäkerhet gick in och säkerhet kom ut, färdigförpackad i grönt.

Hon satt i testrummet som egentligen hette Aspen men som alla kallade Förprod eftersom rummet hade den ovanliga egenskapen att faktiskt ligga nära den miljö det pratades om. På bordet stod fyra halvdruckna kaffemuggar, två skärmar visade loggar och på whiteboarden hade Sofia skrivit tre rubriker med blå penna.

**Oracle timeout**  
**MQ-stopp**  
**Rollback/kompensation**

Under dem hade Naya fyllt på med mindre pilar och frågetecken. Hon hade inte gjort det för att vara dramatisk. Frågetecken var bara ärligare än de flesta statusmarkeringar.

Amir stod vid fönstret och pratade lågt i telefon med Sara. Han hade den där stillheten i kroppen som han fick när han ansträngde sig för att inte låta otålig. Naya hade arbetat med honom tillräckligt länge för att se skillnaden mellan lugn och kontrollerad acceleration.

“Nej”, sa han. “Vi bokar inte produktion efter dagens körning. Vi bokar när miniminivån faktiskt håller.”

Han lyssnade.

“Jag vet. Jag vet vad jag sa för två veckor sedan.”

Naya tittade bort, inte för att ge honom integritet utan för att slippa se hur mycket det kostade honom att säga det där. Amir var bra på att ändra sig i sak när han väl hade förstått varför. Han var sämre på att förlåta sig själv för att han inte förstått det tidigare.

Vid andra sidan bordet satt Mats med runbooken utskriven framför sig. Han hade skrivit ut den trots att den låg i Git, vilket Jonas hade kommenterat som “analog observability”. Mats hade svarat att papper åtminstone inte krävde single sign-on när allt annat brann. Ingen hade riktigt vågat säga emot.

Sofia stod vid tavlan. Hon skrev inte just nu. Hon höll pennan mot handflatan och såg på flödet som om det redan hade gått sönder och hon försökte förstå var sprickan skulle börja.

Naya tyckte om det hos henne. Inte oron i sig, men sättet Sofia lät oron arbeta. Många tekniker blev antingen förälskade i sin lösning eller rädda för den. Sofia gjorde något tredje. Hon betraktade lösningen som ett förslag verkligheten ännu inte hade hunnit förolämpa.

Lena kom in två minuter efter utsatt tid med datorn under armen och blicken redan fäst vid skärmen.

“Förlåt”, sa hon. “Ett certifikatärende som vägrade dö.”

Mats lyfte inte ens blicken.

“De gör sällan det. De odöda bland driftärenden.”

Lena satte sig bredvid honom. Hon såg trött ut, men inte frånvarande. Det var något med henne den här veckan som Naya hade lagt märke till: samma vaksamhet som tidigare, men mindre automatisk nej-rörelse. Som om hon fortfarande stod vid bromsen, men nu också tittade efter var vägen faktiskt gick.

Karin kom sist. Hon hade ingen dator i händerna den här gången, bara en anteckningsbok och en penna. Naya hade först trott att det var en stilgrej. Nu undrade hon om Karin använde papper för att inte gömma sig bakom skärmen när rummet blev obekvämt.

“Vi börjar inte med status”, sa Karin när hon hade satt sig. “Vi börjar med syfte. Vad ska vi veta efter den här körningen som vi inte vet nu?”

Naya kände hur alla blickar drogs åt hennes håll.

Hon hade förberett sig. Ändå stack det till. Det var skillnad på att äga en testplan och att bli den som förväntades tala om när osäkerheten var borta.

“Vi ska veta tre saker”, sa hon. “Ett: vad som händer när Oracle svarar långsamt eller inte alls under meddelandeflödet. Två: vad som händer när MQ inte tar emot eller levererar som väntat. Tre: om vår kompensation faktiskt lämnar ärendet i ett begripligt tillstånd, både tekniskt och verksamhetsmässigt.”

“Begripligt för vem?” frågade Karin.

Naya uppskattade frågan och hatade att den behövde ställas.

“För oss. För drift. För support. För Sara och verksamheten. Och helst för den medborgare som inte ska behöva veta att något gick fel.”

Sara deltog digitalt och hennes ruta tändes när hon nickade.

“Helst”, sa hon. “Men om medborgaren påverkas behöver vi veta vad vi säger. Inte bara vad vi loggar.”

Amir avslutade samtalet och vände sig mot gruppen.

“Då kör vi Oracle timeout först. Vi har satt upp simulering via testprofilen. Jonas triggar flödet, Naya följer testfall, Mats och Lena följer driftvyn, Sofia tittar på plattformsloggar och pipelineartefakter.”

Han stannade upp, som om han hörde sig själv tala från en ny plats. Förr hade han sagt det snabbare, mer som order än som gemensam överenskommelse.

“Låter det rätt?” lade han till.

Lena nickade långsamt.

“Ja. Men jag vill att någon säger högt vad vi förväntar oss innan vi kör. Inte efteråt när vi redan vet vad som hände.”

Amir såg på Naya.

Hon bläddrade i testplanen.

“Vid Oracle timeout ska applikationen inte fortsätta konsumera nya MQ-meddelanden om den inte kan skriva status. Meddelandet ska antingen ligga kvar för retry eller hamna i definierad felhantering beroende på var i flödet felet sker. Readiness ska gå röd om beroendet är nere längre än tröskelvärdet. Larm ska gå till pilotens incidentkanal med korrelations-id. Runbook ska säga vem som kontrollerar vad.”

Mats pekade med pennan mot pappret.

“Och vem väcks?”

“Det här är förproduktion”, sa Jonas från sin plats vid skärmen.

Mats tittade på honom.

“Då kan du låtsas att klockan är 02.17 och att du hatar alla.”

Jonas log först, men logendet blev mindre när han förstod att Mats inte skämtade helt.

“Teamets beredskapskontakt först”, sa Amir. “Sedan drift enligt pilotens incidentväg om plattforms- eller infrastrukturindikatorer pekar dit. Databas om Oracle-indikatorer pekar dit. Men teamet äger triage initialt.”

Lena skrev något.

Naya såg det och undrade om det var godkänt eller bara antecknat. Med Lena var skillnaden viktig.

“Då kör vi”, sa Sofia.

Jonas startade testet.

Först hände ingenting på ett sätt som alltid fick Naya att tänka att system var som människor i obekväma samtal. De gjorde först anspråk på normalitet. Requesten gick igenom. Meddelandet landade på kön. Applikationen plockade upp det. Loggarna rörde sig med små, ordnade rader över skärmen.

Sedan började väntan.

Ett anrop till Oracle hängde längre än det borde.

Naya såg på sin skärm hur tiden växte.

Två sekunder. Fem. Tio.

“Timeout nu”, sa Jonas.

“Applikationen retryar”, sa Sofia.

“Readiness fortfarande grön”, sa Lena.

Det blev alldeles tyst.

Inte länge. Kanske tre sekunder. Men Naya kände hur rummet bytte temperatur.

“Den ska inte vara grön”, sa Amir.

“Nej”, sa Sofia.

Mats lutade sig fram mot driftvyn.

“Larm?”

“Inget än”, sa Lena.

Naya följde testfallet och kände den välbekanta, sjunkande känslan när verkligheten inte ens valde den intressanta felvägen utan en mycket enklare: den hade bara låtit bli att berätta att den mådde dåligt.

“Korrelations-id finns i applikationsloggen”, sa Jonas. “Men inte i larmet. För det finns inget larm.”

“Fortsätter den konsumera?” frågade Sofia.

Jonas skrev något.

Ett nytt meddelande rörde sig genom flödet.

Sedan ett till.

“Ja”, sa han. “Den fortsätter.”

Naya hörde sin egen röst innan hon hann göra den lugn.

“Då riskerar vi backlogg av halvbehandlade ärenden eller fel status, beroende på var timeouten träffar.”

“Det är förproduktion”, sa Amir, men inte försvarande. Mer som en påminnelse till sin egen puls.

“Det är därför vi är här”, sa Sofia.

Karin skrev inte. Hon tittade på dem, en efter en, och Naya förstod att hon inte bara observerade felet. Hon observerade vad felet gjorde med gruppen.

“Pausa testet”, sa Sofia.

Jonas stoppade flödet.

“Vad är hypotesen?” frågade Lena.

Sofia gick fram till tavlan och skrev under Oracle timeout:

**Readiness kontrollerar koppling vid start, inte aktuell beroendestatus.**  
**Konsument pausas inte vid beroendefel.**  
**Larm saknar affärsnära signal.**

“Det första är mitt”, sa Sofia.

Amir vände sig mot henne.

“Hur menar du?”

“Jag godkände readinessmönstret som tillräckligt för Pilotväg 0.1 om beroendekontrollerna kompletterades. Men jag såg inte att implementationen bara verifierade beroendet vid uppstart och sedan cacheade resultatet för länge. Det borde ha varit tydligare i mallen.”

“Det är vår implementation”, sa Amir.

“Det är också en mallfråga.”

“Det ena utesluter inte det andra”, sa Karin.

Det var en sådan där mening som kunde låta banal om man sa den fel. Karin sa den utan att mildra ansvaret. Naya märkte att både Sofia och Amir faktiskt hörde henne.

Lena tittade på loggvyn.

“Det viktigaste just nu är inte vems det är. Det viktigaste är att den gröna signalen ljuger.”

Mats nickade.

“Och en ljugande grön signal är värre än en röd. Rött får folk att vakna. Grönt får folk att gå och lägga sig.”

Naya skrev in avvikelsen i testprotokollet. Hon försökte hålla formuleringen saklig. Det var en professionell reflex, men också ett skydd. Om hon skrev för hårt skulle någon gå i försvar. Om hon skrev för mjukt skulle felet försvinna in i en lista över förbättringar.

Hon skrev:

**Blockerande avvikelse: readiness signalerar frisk tjänst trots att kritiskt beroende är otillgängligt och meddelandekonsumtion fortsätter. Risk för felaktig produktionell status och otillräcklig incidentrespons.**

Hon läste meningen igen. Den var inte vacker. Den var användbar.

“Det här stoppar inte bara dagens testfall”, sa Lena.

Amir såg upp.

“Vad menar du?”

“Om readiness inte går att lita på stoppar det produktionsförsöket tills det är åtgärdat och omtestat.”

Naya såg hur det drog genom Amir. Inte som ilska först, utan som förlust. Han hade vetat att det kunde hända. De hade alla vetat. Men viss kunskap fanns bara på rätt sida om händelsen. Före var den risk. Efter var den verklighet.

“Vi har fortfarande två veckors prioritering”, sa han. “Det här är exakt varför vi fick den.”

“Ja”, sa Lena. “Men jag vill vara tydlig innan någon börjar kalla det här för en mindre justering.”

“Jag tänkte inte—”

“Du tänkte boka nytt fönster så snart vi fick en grön körning.”

Amir öppnade munnen och stängde den igen.

Det var orättvist och sant på samma gång. Naya såg det i hans ansikte. Han hade tänkt det, kanske inte som beslut men som längtan. En grön körning, ett datum, en väg tillbaka till framåtrörelse.

Karin lade pennan på bordet.

“Kan vi stanna där ett ögonblick?”

Ingen svarade. Det brukade betyda ja.

“Det som händer nu är viktigt. Felet är tekniskt, men reaktionen är organisatorisk. Lena vill förhindra att vi bagatelliserar. Amir vill förhindra att vi tappar fart. Sofia vill förstå systemmönstret. Naya försöker formulera det så att det blir åtgärdbart. Mats försöker skydda natten.”

Mats höjde ögonbrynen.

“Det var ovanligt poetiskt för att handla om ett trasigt health check.”

“Jag har mina stunder”, sa Karin. “Poängen är att alla gör något rimligt. Men om vi inte säger det högt kommer vi om tio minuter ha en konflikt om att någon bromsar och någon slarvar.”

Naya kände hur något i hennes bröstkorg släppte en aning. Inte mycket. Bara tillräckligt för att hon skulle märka hur spänt det varit.

Sara, fortfarande på skärm, harklade sig.

“Från verksamhetens sida behöver jag kunna säga om det här påverkar tidplanen. Men jag vill hellre säga att testet hittade ett blockerande fel än att produktion hittade det åt oss.”

Det var kanske den mest användbara meningen i rummet.

Amir tog den som man tog emot en hand från någon som stod på fastare mark.

“Ja”, sa han. “Det är så vi ska formulera det.”

Sofia nickade.

“Vi behöver justera readinessmönstret, konsumentbeteendet och larmet. Sedan kör vi om Oracle timeout innan vi går vidare.”

“Går vi inte vidare till MQ-stopp i dag?” frågade Jonas.

Sofia tittade på Naya.

Naya kände hur hon ville säga nej direkt. Inte av försiktighet, utan av respekt för vad de just hittat. Ett testfall som avslöjade ett blockerande fel var inte en station man passerade på vägen till nästa rubrik. Det var vägen.

“Jag tycker inte det”, sa hon. “Inte om MQ-testet bygger på samma antagande om hälsosignal och larm. Då testar vi ovanpå något vi redan vet är fel.”

Lena nickade.

“Instämmer.”

Amir drog handen genom håret.

“Det betyder att dagens plan spricker.”

“Ja”, sa Naya.

Hon väntade på den gamla Amir, den som skulle säga att de åtminstone kunde parallellisera, att de inte behövde göra det sekventiellt, att de riskerade att förlora styrgruppens förtroende om de kom tillbaka med ännu ett stopp.

Han sa inget av det.

I stället gick han fram till whiteboarden och skrev under Sofias punkter:

**Åtgärd i kod**  
**Åtgärd i mall**  
**Åtgärd i larm/runbook**  
**Omkörning innan nytt testfall**

“Då gör vi så här”, sa han. “Jonas och jag tittar på konsumentbeteendet. Sofia, kan du ta mallen och readinesskravet? Naya, du uppdaterar testfall och blockerande kriterier. Mats och Lena, kan ni titta på larmtext och runbook så att signalen faktiskt går att agera på?”

Mats lutade sig tillbaka.

“Kan vi? Ja. Hinner vi? Det beror på om ingen tycker att vi också ska lösa certifikat, reindex och mänsklighetens fall under eftermiddagen.”

Lena tittade på honom, sedan på Karin.

“Det här måste in i avstämningen som faktisk förbrukning av prioriterad tid. Inte som sidouppgift.”

Karin nickade.

“Jag skriver det så.”

Naya såg hur Amir reagerade på ordet förbrukning. Han tyckte inte om det. Hon gjorde det inte heller. Men det var sant. Tid försvann inte för att en uppgift var meningsfull. Den bytte ägare.

De arbetade i nästan två timmar utan att någon höjde rösten.

Det var inte samma sak som att det gick bra.

Jonas hittade snabbt att konsumenten saknade ett tydligt stoppvillkor vid beroendefel. Den hade byggts för att vara robust genom att försöka igen, men robustheten var riktad mot fel sorts verklighet. Den antog att tillfälliga fel var just tillfälliga, och att fortsatt konsumtion var bättre än stopp. I ett isolerat utvecklingstest hade det sett klokt ut. I ett produktionsflöde med statusuppdateringar och medborgarärenden blev det en risk.

Sofia ändrade mallen med en koncentration som gjorde henne nästan svår att störa. Hon ställde frågor utan att lyfta blicken.

“Hur ofta ska beroendestatus uppdateras?”

“Vad är acceptabelt tröskelvärde innan readiness går röd?”

“Vill vi att liveness påverkas eller bara readiness?”

“Vad ska hända om Oracle är nere men applikationen i sig kan svara?”

Varje fråga lät teknisk. Varje fråga handlade egentligen om ansvar.

Naya uppdaterade testfallet och lade in ett tydligt förväntat resultat: tjänsten skulle sluta konsumera nya meddelanden vid verifierat beroendefel efter tröskel, readiness skulle gå röd, larm skulle bära korrelations-id och felklass, runbook skulle ange första triagesteg och ansvarig roll.

När hon skrev ansvarig roll stannade hon upp.

Inte person.

Roll.

Det var en liten seger, nästan osynlig. Tidigare hade hon skrivit namn i testplaner för att få något att hända. Amir för att han visste. Lena för att hon kunde stoppa. Mats för att han mindes. Sofia för att hon såg. Nu skrev hon roll, och för första gången kändes det inte som en lögn.

Vid halv tre körde de om testet.

Den här gången gick felet annorlunda.

Oracle timeouten kom. Applikationen försökte enligt definierat mönster. Konsumenten pausades. Readiness gick röd efter tröskeln. Ett larm gick till pilotens incidentkanal.

Alla lutade sig fram samtidigt.

Lena läste larmtexten högt.

“Pilot Kundportal Meddelandehantering: kritiskt beroende Oracle otillgängligt. Meddelandekonsumtion pausad. Korrelations-id finns. Första triage: teamets beredskapskontakt verifierar applikationslogg, drift verifierar plattformsstatus, databas kontaktas vid kvarstående Oracle-indikator.”

Hon tystnade.

Mats tittade på henne.

“Det där var nästan begripligt.”

“För att vara ett larm”, sa Lena. “Ja.”

Naya kände hur rummet började andas ut.

Det var då Jonas sa:

“Vänta.”

Allt stannade igen.

Han pekade på sin skärm.

“Varför ligger det tre meddelanden i felkö?”

Sofia var vid hans sida på två steg.

“Från första körningen?”

“Nej. Tidsstämpel nu.”

“Det ska inte gå till felkö vid pausad konsumtion”, sa Naya. “Det ska ligga kvar för retry.”

Jonas klickade vidare.

“Det är kompensationsjobbet.”

Amir kom närmare.

“Det ska inte triggas vid Oracle timeout före statusändring.”

“Det gör det ändå”, sa Jonas.

Naya kände hur den lilla lättnaden försvann så snabbt att den nästan blev pinsam. Där var romanens sanna antagonist, tänkte hon plötsligt, fast hon inte brukade tänka i sådana ord. Inte drift. Inte utveckling. Inte ledning. Utan det lilla “ändå” som gömde sig mellan antaganden.

Sofia läste loggen över Jonas axel.

“Kompensationsjobbet tolkar pausad konsumtion som avbruten behandling.”

“Varför?” frågade Amir.

Jonas svarade inte direkt. Han följde koden, klickade, läste, svor lågt.

“För att statusflaggan `PROCESSING` sätts innan Oracle-skrivningen bekräftas. När timeouten kommer finns inget bekräftat ärende i databasen, men kompensationen tror att det finns ett halvt ärende att städa.”

Mats såg på Naya.

“Översätt till nattmänniska.”

Naya hörde sig själv svara lugnare än hon kände sig.

“Vi har byggt en städare som börjar städa ett rum som ännu inte finns, och under tiden flyttar den posten till felkö.”

Mats nickade.

“Då hatar jag städaren.”

Amir stirrade på skärmen. Det fanns en punkt där tekniska fel slutade vara intressanta och började kännas personliga. Naya såg honom passera den. Inte för att han ägde just den kodraden ensam, utan för att han ägde teamets självbild. De hade velat visa att de kunde ta ansvar. Nu visade testet att ansvaret var större än deras bild av flödet.

“Det här är vårt”, sa han.

Ingen protesterade.

Det gjorde nästan mer ont än om någon hade gjort det.

Lena stängde långsamt sin dator halvvägs, inte helt.

“Då är produktionsfönster den här veckan inte realistiskt.”

Orden föll tungt, trots att alla redan visste.

Amir vände sig mot henne.

“Vi vet inte det än.”

“Jo”, sa Lena. “Det vet vi.”

Hans ansikte hårdnade.

“Vi hittade ett fel i förproduktion. Vi har prioriterad tid. Vi kan åtgärda.”

“Ni kan åtgärda felet. Sedan behöver ni testa om Oracle-fallet. Sedan MQ-stopp. Sedan kompensation. Sedan behöver runbook och larm uppdateras. Sedan behöver drift hinna granska det som faktiskt blev ändrat.”

“Om vi säger så där varje gång—”

“Varje gång vi hittar ett blockerande fel?”

“Varje gång något inte är perfekt.”

“Det här är inte perfekt. Det här är fel ärende i fel kö med fel status.”

Tystnaden efter det var inte produktiv. Den var gammal.

Naya såg hur de gamla rollerna kom tillbaka som reflexer. Lena i stopp. Amir i tryck. Mats i skeptisk bekräftelse. Sofia i ensam analys. Karin i mitten, alldeles för medveten om vad som höll på att hända.

Amir sa:

“Det är lätt att säga stopp när man inte behöver förklara för verksamheten varför nyttan skjuts igen.”

Lena blev stilla.

Det var värre än om hon hade blivit arg.

Naya såg Mats röra sig lite, som om han tänkte gå in. Sofia hann före.

“Amir.”

Bara hans namn. Inte hårt. Men med en gräns i.

Han blundade kort.

“Förlåt”, sa han. “Det där var inte rättvist.”

Lena svarade inte.

Karin lade händerna på bordet.

“Vi tar fem minuter.”

“Inte för min skull”, sa Lena.

“Jo”, sa Karin. “Och för allas. För nu är vi på väg att diskutera förra årets konflikter med dagens loggar som ursäkt.”

Det var en märklig mening. Den var också så exakt att ingen protesterade.

De tog paus.

Naya gick ut i korridoren och ställde sig vid automaten utan att köpa något. Hon behövde inte kaffe. Hon behövde en plats där ingen skärm visade en sanning till.

Amir kom efter en stund. Han ställde sig bredvid henne, inte för nära.

“Jag gjorde det där dåligt.”

“Ja.”

Han skrattade utan glädje.

“Du kunde ha lindat in det.”

“Du hade märkt det.”

Han nickade.

Genom glaset såg de Lena stå kvar i rummet med Sofia. Lena hade armarna i kors, men hon lyssnade. Sofia pekade på tavlan, inte på skärmen. Det gjorde samtalet mindre som bevisföring och mer som orientering.

“Jag trodde faktiskt vi hade börjat göra det här rätt”, sa Amir.

“Det har vi.”

“Det känns inte så.”

“För att rätt nu betyder att vi hittar felen tidigare.”

Han tittade på henne.

“Det där låter som något Karin skulle säga.”

“Då får du låtsas att jag sa det med mindre workshopröst.”

Han log, bara lite.

Naya vände blicken mot rummet igen. Hon tänkte på hur ofta teamet hade pratat om självservice som om det handlade om att slippa vänta på andra. Nu började hon förstå att det också handlade om att slippa gömma sig bakom andra. Om de själva ägde vägen fram, ägde de också det som föll av den.

“Du behöver säga till Sara att datumet rör sig”, sa hon.

“Jag vet.”

“Och du behöver säga att det är vårt fel utan att göra det till vår skam.”

Han tog in det långsamt.

“Det är en svår balans.”

“Ja.”

“Är det där också testbarhet?”

“Nej”, sa Naya. “Det är vuxenhet.”

När de kom tillbaka hade Karin ritat en enkel ruta på whiteboarden.

**Fakta**  
**Konsekvens**  
**Beslut**  
**Kommunikation**

“Vi går igenom det i den ordningen”, sa hon. “Inte skuld först. Inte lösning först.”

Lena satt ner igen. Hon såg fortfarande sluten ut, men hon hade öppnat datorn.

Amir satte sig mitt emot henne.

“Jag vill börja med att säga att min kommentar var orättvis”, sa han. “Du har förklarat för verksamheten i flera år när saker inte kan gå. Jag uttryckte mig som om det var bekvämt. Det var fel.”

Lena tittade på honom.

Naya kunde inte läsa henne. Sedan nickade hon en gång.

“Tack.”

Det var inte försoning. Men det var en dörr som inte stängdes.

De gick igenom fakta.

Readinessproblemet var åtgärdat i första version men behövde härdas. Konsumentpausen fungerade efter ändring. Larmet var begripligt. Men kompensationsjobbet hanterade Oracle timeout fel och flyttade meddelanden till felkö trots att behandlingen inte var korrekt etablerad. Det innebar risk för felaktig verksamhetsstatus och manuell återställning.

Konsekvensen blev tydlig innan någon behövde säga beslutet.

Produktionsfönster den veckan var borta.

Amir sa det själv.

“Vi bokar inte nytt fönster förrän Oracle timeout och kompensation är omtestade, MQ-stopp är genomfört, och runbooken är uppdaterad med faktisk felköhantering.”

Lena såg på honom. Den här gången antecknade hon inte direkt.

“Bra”, sa hon.

Ett litet ord. Men det hade vikt.

Sara, fortfarande digital, såg trött ut men inte arg.

“Jag kan ta det med verksamheten om jag får en formulering jag kan stå för.”

Karin skrev.

“Förslag: Förproduktionstest har hittat blockerande fel i felhanteringen som hade kunnat leda till felaktig ärendestatus och manuell återställning i produktion. Produktionsfönster flyttas tills åtgärd och omtest är genomförda. Beslutet är enligt Pilotväg 0.1:s miniminivå.”

Sara läste det tyst.

“Lägg till att testet visar att den nya vägen fungerar genom att stoppa oss före produktion.”

Mats tittade mot skärmen.

“Det där kommer ingen tro att verksamheten sa.”

Sara log svagt.

“Då får ni njuta av ögonblicket.”

När mötet avslutades hade de en åtgärdslista, ett stoppat datum och en märklig känsla av både nederlag och framsteg. Naya visste inte vad man kallade det. Hon skrev i testprotokollet:

**Resultat: Ej godkänd för produktionsförsök. Blockerande fel upptäckta i förproduktion. Pilotväg 0.1 användes för att stoppa före produktion och definiera åtgärd, ansvar och omtest.**

Hon sparade.

Sofia stod kvar vid tavlan när de andra började packa ihop. Amir gick fram till henne, men höll ett avstånd som både var hänsyn och påminnelse.

“Jag trodde du skulle säga att det här var ett misslyckande”, sa han.

Sofia satte på korken på pennan.

“Det är ett misslyckat produktionsförsök.”

“Vi försökte inte ens produktion.”

“Precis.”

Han såg på henne, och Naya hann uppfatta något i blicken innan hon vände sig bort. Inte för att det var olämpligt. Bara för att vissa saker blev skörare när andra såg dem.

“Så vad är det då?” frågade Amir.

Sofia svarade efter en stund.

“Det är första gången plattformen sa nej innan Lena behövde göra det ensam.”

Lena, som hade varit på väg ut, stannade i dörren.

Hon sa inget.

Men Naya såg att hon hörde.

Och för en gångs skull verkade ingen i rummet veta om det som just hänt var en försening eller början på något som faktiskt kunde hålla.
