// Smooth scroll to sections
document.querySelectorAll('a[href^="/#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const id = this.getAttribute('href').substring(2);
    document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
  });
});
