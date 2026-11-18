/* =========================================================
   The Foremost Institute — interactions
   ========================================================= */

(function () {
  'use strict';

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const header = document.getElementById('site-header');
  const backToTop = document.getElementById('back-to-top');
  const heroImage = document.getElementById('hero-image');

  /* ---------- Header state + back to top ---------- */

  let scrollTicking = false;

  function updateOnScroll() {
    const y = window.scrollY || window.pageYOffset;

    if (header) header.classList.toggle('is-scrolled', y > 8);
    if (backToTop) backToTop.classList.toggle('is-visible', y > 720);

    if (heroImage && !reduceMotion) {
      const maxShift = 70;
      const shift = Math.min(y * 0.07, maxShift);
      heroImage.style.transform = 'translate3d(0, ' + shift + 'px, 0) scale(1.05)';
    }

    scrollTicking = false;
  }

  function requestScrollUpdate() {
    if (!scrollTicking) {
      window.requestAnimationFrame(updateOnScroll);
      scrollTicking = true;
    }
  }

  window.addEventListener('scroll', requestScrollUpdate, { passive: true });
  updateOnScroll();

  if (backToTop) {
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  /* ---------- Reveal on scroll ---------- */

  const revealItems = Array.prototype.slice.call(document.querySelectorAll('.reveal'));

  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealItems.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    const revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    revealItems.forEach(function (el) { revealObserver.observe(el); });
  }

  /* ---------- Active nav link ---------- */

  const navLinks = Array.prototype.slice.call(document.querySelectorAll('.primary-nav .nav-link'));
  const navMap = {};
  navLinks.forEach(function (link) {
    const hash = link.getAttribute('href');
    if (hash && hash.charAt(0) === '#') navMap[hash.slice(1)] = link;
  });

  const observedSections = ['about', 'approach', 'courses', 'teacher']
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);

  if ('IntersectionObserver' in window && observedSections.length && Object.keys(navMap).length) {
    const sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (link) { link.classList.remove('is-active'); });
        const active = navMap[entry.target.id];
        if (active) active.classList.add('is-active');
      });
    }, { rootMargin: '-38% 0px -55% 0px', threshold: 0 });

    observedSections.forEach(function (section) { sectionObserver.observe(section); });
  }

  /* ---------- Mobile menu ---------- */

  const menu = document.getElementById('mobile-menu');
  const menuToggle = document.querySelector('.menu-toggle');
  const menuClose = document.querySelector('.menu-close');
  let lastFocused = null;

  function menuFocusables() {
    if (!menu) return [];
    return Array.prototype.slice.call(menu.querySelectorAll('a[href], button:not([disabled])'))
      .filter(function (el) { return el.offsetParent !== null; });
  }

  function openMenu() {
    if (!menu || !menuToggle) return;
    lastFocused = document.activeElement;
    menu.classList.add('is-open');
    menu.removeAttribute('inert');
    menu.setAttribute('aria-hidden', 'false');
    menuToggle.setAttribute('aria-expanded', 'true');
    menuToggle.setAttribute('aria-label', 'Close menu');
    document.body.classList.add('menu-open');
    if (menuClose) menuClose.focus();
    document.addEventListener('keydown', onMenuKeydown);
  }

  function closeMenu(restoreFocus) {
    if (!menu || !menuToggle) return;
    menu.classList.remove('is-open');
    menu.setAttribute('inert', '');
    menu.setAttribute('aria-hidden', 'true');
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', 'Open menu');
    document.body.classList.remove('menu-open');
    document.removeEventListener('keydown', onMenuKeydown);
    if (restoreFocus !== false && lastFocused && typeof lastFocused.focus === 'function') {
      lastFocused.focus({ preventScroll: true });
    }
  }

  function onMenuKeydown(event) {
    if (!menu) return;

    if (event.key === 'Escape') {
      event.preventDefault();
      closeMenu();
      return;
    }

    if (event.key !== 'Tab') return;

    const focusables = menuFocusables();
    if (!focusables.length) return;

    const first = focusables[0];
    const last = focusables[focusables.length - 1];

    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  if (menuToggle) {
    menuToggle.addEventListener('click', function () {
      if (menu && menu.classList.contains('is-open')) closeMenu();
      else openMenu();
    });
  }

  if (menuClose) {
    menuClose.addEventListener('click', function () { closeMenu(); });
  }

  if (menu) {
    Array.prototype.slice.call(menu.querySelectorAll('a[href]')).forEach(function (link) {
      link.addEventListener('click', function () { closeMenu(false); });
    });
  }

  window.addEventListener('resize', function () {
    if (window.innerWidth > 1080 && menu && menu.classList.contains('is-open')) {
      closeMenu(false);
    }
  });

  /* ---------- Course filtering ---------- */

  const filterButtons = Array.prototype.slice.call(document.querySelectorAll('.filter'));
  const courseCards = Array.prototype.slice.call(document.querySelectorAll('.course-card'));
  const filterCount = document.getElementById('filter-count');

  function applyCourseFilter(filter) {
    let visible = 0;

    courseCards.forEach(function (card) {
      const show = filter === 'all' || card.getAttribute('data-category') === filter;
      card.hidden = !show;
      if (show) {
        visible += 1;
        card.classList.add('is-visible');
      }
    });

    if (filterCount) {
      filterCount.textContent = visible + (visible === 1 ? ' course' : ' courses');
    }
  }

  filterButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      const filter = button.getAttribute('data-filter') || 'all';

      filterButtons.forEach(function (btn) {
        const isCurrent = btn === button;
        btn.classList.toggle('is-active', isCurrent);
        btn.setAttribute('aria-pressed', isCurrent ? 'true' : 'false');
      });

      applyCourseFilter(filter);
    });
  });

  /* ---------- FAQ accordion ---------- */

  const faqItems = Array.prototype.slice.call(document.querySelectorAll('.faq-item'));

  faqItems.forEach(function (item) {
    const trigger = item.querySelector('.faq-trigger');
    if (!trigger) return;

    trigger.addEventListener('click', function () {
      const wasOpen = item.classList.contains('open');

      faqItems.forEach(function (other) {
        other.classList.remove('open');
        const otherTrigger = other.querySelector('.faq-trigger');
        if (otherTrigger) otherTrigger.setAttribute('aria-expanded', 'false');
      });

      if (!wasOpen) {
        item.classList.add('open');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---------- Newsletter ---------- */

  const newsletterForm = document.getElementById('newsletter-form');
  const newsletterEmail = document.getElementById('newsletter-email');
  const newsletterStatus = document.getElementById('newsletter-status');
  const toast = document.getElementById('toast');
  let toastTimer = null;

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('is-visible');
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(function () {
      toast.classList.remove('is-visible');
    }, 4200);
  }

  if (newsletterForm && newsletterEmail && newsletterStatus) {
    newsletterForm.addEventListener('submit', function (event) {
      event.preventDefault();

      const value = newsletterEmail.value.trim();
      const valid = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);

      newsletterStatus.classList.remove('is-error');

      if (!valid) {
        newsletterStatus.textContent = 'Please enter a valid email address.';
        newsletterStatus.classList.add('is-error');
        newsletterEmail.focus();
        return;
      }

      /* This concept form is front-end only. Connect it to your email
         provider or CRM before publishing. */
      newsletterStatus.textContent = 'JazakAllah khair — you are on the list.';
      newsletterEmail.value = '';
      showToast('Thank you — you are on the list.');
    });

    newsletterEmail.addEventListener('input', function () {
      if (newsletterStatus.classList.contains('is-error')) {
        newsletterStatus.textContent = '';
        newsletterStatus.classList.remove('is-error');
      }
    });
  }

  /* ---------- Contact form ---------- */

  const contactForm = document.getElementById('contact-form');
  const contactFirstName = document.getElementById('contact-first-name');
  const contactEmail = document.getElementById('contact-email');
  const contactMessage = document.getElementById('contact-message');
  const contactCount = document.getElementById('contact-count');
  const contactStatus = document.getElementById('contact-status');

  if (contactForm && contactFirstName && contactEmail && contactMessage && contactStatus) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

    function updateMessageCount() {
      if (!contactCount) return;
      contactCount.textContent = contactMessage.value.length + ' / 180';
    }

    function markInvalid(field, invalid) {
      if (!field) return;
      if (invalid) field.setAttribute('aria-invalid', 'true');
      else field.removeAttribute('aria-invalid');
    }

    contactMessage.addEventListener('input', function () {
      updateMessageCount();
      if (contactMessage.value.trim()) markInvalid(contactMessage, false);
    });

    contactFirstName.addEventListener('input', function () {
      if (contactFirstName.value.trim()) markInvalid(contactFirstName, false);
    });

    contactEmail.addEventListener('input', function () {
      if (emailPattern.test(contactEmail.value.trim())) markInvalid(contactEmail, false);
    });

    contactForm.addEventListener('submit', function (event) {
      event.preventDefault();

      const firstNameValid = contactFirstName.value.trim().length > 0;
      const emailValid = emailPattern.test(contactEmail.value.trim());
      const messageValid = contactMessage.value.trim().length > 0;

      markInvalid(contactFirstName, !firstNameValid);
      markInvalid(contactEmail, !emailValid);
      markInvalid(contactMessage, !messageValid);

      contactStatus.classList.remove('is-error');

      if (!firstNameValid || !emailValid || !messageValid) {
        contactStatus.textContent = 'Please complete the highlighted fields with a valid email address.';
        contactStatus.classList.add('is-error');
        const firstInvalid = contactForm.querySelector('[aria-invalid="true"]');
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      /* This concept form is front-end only. Connect it to an email provider
         or CRM before publishing. */
      contactStatus.textContent = 'Thank you — we will be in touch.';
      contactForm.reset();
      updateMessageCount();
      showToast('Your message has been received.');
    });

    updateMessageCount();
  }

  /* ---------- Account form ---------- */

  const accountForm = document.getElementById('account-form');
  const accountEmail = document.getElementById('account-email');
  const accountPassword = document.getElementById('account-password');
  const accountStatus = document.getElementById('account-status');

  if (accountForm && accountEmail && accountPassword && accountStatus) {
    accountForm.addEventListener('submit', function (event) {
      event.preventDefault();
      const emailValid = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(accountEmail.value.trim());
      const passwordValid = accountPassword.value.length > 0;

      if (!emailValid || !passwordValid) {
        accountStatus.textContent = 'Please enter your email address and password.';
        accountStatus.classList.add('is-error');
        (emailValid ? accountPassword : accountEmail).focus();
        return;
      }

      accountStatus.classList.remove('is-error');
      accountStatus.textContent = 'Demo sign-in complete — authentication is not connected in this preview.';
    });
  }

  /* ---------- Footer year ---------- */

  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

})();
