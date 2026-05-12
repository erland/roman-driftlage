# Kapitel 3 – Driftens vardag

Lena hann inte tillbaka till sin plats innan telefonen ringde.

Hon såg numret på skärmen och stannade mitt i korridoren, med datorn tryckt mot bröstet och kaffemuggen fortfarande tom i andra handen. Växeln hade kopplat vidare ett samtal från servicedesk. Det betydde nästan alltid att någon redan försökt lösa något genom rätt kanal, misslyckats med att hitta rätt kategori och till slut valt människa före process.

Hon svarade.

“Lena Holm.”

“Hej, det är Jonas på servicedesk. Vi har flera samtal om att e-tjänsten för intygsbeställning är långsam igen. Inte nere, men användarna får timeout ibland. Vi ser inget rött i övervakningen.”

Inte nere, men långsam. Det var ett av Lenas minst omtyckta tillstånd. Nere var åtminstone tydligt. Långsam kunde vara applikation, databas, nät, kö, sökindex, lastbalanserare, klient, extern tjänst eller bara en användare med trettiosju flikar och dåligt tålamod. Långsam var ett ord som lät litet tills det hamnade i en veckorapport.

“Hur många samtal?”

“Sex på tio minuter.”

“Från samma region?”

“Vänta.” Hon hörde tangentbordsknatter. “Nej. Tre olika.”

Lena slöt ögonen ett ögonblick. Det kunde fortfarande vara slump. Men slump var inte en driftstrategi.

“Lägg en P2:a och pinga incidentkanalen. Skriv att drift koordinerar initial felsökning. Jag tar den.”

När hon lade på såg hon att hon fått ännu en mötesinbjudan från Karin. **Pilotens miniminivå – ansvar, krav och arbetssätt.** Sextio minuter. I eftermiddag.

Lena stod kvar några sekunder och läste titeln.

Ansvar, krav och arbetssätt.

Det var bättre än samverkan. Hon gav Karin det. Men sextio minuter var ett nästan komiskt format för det som egentligen behövde sägas. Det var som att försöka tömma ett serverrum med kaffekopp.

Hon accepterade mötet ändå.

Sedan gick hon tillbaka till driftön.

Det kallades driftön för att arbetsplatserna låg i en öppen fyrkant längst bort i lokalen, avskärmad med låga hyllor, gamla whiteboards och den sorts tyst överenskommelse som uppstår bland människor som ofta blir avbrutna. Här pratade man inte högt i onödan. Inte för att någon var högtidlig, utan för att alla samtidigt lyssnade efter något annat: ett larm, en suck, ett namn i en kanal, en ovanlig formulering från servicedesk.

Mats satt på sin plats med headsetet runt halsen och en skål med nötter bredvid tangentbordet. På hans skärm låg tre fönster staplade över varandra: övervakning, ärendesystem och en terminal med loggar som rullade i för snabb takt för att någon utom Mats skulle hävda att han läste dem.

“Intygsbeställningen är seg igen”, sa Lena.

“Jag kände på mig att dagen hade för mycket luft.”

“Servicedesk lägger P2.”

“Databas?”

“För tidigt att säga.”

Mats gjorde en min som betydde att det aldrig var för tidigt att misstänka databasen, men att han var för erfaren för att säga det högt utan mätvärden.

Lena satte sig, väckte skärmarna och öppnade incidentkanalen. Jonas hade redan skrivit:

> Flera användare rapporterar timeout i e-tjänst Intygsbeställning. Ej totalstopp. Drift koordinerar initial felsökning. Prioritet P2.

Hon svarade:

> Lena tar koordinerande roll. Mats tittar applikationsloggar. Behöver snabb koll från databas på väntetider senaste 30 min. Någon från nät kan verifiera lastbalanserare?

Det var en enkel rad. Den såg nästan självklar ut. Men bakom den låg år av informell kunskap: vem som brukade svara snabbt, vilken databasjour som behövde konkreta frågor, vilken nätperson som annars skulle börja i fel ände, vilka ord som fick servicedesk att lugna verksamheten i stället för att skicka vidare fem olika spekulationer.

Hon skapade incidentkortet, kopplade de första ärendena och öppnade tjänstens driftdokumentation. Den var senast uppdaterad för åtta månader sedan. Ägare: oklar. Teknisk kontakt: en konsult som slutat i februari.

Lena stirrade på namnet.

