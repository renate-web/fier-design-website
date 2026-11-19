#!/usr/bin/env python3
"""Genereert de statische Fierdesign-site in de map die als argument wordt meegegeven."""
import os, sys, html

UIT = sys.argv[1]
U = "https://fierdesign.nl/wp-content/uploads/"
LOGO = "assets/logo/fd-logo-kop.svg"            # compact logo uit het briefhoofd (Illustrator-huisstijl)
LOGO_LICHT = "assets/logo/fd-woordmerk-licht.svg"  # linnen woordmerk voor de zwarte voet
ICOON = "assets/logo/fd-monogram.svg"
ICOON_PNG = U + "2024/04/cropped-icon-1-192x192.png"

MENU = [
    ("index.html", "Home"),
    ("diensten.html", "Diensten"),
    ("opdrachtgevers.html", "Opdrachtgevers"),
    ("projecten.html", "Projecten"),
    ("referenties.html", "Referenties"),
    ("over-mij.html", "Over mij"),
    ("contact.html", "Contact"),
]

e = html.escape


def pagina(pad, titel, beschrijving, inhoud, actief=None):
    diepte = pad.count("/")
    r = "../" * diepte
    items = "\n".join(
        f'        <li><a href="{r}{href}"{" aria-current=\"page\"" if href == actief else ""}>{naam}</a></li>'
        for href, naam in MENU
    )
    doc = f"""<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(titel)}</title>
  <meta name="description" content="{e(beschrijving)}">
  <meta property="og:title" content="{e(titel)}">
  <meta property="og:description" content="{e(beschrijving)}">
  <link rel="icon" href="{r}{ICOON}" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{ICOON_PNG}">
  <link rel="preconnect" href="https://use.typekit.net" crossorigin>
  <link rel="stylesheet" href="https://use.typekit.net/ioi2olt.css">
  <link rel="stylesheet" href="{r}assets/style.css">
</head>
<body>
  <a class="skip" href="#inhoud">Ga naar de inhoud</a>
  <header class="kop">
    <div class="wrap">
      <a class="logo" href="{r}index.html"><img src="{r}{LOGO}" alt="Fierdesign – light &amp; interior concepts" width="147" height="48"></a>
      <button class="menuknop" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
      <nav aria-label="Hoofdmenu">
      <ul class="menu" id="menu">
{items}
      </ul>
      </nav>
    </div>
  </header>

  <main id="inhoud">
{inhoud}
  </main>

  <footer class="voet">
    <div class="wrap">
      <img class="voet__logo" src="{r}{LOGO_LICHT}" alt="" width="150" height="35">
      <div class="voet__raster">
        <div>
          <h2>Heb je een licht- of interieurvraag? Ik denk graag met je mee!</h2>
          <p>Fierdesign maakt deel uit van <a href="https://xoomlab.nl">Xoomlab.nl</a>, een coöperatie van architecten, interieurontwerpers, stedenbouwkundigen en bouwkundigen, gevestigd op het Cruquiuseiland in Amsterdam.</p>
        </div>
        <ul>
          <li><a href="mailto:renate@fierdesign.nl">renate@fierdesign.nl</a></li>
          <li><a href="tel:+31628567546">+31 (0)6 28 56 75 46</a></li>
          <li><a href="https://www.instagram.com/fierdesign_interieur/">Instagram</a></li>
          <li><a href="https://www.linkedin.com/in/renate-heeringa-popma-59689616/">LinkedIn</a></li>
        </ul>
      </div>
      <div class="voet__onder">
        <span>© 2026 Fierdesign &nbsp; KVK 34376208 &nbsp; BTW NL001449878B96</span>
        <a href="{r}algemene-voorwaarden.html">Algemene voorwaarden</a>
      </div>
    </div>
  </footer>
  <script src="{r}assets/site.js"></script>
</body>
</html>
"""
    doel = os.path.join(UIT, pad)
    os.makedirs(os.path.dirname(doel), exist_ok=True)
    with open(doel, "w", encoding="utf-8") as f:
        f.write(doc)


def alinea(t):
    return "\n".join(f"<p>{e(x)}</p>" for x in t.strip().split("\n\n"))


# ------------------------------------------------------------------ projecten
P = []  # (slug, titel, kaartbeeld, quote, tekst, resultaat, ontwerp, voor, voorna, opdrachtgever)


def proj(slug, titel, kaart, quote, tekst, resultaat, ontwerp=(), voor=(), voorna=(), doel="particulier"):
    P.append(dict(slug=slug, titel=titel, kaart=U + kaart, quote=quote, tekst=tekst,
                  resultaat=[U + x for x in resultaat], ontwerp=[U + x for x in ontwerp],
                  voor=[U + x for x in voor], voorna=[(U + a, U + b) for a, b in voorna], doel=doel))


g50 = "2026/11/{}.interieur-ontwerp-lichtplan-gezinswoning-amsterdam.jpg"
proj("jaren-50-uitbouw-gezinswoning", "Jaren ’50 uitbouw gezinswoning", g50.format(9),
     "Het kookeiland biedt ruimte voor koken én samenkomen voor het hele gezin.",
     """Deze eengezinswoning uit het midden van de jaren ’50 ligt omringd door licht, lucht en groen. Voor de eigenaren en hun drie kinderen draaide de verbouwing om één woord: balans. Op de begane grond was meer ruimte nodig, en die is gevonden in een uitbouw. Een daklicht laat extra natuurlijk licht binnen, tot diep in de woning.

In het ontwerp stond de dynamiek van het gezin centraal. Materialisering en functionaliteit moesten in evenwicht zijn. De indeling van het meubilair, het kleurenpalet en de gekozen materialen vormen samen één geheel. Het lichtplan maakt dat af: het brengt rust en evenwicht en geeft de ruimte een warme, optimale sfeer, van dag tot avond.

De keuken kreeg een royaal kookeiland met natuurstenen blad en extra zitplekken. Door het lichtplan is zowel een sfeervol als functioneel sterk beeld ontstaan.""",
     [g50.format(n) for n in (9, 7, 20, 18, 14, 12, 36, 34, 29, 28, 25, 19, 16, 4, 2)] + ["2026/11/interieur-ontwerp-amsterdam-.jpg"],
     ["2026/11/1.CONCEPT-MOODBOARD-1024x724.png", "2026/11/2.CONCEPT-INDELINGSPLAN-1024x721.png", "2026/11/2.CONCEPT-SHOPPING-1024x721.png"],
     ["2026/11/1.FUNDA-1-1.jpeg", "2026/11/2.FUNDA-1-1.jpeg", "2026/11/4.FUNDA-.jpeg"])

