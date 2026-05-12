# Kapitel 14 – Det som kostar

Elin Varga hade lärt sig att styrgrupper sällan började med det som var svårt.

De började med föregående protokoll, med statusrutor, med gröna markeringar som egentligen betydde att ingen ännu hade vågat ändra färg. De började med försiktiga formuleringar om framdrift, beroenden och behov av förankring. Det svåra kom först när någon insåg att ett beslut inte bara var en mening i minnesanteckningarna utan något som krävde att någon annan slutade göra något annat.

Hon stod kvar utanför mötesrummet Almen med datorn mot bröstet och såg genom glasväggen hur de andra redan hade börjat ta plats. IT-chefen satt längst in, vänd mot skärmen. Två sektionschefer pratade lågt med varandra. Verksamhetsrepresentanten från kundportalen bläddrade i sin mobil med den koncentrerade minen hos någon som försökte hålla irritation professionell. På den stora skärmen stod mötesrubriken redan uppe.

**Containerplattform – pilot, prioritering och produktionsförutsättning**

Elin hade själv bett att ordet prioritering skulle stå där. Hon hade ångrat det tre gånger sedan dess.

Det var enklare att säga att något var viktigt än att säga vad som därmed inte längre var lika viktigt. Myndigheten hade gott om viktiga saker. Vissa var lagstyrda, vissa politiskt synliga, vissa bara gamla nog att ha blivit självklara. Alla hade ägare. Alla hade datum. Alla hade någon som skulle bli upprörd om de flyttades.

Hon öppnade presentationen en sista gång.

Sofia hade skrivit den tekniska delen med sin vanliga sparsamhet. Inga dramatiska ord. Bara konsekvenser. Pilotväg 0.1 krävde mall, pipeline, policy, observability och runbook. Blockerande krav behövde verifieras. Felvägar behövde testas: Oracle-timeout, MQ-stopp, rollback eller kompensation. Minst två personer behövde kunna bära plattformsförmågan bredvid Sofia.

Karin hade lagt till en bild som Elin först hade velat ta bort.

Den hette **Vad kostar det om vi inte prioriterar?**

På bilden fanns inga pengar. Bara fyra punkter.

Mer manuell granskning sent.  
Fler omtag.  
Högre incidentrisk.  
Lägre tillit till plattformen.

Elin hade läst den flera gånger och känt hur den störde henne just för att den inte gick att avfärda. Den anklagade ingen. Den bara tog bort illusionen att det gick att få allt.

Hon öppnade dörren.

Samtalen i rummet sjönk en nivå. Inte för att hon var högst i hierarkin. Hon var det inte. Men hon ägde punkten, och alla som ägde en svår punkt bar med sig en sorts väder.

“Då börjar vi”, sa IT-chefen, Per Norling, och nickade mot henne. “Elin, du ville ha ett beslutsärende om piloten.”

“Ja.”

Hon kopplade in datorn. Skärmen blinkade till och visade första bilden: en enkel tidslinje från stoppat produktionsfönster till föreslagen ny plan.

Elin hade bestämt sig för att inte börja med tekniken. Teknik kunde få människor att välja sida för fort. Antingen blev de trygga av detaljer och slutade lyssna på konsekvenser, eller också blev de osäkra och började prata om governance.

“Vi har gjort en genomgång av vad som krävs för att piloten ska kunna gå vidare på ett sätt som faktiskt testar den nya vägen”, sa hon. “Inte bara trycker en gammal produktionsprocess genom en ny plattform.”

Hon hörde själv hur meningen lät. Den hade Lenas fingeravtryck i sig, även om Lena aldrig skulle ha uttryckt den så i styrgruppen. Elin hade börjat samla sådana formuleringar i huvudet. De var ofta skarpare än hennes egna.

“Piloten är fortfarande viktig”, fortsatte hon. “Men vi har ett vägval. Antingen ger vi arbetet prioriterad bemanning under en kortare period och accepterar att annat flyttas, eller så kör vi det vid sidan av ordinarie drift och leverans. Då tar det längre tid och risken ökar.”