Det var inte ens förvånande längre. Det var det värsta.

Hon hade varit stolt över sin förmåga att hitta runt i sådana här brister. En gång i tiden hade det känts som yrkesskicklighet: att veta var sanningen fanns när dokumentationen ljög, att minnas vilken server som egentligen körde batchen, att känna igen ett felmeddelande från en incident tre år tidigare. Men på senare tid hade stoltheten börjat få en annan smak. Varje sak hon mindes för att systemet inte gjorde det åt henne var också en sak som kunde gå sönder när hon var sjuk, ledig eller bara upptagen i fel möte.

Hon tänkte på Karins fråga från förmiddagen.

Vilka är absoluta stoppunkter och vilka är förbättringar?

Det var en bra fråga. Men driftens vardag bestod sällan av rena kategorier. Allt var både stoppunkt och förbättring, både risk och vana, både brand och brandskyddsarbete som aldrig hann göras.

“Jag ser timeouter mot sök”, sa Mats.

Lena vred stolen mot honom.

“Elasticsearch?”

“Ja. Men vänta innan du ser lycklig ut över att det inte är Oracle.”

“Jag är aldrig lycklig under P2.”

“Klokt. Applikationen försöker slå upp gamla intyg i sökindex. Får lång svarstid, håller trådar, och sedan börjar användarflödet köa upp. Det är inte dött. Det bara tänker för länge.”

“Är det samma mönster som i mars?”

Mats svarade inte direkt. Han klickade mellan fönstren, kisade och lutade sig närmare skärmen.

“Kanske. I mars var det indexoptimeringen som krockade med batch. Nu…” Han stannade. “Nu ser det ut som att någon kör omindexering.”

Lena öppnade kalendern för driftaktiviteter. Hon visste redan vad hon skulle hitta, eller snarare inte hitta. Ingen omindexering stod planerad för förmiddagen.

“Schemalagd?”

“Nej.”

Hon skrev i incidentkanalen:

> Ser långsamma svar från sök/Elasticsearch. Indikation på pågående omindexering. Vem har initierat aktivitet? Finns planerad ändring?

Det tog mindre än en minut innan någon från ett utvecklingsteam svarade:

> Vi körde en mindre reindex i test igår, inte prod.

Mats läste högt och skrattade utan glädje.

“Det där är en mening som ofta betyder att någon snart upptäcker sin miljövariabel.”

Lena ville inte att han skulle ha rätt. Inte för att hon brydde sig om prestigen, utan för att varje sådan händelse blev ännu ett bevis i driftens interna domstol: se, de förstår inte produktion. Och varje bevis gjorde det svårare att senare säga något annat.

Hon öppnade ändringsloggen. Ingen godkänd ändring. Hon öppnade deploymenthistoriken. Inget nytt för tjänsten. Hon öppnade plattformens gamla automationsvy, den som egentligen skulle ersättas men fortfarande användes för en del jobb eftersom “ingen hunnit migrera allt”.

Där låg den.

Ett jobb startat 09.47. Namn: `reindex-intyg-prod`. Initierat av ett tekniskt konto.

Hon kände hur käken spändes.

Tekniskt konto. Alltid dessa tekniska konton. De var tänkta att skapa spårbarhet och slutade ofta som maskerade människor.

“Mats.”

“Du hittade den?”

“Prodjobb startat 09.47.”

“Av vem?”

“Tekniskt konto.”

“Naturligtvis. Människor är dödliga, men servicekonton är eviga.”

Lena skrev till incidentkanalen, fortfarande sakligt:

> Reindex-jobb i produktion startat 09.47 via tekniskt konto. Drift stoppar jobbet om ingen invändning inom två minuter. Behöver ägare på aktivitet och bedömning av påverkan.

Hon väntade inte på reaktionerna innan hon öppnade proceduren för stopp. Hon visste att någon kanske skulle protestera. Hon visste också att användarna just nu fick timeout och att ingen planerad ändring fanns. Det var ett beslut av den sort som inte såg dramatiskt ut utifrån, men som alltid krävde att någon accepterade risken för att ha fel.

När jobbet stoppades planade svarstiderna långsamt ut.

Servicedesk skrev att samtalen minskade. Nät såg inget avvikande. Databas meddelade att de inte såg ökade väntetider. En utvecklare erkände efter fjorton minuter att ett script från gårdagens test hade haft fel parameterfil i körningen, och att det “inte borde ha kunnat peka mot produktion”.