proj("uniek-wonen-in-een-school", "Uniek wonen in een school", "2025/07/slider-5.jpg",
     "De plafondhoge maatwerkkasten en vensterzitjes in een zachte groene tint verbinden de ruimte en halen buiten naar binnen.",
     """Deze bijzondere woonruimte bevindt zich in een voormalige school uit 1927, ontworpen door architect N. Lansdorp. De ruimte bood veel potentie dankzij het hoge plafond en veel daglicht.

Na een doordacht ontwerp voor de indeling, volgde een belangrijke volgende stap: het creëren van plafondhoge maatwerkkasten, die niet alleen veel opbergruimte bieden, maar ook bijdragen aan een rustige en samenhangende uitstraling. Door de kasten te verbinden met vensterzitjes in een zachte, groene tint, is eenheid gecreëerd én is het zicht op de groene tuin versterkt. De elektrische raambekleding van natuurlijk materiaal maakt het geheel af.

Ook de keuken kreeg een nieuwe invulling, met een royaal kookeiland en extra zitplekken. Door maatwerk en zorgvuldige kleurkeuzes is een functionele, sfeervolle en rustgevende leefruimte ontstaan.""",
     ["2025/07/slider-5.jpg"] + [f"2025/07/543A{n}-Verbeterd-NR{s}.jpg" for n, s in
      (("8679", "_zonder-lampen"), ("8688", ""), ("8683", ""), ("8661", "-1"), ("8742", ""), ("8884", ""), ("8674", ""),
       ("8670", "2"), ("8663", ""), ("8835", ""), ("8759", ""), ("8925", ""), ("8953", "-1"))],
     ["2025/07/2-1.jpg", "2025/07/1.KLEUROPTIE-_-HUISMANHOF-1.jpg", "2025/07/2.Maat-indicatie-perspectief-1.jpg",
      "2025/07/3A-1.jpg", "2025/07/3B-1.jpg", "2025/07/4B-1.jpg", "2025/07/5A-1.jpg", "2025/07/5C-1.jpg", "2025/07/5D-1.jpg"],
     ["2025/07/keuken_voor.jpg", "2025/07/raam_voor.jpg", "2025/07/IMG_7003.jpg", "2025/07/IMG_7060-scaled.jpg",
      "2025/07/IMG_7171.jpg", "2025/07/IMG_7469.jpg"])

ch = "2025/07/chiela-fierdesign-27mei-hogeresolutie{}.jpg"
proj("maatwerk-en-karakter-in-split-level-woning", "Maatwerk en karakter in een split-level woning", "2025/07/chiela-fierdesign-27mei-hogeresolutie28-1.jpg",
     "Door de ruimtes opnieuw in te delen, hebben alle functies een eigen plek gekregen.",
     """Deze totaalrenovatie had een aantal specifieke wensen: ruimte voor thuiswerken, eigenheid en een warme sfeer. Thuiswerken is niet meer weg te denken, maar hoe creëer je een werkplek zonder dat dit het gezinsleven verstoort?

Voor het indelingsplan is er flink gepuzzeld. Al snel bleek een grondige herinrichting noodzakelijk. Door de ruimtes opnieuw in te delen, hebben alle functies een eigen plek gekregen. Maatwerk en authentieke materialen, zoals massief eiken vloeren en deuren, zorgen voor een warme en karaktervolle uitstraling. Prachtige structuurtegels hebben in de badkamer kleur en relief gebracht.

In de master bedroom is een roomdivider geplaatst, waardoor een walk-in closet is ontstaan. De ruimte blijft als geheel voelbaar, maar krijgt tegelijkertijd rust en structuur. De glazen wand in de woonkamer biedt een afsluitbare werkplek zonder verlies van ruimtelijkheid en daglicht.

Het lichtplan vormt de kers op de taart: functionele verlichting is gecombineerd met eyecatchers, waardoor elke verdieping en ruimte sfeervol is verlicht.""",
     ["2025/07/chiela-fierdesign-27mei-hogeresolutie28-1.jpg"] + [ch.format(n) for n in (37, 29, 26, 36, 35, 30, 41, 60, 55, 56, 48, 49, 50, 3, 2, 6, 7, 63)],
     ["2025/07/2.1-2.jpg", "2025/07/2.5-1.jpg", "2025/07/4.1-1.jpg", "2025/07/4.2-1-1.jpg", "2025/07/4.4-1.jpg",
      "2025/07/6A-1.jpg", "2025/07/6B-1.jpg", "2025/07/6C-1.jpg", "2025/07/6E-1.jpg", "2025/07/3.3-1.jpg", "2025/07/3.2-1.jpg"],
     ["2025/07/keuken_voorA.jpg", "2025/07/woonkamer_voor_A.jpg", "2025/07/woonkamer_voor2b.jpg",
      "2025/07/IMG_4246-scaled.jpg", "2025/07/IMG_4806.jpg", "2025/07/IMG_5523.jpg"])

proj("jaren-30-in-een-nieuw-jasje", "Jaren ’30 in een nieuw jasje", "2025/03/1.jarendertig-interieurontwer-kleur-maatwerk-1920x1072.jpeg",
     "Een zacht kleurpalet en doordacht lichtplan accentueren de jaren ’30-details en creëren een eigentijdse, warme ambiance.",
     """Dit karakteristieke jaren ’30-huis was toe aan meer eigenheid en sfeer. De basisindeling was prettig, maar de ruimtes misten samenhang en er was geen duidelijke plek voor spullen.

Door de functies van de ruimtes helder te definiëren, ontstond een logische en open indeling. Een zacht kleurpalet benadrukt de authentieke jaren ’30-details en legt tegelijkertijd een natuurlijke verbinding met de tuin. De keuken werd uitgebreid met een maatwerk bar en kast, waarbij de groene tint het geheel samenbrengt en karakter geeft.

Het opvallende behang in de leefkeuken en het zorgvuldig ontworpen lichtplan zorgen samen voor een sfeervolle beleving in elke hoek van de ruimte. De mix van richtbare spots en unieke armaturen creëert een eigentijdse, warme ambiance.

In de living zorgt een op maat gemaakte wandkast met geïntegreerde werkplek voor een praktische én stijlvolle oplossing. Zo is er nu een fijne plek om te spelen en te werken, mét volop opbergruimte.""",
     ["2025/03/1.jarendertig-interieurontwer-kleur-maatwerk-scaled.jpeg", "2025/07/IMG_2435.jpg", "2025/07/IMG_2408-scaled.jpg",
      "2025/07/IMG_2403-scaled.jpg", "2025/07/IMG_2412-scaled.jpg"],
     ["2025/07/1.START_.jpg", "2025/07/2.START_.jpg", "2025/07/3.START_.jpg", "2025/07/4.START_.jpg", "2025/07/5.START_.jpg",
      "2025/07/6.START_.jpg", "2025/07/3.1-.jpg", "2025/07/3.2-2.jpg", "2025/07/3.3-2.jpg", "2025/07/4.1-2.jpg", "2025/07/4.2.jpg",
      "2025/07/5.1.jpg", "2025/07/5.2.jpg", "2025/07/5.3.jpg", "2025/07/6.1.jpg", "2025/07/7.2.jpg", "2025/07/7.3.jpg",
      "2025/07/9.7.jpg", "2025/07/9.8.jpg", "2025/07/1-1.jpg", "2025/07/1A.jpg", "2025/07/1B.jpg", "2025/07/1C.jpg"],
     ["2025/07/Schermafbeelding-2019-05-10-om-12.21.24.jpg", "2025/07/Schermafbeelding-2019-05-10-om-12.22.06.jpg",
      "2025/07/Schermafbeelding-2019-05-10-om-12.22.34.jpg", "2025/07/Schermafbeelding-2019-05-10-om-12.22.45.jpg",
      "2025/07/PHOTO-2023-03-07-10-38-36.jpg", "2025/07/PHOTO-2023-03-14-15-03-40.jpg", "2025/07/PHOTO-2023-03-27-16-40-46.jpg"])