Verksamhetsrepresentanten, Maria Ek, såg upp.

“Vad betyder längre tid?”

“Ungefär tre veckor till första möjliga försök, med högre osäkerhet. Med prioriterad bemanning bedömer vi att vi kan ha en verifierad miniminivå på ungefär en vecka.”

En av sektionscheferna, Henrik, lutade sig bakåt.

“Jag vill bara förstå. Vi pratar om att frigöra folk för att ta fram dokumentation och mallar?”

Där var den. Den första minskningen. Från arbetssätt till dokumentation. Från förmåga till papper.

Elin klickade fram nästa bild.

“Nej. Vi pratar om att bygga och verifiera en första användbar väg till produktion. Det innefattar dokumentation, men också pipelinekrav, felvägstester, runbook, ansvarsfördelning, observability och beslut om externa beroenden.”

“Men det här är väl sådant som redan ingår i projektet?” frågade Henrik.

Elin höll kvar blicken på honom. Hon kände impulsen att mildra svaret, att säga både ja och nej, att lämna en liten öppning där ingen behövde känna sig träffad. Det var så många möten överlevde. Det var också så de blev meningslösa.

“Det ingår som förväntan”, sa hon. “Inte som faktisk kapacitet.”

Rummet blev tystare.

Karin satt inte med i styrgruppen. Hon hade erbjudit sig att finnas tillgänglig efteråt, och Elin hade nästan bett henne vara med ändå. Sedan hade hon låtit bli. Det här var hennes beslutspunkt. Hon kunde inte låna mod från Karin varje gång någon behövde säga något obekvämt.

Per Norling vek händerna framför sig.

“Vilka resurser pratar vi om?”

Elin klickade fram bilden med bemanningsförslaget.

“Sofia på femtio procent under två veckor för pilotens standardmönster och teknisk samordning. Lena eller utsedd driftkoordinator på tjugo procent under samma period för att bygga in driftkraven tidigare. Mats på avgränsade pass för runbook, beroenden och legacykunskap. Amir och Naya från utvecklingsteamet för implementation och felvägstester. Annika från MQ och Peter från databas vid definierade beslutspunkter.”

Henrik gjorde en min som nästan var ett leende.

“Det där låter mer än en vecka.”

“Kalendertid och arbetstid är inte samma sak.”

Elin hade inte tänkt säga det så rakt. Men när orden väl var ute kände hon samma blandning av obehag och lättnad som när man öppnade ett fönster i ett rum där alla låtsades att luften var bra.

Maria från verksamheten lade ner mobilen.

“Vad händer med leveransen till kundportalen om vi väljer treveckorsspåret?”

“Då skjuts produktionsfönstret fram, och teamet fortsätter arbeta med delar av flödet parallellt. Men de får mer väntan på granskning, och risken är att vi hittar brister sent.”

“Vad händer med våra användare?”

“Just den här ändringen handlar inte om en lagdeadline”, sa Elin. “Men den påverkar vår förmåga att hantera meddelandestatus mer tillförlitligt framåt.”

Maria nickade långsamt.

“Så verksamheten vill ha den. Men den måste inte ut på fredag.”

“Tack”, sa Elin, innan hon hann stoppa sig.

Maria log svagt. “Det var inget löfte om tålamod. Bara fakta.”

Per bläddrade i underlaget på sin skärm.

“Vad skjuter vi på om vi frigör drift?”

Där var frågan. Den riktiga.

Elin hade förberett svaret, men det kändes ändå som att hon tog fram något ömtåligt och lade det på bordet.

“Vi föreslår att den interna förbättringen kring certifikatinventering skjuts en vecka. Patchplaneringen för två lågkritiska interna system flyttas inom godkänt fönster. Driftkoordineringen avstår från att delta i två mindre designgranskningar som inte är produktionsnära. Utvecklingsteamet pausar en planerad refaktorering utan verksamhetsdeadline.”

Henrik höjde ögonbrynen.

