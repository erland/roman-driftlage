# Kapitel 1 – Stopp i kön

Lena Holm såg ärendet redan innan hon öppnade det.

Inte bokstavligen. Det låg förstås där som alla andra ärenden i kön, med sitt automatiskt genererade nummer, sin prioritet, sina etiketter och sin förhoppningsfulla rubrik:

**Produktionssättning pilot containerplattform – Kundportal Meddelandehantering**

Men hon visste vad som skulle saknas.

Det var alltid något.

Hon tog upp kaffemuggen, märkte att den var tom och ställde ner den igen utan att resa sig. Hon hade tänkt hämta nytt kaffe efter morgonens incidentmöte, men någon hade ställt en fråga om certifikatförnyelser på vägen ut, och sedan hade frågan förökat sig till tre nya ärenden, två korta samtal och en påminnelse från Elin om att containerpiloten hade “hög synlighet”.

Hög synlighet. Lena hade arbetat tillräckligt länge för att veta vad det betydde. Om det gick bra skulle det bli en punkt på intranätet. Om det gick dåligt skulle det bli ett extra möte med rubriken “lärdomar”.

På den vänstra skärmen blinkade incidentkanalen fortfarande gult efter morgonens störning i e-tjänsten för arbetsgivarintyg. På den högra låg produktionssättningsärendet och väntade på hennes beslut. Bakom henne pratade Mats lågt i telefon med någon från databasteamet.

“Nej, jag säger inte att indexet är borta”, sa han. “Jag säger att applikationen beter sig som om indexet är borta. Det är en skillnad som betyder något för den som vill sova i natt.”

Lena drog handen över pannan och öppnade ärendet.

Hon skummade sammanfattningen först. Ny version av tjänst. Första produktionssättning via containerplattformens pilotspår. JBoss EAP-baserad applikation, extern koppling mot Oracle, meddelandeflöde via IBM MQ, loggning och sökdata till Elasticsearch. Utvecklingsteamet hade markerat allt som “klart för driftöverlämning”.

Det var nästan poetiskt, tänkte hon. Klart för driftöverlämning. Som om drift var en plats man kastade saker över staketet till.

Hon avskydde att hon tänkte så. Det gjorde henne till den person utvecklarna redan trodde att hon var: någon som satt med armarna i kors och väntade på att få säga nej. Det var inte så hon såg sig själv. Hon ville säga ja. Hon ville att saker skulle fungera, att medborgarna skulle kunna använda tjänsterna, att teamen skulle få ut det de hade byggt. Men ett ja i hennes värld betydde inte samma sak som i deras. Ett ja betydde att någon hade tänkt igenom natten efter releasen, inte bara minuterna före den.

Hon klickade vidare till bilagorna.

Deploymentbeskrivning.  
Rollbackplan.  
Kontaktlista.  
Brandväggsöppningar.  
Databaskopplingar.  
MQ-beroenden.  
Övervakning.  
Loggning.  
Säkerhetsklassning.  
Testprotokoll.

Allt hade rubriker. Det var något nytt. För två år sedan hade hälften av detta kommit som lösa kommentarer i ärendet, ofta med hänvisningen “enligt Teams-dialog”.

Lena borde ha varit glad. En del av henne var det också. Den del som fortfarande orkade se förbättringar. Men den större delen hade lärt sig att rubriker inte räddade produktion. Innehåll gjorde det.

Hon öppnade rollbackplanen och läste den två gånger.

Sedan en tredje.

Hon lutade sig bakåt.

“Mats”, sa hon.

Han höll fortfarande telefonen mot örat men vred huvudet lite mot henne.

“Mm?”

“Har du sett rollbacken för kundportalens containerpilot?”

Mats blundade kort, som om själva ordet containerpilot aktiverade en huvudvärk han hade sparat till senare.

“Jag har aktivt försökt att inte se den.”

“Det står att de rullar tillbaka genom att deploya föregående image.”

“Det är väl så man säger nu för tiden.”

“Det står inget om databasskriptet.”

Mats öppnade ögonen.

“Finns det databasskript?”

“En kolumnändring. En ny tabell för meddelandestatus. Och någon form av migrering av gamla statusvärden.”

