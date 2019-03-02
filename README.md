# Wie is de Mol gezichtsherkenning!

Is het mogelijk om de Mol te detecteren met behulp van big-data analyse en een gezichtsherkenning algoritme?

Op basis van vorige seizoenen had ik na afloop van de Mol altijd het gevoel dat ik de Mol nauwelijks had gezien in de eerste paar afleveringen. 

Tijdens het kijken van de eerste drie afleveringen van dit seizoen had ik weer het gevoel dat de montage in staat is om door middel van framing of juist het gebrek aan framing een bepaalde deelnemer wel of niet verdacht te maken. 

Mijn stelling is dan ook:
* Ik denk dat de Mol significant minder vaak, duidelijk in beeld komt in de eerste 3 afleveringen.

Deze stelling toets ik door de eerste 3 afleveringen van seizoen 2018 te analyseren, waarvan we weten wie de Mol was (Jan). 

Vervolgens neem ik de aanname dat de montage tussen vorig seizoen en het huidige seizoen soortgelijk is. En dat we daarmee dus ook de Mol van dit seizoen kunnen voorspellen op basis van enkel de eerste 3 afleveringen van dit seizoen.

## Gezichtsherkennings algoritme + big-data analyse
Dit willen we gaan doen door gebruik te maken algoritmes en big-data analyse. Een van de meest bekende gezichtsherkenning algoritme is vrij beschikbaar. Het karakteriseert het gezicht op 128 punten, zoals de vorm wenkbrauw, neus, lippen en kaaklijn: 

Hierbij als voorbeeld de karakteristieken van Jan en Merel:

Gezicht karakteristiek Jan             |  Gezicht karakteristiek Merel
:-------------------------:|:-------------------------:
![2018](img/jan_2018.jpg "jan")  |  ![2019](img/merel_2019.jpg "merel")

Via [downloadgemist.nl](http://downloadgemist.nl) is het mogelijk om afleveringen van de publieke omroep te downloaden (**EDIT**: de dag nadat deze post online kwam is dit niet meer mogelijk). Dit heb ik gedaan voor de aflevering 1-3 van seizoen 2018 en 2019. 

Als voorbereiding tonen we het algoritme 1 foto van elke deelnemer (de foto's zijn afkomstig van de WIDM website [deelnemers 2019](https://wieisdemol.avrotros.nl/home/), [deelnemers 2018](https://wieisdemol.avrotros.nl/archief/#/&filter=season:seizoen%2018%7Ccategories:kandidaten&sort=datetime:desc&page=1&layout=list)). 

Vervolgens analyseren we de afleveringen frame per frame op zoek naar gezichten en van elk gezicht dat het detecteert bekijkt het algoritme of het overeenkomt met 1 van de deelnemers.

Gezichtsherkenning shot 2018             |  Gezichtsherkenning shot 2019
:-------------------------:|:-------------------------:
![2018](img/widm_2018.gif)  |  ![2019](img/widm_2019.gif)

Hierboven zie je in een kort shot uit seizoen 2018 en seizoen 2019 hoe accuraat het algoritme is. Je kan afstellen hoe klein of groot een gezicht moet zijn voor detectie en ik heb het zodanig afgesteld dat de gezichten goed in beeld moeten zijn.

Ondanks dat het 1 van de beste vrij beschikbare algoritme is, zie je ook dat het niet in staat is om elk frame correct te interpreteren. Maar dat geeft ook niet, want we zijn niet zozeer geinteresseerd in de losse frames maar in de grote getallen. 

Hieronder zie je dan ook de percentages hoe vaak elke deelnemer ten opzichte van elkaar per aflevering in beeld komt. Neem bijvoorbeeld Sinan welke zeer vaak te zien was in aflevering 2 (bijna 25%). Maar ook hier weer, we zijn niet op zoek naar degene die vaak in beeld zijn, maar juist minder vaak.

Voorkomen deelnemers 2018 (%)             |  Voorkomen deelnemers 2019 (%)
:-------------------------:|:-------------------------:
![2018](img/widm_2018_df.png)  |  ![2019](img/widm_2019_df.png)

Wanneer we kijken naar de resultaten van seizoen 2018 zien we dan ook dat Jan daadwerkelijk minder vaak is gedetecteerd. Niet als minste, dat was Ron die er als eerste uitlag. Maar wel aan de lage kant. Laten we dat vasthouden als gegeven: de montage laat de Mol significant minder vaak in beeld, maar niet de minste. Op basis van seizoen 2018 komt de Mol op plaats 4 van minst voorkomende deelnemers.

Nu kunnen we de statistieken van seizoen 2019 ernaast leggen en bekijken wie er gemiddeld gezien over de eerste drie afleveringen minder vaak in beeld kwam. Wanneer we dan ook kijken naar degene die minder vaak in beeld kwam, maar niet als minste, dan zien we dat Merel op dezelfde plaats van voorkomen staat. 

**Dus wanneer we aannemen dat er in de montage van seizoen 2018 en 2019 ongeveer dezelfde afwegingen zijn gemaakt en onze  stelling aannemelijk is, dan denk ik dat Merel de Mol is van seizoen 2019.**

Uiteraard zou het mooi zijn om de gehele historie van WIDM te analyseren, maar de aanname dat de montage hetzelfde is door de tijd heen is minder aannemelijk. 

Daarnaast is het statistisch gezien niet uitstekend onderbouwd, maar al met al een plezierige ontspannings oefening hoe kunstmatige intelligentie, gezichtsherkenning en big-data analyses ook erg leuke toepassingen kan hebben!

De gebruikte code is open-source en staat hierbij in de repository. 
Dus heb je meer tijd, ga ook lekker aan de slag!

## Reageren?
Reacties zijn uiteraard welkom. Stuur me een email op: mattijn.vanhoek@hkv.nl