“Certifikatinventeringen? Den var ju resultat av senaste tillbudet.”

“Ja.”

“Och nu vill vi skjuta den?”

“En vecka”, sa Elin. “Inte avbryta.”

Han såg inte övertygad ut. Det var rimligt. Hon var inte heller helt övertygad. Hon hade suttit med Lena dagen innan och gått igenom listan över vad som kunde flyttas utan att någon ljög om konsekvensen. Lena hade inte tyckt om något av alternativen. Det hade blivit kriteriet.

Om det fanns ett alternativ ingen ogillade hade de antagligen missat något.

“Det är det här jag menar”, sa Henrik. “Vi säger att vi ska minska risk, och så skjuter vi på riskreducerande arbete för att införa ny teknik.”

Elin kände hur flera i rummet följde frågan med blicken och vände den mot henne. Hon förstod dem. Det lät motsägelsefullt.

“Vi skjuter inte på riskreducering för teknikens skull”, sa hon. “Vi väljer mellan olika risker. Om vi inte prioriterar piloten kommer drift ändå behöva göra sena manuella granskningar varje gång utvecklingsteamet försöker komma framåt. Då skjuter vi bara kostnaden till kvällar, omtag och informella undantag. Det ser billigare ut eftersom det inte står i någons plan.”

Hon såg ner på sina händer. De låg stilla på bordet, vilket förvånade henne.

“Jag tror att det är det vi har gjort länge”, fortsatte hon. “Vi har låtit drift betala med osynlig tid.”

Det sista var egentligen Lenas ord. Eller kanske Karins. Eller kanske hade det blivit hennes först när hon vågade säga det i ett rum där det kunde kosta något.

Per lutade sig tillbaka. Han var tyst länge nog för att någon skulle hinna fylla i, men ingen gjorde det.

“Vad säger driftchefen?” frågade han till slut.

Henrik såg åt sidan. Han var inte driftchef, men han ägde en av de berörda linjerna.

“Jag säger att vi inte kan behandla den här typen av arbete som om det ligger ovanpå allt annat. Där håller jag med. Men jag vill ha tydlig avgränsning. Annars kommer allt som rör plattformen bli prioriterat.”

Elin nickade.

“Därför är förslaget begränsat till Pilotväg 0.1 och Kundportal Meddelandehantering. Inte generell containerplattform. Inte alla framtida team. Inte en öppen konsultationstjänst från Sofia eller drift.”

Hon klickade fram bilden med avgränsningen. Sofia hade insisterat på den.

**Gäller:** pilotens standardmönster för applikationsdeployment med externa beroenden.  
**Gäller inte:** generell migrering av alla applikationer, databasplattform, MQ-plattformsstrategi, fullständig målarkitektur.

När Sofia hade skrivit “gäller inte” hade Elin först tänkt att det såg defensivt ut. Nu kände hon att det kanske var den viktigaste delen av hela beslutet.

Maria pekade på skärmen.

“Vem säger nej om någon försöker använda piloten för något utanför det där?”

“Sofia inom det tekniska standardmönstret”, sa Elin. “Jag när det gäller prioritering och omfattning. Karin håller ihop uppdraget och synliggör avvikelser.”

“Och om utvecklingsteamet inte håller med?”

“Då eskaleras det till mig, inte till en korridorförhandling med drift.”

Det kom lite för snabbt. För mycket irritation sipprade igenom. Elin märkte det och lät tystnaden efteråt göra jobbet i stället för att lägga till en ursäkt.

Per såg mot Henrik.

“Kan du leva med det?”

Henrik svarade inte direkt.

“Jag kan leva med det om det är tidsatt, om de flyttade driftaktiviteterna dokumenteras och om vi får en återrapport där det framgår vad som blev byggt bort och vad som bara flyttades.”

Det var en bra formulering. Elin skrev ner den.

“Det kan vi göra.”

Maria lutade sig framåt.

“Jag vill också ha ett verksamhetsspråk i återrapporten. Inte bara teknisk färgstatus. Vad betyder det här för vår förmåga att leverera nästa förändring?”

