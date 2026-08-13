/* Alpha Fresh — shared behaviour for every page.
   Language toggle · sticky nav · mobile menu · scroll reveal · hero slider */

(function () {
  'use strict';

  /* ---------- language ----------
     Four languages share one document. The markup is English; the other three
     titles and descriptions ride along in <meta name="title-xx"> so search
     engines still get the right text for whichever language a visitor picks. */
  var root = document.documentElement;
  var LANGS = ['en', 'th', 'zh', 'ar'];

  function meta(name) {
    var el = document.querySelector('meta[name="' + name + '"]');
    return el ? el.getAttribute('content') : '';
  }
  var TITLE = { en: document.title };
  var DESC = { en: meta('description') };
  LANGS.slice(1).forEach(function (l) {
    TITLE[l] = meta('title-' + l) || TITLE.en;
    DESC[l] = meta('description-' + l) || DESC.en;
  });

  /* The Chinese and Arabic webfonts are large and most visitors never see
     them, so they are only fetched the first time someone picks that
     language rather than blocking the first paint for everybody. */
  var FONT = {
    zh: 'https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap',
    ar: 'https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;500;700&display=swap'
  };
  var fontDone = {};
  function loadFont(l) {
    if (!FONT[l] || fontDone[l]) return;
    fontDone[l] = true;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = FONT[l];
    document.head.appendChild(link);
  }

  function setLang(l) {
    if (LANGS.indexOf(l) === -1) l = 'en';
    loadFont(l);
    root.lang = l;
    root.dataset.lang = l;
    root.dir = l === 'ar' ? 'rtl' : 'ltr';       /* Arabic reads right to left */
    document.title = TITLE[l];
    var d = document.querySelector('meta[name="description"]');
    if (d) d.setAttribute('content', DESC[l]);
    document.querySelectorAll('.lang-opt').forEach(function (b) {
      b.setAttribute('aria-selected', b.dataset.setLang === l ? 'true' : 'false');
    });
    try { localStorage.setItem('af_lang', l); } catch (e) {}
  }
  window.setLang = setLang;

  var picker = document.getElementById('langpick');
  if (picker) {
    var trigger = picker.querySelector('.lang-btn');
    function closeLang() {
      picker.classList.remove('open');
      trigger.setAttribute('aria-expanded', 'false');
    }
    trigger.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = picker.classList.toggle('open');
      trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    picker.querySelectorAll('.lang-opt').forEach(function (b) {
      b.addEventListener('click', function () { setLang(b.dataset.setLang); closeLang(); });
    });
    document.addEventListener('click', closeLang);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeLang(); });
  }

  /* English is the default; a visitor's own choice is remembered from then on. */
  var start = 'en';
  try { start = localStorage.getItem('af_lang') || 'en'; } catch (e) {}
  setLang(start);

  /* ---------- sticky nav ----------
     scrollY is read inside requestAnimationFrame and the class is only written
     when the state actually changes. Reading it straight from the scroll
     handler forced the browser to recompute layout on every single event. */
  var nav = document.querySelector('.nav');
  if (nav) {
    var stuck = false, queued = false;
    function applyNav() {
      queued = false;
      var next = window.scrollY > 40;
      if (next !== stuck) { stuck = next; nav.classList.toggle('scrolled', stuck); }
    }
    window.addEventListener('scroll', function () {
      if (!queued) { queued = true; requestAnimationFrame(applyNav); }
    }, { passive: true });
    applyNav();
  }

  /* ---------- mobile menu ---------- */
  var burger = document.querySelector('.burger'), menu = document.getElementById('menu');
  if (burger && menu) {
    burger.addEventListener('click', function () { menu.classList.toggle('open'); });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { menu.classList.remove('open'); });
    });
  }

  /* ---------- reveal on scroll ---------- */
  var els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- harvest calendar: mark the current month ---------- */
  var cal = document.querySelector('.cal');
  if (cal) {
    var m = new Date().getMonth();                       // 0 = January
    cal.classList.add('has-now');
    cal.querySelectorAll('.lane').forEach(function (l) { l.style.setProperty('--now', m); });
    var heads = cal.querySelectorAll('thead th.m');
    if (heads[m]) heads[m].classList.add('now');
    var key = document.querySelector('.k-now-wrap');
    if (key) key.classList.add('on');
  }

  /* ---------- hero: photo slider, handing over to video when it loads ---------- */
  var media = document.getElementById('heroMedia');
  if (!media) return;
  var viewportW = window.innerWidth;
  var dots = document.getElementById('dots');
  var slides = [].slice.call(media.querySelectorAll('.hero-slide'));
  var vids = [].slice.call(media.querySelectorAll('.hero-vid'));
  var reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  var mode = 'img', i = 0, timer;

  slides.forEach(function (_, n) {
    var b = document.createElement('button');
    b.setAttribute('aria-label', 'slide ' + (n + 1));
    b.addEventListener('click', function () { go(n); });
    dots.appendChild(b);
  });
  var dotEls = [].slice.call(dots.children);

  function paint() {
    var set = mode === 'img' ? slides : vids;
    set.forEach(function (s, n) { s.classList.toggle('on', n === i); });
    dotEls.forEach(function (d, n) { d.classList.toggle('on', n === i); });
    if (mode === 'vid') {
      vids.forEach(function (v, n) {
        if (n === i) { v.currentTime = 0; v.play().catch(function () {}); } else { v.pause(); }
      });
    }
  }
  function go(n) {
    var len = mode === 'img' ? slides.length : vids.length;
    i = ((n % len) + len) % len;
    paint();
    clearTimeout(timer);
    if (mode === 'img') timer = setTimeout(function () { go(i + 1); }, 6000);
  }
  paint();

  /* Video plays on phones too. On a narrow screen only the first clip is
     fetched and looped — three clips would be a lot of mobile data for a
     background that is mostly hidden behind the headline anyway.

     The photo slider is only dismissed once a clip has actually started
     playing. iOS refuses autoplay in Low Power Mode, and swapping first would
     leave the hero blank. */
  /* Slides 2 and 3 are not visible for the first six seconds, so they wait
     until the page has finished loading. Nothing competes with the hero
     image, which is what Google measures as the Largest Contentful Paint. */
  function afterLoad(fn) {
    function go() {
      if (window.requestIdleCallback) window.requestIdleCallback(fn, { timeout: 1500 });
      else setTimeout(fn, 200);
    }
    if (document.readyState === 'complete') go();
    else window.addEventListener('load', go, { once: true });
  }
  /* On a phone the hero is one photo and one looping clip. Fetching two more
     full-bleed photos for a slider that sits behind the headline is a lot of
     mobile data for something almost nobody watches, and those downloads were
     crowding out everything else on the page. Wide screens keep the slider. */
  var phone = viewportW <= 760;
  if (phone) {
    if (dots) dots.style.display = 'none';
    clearTimeout(timer);
  } else {
    afterLoad(function () {
      slides.forEach(function (s) { if (s.dataset.src) s.src = s.dataset.src; });
      /* start cycling only once there is a second photo to cycle to */
      clearTimeout(timer);
      timer = setTimeout(function () { go(i + 1); }, 6000);
    });
  }

  var saveData = navigator.connection && navigator.connection.saveData === true;
  if (!reduce && !saveData) {
    var small = phone;
    var list = small ? vids.slice(0, 1) : vids;
    if (small) list[0].loop = true;
    /* clips 2 and 3 only start downloading once clip 1 is on screen, so the
       first paint competes with one file instead of three */
    var queue = list.slice(1);
    var switched = false;

    function handOver(v) {
      if (switched) return;
      var p = v.play();
      if (p && p.then) {
        p.then(function () {
          switched = true;
          mode = 'vid'; i = 0; vids = list;
          media.classList.add('video-on');
          if (small && dots) dots.style.display = 'none';
          clearTimeout(timer);
          paint();
        }).catch(function () { /* autoplay blocked — keep the photos */ });
      }
    }

    list.forEach(function (v) {
      v.addEventListener('ended', function () { if (mode === 'vid' && !small) go(i + 1); });
    });
    var first = list[0];
    first.addEventListener('canplay', function () { handOver(first); }, { once: true });
    first.addEventListener('loadeddata', function () { handOver(first); }, { once: true });
    /* The video only starts downloading once the page itself has loaded, so
       the hero photo gets the whole connection to itself first. */
    afterLoad(function () {
      first.src = (small && first.dataset.srcSmall) ? first.dataset.srcSmall : first.dataset.src;
      first.load();
    });
    first.addEventListener('playing', function () {
      queue.forEach(function (v) { v.src = v.dataset.src; v.load(); });
    }, { once: true });
  }

})();
