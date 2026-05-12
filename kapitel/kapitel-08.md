# Kapitel 8 – Mer än en kö

Mats hade alltid tyckt illa om ordet kö.

Inte för att det var fel. Det var ett kort, svenskt och i grunden användbart ord. Men i möten hade det en märklig förmåga att få människor att tänka på något stillastående. En rad. Något som väntade på sin tur. Något som gick att tömma om man bara ökade takten.

IBM MQ var inte en kö på det sättet.

Inte för honom.

För honom var det snarare ett löfte.

Ett meddelande lades någonstans för att någon annan skulle kunna hämta det senare. Inte när nätverket hade lust. Inte när applikationen råkade vara uppe. Inte när alla beroenden låg i rätt ordning och ingen hade glömt ett certifikat. Senare. Det var hela poängen. Köhanteraren fanns där för att verkligheten inte var synkron, inte lydig och definitivt inte optimerad för utvecklingsteamens sprintplaner.

Han stod vid kaffemaskinen och såg sin kopp fyllas med något som myndigheten kallade mörkrost. På skärmen ovanför maskinen rullade informationsbilder om cybersäkerhetsmånaden och ergonomi vid distansarbete. En bild uppmanade alla att låsa datorn när de lämnade skrivbordet.

Mats tänkte att om någon ville åt myndighetens mest känsliga information behövde de inte smyga fram till ett olåst tangentbord. De kunde gå på ett möte och vänta tills någon sa “det där äger väl plattformen”.

Då skulle allt avslöjas.

Han tog koppen och gick mot rummet Granen, där dagens möte om MQ-frågan redan hade börjat samla människor innan klockslaget. Det var ett dåligt tecken. När folk kom tidigt betydde det antingen att de var engagerade eller att de ville vinna första formuleringen.

Genom glasväggen såg han Lena sitta med armarna korsade och blicken på en utskriven flödesbild. Amir stod vid skärmen och kopplade in sin dator. Sofia satt vid bordets ena långsida, med sin anteckningsbok öppen och pennan liggande tvärs över sidan, som om hon höll kvar sig själv från att börja skriva innan någon sagt något värt att spara. Karin var där också, förstås. Hon hade ställt sig vid whiteboarden, inte mitt i rummet. Det såg ödmjukt ut, men Mats började förstå att Karin sällan placerade sig av en slump.

På distans fanns två namn i Teamsfönstret: Peter från databas och Annika Lind från integration. Annika var MQ-specialist, vilket på myndigheten betydde att alla förväntade sig att hon kunde svara på varje fråga som innehöll bokstäverna M och Q, oavsett om frågan egentligen gällde nät, applikationslogik, säkerhet, behörigheter eller verksamhetsprocesser som ingen dokumenterat sedan 2014.

Mats klev in.

“Förlåt”, sa han. “Kaffet hade incident.”

Ingen skrattade. Det var också ett tecken.

Karin såg upp.

“Vi har inte börjat. Vi väntade på dig.”

“Det brukar folk ångra.”

Han satte sig bredvid Lena. Hon sköt över en papperskopia utan att säga något. Han såg rubriken: **Meddelandeflöde – Kundportal Meddelandehantering**.

Diagrammet såg prydligt ut. Alldeles för prydligt.

En ruta för applikationen. En ruta för MQ. En ruta för mottagande system. Pilar mellan rutorna. Små etiketter med kö-namn, kanal, certifikat och ungefärlig volym.

Det fanns inga nattliga omstarter i diagrammet. Inga halvlevererade meddelanden. Inga driftfönster. Inga människor som behövde avgöra om ett meddelande fick skickas om eller om det då skulle skapa dubbla ärenden hos mottagaren. Inga förlorade minuter när övervakningen sa att allt var grönt men verksamheten ringde och frågade varför inget hade hänt.

Mats lade kaffet på bordet.

“Vems bild är det här?”

Amir vände sig om från skärmen.

“Vår. Med input från Annika.”

“Det syns.”

Amir höll tillbaka ett svar. Mats såg det på käken. Förr hade Amir antagligen svarat direkt. Nu stannade han en halv sekund längre. Det var inte mycket, men det var något.

“Vad menar du?” frågade Amir.

“Att den visar meddelandets glada väg.”

Karin tog ett steg närmare whiteboarden.

“Bra. Då börjar vi där. Vad saknas i den olyckliga vägen?”