Elin nickade. “Rimligt.”

Per tittade på klockan och sedan på gruppen.

“Då sammanfattar jag. Vi beslutar att piloten får prioriterad bemanning enligt Elins förslag under två veckor, med första avstämning efter en vecka. Omfattningen är Pilotväg 0.1 för Kundportal Meddelandehantering. Flyttade aktiviteter dokumenteras. Återrapport ska innehålla vad som byggts bort, vad som flyttats och vad det betyder för kommande leveranser. Elin äger prioriteringen. Sofia får tekniskt mandat inom standardmönstret. Karin håller ihop uppdraget. Stämmer det?”

Elin väntade på invändningen.

Den kom inte.

Beslut kunde ibland låta så enkelt när någon sammanfattade dem. Som om alla hade varit på väg dit hela tiden.

“Stämmer”, sa hon.

Det var först när hon satte sig i det lilla telefonrummet efteråt som hon märkte att hon var trött. Inte vanlig möteströtthet. Något djupare, som om hon hade hållit upp en möbel medan någon annan skruvade fast benen.

Hon skrev till Karin.

> Beslut taget. Prioriterad bemanning två veckor, första avstämning efter en. Avgränsat till Pilotväg 0.1 och Kundportal Meddelandehantering. Vi fick igenom dokumentation av vad som byggs bort vs flyttas.

Svaret kom efter nästan en minut.

> Bra. Och hur känns det?

Elin stirrade på frågan.

Hon hade förväntat sig nästa steg, bokningslista, kommunikationsplan. Inte det där.

Hon skrev:

> Dyrt.

Sedan lade hon till:

> Men ärligt.

Karin svarade:

> Det är en bra början.

Elin lade ner telefonen och blundade.

När hon öppnade ögonen igen hade hon ett nytt meddelande från Lena.

> Jag hörde att beslutet är taget. Behöver veta exakt vilka driftaktiviteter som flyttas innan jag kommunicerar till gruppen.

Elin log trots sig själv. Lena började inte med tack. Lena började med konsekvens.

Hon svarade:

> Jag kommer till driftön 13.00. Vi går igenom listan tillsammans.

Lenas svar kom direkt.

> Ta med faktisk lista. Inte styrgruppsformuleringar.

Elin skrev:

> Jag vet.

Hon gick dit fem minuter före utsatt tid.

Driftön var mer högljudd än vanligt. Inte högljudd på ett öppet sätt, utan på det där dämpade sättet när människor försökte arbeta och samtidigt låta bli att kommentera något de alla redan visste. Mats satt med hörlurar runt halsen och läste något på sin skärm med armarna i kors. Lena stod vid whiteboarden och hade redan ritat tre kolumner.

**Flyttas**  
**Skyddas**  
**Behöver ersättare**

“Du är tidig”, sa Lena.

“Jag tänkte att det var bäst att komma innan ryktet hann bli bättre än beslutet.”

Mats snurrade stolen ett halvt varv.

“För sent. Enligt ryktet ska vi nu jobba agilt med certifikaten genom att hoppas på det bästa.”

Elin tog av sig jackan.

“Då börjar vi där.”

Hon gick igenom beslutet punkt för punkt. Lena avbröt inte lika ofta som Elin hade väntat sig. Det oroade henne nästan mer. Lena skrev bara på tavlan, flyttade en aktivitet från Flyttas till Skyddas, drog ett streck under “certifikatinventering en vecka, ej mer” och ringade in Mats namn vid runbookpassen.

“Jag vill inte att Mats blir uppäten av det här”, sa Lena.

“Det är avgränsade pass”, sa Elin.

“Det är allt tills någon börjar fråga ‘kan du bara titta på’.”

Mats pekade på henne utan att släppa skärmen.

“Det där borde stå på min gravsten.”

Elin nickade.

“Då skriver vi det som regel. Inga informella ‘kan du bara’-uppdrag in i piloten. Allt går via Karin och Sofia.”

