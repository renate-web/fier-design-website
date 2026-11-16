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
- Afbeeldingen worden nu nog geladen vanaf de oude WordPress-site (fierdesign.nl/wp-content/uploads).