Lena läste formuleringen tre gånger.

Inte borde ha kunnat.

Hon skrev inte det hon tänkte.

Det var en av hennes mer underskattade yrkeskunskaper.

I stället sammanfattade hon incidenten, satte status till bevakning och bad om en kort efteranalys med fokus på hur tekniskt konto, parameterfil och miljöskydd skulle förhindras från att kombineras på samma sätt igen.

Sedan lutade hon sig bakåt.

Klockan var 10.58.

Hennes yoghurt var nu bortom räddning.

Mats tog av sig headsetet.

“Det där var en liten sådan.”

“Ja.”

“En liten sådan som äter fyrtiofem minuter, tre personers fokus och två år av förtroendekapital.”

Lena såg på honom.

Han mötte hennes blick och ryckte på axlarna.

“Jag kan också formulera mig strategiskt om jag får tillräckligt lite sömn.”

Hon log, men bara med munnen.

På skärmen blinkade Karins möte i kalendern. Pilotens miniminivå. Om mindre än fyra timmar skulle hon sitta i ett rum med Amir och förklara varför “inte borde ha kunnat” inte dög som kontrollmodell. Hon visste redan hur det riskerade att låta: som om hon använde ett fel i ett annat team som argument mot all självservice. Som om varje misstag i produktion bevisade att drift måste godkänna allt för alltid.

Hon ville inte hamna där.

Samtidigt var det precis sådana här händelser som byggt de manuella grindarna.

Ingen hade satt upp dem för att vara besvärlig. De hade vuxit fram, en efter en, efter incidenter där det visat sig att ett script kunde peka fel, att en rollback saknade databasen, att en kontaktlista innehöll en konsult som slutat, att en grön lampa betydde att en process levde men inte att tjänsten fungerade.

Hon öppnade sin egen anteckningsfil. Den hette bara `drift_komihag.txt`, vilket hon skämdes lite över varje gång hon såg den. Den borde ligga i ett system. Den borde ha ägare, versionshistorik och struktur. I stället var den hennes privata karta över sådant som ingen hunnit göra ordentligt.

Hon skrev:

- Reindex prod via tekniskt konto 09.47. Fel parameterfil. Efteranalys behövs.
- Koppling till pilot: miljöskydd, spårbarhet, tekniska konton, automatiska spärrar.
- Miniminivå får inte bli dokumentlista. Måste vara beteende i systemet.

Hon stannade vid den sista meningen.

Måste vara beteende i systemet.

Det var kanske så hon skulle säga det till Amir. Inte att drift behövde fler dokument. Inte att utveckling behövde be om lov. Utan att kraven behövde leva där arbetet skedde. Pipeline. Mallar. Behörigheter. Automatiska kontroller. Tydliga ägarskap. Sådant som inte var beroende av att Lena råkade läsa rätt rad i rätt bilaga på rätt morgon.

Tanken var oväntat lättande.

Sedan plingade ett nytt ärende.

**Certifikatförnyelse – akut risk för utgång kommande helg**

Lättnaden försvann.

“Nej”, sa hon lågt.

Mats tittade upp.

“Jo.”

“Du vet inte ens vad jag tittar på.”

“Du sa nej med certifikatröst.”

Lena öppnade ärendet. Ett externt certifikat för en integration mot en samverkande myndighet gick ut på söndag. Beställningen hade fastnat hos leverantören. Kontaktpersonen var fel. Den interna systemägaren hade semester. Någon hade markerat ärendet som normal prioritet eftersom “det är flera dagar kvar”.

Flera dagar kvar. På en tisdag. Med helg, leverantör, signering och ändringsfönster mellan nu och då.

Hon kände hur en tunn, bekant ilska rörde sig genom kroppen. Den var inte riktad mot en person. Det hade varit enklare om den var det. Den riktade sig mot hela mönstret där tid alltid behandlades som en buffert tills den plötsligt blev ett akutrum.

Hon ringde numret i ärendet. Inget svar. Hon skrev till systemägarkanalen. Inget svar. Hon letade upp ersättare i organisationskatalogen. Personen hade slutat för tre månader sedan.

Mats kom bort till hennes plats med sin kaffemugg.

“Vill du ha hjälp?”

“Jag vill ha ett system där certifikat inte blir personarkeologi.”