ek = "2024/{}/{}Amsterdam-Ertskade-by-Lilian-{}.jpg"
proj("functionele-blikvanger", "Functionele blikvanger", "2024/07/1.-Amsterdam-Ertskade-by-Lilian-5-v2.jpg",
     "Optimale gebruiksfunctie in een sfeervolle ruimte.",
     """In een prachtige ruime woning kreeg ik de vraag over de inrichting van een ‘tussenruimte’. Deze architectonisch interessante ruimte met veel daglicht was in de praktijk een doorloop die makkelijk rommelig werd. Door het ontwerpproces stapsgewijs te doorlopen kwamen de smaken van de eigenaren samen en zijn hele goede keuzes gemaakt.

De werkplek en kast zijn op maat gemaakt door een meubelmaker en samen hebben we het juiste vloerkleed, verlichting en meubels weten te vinden. De tussenruimte is een prachtige plek geworden die door de hele familie (en huisdieren) optimaal gebruikt wordt.""",
     [ek.format("07", "", 6), ek.format("04", "1.-", "5-v2"), ek.format("04", "", 4), ek.format("04", "", 7), ek.format("07", "", 8)],
     ["2024/07/5M.jpg", "2024/07/6M-1-1024x684.jpg", "2024/07/10.LAYERED-LICHT-VB-OPTIE-2.jpg", "2024/07/7.LICHTPLAN.jpg", "2024/07/8.ARMANTUREN.jpg"])

jv = "2024/04/{}Amsterdam-Jan-Vrijman-by-Lilian-{}.jpg"
proj("kleur-in-nieuwbouw", "Kleur in nieuwbouw", jv.format("", 21),
     "Handbewerkte materiaaltechnieken en warme kleurtinten brengen leven in het huis.",
     """Het interieur van deze bijzondere woning had een eigen gezicht nodig. Bestaande elementen waren mooi, maar er was behoefte aan warmte. Stapsgewijs heb ik de eigenaren meegenomen in het proces van kleur- en materiaalkeuzes. Door het ontwerp driedimensionaal te tekenen kwamen de mogelijkheden tot leven en werd het makkelijker om keuzes te maken.

Door handbewerkte materiaaltechnieken toe te passen (beton ciré op wand en vloer) en warme kleurtinten toe te voegen is er leven in het huis gekomen. Ook het lichtplan heeft veel toegevoegd aan het geheel. Doordat ik ook de uitvoering mocht begeleiden, kon ik de opdrachtgever adviseren over de afwerkingsdetails en bespaarde ik hen veel tijd.""",
     [jv.format("", 21), jv.format("", 15), jv.format("1.", 8), jv.format("", 12), jv.format("3.", 25), jv.format("2.", 7),
      jv.format("", 18), jv.format("5.", 2), jv.format("4.", 26), jv.format("", 14), jv.format("", 13)],
     ["2024/04/2-THEMA-1-1024x699.jpg", "2024/04/2A.-VLEKKENPLAN-1-1024x699.jpg", "2024/04/2A1.-LICHTPUNTEN-1-1024x698.jpg",
      "2024/04/2B.-LICHTZONES-1-1024x698.jpg", "2024/04/6A.-PLAN-LAYERED-1-1024x699.jpg", "2024/04/6B-PL-1-1-1024x699.jpg",
      "2024/12/Kleur-in-nieuwbouw.png"],
     ["2024/04/IMG_3820-scaled.jpg", "2024/04/IMG_4258-scaled.jpg", "2024/04/IMG_4520-scaled.jpg", "2024/04/IMG_4330-scaled.jpg"])

lo = "2026/11/{}.png"
proj("loft-aan-het-water", "Loft aan het water", "2026/11/1.LOFT_-7.png",
     "Ruimtelijkheid creëren en een optimale lichtbeleving realiseren binnen een compacte ruimte.",
     """Dit nieuwbouwappartement ligt op een prachtige locatie aan het water in Amsterdam. Bij de aankoop waren al veel keuzes gemaakt, maar rond de oplevering begon de klant te twijfelen. Hij miste richting en overzicht om de juiste beslissingen te nemen.

Stap voor stap hebben we zijn wensen besproken. Een helder interieurplan maakte het eenvoudiger om keuzes te maken, zoals de materialen en kleuren voor de keuken, de badkamer en de vloer. Het lichtplan maakt het geheel af, zowel esthetisch als functioneel.

Het licht- en interieurconcept ‘Scandinavian Loft’ draait om licht, luxe en ruimtelijkheid binnen een compacte ruimte. Een helder Scandinavisch palet van wittinten, licht hout en zachte natuurtinten versterkt het daglicht en brengt rust. Dankzij een open indeling, multifunctionele meubels en subtiel luxe materialen ontstaat een luchtige, elegante leefruimte die groots aanvoelt, ondanks het beperkte oppervlak.

Overdag krijgt het daglicht alle ruimte, ’s avonds zorgen gelaagde, dimbare lichtbronnen in warm wit voor rust en sfeer. Functioneel licht waar nodig, sfeerlicht waar het mag: licht, eerlijk en tijdloos.""",
     [lo.format(x) for x in ("1.LOFT_-7", "1.LOFT_-4-1024x680", "4LOFT-3", "3.LOFT_-4", "9.LOFT_-3", "7.LOFT_-3", "6.LOFT_-3", "5.LOFT_-3", "8.LOFT_-3")],
     [lo.format(x) for x in ("1.LOFT-LICHT", "2.LOFT-LICHT", "3.LOFT-LICHT")])

kp = "2024/08/{}.jpg"
proj("wonen-in-een-kapel", "Wonen in een kapel", "2024/08/header_img_kerk-1920x1112.jpg",
     "In het oog springende armaturen geven de ruimte nog meer warmte.",
     """Deze voormalige kapel was al omgebouwd tot een prachtige woonruimte met een strakke witte keuken. Voor de nieuwe eigenaar heb ik een ontwerp gemaakt met veel aandacht voor licht en warmte en een persoonlijke touch.

Door een prachtig behang met een natuurlijk tafereel toe te voegen is er sfeer, diepte en warmte in de keuken gekomen. Met het lichtplan is door het hele huis zowel functioneel licht als sfeerlicht toegevoegd. Met prachtige eyecatching armaturen heeft iedere ruimte de aandacht gekregen die het verdient en komt de originele architectuur nog beter tot zijn recht.""",
     [kp.format(x) for x in ("header_img_kerk", "IMG_3027-1", "IMG_2976-1", "1-1", "IMG_2990-1", "2-1", "3-1", "IMG_2978-1", "IMG_3018", "IMG_2996-1", "IMG_3010")],
     [kp.format(x) for x in ("2A.-CONCEPT", "4B1", "4C", "5A1", "5B", "5C-2", "6A", "6B", "6C", "6D", "6E", "6F", "6G", "6H")],
     [kp.format("1.VOOR_")])

