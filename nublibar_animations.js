// nublibar_animations.js

document.addEventListener('DOMContentLoaded', () => {
  const hamburger   = document.querySelector('.hamburger');
  const navLinks    = document.querySelector('.nav-links');
  const scrollLinks = Array.from(document.querySelectorAll('a[href^="#"]'));

  // Ahora animamos sólo .benefit y el formulario
  const animatedEls = Array.from(document.querySelectorAll(
  '.benefit, .contact-form'
   ));

  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    hamburger.classList.toggle('active');
  });

  scrollLinks.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const targetId = link.getAttribute('href').slice(1);
      const targetEl = document.getElementById(targetId);
      if (!targetEl) return;
      targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      if (navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        hamburger.classList.remove('active');
      }
    }, { passive: true });
  });

  const appearOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  const appearOnScroll = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('appear');
      observer.unobserve(entry.target);
    });
  }, appearOptions);

  animatedEls.forEach(el => appearOnScroll.observe(el));
});