Mats såg på henne. Det var fortfarande något med hennes sätt att få kritik att låta som material. Irriterande, men effektivt.

Annika slog på sin mikrofon.

“Jag kan börja. Det saknas vad som händer om mottagande system är nere längre än förväntat. Vi har retry, men frågan är hur länge meddelanden får ligga och vad som räknas som backlogg kontra incident.”

“Vi har tänkt att MQ hanterar det”, sa Jonas, som satt uppkopplad bredvid Amir på skärmen från utvecklingsteamets rum.

Mats lutade sig bakåt.

Där var den.

MQ hanterar det.

Han hade hört meningen i olika former i många år. Databasen hanterar det. Lastbalanseraren hanterar det. Plattformen hanterar det. Övervakningen hanterar det. Som om systemen var små ansvarsfulla tjänstemän som tog på sig ärenden, gjorde bedömningar och ringde rätt person när verkligheten avvek från dokumentationen.

“MQ lagrar meddelanden enligt sina regler”, sa Annika. Hennes röst var jämn, men Mats hörde tröttheten under den. “Det är inte samma sak som att den hanterar verksamhetskonsekvensen.”

Jonas såg generad ut i den lilla videorutan.

“Jag menade inte—”

“Jo”, sa Annika, inte hårt men tydligt. “Det gjorde du nog. Och det är därför vi behöver prata om det.”

Lena skrev något i sitt block. Mats kunde inte se vad, men han gissade att det var en formulering som senare skulle bli ett krav.

Sofia hade fortfarande inte sagt något. Hon följde samtalet med blicken mellan Amir, Annika och diagrammet. Mats hade märkt att hon ofta väntade tills rummet fyllt sig självt med halva sanningar innan hon tog fram den fråga som gjorde dem hela.

Karin ritade tre kolumner på whiteboarden.

**Tekniskt beteende**  
**Operativt ansvar**  
**Verksamhetsrisk**

“Kan vi fylla på här?” frågade hon.

Mats tyckte först att det såg ut som ännu en övning. Sedan såg han Lenas ansikte. Hon hade slutat försvara sig i stolen. Det här var faktiskt rätt uppdelning. Inte för att kolumnerna var magiska, utan för att de hindrade rummet från att låtsas att ett tekniskt svar var detsamma som ett operativt beslut.

Amir tog fjärrkontrollen och visade nästa bild.

“Vi har definierat tre huvudflöden. Inkommande meddelande från kundportalen, statusuppdatering till mottagande handläggningssystem och kvittens tillbaka. Volymerna är låga initialt, men kan öka när fler ärendetyper kopplas på.”

“Vad är låga?” frågade Lena.

“Ett par tusen per dygn i första versionen.”

“Peak?”

Amir tittade ner på sina anteckningar.

“Det har vi inte ett säkert tal på än.”

“Då har vi inte volymen.”

Han såg upp. För ett ögonblick såg han ut som om han skulle säga emot. Sedan nickade han.

“Nej. Då har vi en uppskattning.”

Mats tog en klunk kaffe och kände att den var för varm och för tunn samtidigt. Han hade väntat sig mer motstånd från Amir. Det gjorde honom nästan misstänksam.

Sofia lyfte pennan.

“Volym är en del. Men den stora frågan är vad applikationen gör när den inte kan leverera vidare. Väntar den? Misslyckas den? Skriver den status? Försöker den igen? Hur ser användaren det?”

Sara, produktägaren, satt med på länk men hade hittills varit tyst. Nu slog hon på mikrofonen.

“Användaren ser bara att meddelandet är inskickat. I dag finns en status i kundportalen, men den är ganska grov. Mottaget, under behandling, avslutat.”

“Om ett meddelande fastnar i kö?” frågade Sofia.

“Då... beror det på var det fastnar.”

Sara hörde själv hur det lät. Hennes blick flackade lite åt sidan, som om hon såg en gammal kravspecifikation som plötsligt inte räckte.

“Då behöver vi veta om användaren får en falsk trygghet”, sa Sofia.

Det blev tyst.

Mats såg hur Amir långsamt vände sig mot diagrammet igen. Det var något i hans hållning som förändrades, en liten sänkning av axlarna. Inte nederlag. Mer som om frågan hade gått förbi hans försvar och träffat det han faktiskt brydde sig om.

För det gjorde han, tänkte Mats motvilligt. Amir brydde sig om tjänsten. Det var inte bara teknikprestige. Han ville att något skulle fungera bättre för människor utanför huset. Problemet var att han ibland trodde att vägen dit gick genom att springa förbi dem som sett vägar rasa förut.

