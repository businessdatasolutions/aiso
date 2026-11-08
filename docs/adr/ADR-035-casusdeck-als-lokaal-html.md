# ADR-035: Het casusdeck als lokaal HTML-bestand met een PDF-knop

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Het template uit FR-02 bestond nog niet. De gebruiker zei: "Ze leren van mij hoe ze dit als een mooi HTML document kunnen maken met een PDF download functie. Die kunnen ze dan lokaal gebruiken (geen hosting instellen)." Voor het verspreiden koos de gebruiker een openbare downloadpagina.

## Besluit

- **`materiaal/casusdeck.html`.** Eén bestand met tien dia's in 16:9, zonder bibliotheken.
  - De knop "Download als PDF" roept de printfunctie van de browser aan, met één dia per pagina.
  - De knop "Download als HTML" bewaart het bestand met de datum van vandaag in de naam. De deelnemer hoeft dan niet via "Opslaan als" te werken.
  - Bovenin staat een instructie voor de AI van de deelnemer, als commentaar in de code. De browser toont dat niet. De knop "Toon de instructie voor je AI" laat dezelfde tekst zien, zodat de deelnemer kan lezen wat de AI krijgt.
  - Onderaan staat de regel "einde casusdeck". Een klein script waarschuwt als het bestand is afgekapt, als het aantal dia's niet klopt of als een dia te vol is.
  - Kleuren en letters staan in CSS-variabelen, zodat de deelnemer de stijl kan laten aanpassen.
- **Nulmeting op papier.** De trainer print dia 1 voor de nulmeting.
- **De downloadpagina** komt in een openbare repo van Business Data Solutions, op GitHub Pages, met alleen het lege template. Eerst draait de lekcheck. Publiceren gebeurt pas na een laatste akkoord van de gebruiker.
- **In de les.** Het deckblok van dag 1 begint met voordoen. De trainer downloadt het bestand, laat de AI het invullen, opent het lokaal en maakt er een PDF van (FR-02, NFR-10).

## Overwogen alternatieven

- **PowerPoint (.pptx).** Verworpen door de gebruiker.
- **Google Slides.** Verworpen: vraagt een account, en sommige organisaties blokkeren het.
- **Een gehoste pagina per deelnemer.** Verworpen: geen hosting.
- **Verspreiden via de online omgeving van S&N of per mail.** De gebruiker koos de openbare pagina.

## Gevolgen

- **De AI van de deelnemer kan het hele bestand lezen en teruggeven.** Het risico is een afgekapt bestand. De slotregel en het nieuwe risico in deel 12 vangen dat op.
- **De PDF verschilt per browser.** Chrome, Edge en Safari moeten getest worden.
- **Een openbare link is naar buiten gericht.** Er komt alleen het lege template op, en de lekcheck draait altijd vooraf.

## Raakt

Deel 6.2, 8 (dag 1 om 15:15), 10 en 12; FR-02 en NFR-10; `materiaal/casusdeck.html`.