Han sa något kort i telefonen, lyssnade, och täckte sedan mikrofonen med handen.

“Då är det inte en rollback. Det är en önskan.”

Lena nickade. Det var precis det. En önskan med versionsnummer.

Det irriterade henne att Mats satte ord på det så lätt. Själv hade hon ägnat år åt att lära sig skriva om farhågor till neutrala formuleringar. “Önskan” blev “rollbackplan saknar hantering av databasskript”. “Det här håller inte” blev “komplettering krävs före beslut”. Hon visste varför. Saklighet skyddade henne. Saklighet var en brandvägg mellan henne och bilden av den besvärliga driftkoordinatorn.

Hon fortsatte läsa. Vid MQ-avsnittet fanns en länk till en sida i teamets wiki. Länken fungerade inte. Hon kopierade adressen, klistrade in den i en annan flik och fick ett åtkomstmeddelande. Hon saknade behörighet.

Naturligtvis.

Hon skrev en anteckning i ärendet men skickade den inte. Inte än. Det var bättre att samla allt på en gång, annars skulle Amir svara på första punkten inom tre minuter och sedan börja argumentera punkt för punkt innan hon hunnit formulera helheten.

Amir Rahman. Team lead, senior utvecklare, ständig producent av välskrivna men otåliga kommentarer. Han använde aldrig utropstecken. Det behövdes inte. Irritationen låg ändå mellan raderna, prydligt paketerad i fraser som “för att undvika ytterligare ledtid” och “enligt tidigare överenskommelse om pilotens arbetssätt”.

Hon hade träffat honom första gången på ett planeringsmöte i januari. Han hade kommit in med en laptop full av diagram och en sådan där självklar energi som fick andra att luta sig framåt. Lena hade tyckt om honom de första tio minuterna. Sedan hade han sagt att driftens nuvarande beställningsmodell var “i praktiken en kö för att få lov att göra sitt jobb”, och rummet hade blivit stilla på det där svenska sättet där ingen säger emot direkt men alla minns.

Det värsta var att han inte hade helt fel.

Lena klickade upp testprotokollet.

Först såg det bra ut. Enhetstester, integrationstester, lasttest i testmiljö. Sedan hittade hon det hon letade efter utan att riktigt vilja hitta det.

Lasttestet var gjort utan faktisk MQ-belastning.

Hon stirrade på raden.

Det var inte nödvändigtvis ett stoppande fel. Inte ens troligen. Men det betydde att ett av de viktigaste beroendena i produktionsflödet var antaget snarare än bevisat. Och antaganden hade en särskild förmåga att vakna till liv klockan 02.17 en lördag.

Bakom henne avslutade Mats samtalet.

“Det var inte indexet”, sa han. “Det var en ny klientversion som skickade tomma sökfält. Så nu är det vårt fel att deras fråga betyder allt och inget samtidigt.”

“Grattis.”

“Jag skriver upp det på listan över saker som egentligen är verksamhetslogik men ändå hamnar hos drift.”

Lena log kort men tappade det när hon kom till avsnittet om övervakning.

Readiness probe: `/health/ready`  
Liveness probe: `/health/live`

Bra.

Hon klickade på beskrivningen.

Readiness kontrollerade att applikationen svarade.

Inte Oracle.  
Inte MQ.  
Inte beroendet mot Elasticsearch.  
Inte att tjänsten faktiskt kunde ta emot och behandla ett meddelande.

Bara att applikationen svarade.

Hon kände tröttheten komma som ett tryck bakom ögonen.

Det var inte slarv, försökte hon säga till sig själv. Det var inte illvilja. Det var kanske till och med rimligt ur deras perspektiv. I en utvecklingsmiljö var en grön endpoint ett tecken på framgång. I produktion kunde samma gröna endpoint vara en lögn med god formatering.

Hon öppnade kontaktlistan. Där fanns Amir, två utvecklare, en testare och en produktägare. Driftkontakt: “enligt ordinarie incidentväg”.

Lena läste raden igen.

Enligt ordinarie incidentväg.

