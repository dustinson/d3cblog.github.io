// This script fixes links that point to production (delta3consulting.com) in development mode
document.addEventListener('DOMContentLoaded', function() {
  // Replace all delta3consulting.com URLs with localhost:4000
  const productionDomain = 'https://delta3consulting.com';
  const localDomain = 'http://localhost:4000';

  // Fix links
  const links = document.querySelectorAll('a[href^="' + productionDomain + '"]');
  for (let i = 0; i < links.length; i++) {
    const link = links[i];
    const href = link.getAttribute('href');
    link.setAttribute('href', href.replace(productionDomain, localDomain));
  }

  // Fix images
  const images = document.querySelectorAll('img[src^="' + productionDomain + '"]');
  for (let i = 0; i < images.length; i++) {
    const img = images[i];
    const src = img.getAttribute('src');
    img.setAttribute('src', src.replace(productionDomain, localDomain));
  }

  // Fix stylesheets
  const stylesheets = document.querySelectorAll('link[rel="stylesheet"][href^="' + productionDomain + '"]');
  for (let i = 0; i < stylesheets.length; i++) {
    const stylesheet = stylesheets[i];
    const href = stylesheet.getAttribute('href');
    stylesheet.setAttribute('href', href.replace(productionDomain, localDomain));
  }

  // Fix scripts
  const scripts = document.querySelectorAll('script[src^="' + productionDomain + '"]');
  for (let i = 0; i < scripts.length; i++) {
    const script = scripts[i];
    const src = script.getAttribute('src');
    script.setAttribute('src', src.replace(productionDomain, localDomain));
  }

  console.log('Fixed links to use localhost instead of production URLs');
});