dz = "2024/04/{}.jpg"
proj("duurzaam-en-elegant-verbouwen", "Duurzaam en elegant verbouwen", "2024/04/IMG_8570-scaled.jpg",
     "Tijdloze elegantie met een zorgvuldig gekozen kleurenpalet en verfijnde materialen.",
     """Deze woning uit de jaren ’30 was een voormalige kantoorruimte en toe aan een upgrade. De woning is niet groot, maar door een muur door te breken is het indelingsplan met een open keuken heel ruimtelijk gaan werken. Duurzame keuzes (isolatie, zonnepanelen en vloerverwarming) hebben het huis futureproof gemaakt.

Het natuurstenen keukenblad was richtinggevend voor het kleurenpalet. Samen met het lichtplan, de vele afwerkingsdetails en de visgraatvloer is de ruimte heel smaakvol geworden. Dit interieur straalt een tijdloze elegantie uit met zijn zorgvuldig gekozen kleurenpalet en verfijnde materialen.""",
     [dz.format(x) for x in ("IMG_8570-scaled", "IMG_7784-scaled", "IMG_8567-scaled", "IMG_8548-scaled", "IMG_8586-scaled",
                             "IMG_8549-2-scaled", "IMG_8542-1-scaled", "IMG_8642-1-scaled", "IMG_7786-scaled")],
     [dz.format(x) for x in ("1.DEF-.LICHT-ELECTRAPLAN-_-JB-STR.-HARLINGEN-1", "2-ELECTRAPLAN-1", "3.JB-BOVENAANZICHT-VOOR-1",
                             "4.keuken-1", "5.LICHTPLAN-1", "47")],
     [dz.format(x) for x in ("IMG_6515-scaled", "IMG_6518-1-scaled", "IMG_6925-1-scaled", "IMG_7133-scaled", "IMG_7134-scaled", "IMG_7142-scaled")],
     doel="zakelijk")

ff = "2024/12/{}.jpg"
proj("vakantiehuisje-in-de-duinen", "Vakantiehuisje in de duinen", "2024/12/flierefluiter_featured_image-1.jpg",
     "Door originele elementen beter tot hun recht te laten komen in kleur- en materiaalgebruik, is er een sfeervol en gezellig interieur ontstaan.",
     """Het verouderde interieur van het vakantiehuisje was toe aan een update. Ik heb een concept uitgewerkt met een kleuren- en materiaalplan, voor een warm en gezellig vakantiehuis.

Na goedkeuring van de plannen mocht ik aan de slag met de realisatie, zowel de verbouwing als het aanschaffen van de meubels en lampen. Omdat het huisje verhuurd wordt, was het van belang dat naast kwaliteit en design, de inrichting ook tegen een stootje kan.""",
     [ff.format(x) for x in ("flierefluiter_header", "Flierefluiter-05102024-YRHE-14", "Flierefluiter-05102024-YRHE-04",
                             "Flierefluiter-05102024-YRHE_4-1", "Flierefluiter-05102024-YRHE-25b", "Flierefluiter-05102024-YRHE-30",
                             "Flierefluiter-05102024-YRHE_7", "Flierefluiter-05102024-YRHE-12", "Flierefluiter-05102024-YRHE_9",
                             "Flierefluiter-05102024-YRHE-28", "Flierefluiter-05102024-YRHE-05")],
     [ff.format("Flierefluiter_1B")],
     [ff.format(x) for x in ("IMG_0737", "IMG_9705", "IMG_0680", "IMG_0749", "IMG_6165")],
     [(ff.format("woonkamer_voor2-1"), ff.format("woonkamer_na2-1")), (ff.format("raamkant_voor"), ff.format("raamkant_na"))],
     doel="zakelijk")

hg = "2024/04/Amsterdam-Hengelstraat-by-Lilian-{}.jpg"
proj("gezinswoning-met-smaak", "Gezinswoning met smaak", "2024/04/IMG_7433-scaled.jpg",
     "De mix van natuurlijke elementen en moderne accenten zorgt voor een smaakvol geheel.",
     """De gezinswoning was toe aan een nieuw gezicht, maar waar begin je dan? Bij de aankoop van ons nieuwe huis dachten we gaandeweg te gaan verbouwen. Wel hadden we een extra slaapkamer nodig en de badkamer en keuken waren niet onze smaak. Na wat onderzoek hebben we besloten de verbouwing meteen goed aan te pakken: slopen, verduurzamen en optimale functionaliteit voor een gezin van 5 personen.

Omdat het een jaren ’90 architectonische bouwstijl is, met strakke lijnen, hebben we bewust natuurlijke elementen toegevoegd in wand- en vloerafwerking. De keuken is verplaatst voor zoveel mogelijk natuurlijke lichtinval. De mix van natuurlijke elementen en moderne accenten zorgt samen met het lichtplan en een verfijnd kleurenschema voor een rustgevende en uitnodigende sfeer. Het resultaat is mede door de fijne aannemer helemaal naar tevredenheid uitgepakt.""",
     ["2024/04/IMG_7433-scaled.jpg"] + [hg.format(x) for x in ("9", "2", "21-v3", "25", "10a", "15", "18-v2-1")] +
     ["2024/04/IMG_7432-scaled.jpg", "2024/04/IMG_8189-scaled.jpg", "2024/04/IMG_7442-scaled.jpg"],
     [],
     ["2024/04/IMG_5183-scaled.jpg", "2024/04/IMG_4780-scaled.jpg", "2024/04/IMG_5386-scaled.jpg",
      "2024/04/IMG_3738-rotated.jpeg", "2024/04/IMG_3730-rotated.jpeg", "2024/04/IMG_4623-1.jpeg", "2024/04/006A.jpeg"])

PS = {p["slug"]: p for p in P}


def galerij(beelden, titel):
    knoppen = "\n".join(
        f'<button type="button" data-groot="{b}"><img src="{b}" alt="{e(titel)}, foto {i + 1}" loading="lazy" decoding="async"></button>'
        for i, b in enumerate(beelden))
    return f'<div class="galerij">\n{knoppen}\n</div>'


for p in P:
    blokken = [f"""  <section class="sectie" aria-labelledby="resultaat">
    <div class="wrap">
      <h2 id="resultaat">Het resultaat</h2>
      {galerij(p['resultaat'][1:] or p['resultaat'], p['titel'])}
    </div>
  </section>"""]
    if p["voorna"]:
        paren = "\n".join(
            f'<figure><img src="{v}" alt="{e(p["titel"])}: voor" loading="lazy"><figcaption>Voor</figcaption></figure>'
            f'<figure><img src="{n}" alt="{e(p["titel"])}: na" loading="lazy"><figcaption>Na</figcaption></figure>'
            for v, n in p["voorna"])
        blokken.append(f"""  <section class="sectie sectie--diep" aria-labelledby="voorna">
    <div class="wrap">
      <h2 id="voorna">Voor en na</h2>
      <div class="voorna">{paren}</div>
    </div>
  </section>""")
    if p["ontwerp"]:
        blokken.append(f"""  <section class="sectie sectie--diep" aria-labelledby="ontwerp">
    <div class="wrap">
      <h2 id="ontwerp">Uit het ontwerpproces</h2>
      <p class="tekst">Concept, moodboards, indelings- en lichtplannen: zo kwam het ontwerp stap voor stap tot stand.</p>
      {galerij(p['ontwerp'], p['titel'] + ' – ontwerp')}
    </div>
  </section>""")
    if p["voor"]:
        blokken.append(f"""  <section class="sectie" aria-labelledby="voor">
    <div class="wrap">
      <h2 id="voor">Voor en tijdens de verbouwing</h2>
      {galerij(p['voor'], p['titel'] + ' – voor')}
    </div>
  </section>""")
    inhoud = f"""  <article>
  <header class="projectkop">
    <img src="{p['resultaat'][0]}" alt="{e(p['titel'])}" fetchpriority="high">
    <div class="wrap">
      <a class="terug" href="../projecten.html">← Alle projecten</a>
      <h1>{e(p['titel'])}</h1>
    </div>
  </header>
  <section class="sectie">
    <div class="wrap twee">
      <div class="tekst">{alinea(p['tekst'])}</div>
      <blockquote class="citaat">{e(p['quote'])}</blockquote>
    </div>
  </section>
{chr(10).join(blokken)}
  </article>"""
    pagina(f"projecten/{p['slug']}.html", f"{p['titel']} – Fierdesign", p["tekst"].split(".")[0] + ".", inhoud, "projecten.html")