“Vi behöver skilja på teknisk leverans och verksamhetsstatus”, sa Amir.

Lena tittade upp.

“Ja.”

Bara ett ord. Men Mats hörde i det att hon hade väntat länge på att någon från utveckling skulle säga något sådant utan att det först behövde pressas ur dem.

Karin skrev under kolumnen Verksamhetsrisk:

**Falsk status mot användare**

Sedan frågade hon:

“Vem äger den risken?”

Alla tittade inte på varandra samtidigt. Det var mer subtilt. Blickar som rörde sig mot skärmen, mot Sara, mot Amir, mot Lena, mot Annika. Ingen ville först ta ordet. Det var ett av organisationens mest pålitliga tecken på att de hittat något viktigt.

Sara tog till slut ett andetag.

“Verksamheten äger vad status betyder för användaren. Teamet äger hur tjänsten visar det. Men vi behöver input från drift och integration om vilka tekniska tillstånd som faktiskt kan uppstå.”

Karin skrev.

“Bra. Det är ett ägarskap med beroenden. Inte ett gruppägande.”

Mats såg hur Lena drog nästan omärkligt på munnen åt orden. Grupp ≠ ägare hade redan börjat bli en intern referens.

Annika gick vidare till nästa punkt.

“Persistens. Om köhanteraren restartar måste persistenta meddelanden finnas kvar. Det låter självklart, men vi måste veta vilka meddelanden som ska vara persistenta, vilka som kan återskapas och vilka som absolut inte får dubbellevereras.”

“Alla ska väl vara persistenta?” sa Jonas.

Mats ställde ner kaffet lite hårdare än han tänkt.

“Det där är som att säga att alla mejl ska vara rekommenderade brev.”

Jonas såg förvirrad ut.

“Är inte säkrare bättre?”

“Inte alltid. Säkrare enligt vilken dimension? Leverans? Prestanda? Spårbarhet? Dubbletthantering? Felsökning? Om allt är viktigast vet vi inte vad som faktiskt är viktigast när det går fel.”

Han hörde sig själv och blev nästan generad. Det lät som något Karin kunde ha sagt, fast med mer kaffe och irritation.

Sofia såg på honom med en blick som var svår att tolka. Uppmuntran, kanske. Eller bara att hon registrerade att hans cynism hade råkat bli användbar.

“Det här är viktigt”, sa hon. “Vi behöver klassificera meddelandetyperna. Inte bara tekniskt, utan efter konsekvens.”

Hon gick fram till whiteboarden och skrev under Tekniskt beteende:

**Persistens per meddelandetyp**  
**Idempotens/dubbletter**  
**Dead-letter-hantering**  
**Backloggtrösklar**

Sedan stannade hon, som om hon märkte att hon tagit pennan från Karin utan att fråga.

“Förlåt”, sa hon.

Karin skakade på huvudet.

“Fortsätt.”

Det var ett litet ögonblick, men Mats såg det. Sofia fick rummet att följa henne utan att höja rösten. Det var inte auktoritet som kom ur roll. Det var auktoritet som kom ur att människor blev lugnare när hon formulerade problemet.

Det var därför det också kunde bli farligt för henne, tänkte han.

Organisationer älskade sådana personer. Först frågade man dem bara om en sak. Sedan en till. Sedan blev de en informell funktion, sedan en flaskhals, sedan ett namn i varenda eskalering. Till slut kallades de nyckelpersoner, vilket ofta betydde att alla andra hade byggt en dörr utan handtag.

Lena lutade sig mot honom och viskade:

“Hon håller på att få jobbet utan att ha fått det.”

“Mm”, sa Mats. “Klassiskt myndighetsutnämnande. Först ansvar, sen kanske titel, sist tid.”

Lena sa inget mer. Men han såg att hon tänkte samma sak.

Karin lät Sofia fylla tavlan. Sedan vände hon sig mot gruppen.

“Jag hör flera olika beslut. Ett: teknisk MQ-konfiguration. Två: operativ incidentmodell. Tre: verksamhetsbeslut om status och konsekvens. Fyra: plattformens standardmönster för framtida team. Är det rätt?”

Annika nickade i videorutan.

“Ja. Och fem: vem som får ändra vad. MQ-konfiguration är inte en fri textyta.”