Hon kände hur något i henne hårdnade. Inte för att formuleringen var den värsta hon sett, utan för att den avslöjade hela glappet. För teamet var incidentvägen en försäkring: om något hände fanns drift där. För henne var den en kö av människor som väcktes, ringdes, jagades och förväntades förstå en lösning de inte fått vara med och forma.

Hon tog ett andetag, långsamt genom näsan, och skrev:

> Produktionssättning kan inte godkännas i nuvarande form.

Hon stannade där. Fingrarna vilade över tangentbordet.

Hon visste vad som skulle hända när hon skickade.

Först skulle det bli tyst i kanske fyra minuter. Sedan skulle Amir skriva i ärendet. Sedan skulle någon lägga till henne i en Teams-tråd som redan hade pågått i två dagar utan driftkoordineringen. Sedan skulle Elin, sektionschefen, fråga om det här verkligen behövde stoppa piloten. Sedan skulle någon säga att de måste hitta ett mer agilt arbetssätt. Och någon annan, kanske Karin Nyström om hon redan hunnit bli inkopplad, skulle föreslå ett gemensamt möte.

Lena hade inget emot möten i teorin.

I praktiken hade hon redan sex i kalendern före lunch. Och någonstans under alla färgkodade rutor fanns det egentliga arbetet, det som inte syntes förrän det inte blev gjort.

Hon fortsatte skriva.

> Följande punkter behöver kompletteras eller förtydligas före nytt beslut:
>
> 1. Rollbackplan saknar hantering av databasskript och migrerade statusvärden.
> 2. MQ-dokumentation är inte åtkomlig för driftkoordinering.
> 3. Testprotokoll visar inte verifiering med representativ MQ-belastning.
> 4. Readiness-kontroll verifierar endast applikationssvar, inte kritiska beroenden.
> 5. Kontakt- och ansvarsfördelning vid incident är otydlig. “Ordinarie incidentväg” är inte tillräckligt för pilot med nytt driftmönster.
>
> Beslut: Ej godkänd för produktionssättning i kväll.

Hon läste igenom texten. Den var saklig. Inte varm, men saklig. Värme var inte ett kravfält.

Hon tryckte på Skicka.

Det tog två minuter och fyrtio sekunder.

Sedan plingade Teams.

Mats skrattade tyst bakom henne.

“Rahman?”

“Jag har inte öppnat än.”

“Du behöver inte. Jag hörde plinget.”

Lena öppnade meddelandet.

> Hej Lena. Vi behöver förstå varför detta stoppas nu. Samtliga punkter har varit synliga i ärendet sedan i måndags och piloten har explicit prioritet från styrgruppen. Kan vi ta detta direkt?

Hon såg på formuleringen. Direkt betydde nu. Nu betydde att hennes nästa möte skulle börja om nio minuter och handla om certifikatsförnyelser som någon hade glömt beställa i tid. Efter det skulle hon sitta i en incidentgenomgång där ingen ville säga att testmiljön och produktionsmiljön skilde sig åt på tre avgörande punkter. Efter det skulle hon äntligen äta den yoghurt som redan hade stått i väskan för länge.

En del av henne ville skriva det. Inte i ärendet, förstås. Men till honom. Hon ville skriva: Jag såg punkterna nu eftersom jag inte har haft en ostörd timme sedan i torsdags. Jag såg dem nu eftersom samma människor som vill ha snabbare flöden också vill att drift ska hålla ihop certifikat, incidenter, patchar, brandväggar, databaser, köer och övervakning utan att något annat prioriteras bort.

I stället svarade hon:

> Jag kan ta 15 minuter kl. 10.30. Beslutet kvarstår tills punkterna är hanterade.

Amir svarade nästan omedelbart.

> Då missar vi kvällens fönster.

Lena skrev:

> Ja.

Hon lät markören stå kvar efter ordet.

Det fanns mycket hon kunde lägga till. Att ett produktionsfönster inte var ett tåg man hoppade på bara för att det stod vid perrongen. Att styrgruppsprioritet inte gjorde en rollbackplan verklig. Att ingen kom ihåg hur snabbt “pilot” blev “skarp drift” när något väl låg i produktion.

Men hon skickade bara:

> Ja.

Mats reste sig och kom fram till hennes skrivbord. Han hade den där blicken han fick när han både sympatiserade med henne och tyckte att hon just hade tänt eld på en papperskorg.

