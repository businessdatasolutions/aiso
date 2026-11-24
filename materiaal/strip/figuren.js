/* Figuren en belettering van de strip (stap 7 en 8 van het bouwplan).
   Stijl: klare lijn, naar het karakterblad uit Gemini (karakterblad-gemini.html): hoge hoofden met een neus,
   een vaste inktlijn en egale vlakken. Eén bron voor het figurenblad en voor de plaatjes.
   Elke functie geeft een stuk SVG als tekst terug.
   Maat: een staande figuur is 290 hoog; het nulpunt ligt tussen de voeten. */
(function () {
  'use strict';

  // Kleuren uit de huisstijl. De signaalkleur staat alleen op Noor en op wat af is.
  var K = {
    signaal: '#d4db3e',
    inkt: '#1a1a1a',
    creme: '#f5f0e6',
    creme2: '#f0ebe0',
    papier: '#f9f8f4',
    wit: '#ffffff',
    grijs: '#6b7280',
    donkergrijs: '#4b5563',
    lijn: '#d1d5db'
  };
  var LIJN = 3;
  var LETTER = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, 'Helvetica Neue', Arial, sans-serif";
  var MONO = "'SF Mono', Monaco, Consolas, 'Liberation Mono', monospace";
  // Lettergrootte. De plaatjes zetten deze hoger, zodat de tekst op een telefoon leesbaar blijft.
  var MAAT = { ballon: 15, bijschrift: 14, scherm: 13, deck: 13 };

  var WIE = {
    noor:    { trui: K.signaal, broek: K.inkt },
    duo:     { trui: K.creme2,  broek: K.donkergrijs },
    trainer: { trui: K.inkt,    broek: K.grijs },
    gast:    { trui: K.creme,   broek: K.grijs }
  };

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  function inkt(w) {
    return 'stroke="' + K.inkt + '" stroke-width="' + (w || LIJN) + '" stroke-linecap="round" stroke-linejoin="round"';
  }

  // Een arm of been: eerst een dikke lijn in inkt, daarover een dunnere in kleur. Zo krijgt de lijn een rand.
  function ledemaat(d, kleur, dikte) {
    var w = dikte || 14;
    return '<path d="' + d + '" fill="none" stroke="' + K.inkt + '" stroke-width="' + (w + 2 * LIJN) + '" stroke-linecap="round" stroke-linejoin="round"/>' +
           '<path d="' + d + '" fill="none" stroke="' + kleur + '" stroke-width="' + w + '" stroke-linecap="round" stroke-linejoin="round"/>';
  }

  function hand(x, y) {
    return '<circle cx="' + x + '" cy="' + y + '" r="8" fill="' + K.papier + '" ' + inkt() + '/>';
  }

  // Gezicht: ogen, wenkbrauwen, neus en mond. cx is het midden van het hoofd.
  function gezicht(soort, aanzicht, cx) {
    var s = '', zij = aanzicht === 'zij', lijn = inkt(2.6) + ' fill="none"';
    var ogen = zij ? [cx + 12] : [cx - 9, cx + 9], oy = -253;
    ogen.forEach(function (x) {
      s += '<circle cx="' + x + '" cy="' + oy + '" r="2.8" fill="' + K.inkt + '"/>';
      var naar = zij ? 1 : (x < cx ? -1 : 1);
      if (soort === 'bezorgd')      s += '<path d="M' + (x - 5) + ',' + (oy - 9 - 2.5 * naar) + ' L' + (x + 5) + ',' + (oy - 9 + 2.5 * naar) + '" ' + lijn + '/>';
      else if (soort === 'verrast') s += '<path d="M' + (x - 5) + ',' + (oy - 12) + ' Q' + x + ',' + (oy - 17) + ' ' + (x + 5) + ',' + (oy - 12) + '" ' + lijn + '/>';
      else if (soort === 'blij')    s += '<path d="M' + (x - 5) + ',' + (oy - 9) + ' Q' + x + ',' + (oy - 12) + ' ' + (x + 5) + ',' + (oy - 9) + '" ' + lijn + '/>';
    });
    if (zij) s += '<path d="M' + (cx + 21) + ',' + (oy + 1) + ' L' + (cx + 29) + ',' + (oy + 10) + ' L' + (cx + 21) + ',' + (oy + 13) + '" fill="' + K.papier + '" ' + inkt(2.6) + '/>';
    else     s += '<path d="M' + cx + ',' + (oy + 3) + ' L' + cx + ',' + (oy + 12) + ' L' + (cx - 4) + ',' + (oy + 12) + '" ' + lijn + '/>';
    var mx = zij ? cx + 13 : cx, my = -229, b = zij ? 6 : 8;
    if (soort === 'blij')         s += '<path d="M' + (mx - b) + ',' + (my - 2) + ' Q' + mx + ',' + (my + 7) + ' ' + (mx + b) + ',' + (my - 2) + '" ' + lijn + '/>';
    else if (soort === 'bezorgd') s += '<path d="M' + (mx - b) + ',' + (my + 3) + ' Q' + mx + ',' + (my - 4) + ' ' + (mx + b) + ',' + (my + 3) + '" ' + lijn + '/>';
    else if (soort === 'verrast') s += '<ellipse cx="' + mx + '" cy="' + (my + 1) + '" rx="3.5" ry="4.5" fill="' + K.papier + '" ' + inkt(2.6) + '/>';
    else                          s += '<path d="M' + (mx - b + 2) + ',' + my + ' Q' + mx + ',' + (my + 3) + ' ' + (mx + b - 2) + ',' + my + '" ' + lijn + '/>';
    return s;
  }

  // Hoofd met haar. Elke figuur is aan het silhouet van het haar te herkennen, zonder kleur.
  function hoofd(wie, soort, aanzicht, haar) {
    var zij = aanzicht === 'zij', cx = zij ? 4 : 0, s = '', k;
    var kop = '<path d="M' + (cx - 21) + ',-228 C' + (cx - 27) + ',-306 ' + (cx + 27) + ',-306 ' + (cx + 21) + ',-228 Q' + (cx + 21) + ',-212 ' + cx + ',-212 Q' + (cx - 21) + ',-212 ' + (cx - 21) + ',-228 Z" fill="' + K.papier + '" ' + inkt() + '/>';
    if (wie === 'noor') {
      if (zij) {
        s += kop + gezicht(soort, aanzicht, cx) +
          '<path d="M-22,-220 C-36,-322 36,-316 29,-262 C18,-278 8,-278 4,-274 C4,-252 0,-234 -5,-220 Z" fill="' + K.inkt + '"/>';
      } else {
        s += '<path d="M-31,-220 C-42,-320 42,-320 31,-220 Z" fill="' + K.inkt + '"/>' + kop + gezicht(soort, aanzicht, cx) +
          '<path d="M-22,-262 C-24,-304 24,-304 22,-262 C13,-277 -3,-283 -22,-262 Z" fill="' + K.inkt + '"/>';
      }
    } else if (wie === 'duo') {
      var van = zij ? 150 : 185, tot = zij ? 320 : 355;
      for (k = 0; k < 8; k++) {
        var h = (van + (tot - van) * k / 7) * Math.PI / 180;
        s += '<circle cx="' + (cx + 25 * Math.cos(h)).toFixed(1) + '" cy="' + (-262 + 30 * Math.sin(h)).toFixed(1) + '" r="10.5" fill="' + K.papier + '" ' + inkt() + '/>';
      }
      s += kop + gezicht(soort, aanzicht, cx);
      var bril = 'fill="none" ' + inkt(2.5);
      if (zij) s += '<circle cx="' + (cx + 12) + '" cy="-253" r="8.5" ' + bril + '/><path d="M' + (cx + 3.5) + ',-254 L' + (cx - 18) + ',-257" ' + bril + '/>';
      else s += '<circle cx="-9.5" cy="-253" r="8.5" ' + bril + '/><circle cx="9.5" cy="-253" r="8.5" ' + bril + '/><path d="M-1,-253 L1,-253" ' + bril + '/>';
    } else if (wie === 'trainer') { // kort grijs haar en een ringbaard
      s += kop;
      if (zij) {
        s += '<path d="M-15,-262 C-22,-308 32,-308 27,-266 C16,-289 -2,-289 -8,-262 Z" fill="' + K.grijs + '" ' + inkt(2) + '/>' +
             '<path d="M4,-238 Q2,-209 16,-209 Q28,-211 26,-232 Q18,-222 4,-238 Z" fill="' + K.grijs + '" ' + inkt(2) + '/>';
      } else {
        s += '<path d="M-22,-264 C-25,-306 25,-306 22,-264 C16,-289 -16,-289 -22,-264 Z" fill="' + K.grijs + '" ' + inkt(2) + '/>' +
             '<path d="M-21,-238 Q-22,-209 0,-209 Q22,-209 21,-238 Q13,-221 0,-221 Q-13,-221 -21,-238 Z" fill="' + K.grijs + '" ' + inkt(2) + '/>';
      }
      s += gezicht(soort, aanzicht, cx);
    } else { // gast: een deelnemer zonder naam. haar: 1, 2 of 3
      s += kop + gezicht(soort, aanzicht, cx);
      if (haar === 2)      s += '<path d="M' + (cx - 22) + ',-256 C' + (cx - 24) + ',-306 ' + (cx + 24) + ',-306 ' + (cx + 22) + ',-256 C' + (cx + 8) + ',-270 ' + (cx - 10) + ',-282 ' + (cx - 22) + ',-256 Z" fill="' + K.grijs + '" ' + inkt(2) + '/>';
      else if (haar === 3) s += '<path d="M' + (cx - 28) + ',-226 C' + (cx - 36) + ',-314 ' + (cx + 36) + ',-314 ' + (cx + 28) + ',-226 L' + (cx + 21) + ',-232 C' + (cx + 24) + ',-292 ' + (cx - 24) + ',-292 ' + (cx - 21) + ',-232 Z" fill="' + K.donkergrijs + '" ' + inkt(2) + '/>';
      else                 s += '<path d="M' + (cx - 22) + ',-262 C' + (cx - 22) + ',-304 ' + (cx + 22) + ',-304 ' + (cx + 22) + ',-262 C' + (cx + 12) + ',-284 ' + (cx - 12) + ',-284 ' + (cx - 22) + ',-262 Z" fill="' + K.inkt + '"/>';
    }
    return s;
  }

  function beker(x, y) {
    return '<rect x="' + x + '" y="' + y + '" width="15" height="18" rx="2" fill="' + K.wit + '" ' + inkt(2.5) + '/>';
  }

  /* Een hele figuur.
     wie: 'noor' | 'duo' | 'trainer' | 'gast'
     o.aanzicht: 'voor' | 'zij'   o.gezicht: 'neutraal' | 'blij' | 'bezorgd' | 'verrast'
     o.arm: 'neer' | 'wijs' | 'koffie' | 'tafel'   o.x, o.y: plek van de voeten   o.schaal   o.spiegel: kijkt naar links */
  function figuur(wie, o) {
    o = o || {};
    var f = WIE[wie], zij = o.aanzicht === 'zij', arm = o.arm || 'neer', s = '';
    var rand = inkt();
    var schoen = function (x) { return '<ellipse cx="' + x + '" cy="-7" rx="17" ry="8" fill="' + K.inkt + '"/>'; };
    if (zij) {
      s += ledemaat('M-5,-112 L-5,-16', f.broek, 16) + ledemaat('M7,-112 L7,-16', f.broek, 16) + schoen(4) + schoen(15);
      s += '<rect x="-3" y="-222" width="14" height="12" fill="' + K.papier + '" ' + rand + '/>';
      s += '<path d="M-22,-202 Q-22,-214 -12,-214 L14,-214 Q24,-214 24,-202 L26,-106 L-24,-106 Z" fill="' + f.trui + '" ' + rand + '/>';
      if (wie === 'duo') s += '<path d="M-22,-176 L24,-176 M-23,-156 L25,-156 M-23,-136 L25,-136" ' + inkt(2.5) + '/>';
      if (arm === 'wijs')        s += ledemaat('M4,-198 Q30,-194 58,-212', f.trui, 12) + hand(62, -214);
      else if (arm === 'koffie') s += ledemaat('M4,-198 Q10,-162 34,-164', f.trui, 12) + beker(36, -188) + hand(38, -166);
      else if (arm === 'tafel')  s += ledemaat('M4,-198 Q22,-170 42,-142', f.trui, 12) + hand(46, -138);
      else                       s += ledemaat('M2,-198 Q0,-162 8,-128', f.trui, 12) + hand(9, -122);
    } else {
      s += ledemaat('M-17,-112 L-17,-16', f.broek, 16) + ledemaat('M17,-112 L17,-16', f.broek, 16) + schoen(-19) + schoen(19);
      s += '<rect x="-7" y="-222" width="14" height="12" fill="' + K.papier + '" ' + rand + '/>';
      s += ledemaat('M-36,-200 Q-52,-166 -48,-128', f.trui, 12) + hand(-48, -122);
      if (arm === 'wijs')        s += ledemaat('M36,-200 Q62,-196 86,-218', f.trui, 12) + hand(90, -221);
      else if (arm === 'koffie') s += ledemaat('M36,-200 Q58,-164 34,-158', f.trui, 12) + beker(20, -184) + hand(28, -160);
      else if (arm === 'tafel')  s += ledemaat('M36,-200 Q58,-168 32,-140', f.trui, 12) + hand(28, -136);
      else                       s += ledemaat('M36,-200 Q52,-166 48,-128', f.trui, 12) + hand(48, -122);
      s += '<path d="M-36,-202 Q-36,-214 -24,-214 L24,-214 Q36,-214 36,-202 L40,-106 L-40,-106 Z" fill="' + f.trui + '" ' + rand + '/>';
      if (wie === 'duo') s += '<path d="M-37,-176 L37,-176 M-38,-156 L38,-156 M-39,-136 L39,-136" ' + inkt(2.5) + '/>';
    }
    s += hoofd(wie, o.gezicht || 'neutraal', zij ? 'zij' : 'voor', o.haar);
    var sx = (o.schaal || 1) * (o.spiegel ? -1 : 1), sy = o.schaal || 1;
    return '<g transform="translate(' + (o.x || 0) + ',' + (o.y || 0) + ') scale(' + sx + ',' + sy + ')">' + s + '</g>';
  }

  // MT-lid: een silhouet zonder gezicht. o.aanzicht: 'voor' | 'zij'   o.telefoon: true
  function mtlid(o) {
    o = o || {};
    var s = '', vul = 'fill="' + K.donkergrijs + '" ' + inkt();
    if (o.aanzicht === 'zij') {
      s += '<path d="M-34,0 L-34,-68 Q-34,-102 -4,-104 L8,-104 Q30,-102 34,-78 L40,0 Z" ' + vul + '/>' +
           '<path d="M-17,-114 C-23,-200 31,-200 25,-114 Q25,-98 4,-98 Q-17,-98 -17,-114 Z" ' + vul + '/>' +
           '<path d="M25,-146 L33,-137 L25,-134" ' + vul + '/>';
      if (o.telefoon) s += ledemaat('M14,-84 Q40,-66 56,-82', K.donkergrijs, 12) +
           '<rect x="54" y="-112" width="15" height="27" rx="3" fill="' + K.inkt + '" transform="rotate(14 61 -98)"/>';
    } else {
      s += '<path d="M-52,0 L-48,-70 Q-44,-104 -14,-104 L14,-104 Q44,-104 48,-70 L52,0 Z" ' + vul + '/>' +
           '<path d="M-21,-114 C-27,-200 27,-200 21,-114 Q21,-98 0,-98 Q-21,-98 -21,-114 Z" ' + vul + '/>';
      if (o.telefoon) s += '<rect x="-9" y="-76" width="18" height="30" rx="3" fill="' + K.inkt + '"/>';
    }
    var sx = (o.schaal || 1) * (o.spiegel ? -1 : 1), sy = o.schaal || 1;
    return '<g transform="translate(' + (o.x || 0) + ',' + (o.y || 0) + ') scale(' + sx + ',' + sy + ')">' + s + '</g>';
  }

  /* Het robotje staat voor de AI: een rond hoofd met een donker vizier, naar het blad uit Gemini.
     De ogen zijn licht in plaats van turquoise, omdat de huisstijl één signaalkleur heeft.
     o.gezicht: 'neutraal' | 'werkt' | 'bezorgd'   o.naam: tekst op het naamkaartje */
  function robot(o) {
    o = o || {};
    var s = '', g = o.gezicht || 'neutraal', licht = 'stroke="' + K.papier + '" stroke-width="2.6" stroke-linecap="round" fill="none"';
    s += '<rect x="-20" y="-34" width="40" height="32" rx="9" fill="' + K.creme + '" ' + inkt() + '/>';
    s += '<path d="M-20,-24 L-31,-12 M20,-24 L31,-12" fill="none" ' + inkt() + '/>';
    s += '<path d="M0,-84 L0,-94" ' + inkt() + '/><rect x="-9" y="-99" width="18" height="6" rx="3" fill="' + K.grijs + '" ' + inkt(2) + '/>';
    s += '<circle cx="0" cy="-58" r="27" fill="' + K.creme + '" ' + inkt() + '/>';
    s += '<ellipse cx="0" cy="-59" rx="20" ry="13" fill="' + K.inkt + '"/>';
    if (g === 'werkt')        s += '<path d="M-13,-59 Q-8,-66 -3,-59 M3,-59 Q8,-66 13,-59" ' + licht + '/>';
    else if (g === 'bezorgd') s += '<circle cx="-8" cy="-58" r="3" fill="' + K.papier + '"/><circle cx="8" cy="-58" r="3" fill="' + K.papier + '"/><path d="M-13,-64 L-4,-67 M13,-64 L4,-67" ' + licht + '/>';
    else                      s += '<circle cx="-8" cy="-59" r="3" fill="' + K.papier + '"/><circle cx="8" cy="-59" r="3" fill="' + K.papier + '"/>';
    if (g === 'bezorgd')    s += '<path d="M-5,-38 Q0,-42 5,-38" fill="none" ' + inkt(2.2) + '/>';
    else if (g === 'werkt') s += '<path d="M-5,-40 Q0,-35 5,-40" fill="none" ' + inkt(2.2) + '/>';
    if (o.naam) {
      s += '<rect x="-17" y="-26" width="34" height="13" rx="2" fill="' + K.wit + '" ' + inkt(1.5) + '/>' +
           '<text x="0" y="-16.5" text-anchor="middle" font-family="' + LETTER + '" font-size="7" font-weight="700" fill="' + K.inkt + '">' + esc(o.naam) + '</text>';
    }
    return '<g transform="translate(' + (o.x || 0) + ',' + (o.y || 0) + ') scale(' + (o.schaal || 1) + ')">' + s + '</g>';
  }

  // Tekst in regels breken. SVG doet dat niet zelf.
  function regels(tekst, max) {
    var uit = [], regel = '';
    String(tekst).split(/\s+/).forEach(function (w) {
      if (regel && (regel + ' ' + w).length > max) { uit.push(regel); regel = w; }
      else regel = regel ? regel + ' ' + w : w;
    });
    if (regel) uit.push(regel);
    return uit;
  }

  function tekstblok(r, x, y, o) {
    var s = '<text x="' + x + '" y="' + y + '" font-family="' + (o.letter || LETTER) + '" font-size="' + o.maat + '" font-weight="' + (o.gewicht || 500) + '" fill="' + (o.kleur || K.inkt) + '"' +
            (o.midden ? ' text-anchor="middle"' : '') + (o.spatie ? ' letter-spacing="' + o.spatie + '"' : '') + (o.schuin ? ' font-style="italic"' : '') + '>';
    r.forEach(function (t, k) { s += '<tspan x="' + x + '" dy="' + (k ? o.hoogte : 0) + '">' + esc(t) + '</tspan>'; });
    return s + '</text>';
  }

  // Losse tekst in het plaatje, bijvoorbeeld op een bord. o.maat, o.gewicht, o.midden, o.breedte (tekens), o.kleur
  function tekst(x, y, t, o) {
    o = o || {};
    var m = o.maat || MAAT.bijschrift;
    return tekstblok(regels(t, o.breedte || 99), x, y, { maat: m, hoogte: Math.round(m * 1.3), gewicht: o.gewicht || 700, midden: o.midden, kleur: o.kleur });
  }

  /* Tekstballon. x, y is de linkerbovenhoek. o.breedte in tekens (standaard 24).
     o.staart: [x, y] van de punt bij de spreker.   o.soort: 'spreek' | 'denk' */
  function ballon(x, y, t, o) {
    o = o || {};
    var maat = MAAT.ballon, lh = Math.round(maat * 1.3), pad = Math.round(maat * 0.85);
    var r = regels(t, o.breedte || 24);
    var w = Math.max.apply(null, r.map(function (q) { return q.length; })) * maat * 0.53 + 2 * pad;
    var h = r.length * lh + 2 * pad - 4, s = '', denk = o.soort === 'denk';
    var rand = 'fill="' + K.wit + '" ' + inkt();
    var onder, bx, by;
    if (o.staart) {
      onder = o.staart[1] > y + h / 2; by = onder ? y + h : y;
      bx = Math.min(Math.max(o.staart[0], x + 30), x + w - 30);
      if (denk) {
        s += '<circle cx="' + (bx + (o.staart[0] - bx) * 0.4) + '" cy="' + (by + (o.staart[1] - by) * 0.4) + '" r="7" ' + rand + '/>' +
             '<circle cx="' + (bx + (o.staart[0] - bx) * 0.85) + '" cy="' + (by + (o.staart[1] - by) * 0.85) + '" r="4" ' + rand + '/>';
      } else {
        s += '<path d="M' + (bx - 12) + ',' + by + ' L' + o.staart[0] + ',' + o.staart[1] + ' L' + (bx + 12) + ',' + by + ' Z" ' + rand + '/>';
      }
    }
    s += '<rect x="' + x + '" y="' + y + '" width="' + w.toFixed(1) + '" height="' + h + '" rx="' + Math.min(h / 2, denk ? 34 : 22) + '" ' + rand + (denk ? ' stroke-dasharray="7 6"' : '') + '/>';
    if (o.staart && !denk) s += '<path d="M' + (bx - 10) + ',' + by + ' L' + (bx + 10) + ',' + by + '" stroke="' + K.wit + '" stroke-width="' + (LIJN + 2) + '"/>';
    s += tekstblok(r, x + pad, y + pad + maat * 0.8, { maat: maat, hoogte: lh, gewicht: 500, schuin: denk });
    return '<g>' + s + '</g>';
  }

  /* Bijschrift. o.soort: 'titel' (zwart vlak, hoofdletters: dag of plaats) | 'verteller' (crème vlak) */
  function bijschrift(x, y, t, o) {
    o = o || {};
    var titel = o.soort === 'titel', maat = titel ? Math.round(MAAT.bijschrift * 0.9) : MAAT.bijschrift, lh = Math.round(maat * 1.32), pad = Math.round(maat * 0.75);
    var r = regels(titel ? String(t).toUpperCase() : t, o.breedte || 34);
    var w = Math.max.apply(null, r.map(function (q) { return q.length; })) * maat * (titel ? 0.66 : 0.52) + 2 * pad;
    var h = r.length * lh + 2 * pad - 5;
    return '<g><rect x="' + x + '" y="' + y + '" width="' + w.toFixed(1) + '" height="' + h + '" rx="6" fill="' + (titel ? K.inkt : K.creme) + '" ' + inkt(2.5) + '/>' +
      tekstblok(r, x + pad, y + pad + maat * 0.78, { maat: maat, hoogte: lh, gewicht: titel ? 700 : 500, kleur: titel ? K.wit : K.inkt, spatie: titel ? '.06em' : null }) + '</g>';
  }

  // Tekst op een scherm in het plaatje.
  function schermtekst(x, y, t, o) {
    o = o || {};
    var m = o.maat || MAAT.scherm;
    return tekstblok(regels(t, o.breedte || 28), x, y, { maat: m, hoogte: Math.round(m * 1.4), gewicht: o.gewicht || 600, letter: MONO });
  }

  /* Het casusdeck: tien vakjes. gevuld: hoeveel er af zijn. o.vink: nummer van het vakje met een vinkje. o.tekst: regel eronder. o.schaal */
  function deck(x, y, gevuld, o) {
    o = o || {};
    var s = '', q = o.schaal || 1, b = 30 * q, tussen = 7 * q, h = 22 * q;
    for (var k = 0; k < 10; k++) {
      var vx = x + k * (b + tussen);
      s += '<rect x="' + vx + '" y="' + y + '" width="' + b + '" height="' + h + '" rx="4" fill="' + (k < gevuld ? K.signaal : K.wit) + '" ' + inkt(2.5) + '/>';
      if (o.vink === k + 1) s += '<path d="M' + (vx + b * 0.3) + ',' + (y + h * 0.5) + ' l' + (b * 0.16) + ',' + (h * 0.24) + ' l' + (b * 0.27) + ',' + (-h * 0.46) + '" fill="none" ' + inkt(3) + '/>';
    }
    if (o.tekst) s += '<text x="' + x + '" y="' + (y + h + MAAT.deck * 1.5) + '" font-family="' + LETTER + '" font-size="' + MAAT.deck + '" font-weight="600" fill="' + K.inkt + '">' + esc(o.tekst) + '</text>';
    return '<g>' + s + '</g>';
  }

  window.Strip = { K: K, LIJN: LIJN, LETTER: LETTER, MAAT: MAAT, inkt: inkt, ledemaat: ledemaat, hand: hand, figuur: figuur, mtlid: mtlid, robot: robot,
                   ballon: ballon, bijschrift: bijschrift, schermtekst: schermtekst, tekst: tekst, deck: deck, regels: regels };
})();