def kaarten(slugs, r=""):
    return "\n".join(
        f'<a class="kaart" href="{r}projecten/{s}.html"><img src="{PS[s]["kaart"]}" alt="" loading="lazy"><span>{e(PS[s]["titel"])}</span></a>'
        for s in slugs)


pagina("projecten.html", "Projecten – Fierdesign", "Licht- en interieurontwerpen van Fierdesign: woningen, verbouwingen en verhuurpanden.",
       f"""  <section class="paginakop"><div class="wrap">
    <h1>Projecten</h1>
    <p>Van een uitbouw uit de jaren ’50 tot wonen in een kapel: een selectie van licht- en interieurontwerpen.</p>
  </div></section>
  <section class="sectie" style="padding-top:0"><div class="wrap raster">
{kaarten([p['slug'] for p in P])}
  </div></section>""", "projecten.html")

# ------------------------------------------------------------------ home
SLIDES = ["2025/07/slider-7.jpg", "2025/07/slider-5.jpg", "2025/07/slider-10.jpg", "2025/07/slider-9.jpg",
          "2025/07/slider-8.jpg", "2024/07/slider-2.jpg", "2024/07/slider-4.jpg"]
slides = "\n".join(
    f'<img src="{U + s}" alt=""{" class=\"zichtbaar\" fetchpriority=\"high\"" if i == 0 else " loading=\"lazy\""}>'
    for i, s in enumerate(SLIDES))

pagina("index.html", "Fierdesign – Licht- & interieurontwerp", "Licht- en interieurontwerp, stijlvol en doordacht: lichtontwerp dat daglicht en kunstlicht samenbrengt, en een persoonlijk interieur. Amsterdam.",
       f"""  <section class="hero" aria-labelledby="hero-titel">
    <div class="hero__tekst">
      <h1 id="hero-titel">Licht- en interieurontwerp, stijlvol en doordacht</h1>
      <p>Een lichtplan, een interieurontwerp of beide, voor je woning of bedrijfsruimte.</p>
      <p style="margin-top:.5rem"><a class="knop" href="contact.html">Plan een kennismaking</a></p>
    </div>
    <div class="hero__beeld">
{slides}
    </div>
  </section>

  <section class="sectie" id="interieur">
    <div class="wrap twee">
      <div class="tekst" id="lichtontwerp">
        <h2><span class="kenmerk kenmerk--licht" aria-hidden="true"></span>Lichtontwerp</h2>
        <p>Licht bepaalt niet alleen wat je ziet, maar ook wat je voelt. Het versterkt de beleving en emotie van een interieur. Tijdens het realiseren van verschillende interieurontwerpen ontdekte ik hoe essentieel licht is.</p>
        <p>Daarom ben ik me verder gaan verdiepen in lichtontwerp. Na diverse opleidingen combineer ik nu licht- en interieurontwerp. Met een doordachte balans tussen daglicht en kunstlicht creëert Fierdesign sfeer én functionaliteit, zowel binnen als buiten, met aandacht voor techniek, esthetiek en budget. Een goed lichtplan bespaart aanpassingen en oponthoud tijdens de bouw en zorgt ervoor dat de sfeer die je voor ogen had, ook precies zo wordt gerealiseerd.</p>
        <a class="lees" href="diensten.html#lichtontwerp">Zo werkt lichtontwerp</a>
      </div>
      <div class="tekst">
        <h2><span class="kenmerk kenmerk--interieur" aria-hidden="true"></span>Interieurontwerp</h2>
        <p>Bij Fierdesign sta jij als opdrachtgever op de eerste plaats: op basis van jouw wensen ontwerp ik je interieur, samen zetten we je eigen stijl neer. Dat kan een groot, maar ook een klein vraagstuk zijn.</p>
        <p>Het proces naar het uiteindelijke ontwerp is minstens zo belangrijk als het resultaat. Met een helder stappenplan doorlopen we het proces naar jouw nieuwe interieur bij zowel residentiële als zakelijke ruimtes. Ik luister goed naar je wensen en vertaal dit naar een persoonlijk, functioneel én mooi ontwerp. Ook help ik je graag met de realisatie van het interieur, samen met mijn netwerk van professionals.</p>
        <a class="lees" href="diensten.html#interieurontwerp">Zo werkt interieurontwerp</a>
      </div>
    </div>
    <div class="wrap" style="margin-top:5rem">
      <blockquote class="citaat">Goed licht brengt sfeer en functionaliteit samen.</blockquote>
    </div>
  </section>

  <section class="sectie sectie--diep" aria-labelledby="voorwie">
    <div class="wrap">
      <h2 id="voorwie">Voor wie ik werk</h2>
      <div class="twee">
        <div class="tekst">
          <h3>Particulier</h3>
          <p>Van verbouwing tot nieuwbouwwoning of een ruimte die niet lekker werkt: we creëren een interieur dat bij je past, goed doordacht is en een eigen karakter heeft.</p>
          <a class="lees" href="opdrachtgevers.html#particulier">Meer voor particulieren</a>
        </div>
        <div class="tekst">
          <h3>Zakelijk</h3>
          <p>Bedrijven, verhuurwoningen, vakantiehuizen of werkplekken die er goed uitzien, prettig voelen en tegen een stootje kunnen.</p>
          <a class="lees" href="opdrachtgevers.html#zakelijk">Meer voor bedrijven</a>
        </div>
      </div>
    </div>
  </section>

  <section class="sectie" aria-labelledby="recent">
    <div class="wrap">
      <h2 id="recent">Recente projecten</h2>
      <div class="raster">
{kaarten(['jaren-50-uitbouw-gezinswoning', 'uniek-wonen-in-een-school', 'maatwerk-en-karakter-in-split-level-woning'])}
      </div>
      <p style="margin-top:2rem"><a class="lees" href="projecten.html">Bekijk alle projecten</a></p>
    </div>
  </section>""", "index.html")

# ------------------------------------------------------------------ diensten
LICHTBEELDEN = [
    ("lichtplan-2-moodboard.jpg", "Moodboard met keukenverlichting, wandlampen, een hanglamp en traptreden met licht"),
    ("lichtplan-3-lichtplan.jpg", "Lichtplan op de plattegrond met de gekozen armaturen L01 tot en met L09"),
    ("lichtplan-4-schakelplan.jpg", "Schakelplan met schakelgroepen en bedieningspunten"),
]
lichtwissel = (
    '        <div class="wissel" aria-label="Voorbeelden uit een lichtplan">\n'
    + "\n".join(
        f'          <button type="button" class="wissel__beeld{" zichtbaar" if i == 0 else ""}" data-groot="assets/beeld/{f}">'
        f'<img src="assets/beeld/{f}" alt="{e(alt)}"{"" if i == 0 else " loading=\"lazy\""}></button>'
        for i, (f, alt) in enumerate(LICHTBEELDEN))
    + '\n          <div class="wissel__stippen" aria-hidden="true">'
    + "".join("<span></span>" for _ in LICHTBEELDEN)
    + '</div>\n        </div>')

