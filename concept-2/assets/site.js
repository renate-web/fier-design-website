// Mobiel menu
(function () {
  var knop = document.querySelector('.menuknop');
  var menu = document.getElementById('menu');
  if (!knop || !menu) return;
  knop.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    knop.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();

// Fotowissel in de hero (rustig; staat stil bij 'verminderde beweging')
(function () {
  var fotos = document.querySelectorAll('.hero__beeld img');
  if (fotos.length < 2) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var i = 0;
  setInterval(function () {
    fotos[i].classList.remove('zichtbaar');
    i = (i + 1) % fotos.length;
    fotos[i].classList.add('zichtbaar');
  }, 6000);
})();

// Beeldwissel (bijv. lichtplan op Diensten): wisselt rustig, klik vergroot
(function () {
  document.querySelectorAll('.wissel').forEach(function (w) {
    var beelden = w.querySelectorAll('.wissel__beeld');
    var stippen = w.querySelectorAll('.wissel__stippen span');
    if (beelden.length < 2) return;
    var i = 0;
    if (stippen[0]) stippen[0].classList.add('actief');
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    setInterval(function () {
      beelden[i].classList.remove('zichtbaar');
      if (stippen[i]) stippen[i].classList.remove('actief');
      i = (i + 1) % beelden.length;
      beelden[i].classList.add('zichtbaar');
      if (stippen[i]) stippen[i].classList.add('actief');
    }, 5000);
  });
})();

// Lightbox voor projectgalerijen
(function () {
  var knoppen = Array.prototype.slice.call(document.querySelectorAll('[data-groot]'));
  if (!knoppen.length) return;
  var dlg = document.createElement('dialog');
  dlg.className = 'lightbox';
  dlg.innerHTML = '<img alt=""><div class="lightbox__balk">' +
    '<button type="button" data-actie="vorige">Vorige</button>' +
    '<button type="button" data-actie="sluit">Sluiten</button>' +
    '<button type="button" data-actie="volgende">Volgende</button></div>';
  document.body.appendChild(dlg);
  var img = dlg.querySelector('img');
  var huidig = 0;
  function toon(n) {
    huidig = (n + knoppen.length) % knoppen.length;
    img.src = knoppen[huidig].getAttribute('data-groot');
    img.alt = knoppen[huidig].querySelector('img').alt;
  }
  knoppen.forEach(function (k, n) {
    k.addEventListener('click', function () { toon(n); dlg.showModal(); });
  });
  dlg.addEventListener('click', function (e) {
    var a = e.target.getAttribute('data-actie');
    if (a === 'vorige') toon(huidig - 1);
    else if (a === 'volgende') toon(huidig + 1);
    else if (a === 'sluit' || e.target === dlg) dlg.close();
  });
  document.addEventListener('keydown', function (e) {
    if (!dlg.open) return;
    if (e.key === 'ArrowLeft') toon(huidig - 1);
    if (e.key === 'ArrowRight') toon(huidig + 1);
  });
})();

// Projectfilter (Alle / Lichtontwerp / Interieurontwerp)
(function () {
  var knoppen = document.querySelectorAll('.filter__knop');
  var kaarten = document.querySelectorAll('#projectraster .kaart');
  if (!knoppen.length) return;
  function zet(f) {
    knoppen.forEach(function (k) { k.setAttribute('aria-pressed', k.dataset.filter === f ? 'true' : 'false'); });
    kaarten.forEach(function (k) {
      var v = k.dataset.vak;
      k.hidden = !(f === 'alle' || v === f || v === 'beide');
    });
  }
  knoppen.forEach(function (k) { k.addEventListener('click', function () { zet(k.dataset.filter); }); });
  var m = location.search.match(/filter=(licht|interieur)/);
  if (m) zet(m[1]);
})();