“Det var inte ett nej.”

Hon pekade på skärmen.

“Kan du kontrollera om den här integrationen har redundant endpoint eller om vi har hårdkodat allt på sämsta möjliga sätt?”

“Du menar enligt tradition?”

“Ja.”

Mats gick tillbaka till sin plats.

Lena började skriva en eskalering. Hon valde orden noga. För hårt, och någon skulle fokusera på tonen. För mjukt, och ärendet skulle fortsätta ligga i fel kö. Det var en märklig sorts översättning hon gjorde varje dag: från faktisk risk till administrativt acceptabel oro.

> Certifikatet löper ut söndag 17 maj. Om förnyelse, leverans och produktionssättning inte hanteras före fredag finns risk för avbrott i integration mot extern myndighet. Ärendet behöver prioriteras om till hög och tilldelas aktiv systemägarkontakt idag.

Hon skickade till Elin och lade till servicedesk, systemförvaltning och leverantörskoordinatorn.

Sedan såg hon på klockan.

11.36.

Hon hade ännu inte gjort något av det som stod i hennes plan för dagen.

Patchplaneringen för JBoss-noderna låg orörd. Uppföljningen av förra veckans MQ-varningar låg orörd. Granskningen av pilotens kompletteringar låg orörd. Dokumentationen som skulle uppdateras efter senaste Oracle-ändringen låg orörd. Och någonstans i bakhuvudet fanns Karins möte, där hon förväntades bidra konstruktivt till framtidens arbetssätt.

Hon öppnade sin att-göra-lista och började flytta punkter.

Inte ta bort. Bara flytta.

Det var så förbättringsarbete dog hos dem. Inte genom beslut. Genom att varje dag vara det som kunde skjutas till i morgon.

Mats kom tillbaka.

“Integrationens sekundära endpoint finns i dokumentationen.”

“Bra.”

“Men inte i konfigurationen.”

Lena blundade.

“Varför?”

“För att den sekundära endpointen infördes i samband med ett projekt som avslutades innan produktionssättningen, och då sköts den upp till förvaltning.”

“Förvaltning gjorde den inte.”

“Nej.”

“För att de inte visste?”

“Eller för att de visste men inte kunde prioritera. Jag försöker vara emotionellt generös.”

Lena skrev in ännu en punkt i eskaleringen. Hon kände sig plötsligt mycket trött.

Det var inte arbetet i sig. Hon hade inget emot arbete. Hon hade valt drift just för att hon tyckte om verklighetens motstånd. Hon tyckte om när system behövde fungera, inte bara se bra ut i en demo. Det hon hade börjat få svårt med var känslan av att de bar organisationens glapp med sina kroppar. Varje gång en ägare saknades, varje gång en rutin var nästan klar, varje gång en miljö skilde sig lite från en annan, blev det någon på drift som fick fånga upp det.

Och när de sedan sa nej betraktades nejet som problemet.

Hon tänkte på Amir. Hans korta meddelanden. Hans frustration. Hon kunde nästan höra hur han skulle beskriva den här dagen för sitt team om han satt på andra sidan: drift är alltid upptagna, alltid i incident, alltid i en kö. Det var sant. Det var också ofullständigt.

Kanske var det där romanens — nej, inte romanens, verklighetens — mest irriterande egenskap: att motpartens förenkling ofta var sann nog för att göra ont.

Vid lunch åt hon yoghurt ändå, trots att den var ljummen. Mats åt en mikrad matlåda vid skrivbordet och hävdade att den smakade bättre om man inte identifierade ingredienserna. De fick sju minuter utan nya larm.

Sedan kom Amir till driftön.

Han stannade ett par meter bort, som om det fanns en osynlig gräns. Lena såg honom innan han sa något. Mörk tröja, passerkortet snett i bandet, datorn under armen. Han såg tröttare ut än i Teams-bilden, vilket gjorde henne mindre nöjd än hon hade kunnat vara.

“Har du en minut?” frågade han.

Mats tittade från Amir till Lena och tillbaka igen.

“Jag kan gå och hämta kaffe”, sa han. “Eller stå kvar och vara arbetsmiljö.”

“Gå”, sa Lena.

Mats reste sig med en överdriven suck.

Amir väntade tills han var utom hörhåll. Det var oväntat respektfullt.

“Jag såg ditt meddelande”, sa han. “Om tydligare krav tidigare.”