pagina("diensten.html", "Diensten: lichtontwerp en interieurontwerp – Fierdesign",
       "Lichtontwerp en interieurontwerp volgens een helder stappenplan, van kennismaking tot oplevering.",
       f"""  <section class="paginakop"><div class="wrap">
    <h1>Diensten</h1>
    <p>Een lichtplan, een interieurontwerp of beide: stijlvol en doordacht, voor je woning of bedrijfsruimte.</p>
  </div></section>

  <section class="sectie sectie--avond" id="lichtontwerp" aria-labelledby="lo-titel">
    <div class="wrap">
      <div class="twee twee--beeld">
        <div class="tekst">
          <h2 id="lo-titel"><span class="kenmerk kenmerk--licht" aria-hidden="true"></span>Lichtontwerp</h2>
          <p>Licht bepaalt niet alleen wat je ziet, maar ook wat je voelt. Met een doordachte balans tussen daglicht en kunstlicht creëert Fierdesign sfeer én functionaliteit, binnen en buiten, met aandacht voor techniek, esthetiek en budget.</p>
          <p>Een lichtplan maak je het best vroeg, vóór de installateur de leidingen trekt. Dat bespaart aanpassingen en oponthoud tijdens de bouw, en zorgt dat de sfeer die je voor ogen had ook precies zo wordt gerealiseerd. Ik werk daarbij graag samen met je architect, aannemer en installateur.</p>
        </div>
{lichtwissel}
      </div>

      <h3 style="margin-top:4rem">Het stappenplan voor een lichtplan</h3>
      <ol class="stappen stappen--vier">
        <li><h3>Plattegrond</h3><p>We kijken naar de indeling van de ruimte. Het startpunt is een gedetailleerde plattegrond op schaal.</p></li>
        <li><h3>Schets en vlekkenplan</h3><p>Ik analyseer de ruimte en maak met jouw input een schetsmatig lichtplan. Het schetsontwerp vertaalt je wensen, en er is ruimte voor overleg.</p></li>
        <li><h3>Lichtplan en presentatie</h3><p>Het lichtplan wordt uitgewerkt, zodat je een goed beeld krijgt van hoe het licht beleefd gaat worden. De gekozen armaturen breng ik in overzicht.</p></li>
        <li><h3>Offerte en realisatie</h3><p>Na goedkeuring van het lichtplan volgt een passende offerte. Na je akkoord verzorgen we de levering en ondersteunen we je bij eventuele vragen.</p></li>
      </ol>
      <p style="margin-top:3rem"><a class="knop" href="contact.html">Vraag een lichtplan aan</a></p>
    </div>
  </section>

  <section class="sectie" id="interieurontwerp" aria-labelledby="io-titel">
    <div class="wrap">
      <div class="twee twee--beeld">
        <div class="tekst">
          <h2 id="io-titel"><span class="kenmerk kenmerk--interieur" aria-hidden="true"></span>Interieurontwerp</h2>
          <p>Bij Fierdesign sta jij als opdrachtgever op de eerste plaats. Op basis van jouw wensen ontwerp ik je interieur, en samen zetten we je eigen stijl neer. Dat kan een groot of juist een klein vraagstuk zijn, voor je woning of je bedrijfsruimte.</p>
          <p>Ik luister goed naar je wensen en vertaal die naar een persoonlijk, functioneel én mooi ontwerp. Met 3D-tekeningen zie je vooraf hoe het wordt, zodat kiezen makkelijker wordt. Ook help ik je graag met de realisatie, samen met mijn netwerk van professionals.</p>
          <h3 style="margin-top:2rem;margin-bottom:.75rem">Fierdesign en Xoomlab</h3>
          <p>Voor grotere verbouwingsplannen, zoals een uitbouw of het aanpassen van de indeling en constructie van je woning, biedt Fierdesign extra mogelijkheden dankzij de samenwerking binnen Xoomlab. Hierdoor kunnen we ook verder kijken dan het interieur alleen. Denk aan het uitwerken van constructieve tekeningen en begeleiding bij vergunningaanvragen. Zo komen interieur, architectuur en techniek samen in één goed doordacht plan.</p>
          <p><a href="https://xoomlab.nl">Xoomlab</a> is een coöperatie van architecten, interieurontwerpers, stedenbouwkundigen en bouwkundigen, gevestigd op het Cruquiuseiland in Amsterdam.</p>
        </div>
        <img src="{U}2025/07/chiela-fierdesign-27mei-hogeresolutie37.jpg" alt="Interieur met maatwerk in een split-level woning" loading="lazy" class="beeld--lager">
      </div>
      <h3 style="margin-top:4rem">Het stappenplan voor interieurontwerp</h3>
      <ol class="stappen">
        <li><h3>Kennismaking</h3><p>We bespreken je wensen, je manier van leven, de ruimte en je budget, het liefst bij jou ter plekke.</p></li>
        <li><h3>Concept en moodboard</h3><p>Een eerste richting voor sfeer, kleur en materiaal, als basis voor alle keuzes die volgen.</p></li>
        <li><h3>Indelingsplan</h3><p>Functies, looproutes en meubelopstelling: elke plek krijgt een logische plaats. Maatwerk teken ik waar het nodig is.</p></li>
        <li><h3>Materialisatie en kleur</h3><p>Vloeren, wanden, tegels en kleuren, uitgewerkt in 3D-tekeningen, zodat je het eindbeeld al ziet.</p></li>
        <li><h3>Definitief ontwerp</h3><p>Tekeningen, maatwerkdetails en een overzicht met meubels, lampen en materialen, klaar voor offertes.</p></li>
        <li><h3>Realisatie</h3><p>Ik breng je in contact met vakmensen uit mijn netwerk, stem af op de bouw en adviseer over de afwerkingsdetails.</p></li>
      </ol>
    </div>
  </section>""", "diensten.html")

# ------------------------------------------------------------------ opdrachtgevers (voorbeeldteksten)
pagina("opdrachtgevers.html", "Opdrachtgevers: particulier en zakelijk – Fierdesign",
       "Licht- en interieurontwerp voor particulieren en bedrijven: woningen, verbouwingen, verhuurwoningen en werkplekken.",
       f"""  <!-- Voorbeeldteksten: nog door Renate aan te passen -->
  <section class="paginakop"><div class="wrap">
    <h1>Opdrachtgevers</h1>
    <p>Ik werk voor mensen die thuis willen wonen zoals het bij ze past, en voor bedrijven die een ruimte willen die werkt en indruk maakt.</p>
  </div></section>

  <div class="wrap" style="padding-bottom:5rem">
    <section class="doelgroep" id="particulier" aria-labelledby="part-titel">
      <div class="twee twee--beeld">
        <div class="tekst">
          <h2 id="part-titel">Particulier</h2>
          <p>Je gaat verbouwen, je hebt een nieuwbouwhuis gekocht of er is die ene ruimte die maar niet lekker werkt. Waar begin je? Samen brengen we rust in de keuzes. Ik luister naar hoe jij woont en vertaal dat naar een ontwerp dat persoonlijk, praktisch en mooi is.</p>
          <ul>
            <li>Totaalrenovatie, uitbouw of nieuwbouw</li>
            <li>Keuken, badkamer of één ruimte</li>
            <li>Kleur- en materiaaladvies, maatwerk en 3D-tekeningen</li>
            <li>Lichtplan voor binnen en buiten</li>
            <li>Begeleiding van de uitvoering, met vakmensen uit mijn netwerk</li>
          </ul>
          <p>Jij houdt de regie zo veel als je wilt: van een adviesgesprek tot volledige begeleiding van de verbouwing.</p>
          <a class="lees" href="projecten/jaren-50-uitbouw-gezinswoning.html">Bekijk: Jaren ’50 uitbouw gezinswoning</a>
        </div>
        <img src="{U}2026/11/7.interieur-ontwerp-lichtplan-gezinswoning-amsterdam.jpg" alt="Gezinswoning met kookeiland en lichtplan" loading="lazy">
      </div>
    </section>

    <section class="doelgroep" id="zakelijk" aria-labelledby="zak-titel">
      <div class="twee twee--beeld">
        <div class="tekst">
          <h2 id="zak-titel">Zakelijk</h2>
          <p>Een ruimte die goed is ingericht en goed is verlicht, werkt beter voor iedereen die er komt: gasten, huurders, klanten en medewerkers. Ik ontwerp zakelijke interieurs die er verzorgd uitzien, prettig voelen en tegen intensief gebruik kunnen.</p>
          <ul>
            <li>Vakantiewoningen en short-stay</li>
            <li>Verbouwen en verduurzamen voor verhuur of verkoop</li>
            <li>Kantoren, praktijken en werkplekken</li>
            <li>Winkels en horeca</li>
            <li>Lichtplannen in samenwerking met architect en installateur</li>
          </ul>
          <p>Via Xoomlab werk ik samen met architecten, bouwkundigen en stedenbouwkundigen, zodat ook grotere projecten in één team worden opgepakt.</p>
          <a class="lees" href="projecten/vakantiehuisje-in-de-duinen.html">Bekijk: Vakantiehuisje in de duinen</a>
        </div>
        <img src="{U}2024/12/Flierefluiter-05102024-YRHE-14.jpg" alt="Vakantiewoning in de duinen" loading="lazy">
      </div>
    </section>
  </div>""", "opdrachtgevers.html")