Lena såg på henne.

“Menar du det?”

“Ja.”

“Det kommer bli obekvämt.”

“Jag börjar vänja mig.”

Det var inte helt sant, men det var tillräckligt nära.

Lena skrev på tavlan:

**Inga sidodörrar.**

Hon stod kvar med pennan mot tavlan en sekund längre än nödvändigt. Elin undrade om hon tänkte på hur många sidodörrar drift hade blivit tvungen att vara genom åren. Människor gick inte alltid runt processer för att de var lata. Ibland gick de runt dem för att det var enda sättet att få något gjort. Problemet var att sidodörrar efter ett tag blev huvudingångar för alla utom dem som behövde hålla reda på huset.

“Jag behöver säga en sak till gruppen”, sa Lena.

“Gör det.”

Lena vände sig mot de andra i driftön. Det var bara fem personer där just då, men fler hade börjat lyssna utan att låtsas om det.

“Vi kommer lägga tid på piloten de kommande två veckorna”, sa hon. “Inte för att allt annat blev mindre viktigt. Inte för att containerplattformen går före drift. Utan för att en del av det här arbetet ska göra att vi slipper sena manuella kontroller längre fram.”

Hon höll blicken på gruppen, inte på Elin.

“Det betyder inte att vi säger ja till allt. Det betyder att vi är med tidigare och tydligare. Om någon försöker lägga extra saker direkt på er vid sidan av, skickar ni det till mig.”

Mats höjde handen halvt.

“Gäller det även om någon säger att det bara tar fem minuter?”

“Särskilt då.”

Det gick ett litet skratt genom gruppen. Inte stort, men tillräckligt för att luften skulle röra sig.

Elin kände något i bröstet släppa. Inte mycket. Men lite.

Efteråt gick hon och Lena åt sidan.

“Det där var bra”, sa Elin.

Lena såg misstänksam ut, som om beröm alltid bar på en efterfrågan.

“Det var nödvändigt.”

“Det kan vara båda.”

Lena svarade inte. Hon såg mot tavlan.

“Vi får inte göra det här till ännu en sak som bygger på att folk är lojala nog att jobba över.”

“Nej.”

“Jag menar det.”

“Jag också.”

Lena tittade på henne då, ordentligt.

“Då behöver du säga nej uppåt när någon vill lägga tillbaka det vi flyttat.”

Elin kände först impulsen att förklara hur komplicerat det var. Hur många beroenden det fanns. Hur ofta uppåt inte var en enda riktning utan ett nät av viljor, avdelningar, deadlines och halvuttalade hot om konsekvenser.

Hon sa inget av det.

“Ja”, sa hon.

Lena verkade väga svaret. Sedan nickade hon en gång.

Det var inte förtroende. Inte än.

Men kanske var det en rad i en annan sorts backlogg.

På vägen tillbaka till sitt rum fick Elin ett meddelande i pilotkanalen. Karin hade skapat en ny tråd.

**Prioriterad pilotbemanning – praktisk plan**

Under låg ett schema med namn, tider och beslutspunkter. Sofia hade redan lagt till en kommentar:

> Första standardforumet imorgon 09.00. Fokus: blockerande krav, felvägstester och runbookstruktur. Inga nya önskemål utan ägare och konsekvens.

Amir hade svarat:

> Bekräftat. Teamet pausar refaktoreringen och fokuserar på felvägar + runbook.

Sedan, några minuter senare, ytterligare en rad från honom:

> Och ja, vi tar med verkliga beroenden. Inte bara den glada vägen.

Elin läste meningen två gånger.

Det var inte en seger. Inte ens nära. Det var fortfarande risker, människor som skulle bli arga, arbete som skulle halka, krav som skulle visa sig vara otydligare än någon trodde. Om en vecka kunde allt se annorlunda ut.

Men för första gången på länge kändes beslutet inte som en grön ruta ovanpå ett rött problem.

Det kostade något.

Därför kanske det också kunde vara värt något.
