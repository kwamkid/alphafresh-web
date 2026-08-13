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

  function setLang(l) {
    if (LANGS.indexOf(l) === -1) l = 'en';
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

  /* ---------- sticky nav ---------- */
  var nav = document.querySelector('.nav');
  function onScroll() { if (nav) nav.classList.toggle('scrolled', window.scrollY > 40); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

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
  timer = setTimeout(function () { go(1); }, 6000);

  /* Video plays on phones too. On a narrow screen only the first clip is
     fetched and looped — three clips would be a lot of mobile data for a
     background that is mostly hidden behind the headline anyway.

     The photo slider is only dismissed once a clip has actually started
     playing. iOS refuses autoplay in Low Power Mode, and swapping first would
     leave the hero blank. */
  var saveData = navigator.connection && navigator.connection.saveData === true;
  if (!reduce && !saveData) {
    var small = window.innerWidth <= 760;
    var list = small ? vids.slice(0, 1) : vids;
    if (small) list[0].loop = true;
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

    list.forEach(function (v, n) {
      v.addEventListener('ended', function () { if (mode === 'vid' && !small) go(i + 1); });
      if (n === 0) {
        v.addEventListener('canplay', function () { handOver(v); }, { once: true });
        v.addEventListener('loadeddata', function () { handOver(v); }, { once: true });
      }
      v.src = v.dataset.src;
      v.load();
    });
  }

})();