Amir höjde händerna lite.

“Det är ingen som vill att teamet ska administrera MQ hur som helst.”

“Bra”, sa Annika. “Men självservice behöver betyda något konkret. Kan teamet beställa en kö via mall? Kan de se metrics? Kan de ändra trösklar? Kan de koppla på nya konsumenter? Kan de rensa meddelanden? Kan de starta om en kanal? Var går gränsen?”

Lena fyllde i:

“Och vem granskar ändringen innan produktion?”

Amir svarade inte direkt. Han hade börjat lära sig att varje snabbt svar här skapade två långsamma problem senare.

“Jag vill att teamet ska kunna göra det som är standardiserat och reversibelt”, sa han till slut. “Inte det som kan förstöra produktion utan att någon märker det förrän efteråt.”

Mats höjde ögonbrynen.

“Det där lät nästan som drift.”

Amir såg på honom.

“Jag försöker att inte ta det som en förolämpning.”

“Det är ett mognadstecken. Obehagligt för alla inblandade.”

För första gången skrattade Jonas. Kort, men äkta. Spänningen i rummet släppte en aning.

Men bara en aning.

För sedan ställde Peter, som hittills lyssnat tyst från databassidan, frågan som gjorde allt mer komplicerat.

“Vad händer om MQ levererar meddelandet och applikationen skriver status till Oracle, men transaktionen mot mottagande system misslyckas?”

Alla såg mot diagrammet igen.

Mats kände en gammal, välbekant trötthet veckla ut sig i bröstet. Där var det. Mellanrummet mellan systemen. Platsen där varje ruta i diagrammet såg hel ut var för sig, men verkligheten ändå kunde gå sönder.

Amir zoomade in bilden, som om svaret skulle finnas mellan pilarna.

“Det beror på var commit sker”, sa han.

“Precis”, sa Peter. “Och på vad ni anser vara sanning. Är status i Oracle sanning? Är MQ-meddelandet sanning? Är mottagande systems kvittens sanning?”

Karin skrev långsamt på tavlan:

**Vilken komponent bär sanningen?**

Det såg nästan filosofiskt ut. Mats hatade när tekniska problem blev filosofiska, eftersom det oftast betydde att de snart skulle bli akuta.

Sofia satte sig igen. Hon såg inte stressad ut, men hennes ansikte hade blivit mer slutet. Amir märkte det också. Mats såg hur han tittade på henne, inte länge, men med en sorts oro han inte hade visat någon annan i rummet.

“Vi behöver inte lösa hela distribuerade transaktionsproblemet i dag”, sa Sofia.

“Skönt”, sa Mats. “Jag hade annars tänkt hinna före lunch.”

Hon log inte, men hennes ögon mjuknade.

“Men vi behöver bestämma vilket felbeteende vi accepterar och hur vi upptäcker det. Exakt en gång kanske inte är realistiskt överallt. Då måste vi designa för minst en gång, idempotens och tydlig avstämning. Eller så måste vi begränsa flödet.”

Naya, som suttit tyst och antecknat testfall, lyfte handen lite trots att de inte var i skolan.

“Då behöver vi testfall för avbrott mitt i flödet. Inte bara lyckade meddelanden. Vi behöver döda konsumenten, starta om podden, simulera att MQ är uppe men mottagaren nere, och kontrollera vad användaren ser.”

Lena såg på henne med en ny sorts respekt.

“Ja.”

Det var andra gången Lena sa ja till någon från utveckling utan reservation. Mats noterade det, inte för att han tänkte använda det mot henne, utan för att sådana ögonblick var lättare att missa än konflikterna.

Karin pekade mot tavlan.

“Det här börjar bli miniminivå för MQ-spåret. Kan vi formulera den?”

Amir nickade och skrev i det gemensamma dokumentet som visades på skärmen.

1. Meddelandetyper klassificeras efter verksamhetskonsekvens.  
2. Persistens beslutas per meddelandetyp.  
3. Idempotens och dubbletthantering dokumenteras.  
4. Dead-letter-hantering definieras med ägare och larm.  
5. Backloggtrösklar och övervakning sätts innan produktion.  
6. Incidentbemanning anger vem som väcks och för vad.  
7. Användarstatus får inte ge falsk trygghet.  
8. Självservicegränser för MQ definieras: vad teamet får göra själva, vad som kräver granskning.

När han skrev den sjätte punkten såg han mot Mats.

“Vill du formulera den?”

