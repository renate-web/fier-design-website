# Werkafspraken voor Claude

## Repositories
- Gebruik voor de Fier-website (Fierdesign) **altijd** de repository `renate-web/fier-design-website`.
- `renate-web/hello-world` is alleen een testrepository.

## Publiceren
- Commit en push updates en nieuwe pagina's **altijd direct naar `main`**.
- Maak geen aparte branches of pull requests, tenzij Renate daar expliciet om vraagt.

## Taal
- Communiceer in het Nederlands.

## Opbouw van de site
- Statische HTML-site, gepubliceerd via GitHub Pages: https://renate-web.github.io/fier-design-website/
- Alle pagina's worden gegenereerd met `_bron/genereer.py` (teksten, projecten, beeldlijsten staan daarin).
  Pas teksten aan in dat script en draai: `python3 _bron/genereer.py .` — bewerk de HTML-bestanden niet los.
- Opmaak in `assets/style.css`, interactie (menu, fotowissel, lightbox) in `assets/site.js`.
- Eigen beelden staan in `assets/beeld/`; een deel van de projectfoto's wordt nog geladen vanaf de oude WordPress-site (fierdesign.nl/wp-content/uploads).

## Versies
- Sinds 23-11-2026 staat de nieuwe opzet (voorheen "concept 2") live: menu Home · Lichtontwerp · Interieurontwerp · Projecten · Over Fierdesign · Contact.
- De vorige versie (concept 1) is bewaard in de branch `concept-1` en kan altijd worden teruggezet.
- De oude adressen `diensten.html`, `opdrachtgevers.html` en `referenties.html` sturen automatisch door naar de nieuwe pagina's.