Lena nickade.

“Jag menade det.”

“Jag tror det.” Han skiftade datorn från ena handen till den andra. “Jag är fortfarande frustrerad över stoppet.”

“Det förväntade jag mig.”

“Men jag förstår några av punkterna bättre efter att ha läst igen. Rollbacken är för tunn.”

Det var inte en ursäkt. Det var kanske bättre. En ursäkt kunde vara socialt smörjmedel. Ett erkännande av sakfrågan gick att bygga något på.

“Databasen gör den svår”, sa Lena.

“Ja. Teamet tänkte image-rollback. Inte data-rollback.”

“Det är vanligt.”

“Du säger det som att det inte gör saken bättre.”

“Det gör saken mänsklig. Inte bättre.”

Han log svagt, trots sig själv.

Sedan såg han mot hennes skärmar. Incidentkortet var fortfarande öppet, certifikatsärendet bredvid, patchplaneringen halvt dold under kalendern.

“Är det alltid så här?” frågade han.

Lena följde hans blick. Hennes första impuls var att säga nej. Inte för att det vore sant, utan för att hon inte ville ge honom ännu ett argument för att drift saknade kapacitet att vara med i förändringen.

Men hon var för trött för kosmetiska svar.

“Nej”, sa hon. “Ibland är det värre.”

Amir sa inget på några sekunder.

Det var också oväntat.

“Då är det kanske inte rimligt att vi ber er granska allt manuellt”, sa han till slut.

Lena såg på honom. Hon letade efter ironin, men hittade ingen.

“Nej”, sa hon. “Det är det kanske inte.”

“Men det är inte heller rimligt att vi väntar tre veckor på varje sak.”

“Nej.”

De stod där i ett ögonblick, på varsin sida av samma omöjliga nej.

Amir drog handen över nacken.

“Jag kommer till Karins möte i eftermiddag. Med kompletterad rollback. Inte perfekt, men bättre.”

“Bra.”

“Du kommer säga att den inte räcker.”

“Kanske.”

“Det var inte lugnande.”

“Det var ärligt.”

Han nickade, och för första gången såg hon inte bara hans otålighet. Hon såg något annat bakom den. Rädsla, kanske. Inte för incidenter på samma sätt som hennes, utan för att fastna. För att teamet skulle tappa fart, kompetens, mening. För att varje förbättring skulle malas ner till ännu en bilaga i ett ärende.

Det var inte hennes rädsla. Men hon kunde känna igen formen.

Mats kom tillbaka med kaffe just när Amir gick.

“Var det vapenvila?” frågade han.

“Nej.”

“Skottpaus?”

“Kanske.”

Mats räckte henne en kopp.

“Jag tog en åt dig också. Den är nästan varm och tekniskt sett kaffe.”

Lena tog emot den.

“Tack.”

Hon såg på kalendern igen. Karins möte låg som en fyrkant mitt i eftermiddagen, inklämd mellan incidentuppföljning och patchråd. Hon visste redan att hon skulle komma dit med för många öppna saker i huvudet. Certifikatet. Reindex-incidenten. Pilotens rollback. MQ-dokumentationen. Frågan om tekniska konton. Frågan om vem som egentligen ägde vad.

Men för första gången den dagen kändes mötet inte bara som ännu ett avbrott.

Kanske kunde det bli en plats att lägga något av allt det där.

Inte som klagomål. Inte som försvar. Utan som bevis.

Hon öppnade en ny sida i anteckningsfilen och skrev rubriken:

**Till mötet: driftens miniminivå**

Under den skrev hon:

- Krav ska komma före granskning, inte upptäckas vid stopp.
- Självservice kräver automatiska spärrar där fel inte får vara möjliga.
- Drift måste kunna se, förstå och påverka beroenden.
- Incidentansvar ska vara konkret, inte “ordinarie väg”.
- Förändring kräver kapacitet. Inte bara vilja.

Hon stannade vid sista punkten.

Sedan lade hon till:

- Om allt nytt läggs ovanpå allt gammalt blir det inget nytt. Bara mer drift.

Hon sparade filen.

Utanför fönstret hade regnet fortsatt. På andra sidan gården blinkade en affisch i glasreflektionen: **Vi förenklar vardagen för alla.**

Lena såg på den och tänkte att det kanske var en bra vision.

Men någon behövde börja med vardagen hos dem som skulle förenkla.