Mats blev överraskad.

“Vadå?”

“Vem som väcks. Det är din formulering.”

Det borde ha känts som en seger. I stället kände Mats ett oväntat motstånd. Det var enklare att kasta in syrliga kommentarer från sidan än att få dem inskrivna som byggstenar. När något hamnade i dokumentet blev man delaktig. Då kunde man inte längre säga att allt var någon annans dumhet.

Han reste sig och gick fram till skärmen.

“Skriv: Incidentmodellen ska ange primär och sekundär kontakt per beroende, kriterier för eskalering och vilket team som äger första analysen vid larm.”

Amir skrev.

“Första analysen?”

“Ja. Inte första skuldplaceringen.”

Karin såg upp från tavlan. Hon sa inget, men Mats önskade nästan att hon hade gjort det. Tystnaden gjorde meningen större än han tänkt.

Lena lade till:

“Och om larmet gäller backlogg behöver det stå vem som bedömer verksamhetskonsekvens. Drift kan se att kön växer. Vi kan inte alltid veta vad det betyder för en handläggare eller en användare.”

Sara nickade på skärmen.

“Det tar jag. Eller verksamheten tar det. Men jag kan vara första väg in.”

“Bra”, sa Karin. “Då har vi ett konkret ägarskap.”

Mötet borde ha känts bättre efter det. På vissa sätt gjorde det det. Tavlan var full, dokumentet hade riktiga punkter, och människor hade börjat säga “vi” utan att det lät som mötesövning.

Ändå satt en oro kvar i Mats.

För varje sak de tydliggjorde blev arbetet större. Inte mindre. Det var det ingen ville säga högt. Den nya vägen skulle på sikt minska handpåläggningen, kanske. Men just nu krävde den mer av alla som redan hade för lite tid. Mer tänkande, mer dokumentation, mer gränsdragning, mer testning, mer ansvar.

Och någon skulle behöva göra det samtidigt som produktionen fortsatte gå sönder i vanlig takt.

Elin hade anslutit sent till mötet och satt nu tyst längst bak. Mats hade inte sett henne komma in. Det oroade honom mer än om hon hade avbrutit.

Karin verkade också ha märkt henne.

“Vi har identifierat arbete som måste göras före nästa produktionsförsök”, sa Karin. “Det här är inte bara kompletteringar i ett ärende. Det är design av ett standardmönster för MQ i plattformen.”

Elin nickade långsamt.

“Hur mycket tid pratar vi om?”

Ingen svarade.

Det var inte för att de inte visste. Det var för att alla visste att rätt svar skulle vara större än vad ledningen ville höra.

Sofia tog till slut ordet.

“För ett första säkert mönster för piloten? Några fokuserade dagar med rätt personer. För ett återanvändbart plattformsmönster? Mer. Och om det ska bli självservice behöver vi bygga in begränsningarna i mallar och kontroller, inte bara skriva dem i ett dokument.”

Elin såg på henne.

“Vem leder det tekniska arbetet?”

Där blev rummet stilla på ett annat sätt.

Mats kände hur Lena bredvid honom spände sig. Amir tittade inte bort från Sofia. Karin höll pennan stilla mot tavlan. Annika på skärmen blev plötsligt mycket intresserad av sina egna anteckningar.

Sofia mötte Elins blick.

“Just nu finns ingen utsedd person som gör det.”

Det var ett farligt svar. Inte för att det var fel, utan för att det var så rent. Det lämnade inget skyddande lager av formuleringar.

Elin lutade sig lite framåt.

“Men i praktiken?”

Sofia sa inget först. Mats såg hur hon vägde svaret. Om hon sa “jag” tog hon ansvar hon inte fått. Om hon sa något annat ljög hon.

Karin klev inte in och räddade henne. Det noterade Mats. Kanske av respekt. Kanske för att hon ville att tystnaden skulle göra sitt arbete.

“I praktiken”, sa Sofia till slut, “har jag börjat hålla ihop vissa delar. Men det är inte hållbart om det fortsätter informellt.”

Amir såg ner i bordet. Inte av ointresse, utan för att han verkade förstå att hans egen önskan om att Sofia skulle lösa saker också var en del av trycket på henne.

Lena sa:

“Hon ska inte bli nästa ‘hitta någon som vet’.”

Mats vände huvudet mot henne.

Orden hade kommit utan hennes vanliga skydd. Ingen syra. Ingen invändning. Bara en rak observation, nästan ett försvar.

