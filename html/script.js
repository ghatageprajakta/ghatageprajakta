// Smooth scroll
document.querySelectorAll('.navbar a').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      target.scrollIntoView({ behavior: 'smooth' });
    });
  });
  
  // Filter function
  function filterImages(category) {
    const images = document.querySelectorAll('.gallery img');
    images.forEach(img => {
      const match = img.dataset.category === category || category === 'all';
      img.style.display = match ? 'inline-block' : 'none';
    });
  }
  
  // Search function
  document.getElementById('searchInput').addEventListener('input', function () {
    const query = this.value.toLowerCase();
    const images = document.querySelectorAll('.gallery img');
    images.forEach(img => {
      const altText = img.alt.toLowerCase();
      img.style.display = altText.includes(query) ? 'inline-block' : 'none';
    });
  });
  