# ------------------------------------------------------------------ referenties
REF = [
    ("uniek-wonen-in-een-school", "Tony & Elaine",
     "Onze woonkamer en keuken waren hard toe aan een verbouwing, maar we zaten vast in het proces. Wat wilden we nu precies, wat was er mogelijk, en hoe zou onze autistische zoon daarop reageren? Toen kwamen we in contact met Renate. Zij heeft niet alleen creatieve oplossingen gevonden voor ons huis, maar ook voor onze persoonlijke situatie, die de nodige uitdagingen met zich meebrengt.\n\nHet resultaat: een mooie, moderne woonkamer en keuken die perfect passen bij onze wensen én het unieke karakter van ons huis. We hebben Renate inmiddels al aanbevolen aan een vriend, die net zo enthousiast over haar werk is. En zodra we klaar zijn voor de volgende verbouwing, weten we haar zeker weer te vinden."),
    ("maatwerk-en-karakter-in-split-level-woning", "Imke & Armen",
     "Renate is van onschatbare waarde geweest voor de verbouwing van onze woning. Op basis van onze smaak en input heeft ze prachtige ontwerpen gemaakt waar we zelf nooit en te nimmer op waren gekomen. Via haar kwamen we in contact met een hele goede aannemer, die alle ideeën ook daadwerkelijk wist te realiseren. Bij iedere grote verbouwing moet soms tussentijds worden ingegrepen of bijgestuurd, maar Renate wist ons altijd tijdig te betrekken en met constructieve oplossingen te komen. Van materialen tot lichtontwerp, van kleurenpalet tot inrichting, onze woning is onherkenbaar verbeterd, maar toch voelde het meteen weer als ons thuis."),
    ("jaren-30-in-een-nieuw-jasje", "Petra",
     "Renate dacht écht met mij mee in de gehele aanpak en luisterde aandachtig naar mijn wensen en behoeften. De details maakten het verschil: van nieuwe keukengrepen tot maatwerk meubelontwerp en prachtige wandlampen. Haar adviezen waren waardevol gedurende het hele proces.\n\nDoor het zorgvuldig uitwerken van het kleuradvies en het lichtplan heeft mijn interieur nu precies de sfeer waarin ik me helemaal thuis voel. Dankzij Fierdesign voelt mijn huis echt als míjn plek."),
    ("kleur-in-nieuwbouw", "Jeroen & Jiska",
     "Vanuit twee kleine appartementen in Amsterdam gingen we samenwonen in een grote nieuwbouwwoning op IJburg, en we hadden geen idee waar te beginnen met de inrichting. Fierdesign bracht rust in dat proces, door goed te luisteren naar onze wensen en te helpen met keuzes maken. Door Renate leerden we technieken en bouwmaterialen kennen die we zelf nooit gevonden zouden hebben en durfden we te kiezen voor kleur. Ze heeft bovendien de verbouwing uitstekend voor ons begeleid. Het voelt nu echt als ons huis."),
    ("vakantiehuisje-in-de-duinen", "Duinhuis Vlieland",
     "Renate kwam met een goed ontwerp en goede ideeën om de vakantiewoning een eigen karakter te geven met een fijne sfeer. Ook heeft ze me enorm geholpen met de realisatie van het ontwerp en het vinden van de juiste meubels. Van de gasten krijgen we positieve reacties over het huis en de inrichting. Een gast vroeg zelfs waar de bank te koop was, omdat het de eerste bank was waar zij prettig op zat."),
    ("wonen-in-een-kapel", "Truida",
     "De ruimtes waren al geweldig, maar ik voelde me nog wel een beetje verloren in de proporties van de ruimtes. Door de 3D-tekeningen van het interieurontwerp kreeg ik meer gevoel bij hoe het eruit kon gaan zien en lukte het om keuzes te maken. Het behang in de keuken is nog mooier uitgevallen dan verwacht. Het lichtplan werkt geweldig en heeft mijn huis zowel functionaliteit als sfeer gegeven. Dat had ik nooit zelf kunnen bedenken, echt een toevoeging."),
    ("functionele-blikvanger", "Jos & Merlijn",
     "Om in ons nieuwe huis naar de woonkamer op de bovenste verdieping te komen, kom je eerst door een ruimte met een glazen dak en een trap in het midden. Het gevaar bestond dat het een soort overloop of hal zou worden. Wij wilden dat het een volwaardig deel van het huis zou zijn waar de kinderen zich konden terugtrekken. Renate van Fierdesign heeft heel goed geluisterd naar onze wensen en kwam met heel mooie ideeën om deze ruimte in te richten. Zelf hadden we dit nooit zo kunnen bedenken. Nu is het een van de blikvangers van het huis geworden waar de hele familie graag zit."),
    ("duurzaam-en-elegant-verbouwen", "Johannes",
     "De woning is grondig verbouwd en verduurzaamd, om daarna te kunnen verhuren. De hele benedenverdieping is tot casco gesloopt, de kans om er echt wat moois van te maken. Renate van Fierdesign heeft het interieurontwerp gemaakt en het project in heldere stappen opgebouwd: indelingsplan, materialisatie en een bijpassend licht- en schakelplan. Voor de afwerking heeft ze de tegels, het deurbeslag, de keukendetails en de kleuren aangedragen. Bij de keuken heeft ze geadviseerd over de opstelling, indeling en het materiaal. Het eindresultaat is een prachtig geheel geworden, ruimtelijk en van hoge kwaliteit en met aandacht voor details. De nieuwe bewoners zijn ontzettend blij met het eindresultaat."),
    ("jaren-50-uitbouw-gezinswoning", "Anke & Clemens",
     "Het sparren met Renate over het interieur en lichtplan heeft ons enorm geholpen. We wilden zelf de regie houden, en dankzij het heldere stappenplan van Fierdesign konden we onze ideeën vertalen naar een concrete aanpak en de juiste uitvoerende partijen. Het lichtplan, met prachtig gekozen armaturen, heeft ons woongenot zowel functioneel als esthetisch echt verrijkt. We zijn heel blij met het resultaat en de inspiratie die Renate ons heeft gegeven!"),
]
refs = "\n".join(f"""    <article class="referentie">
      <a href="projecten/{s}.html"><img src="{PS[s]['kaart']}" alt="{e(PS[s]['titel'])}" loading="lazy"></a>
      <div>
        <h2 style="font-size:1.6rem;margin-bottom:1rem"><a href="projecten/{s}.html" style="text-decoration:none">{e(PS[s]['titel'])}</a></h2>
        <blockquote>{alinea(t)}</blockquote>
        <footer>{e(n)}</footer>
      </div>
    </article>""" for s, n, t in REF)