Sofia tittade på Lena. Något passerade mellan dem. Inte vänskap, inte än. Men kanske en liten förskjutning i hur de såg varandra.

Elin andades ut.

“Jag hör er.”

Mats ville säga att det var en av chefssvenskans mest riskabla meningar. Den kunde betyda allt från “jag kommer agera” till “jag har registrerat ljud”. Men han lät bli.

Karin gjorde det inte.

“Vad betyder det konkret?”

Elin såg på henne, och för första gången under mötet såg hon inte irriterad ut över att bli pressad. Snarare trött på att hon själv inte hade pressat frågan tidigare.

“Det betyder att jag tar upp tekniskt ägarskap i eftermiddag med styrgruppen. Och att piloten inte får ett nytt produktionsdatum förrän vi har miniminivån beslutad och bemannad.”

Amir såg ut som om meningen gjorde fysiskt ont. Mats förstod honom nästan. Ett stopp var ett stopp även när det var klokt.

Sara hann före honom.

“Då behöver jag något att säga till verksamheten.”

Elin nickade.

“Säg att vi hittat risker som vi kan hantera nu eller betala för senare. Och att vi väljer nu.”

Det var ovanligt bra, tänkte Mats. Nästan misstänkt bra.

Karin skrev det längst ner på tavlan:

**Hantera nu – eller betala senare**

När mötet avslutades satt ingen kvar och låtsades arbeta. De reste sig långsamt, samlade ihop datorer, koppar och anteckningar. Teamsrutorna slocknade en efter en. Jonas vinkade stelt innan han försvann. Annika skrev i chatten att hon skulle lägga in sina MQ-noteringar i dokumentet.

Amir stod kvar vid skärmen och sparade filen. Sofia packade ner sin penna.

Mats tog sin kopp och såg att kaffet fortfarande inte var urdrucket. Kallt nu. Det var väl också ett slags verksamhetsstatus.

Vid dörren hann Amir ikapp honom.

“Mats.”

Han stannade.

“Ja?”

“Det där med exakt en gång och minst en gång. Har du något gammalt exempel vi kan läsa på? Något från en incident eller tidigare lösning?”

Mats första impuls var att säga att dokumentationen låg i det gamla filarkivet, vilket var sant och samtidigt nästan omöjligt att använda. Hans andra impuls var att säga att Amir kunde söka själv. Hans tredje, mer ovälkomna impuls, var att faktiskt hjälpa till.

“Det finns en incident från 2019”, sa han. “Meddelanden skickades om efter en omstart och skapade dubbletter i mottagande system. Inte samma tjänst, men samma typ av dumhet.”

Amir nickade.

“Kan du visa den?”

“Jag kan leta fram den.”

“Tack.”

Mats väntade på att Amir skulle lägga till något om att de behövde det snabbt eller att det var viktigt för sprinten. Det gjorde han inte.

I stället sa han:

“Jag tror att vi har underskattat hur mycket gammal driftkunskap som aldrig blivit krav.”

Det var en sådan mening som kunde få en människa att förlåta nästan fem procent av tidigare irritation.

Mats ryckte på axlarna.

“Vi har också underskattat hur mycket av vår kunskap som bara är skräckhistorier vid kaffemaskinen.”

Amir log.

“Då kanske vi kan börja där.”

När Amir gick stod Mats kvar en stund i korridoren. Genom glasväggen såg han Lena prata med Sofia. Han hörde inte orden, men kroppsspråket var annorlunda än i början av dagen. Mindre försvar. Mer försiktig prövning.

Karin stod ensam vid tavlan och fotograferade kolumnerna innan någon hann sudda ut dem.

Mats tänkte på det han hade sagt tidigare. Att Sofia höll på att få jobbet utan att ha fått det. Det var fortfarande sant. Men något hade ändrats. Flera hade sett det nu. Flera hade sagt det nästan högt.

Det kanske var så förändring började på en myndighet. Inte med ett beslut, utan med att en tyst ansvarsförskjutning blev synlig nog för att inte kunna förnekas.

Han gick tillbaka mot driftön.

På vägen plingade telefonen. Ett nytt incidentärende. Prioritet 3. En integration som rapporterade ökande svarstider.

Mats suckade.

Kön tog aldrig slut.

Men för första gången den dagen tänkte han att alla köer kanske inte behövde hanteras av samma person, på samma sätt, med samma gamla händer.
