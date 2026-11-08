# ADR-031: Een startpagina zonder afteller, met een tijdlijn die in beeld blijft

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

ADR-021 gaf de startpagina per lesdag een tijdlijn en een afteller per blok. NFR-06 vroeg namelijk een timer die de groep kan zien. De afteller had twee standen: "Volg de klok" en "Handmatig", met de knoppen Pauze en Opnieuw. Rechtsboven stond de klok. Een klik op een blok startte de timer voor dat blok.

Bij het proberen op het scherm bleek de kop te groot. Afteller, knoppen, klok en het blok van nu bleven altijd boven in beeld staan. Dat gold ook als de trainer naar het materiaal van een blok scrolde. De inhoud kreeg zo maar de helft van het scherm. De trainer heeft de afteller niet nodig. De tijdlijn wil hij wel steeds zien.

## Besluit

- **De afteller vervalt,** met de standen "Volg de klok" en "Handmatig", de knoppen Pauze en Opnieuw en de klok rechtsboven. NFR-06 vraagt geen timer meer: tijdblokken zijn veelvouden van 5 minuten, en de tijdlijn laat zien waar de dag staat.
- **De pagina volgt nog wel de tijd van de dag.** Het blok van nu staat bovenaan, en de tijdlijn heeft een streep op de tijd van nu. In de lijst heeft dat blok het label "Nu". Werkregel 1 verschijnt vijf minuten vóór elke pauze (FR-28). Met `?tijd=HH:MM` kan de trainer een lesdag vooraf doorlopen.
- **De kop rolt mee, de tijdlijn blijft staan.** Bovenaan staan de dag, het blok van nu, de uitkomst en het volgende blok. Scrolt de trainer naar beneden, dan ziet de groep alleen nog de tijdlijn boven de inhoud.
- **Werkregel 1 staat onder de tijdlijn,** niet meer in de kop. Zo blijft hij in beeld als de kop is weggerold.
- **Een blok in de tijdlijn is een snelkoppeling.** Een klik brengt dat blok in de lijst in beeld.
- **Bij een nieuw blok scrolt de pagina mee,** maar alleen als de kop al uit beeld is. Staat de pagina bovenaan, dan blijft de kop in beeld.

## Overwogen alternatieven

- **De afteller houden en klein maken in de vaste band.** Verworpen. De trainer heeft hem niet nodig, en elke regel die blijft staan, gaat van de inhoud af.
- **Een kop die krimpt bij scrollen.** Verworpen. Dan blijft er een donkere balk boven de inhoud staan, en de pagina wordt ingewikkelder.
- **De timer als eis houden, met een aparte app.** Verworpen door de trainer: de eis vervalt.
- **Werkregel 1 in de kop laten.** Verworpen. Na scrollen is hij dan weg, terwijl NFR-09 vraagt dat de startpagina hem vóór en tijdens de pauze toont.

## Gevolgen

- **Niemand ziet op het scherm hoeveel minuten een blok nog heeft.** De trainer bewaakt de tijd. Bij het risico "Een boardmoment loopt uit" steunt de maatregel nu op één beslispunt per moment en de tijdlijn.
- **Rond een pauze is de vaste band hoger.** Werkregel 1 en de AI-taak nemen dan twee tot vier regels in. Dat is bewust: op dat moment is die boodschap het belangrijkst. Buiten die momenten is de band één smalle strook.
- **De schaduw onder de vaste tijdlijn is een extra.** Die werkt in Chrome en Edge. In Safari en Firefox blijft de tijdlijn ook staan, zonder schaduw.
- **De pagina bewaart niets meer in de browser.** De handmatige timer gebruikte `localStorage`; die is weg.
- **ADR-021 is deels vervangen.** De map, de voorbeeldcasus, de lespagina's en de startpagina blijven. Alleen de afteller vervalt.

## Raakt

NFR-06, NFR-09; deel 5 (KISS · Begeleider); deel 12 (risico "Een boardmoment loopt uit"); `materiaal/index.html`; ADR-021.