“Du vet att det kommer bli liv.”

“Det är redan liv.”

“Mer liv.”

“Det saknas rollback för databasen.”

“Då saknas rollback.”

“Readiness säger bara att applikationen svarar.”

“Det är ju positivt. Den kunde ha sagt ingenting.”

Lena gav honom en blick.

Han höjde händerna.

“Förlåt. Jag använder humor som försvar mot modernisering.”

“Det fungerar dåligt.”

“Det har hållit mig vid liv sedan WebSphere.”

Hon ville skratta, men Teams plingade igen. Den här gången var det inte Amir. Det var Elin.

> Har du möjlighet att komma förbi efter certifikatmötet? Vi behöver prata om pilotstoppet. Karin Nyström är med.

Lena stängde ögonen en sekund.

Där var hon. Karin.

Hon hade bara träffat Karin två gånger. Första gången hade Karin lett en workshop om teamgränser och beroenden. Hon hade haft lugn röst, färgglada pennor och en nästan provocerande förmåga att låta varje invändning som början på en insikt. Andra gången hade hon suttit tyst längst bak under en styrgrupp och antecknat medan utvecklingschefen förklarade att containerplattformen skulle korta ledtiderna “utan att tumma på kvaliteten”.

Det var den sortens mening som fick Lena att vilja be om en definition av varje ord.

Hon svarade Elin:

> Jag kommer efter mötet. Cirka 10.05.

Sedan lade hon till:

> Beslutet i ärendet kvarstår.

Hon raderade det. Skrev om.

> Jag kan redogöra för bedömningen.

Det var bättre. Mindre som en sköld. Även om det var en sköld.

Certifikatmötet blev sämre än väntat. Vilket i sig var imponerande. En extern leverantör hade bytt kontaktperson, den nya kontaktpersonen hade inte åtkomst till rätt portal, och någon hade antagit att automatisk förnyelse var aktiverad eftersom det “brukade vara så på de nya tjänsterna”. Det var det inte.

Medan de pratade om ägarskap för certifikatet kom Lena på sig själv med att tänka på Amir. Hon undrade om han satt med sitt team nu och ritade pilar på en whiteboard, eller om de redan hade börjat komplettera underlaget. Hon undrade om han förstod att hon inte njöt av att stoppa dem.

Det störde henne att hon brydde sig om det. Professionellt sett borde det räcka att beslutet var korrekt. Men beslut levde inte bara i ärenden. De levde i människors blickar nästa gång man möttes i ett rum.

När Lena kom ut från mötesrummet hade hon tre nya meddelanden från Amir, två från Elin och ett från en okänd kanal som hette `container-pilot-samverkan`.

Hon stod stilla i korridoren och såg på kanalnamnet.

Samverkan.

Det var ett sådant ord som kunde betyda allt från gemensamt ansvar till att någon ville att man skulle säga ja med mjukare röst.

Hon gick mot Elins rum.

Myndigheten för samhällstjänster låg i ett grått kontorskomplex nära järnvägen. Huset hade byggts om flera gånger, men aldrig tillräckligt mycket för att kännas nytt. Glasväggar hade satts upp framför gamla korridorer. Tysta rum hade skapats där förråd hade legat. På väggarna satt affischer om digital förnyelse, tillgänglighet och medborgarnytta.

Lena passerade en av dem på vägen.

**Vi förenklar vardagen för alla.**

Hon undrade ibland vilka “vi” var tänkta att vara. Hon hade inget emot medborgarnyttan. Tvärtom. Det var därför hon fortfarande var kvar. Men vardagen blev sällan enklare för dem som skulle hålla förenklingen igång.

Elins dörr stod öppen. Karin satt redan där med en bärbar dator framför sig och en anteckningsbok bredvid. Hon såg upp när Lena kom in.

“Lena. Hej.”

“Hej.”

Elin pekade mot stolen närmast dörren.

“Tack för att du kom snabbt.”

“Jag har nio minuter innan incidentgenomgången.”

Hon hörde själv hur kantigt det lät. Hon hade inte tänkt låta otrevlig. Men hon ville markera tiden, för annars försvann den. Tid var det enda alla tog för givet att drift alltid kunde hitta mer av.