pagina("referenties.html", "Referenties – Fierdesign", "Wat opdrachtgevers zeggen over het licht- en interieurontwerp van Fierdesign.",
       f"""  <section class="paginakop"><div class="wrap"><h1>Referenties</h1></div></section>
  <section class="sectie" style="padding-top:0"><div class="wrap">
{refs}
  </div></section>""", "referenties.html")

# ------------------------------------------------------------------ over mij
pagina("over-mij.html", "Over mij – Fierdesign", "Renate Heeringa Popma: van modeontwerper naar licht- en interieurontwerper in Amsterdam.",
       f"""  <section class="paginakop"><div class="wrap">
    <h1>Over mij</h1>
  </div></section>
  <section class="sectie" style="padding-top:0">
    <div class="wrap twee twee--beeld">
      <div class="tekst">
        <p>Mijn naam is Renate en met mijn bedrijf Fierdesign maak ik licht- en interieurontwerpen voor zowel zakelijke als residentiële projecten.</p>
        <p>Mijn hbo-opleiding aan Modeacademie Charles Montaigne (nu AMFI) bracht me naar Amsterdam. Na mijn bachelor rondde ik aan de kunstacademie in Arnhem de master Modevormgeving en Strategie af. Daarna werkte ik ruim vijftien jaar als modeontwerper voor uiteenlopende merken. Om me verder te verdiepen in licht- en interieurontwerp volgde ik diverse opleidingen.</p>
        <p>Mijn Friese roots zijn niet alleen terug te vinden in mijn bedrijfsnaam, maar verwijzen ook naar de liefde voor roeien, schaatsen en het gezinsleven met onze Friese stabij.</p>
      </div>
      <img src="{U}2025/07/RENATE-vensterbank_lowres.jpg" alt="Renate Heeringa Popma van Fierdesign" loading="lazy">
    </div>
  </section>
  <section class="sectie sectie--diep">
    <div class="wrap twee twee--beeld">
      <img src="{U}2025/07/renate_werk_zw2.jpg" alt="Renate aan het werk" loading="lazy">
      <div class="tekst">
        <h2>Van mode naar licht- en interieur</h2>
        <p>In 2020 heb ik het roer omgegooid en ben ik, na diverse scholing waaronder 3D-tekenen en lichtontwerp, gestart als licht- en interieurontwerper.</p>
        <p>Voor mij spelen zowel in mode- als licht- en interieurontwerp functionaliteit en natuurlijke elementen een belangrijke rol. Bij mode draait het om vormen, kleuren en details waarmee een geheel binnen een collectie wordt gevormd. Bij een interieurontwerp is dat niet anders. Het totaal van indeling van ruimtes, meubels en materialisatie vormt een samenhangend geheel met eigenheid.</p>
        <p>Na meerdere interieurontwerpen te hebben gerealiseerd, kwam ik erachter dat licht essentieel is binnen het interieur. Zodoende heb ik een jaar lang de studie Lichtontwerp gevolgd aan de Lighting Design Academy. Met veel plezier maak ik naast interieur- ook lichtontwerpen.</p>
        <p>Inmiddels heb ik vele interieurs ontworpen en ik kijk ernaar uit om met jou het volgende mooie plan te maken!</p>
      </div>
    </div>
  </section>
  <section class="sectie">
    <div class="wrap twee twee--beeld">
      <blockquote class="citaat">Een interieur zonder licht is onzichtbaar.</blockquote>
      <img src="{U}2025/07/543A8880-Verbeterd-NR.jpg" alt="" loading="lazy">
    </div>
    <div class="wrap"><p class="tekst" style="margin-top:2rem">Door met zowel daglicht als kunstlicht te werken creëert Fierdesign zowel sfeer als functionaliteit, met binnen- en buitenverlichting.</p></div>
  </section>""", "over-mij.html")

# ------------------------------------------------------------------ contact
pagina("contact.html", "Contact – Fierdesign", "Neem contact op met Fierdesign voor interieur- of lichtontwerp.",
       f"""  <section class="paginakop"><div class="wrap">
    <h1>Contact</h1>
  </div></section>
  <section class="sectie" style="padding-top:0">
    <div class="wrap twee twee--beeld">
      <div class="tekst">
        <p style="font-size:1.2rem">Fierdesign staat voor je klaar! Of je informatie wilt inwinnen, een inspiratiesessie wilt inplannen of meteen wilt praten over samenwerking, ik hoor het graag.</p>
        <p><a class="lees" href="mailto:renate@fierdesign.nl">renate@fierdesign.nl</a></p>
        <p><a class="lees" href="tel:+31628567546">+31 (0)6 28 56 75 46</a></p>
        <p style="margin-top:2rem;color:var(--steen)">Fierdesign is gevestigd bij Xoomlab op het Cruquiuseiland in Amsterdam.</p>
        <p style="margin-top:2rem"><a class="knop" href="mailto:renate@fierdesign.nl?subject=Interieurvraag">Stuur een e-mail</a></p>
      </div>
      <img src="{U}2025/07/BRANDINGSHOOT-Renate-by-Lilian-9.jpg" alt="Renate van Fierdesign" loading="lazy">
    </div>
  </section>""", "contact.html")

# ------------------------------------------------------------------ algemene voorwaarden
with open(os.path.join(os.path.dirname(__file__), "voorwaarden.txt"), encoding="utf-8") as f:
    vw = f.read().strip()
blok = []
for regel in vw.split("\n"):
    regel = regel.strip()
    if not regel:
        continue
    if regel[0].isdigit() and ". " in regel[:4] and not regel[:4].count(".") > 1:
        blok.append(f"<h2>{e(regel)}</h2>")
    else:
        blok.append(f"<p>{e(regel)}</p>")
pagina("algemene-voorwaarden.html", "Algemene voorwaarden – Fierdesign", "Algemene voorwaarden van Fierdesign.",
       f"""  <section class="paginakop"><div class="wrap"><h1>Algemene voorwaarden</h1></div></section>
  <section class="sectie voorwaarden" style="padding-top:0"><div class="wrap">
{chr(10).join(blok)}
  </div></section>""")

# ------------------------------------------------------------------ 404
pagina("404.html", "Pagina niet gevonden – Fierdesign", "Deze pagina bestaat niet (meer).",
       """  <section class="paginakop"><div class="wrap">
    <h1>Deze pagina bestaat niet (meer)</h1>
    <p>Misschien is hij verhuisd. Ga terug naar de <a href="/fier-design-website/index.html">homepage</a> of bekijk de <a href="/fier-design-website/projecten.html">projecten</a>.</p>
  </div></section>""")

print("klaar:", len(P), "projecten")
