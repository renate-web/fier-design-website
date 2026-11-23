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

## Concept 2 (in ontwikkeling)
- Concept 1 (de huidige live site) is bewaard in de branch `concept-1`.
- Concept 2 (menu: Home · Lichtontwerp · Interieurontwerp · Projecten · Over Fierdesign · Contact) staat in de map `concept-2/` en is te bekijken op https://renate-web.github.io/fier-design-website/concept-2/
  (niet vindbaar in Google: noindex). Generator: `python3 _bron/concept-2/genereer.py concept-2`.
- Concept 2 heeft een eigen kopie van `assets/` in `concept-2/assets/`; wijzigingen daar raken de live site niet.
- Wijzigingen voor concept 2 alleen in de concept-map doen, tenzij Renate vraagt om iets op de live site aan te passen.