Elin tog in det, nickade lite för snabbt och lade händerna på bordet.

“Då går vi rakt på. Vi behöver förstå stoppet.”

Lena satte sig.

“Jag skrev fem punkter i ärendet.”

“Ja”, sa Elin. “Och jag har läst dem. Frågan är om de behöver stoppa kvällens fönster eller om de kan hanteras parallellt.”

“Rollback kan inte hanteras parallellt med en produktionssättning.”

Karin skrev något i sin anteckningsbok. Inte på datorn. För hand. Lena visste inte varför det störde henne. Kanske för att det såg eftertänksamt ut. Som om situationen var något som kunde förstås lugnt, bara man lyssnade tillräckligt noga.

Elin höll kvar blicken på henne.

“Piloten är viktig.”

“Det är produktion också.”

“Det förstår jag.”

Lena hörde att hon menade det. Elin var inte dum. Hon var bara placerad i en roll där varje försening såg ut som en brist på styrning, och varje risk som inte inträffat ännu såg ut som försiktighet.

Karin lutade sig lite framåt.

“Kan jag ställa en fråga?”

Lena såg på henne.

“Det brukar vara därför du är med.”

Karin log inte bort det, vilket Lena motvilligt uppskattade.

“Av de fem punkterna, vilka är absoluta stoppunkter och vilka är förbättringar som behöver in i plattformens arbetssätt framåt?”

Det var en bra fråga. Irriterande nog.

“Rollback för databasen är stoppande”, sa Lena. “Otillgänglig MQ-dokumentation är stoppande, eftersom drift inte kan verifiera beroenden. Incidentansvar är stoppande eftersom piloten innebär nytt driftmönster.”

“Och readiness-kontrollen?”

“Den är felaktig som garanti, men kanske inte stoppande ensam.”

“Test med MQ-belastning?”

“Beror på volym och risk. Men tillsammans med övrigt stärker det stoppet.”

Karin nickade och skrev.

Lena märkte att hon hade svarat mer nyanserat än hon tänkt. Det var farligt med bra frågor. De kunde få en att låta som om man var beredd att förhandla om sådant som egentligen borde vara självklart. Samtidigt visste hon att allt inte var lika viktigt. Hon visste det bättre än de flesta. Drift var att skilja på rök, damm och eld medan alla andra ropade att det luktade bränt.

Elin såg mellan dem.

“Så om teamet kompletterar de tre första punkterna före eftermiddag, finns möjlighet att köra i kväll?”

Lena kände hur fällan nästan slog igen. Möjlighet. Ett mjukt ord som i efterhand kunde citeras som löfte.

“Nej”, sa hon.

Elins ansikte blev stelt.

“Du sa just—”

“Jag sa vad som är stoppande. Jag sa inte att vi hinner granska, förstå och bemanna ett nytt underlag före kvällens fönster samtidigt som vi hanterar dagens drift.”

“Hur lång tid behöver ni?”

Lena tänkte på rätt svar. Det fanns inget.

Om hon sa två dagar skulle Amir säga att det var orimligt. Om hon sa en dag skulle hennes egen grupp få betala med ännu en kväll. Om hon sa att hon inte visste skulle det låta som att drift saknade kontroll.

Det var en av de saker hon hatade mest med sin roll: hon förväntades alltid kunna ge ett exakt svar på hur lång tid ansvar tog.

“Vi behöver ett faktiskt arbetssätt för piloten”, sa hon till slut. “Inte ett vanligt produktionsärende med ordet container i rubriken.”

Det blev tyst.

Karin slutade skriva.

Elin lutade sig tillbaka.

“Vad menar du?”

Lena hade inte tänkt säga det. Inte nu. Kanske inte alls. Men orden hade kommit, och när de väl låg där kände hon att de var sannare än de fem punkterna i ärendet.

“Vi försöker pressa in ett nytt sätt att drifta i en gammal grindmodell. Utvecklingsteamet tror att pilot betyder snabbspår. Drift tror att pilot betyder extra risk. Ledningen tror att pilot betyder bevis på framdrift. Ingen har definierat vad som faktiskt ska vara sant innan något får gå i produktion.”

Karin såg på henne på ett annat sätt nu. Mindre som en facilitator, mer som någon som just fått en tråd att dra i.

“Och vem tycker du ska definiera det?”

Lena skrattade en gång, torrt.

“Det är väl därför jag är här? För att ni vill att jag ska säga drift.”

“Vill du säga drift?” frågade Karin.

Lena svarade inte direkt.

Genom glasväggen såg hon två personer från Amirs team gå förbi i korridoren. Den ena sa något med händerna i luften. Den andra skakade på huvudet. De såg unga ut, fast de kanske inte var det. Det var något med människor som fortfarande trodde att motstånd betydde att någon inte förstått.

Hon mindes att hon själv hade varit sådan en gång. Inte med containrar, men med annat. Hon hade kommit in som ny drifttekniker och sett gamla rutiner som onödigt krångliga. Hon hade frågat varför samma kontroll skulle göras två gånger. Varför någon behövde signera en ändring som redan var testad. Varför produktionssättningarna låg på kvällstid när alla var trötta. Ofta hade hon fått dåliga svar. Ibland hade hon senare förstått att de dåliga svaren skyddade mot verkliga problem som ingen längre orkade förklara.

“Nej”, sa Lena till slut. “Inte ensamt.”

Elin höjde ögonbrynen.

“Det var nytt.”

“Det betyder inte att jag tycker att de ska köra i kväll.”

“Det förstod jag nästan.”

För första gången log Karin lite.

Lena såg bort. Hon ville inte bli belönad för rimlighet. Rimlighet hade en tendens att bli extraarbete.

Hennes telefon vibrerade. Incidentgenomgången började om två minuter.

“Jag måste gå.”

Elin nickade, men Karin ställde en sista fråga.

“Om vi samlar rätt personer i eftermiddag, inte för att rädda kvällens fönster utan för att definiera pilotens miniminivå — kommer du?”

Lena borde ha sagt att hon inte hade tid. Det var sant. Hon borde ha sagt att de fick skicka underlag. Det var rimligt. Hon borde ha sagt att hon behövde prioritera operativ drift, vilket alltid fungerade som både argument och fängelse.

I stället hörde hon sig själv fråga:

“Vilka är rätt personer?”

Karin svarade utan att titta på Elin.

“Du. Amir. Någon som kan MQ. Någon från databassidan. Sofia Berg, om hon kan.”

Lena reagerade på det sista namnet.

“Sofia?”

“Känner du henne?”

“Jag vet vem hon är.”

Alla visste vem Sofia var, på det där sättet man visste vem någon var när den personen sällan pratade högst men ofta var den sista som lämnade ett problem.

Karin lade ner pennan.

“Jag tror att hon ser något i det här som vi andra inte riktigt har formulerat än.”

Lena reste sig.

“Då får vi hoppas att hon har bättre kalender än jag.”

Hon gick därifrån innan någon hann kalla det konstruktivt.

I korridoren plingade Teams igen. Amir, förstås.

> Vi kommer komplettera underlaget. Men jag vill vara tydlig med att om varje pilot behandlas som traditionell produktion kommer vi aldrig få någon faktisk förändring.

Lena stannade vid fönstret mot innergården. Det hade börjat regna, ett tunt majregn som gjorde betongen mörkare men inte renare.

Hon läste meddelandet två gånger. Första gången hörde hon bara anklagelsen. Andra gången hörde hon något annat också. Frustration, ja, men kanske också rädsla. Inte samma sorts rädsla som hennes. Amir var nog inte rädd för produktion på samma sätt. Han var rädd för stillastående. För att allt de byggde skulle fastna i rutiner som ingen längre trodde på men alla fortsatte följa.

Det gjorde inte honom mindre irriterande.

Men det gjorde honom svårare att avfärda.

Hon skrev:

> Jag håller med om att vi behöver ett annat arbetssätt för piloten.

Hon såg på meningen länge.

Sedan lade hon till:

> Det betyder inte lägre krav. Det betyder tydligare krav tidigare.

Hon skickade innan hon hann ångra sig.

Svaret kom inte direkt.

Det var första gången på hela morgonen som tystnaden kändes som något annat än väntan på nästa problem.
