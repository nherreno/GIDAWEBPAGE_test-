---
layout: single
title: "Recuerdos GIDA"
permalink: /recuerdos/
author_profile: true
header:
  # Dejamos esto transparente para que el canvas mande sobre el fondo
  overlay_color: "transparent"
  caption: "Galería conmemorativa del GIDA"
---

<div id="starfield-container" style="position: absolute; top: 0; left: 0; width: 100%; height: 300px; z-index: 0; overflow: hidden; background: #05070a;">
  <canvas id="starfield"></canvas>
</div>

<style>
  /* 2. AJUSTE DE LA "CINTA" DEL TÍTULO */
  .page__hero--overlay {
    background-color: transparent !important;
    position: relative;
    height: 300px; /* Reducimos la altura para que sea una cinta elegante */
    display: flex;
    align-items: center;
    z-index: 1; /* Esto pone el título POR ENCIMA de las estrellas */
  }

  /* Forzamos que el título sea blanco brillante para que resalte en el espacio */
  .page__hero-title {
    color: #ffffff !important;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
  }

  /* 3. ESTILOS DE TU COLLAGE (SE MANTIENEN IGUAL) */
  .collage-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    grid-auto-rows: 150px;
    gap: 15px;
    padding: 20px;
    background: #f4f4f4;
    border-radius: 10px;
    margin-top: 30px; /* Espacio para que no choque con el header */
  }

  .collage-item {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    animation: float 6s ease-in-out infinite;
  }

  @keyframes float {
    0% { transform: translate(0, 0); }
    50% { transform: translate(0, -5px); }
    100% { transform: translate(0, 0); }
  }
</style>

Esta sección rinde homenaje a nuestra trayectoria. Las imágenes se entrelazan y fluyen con suavidad.

<div class="collage-container" id="collage">
  {% for file in site.static_files %}
    {% if file.path contains 'assets/images/recuerdos' %}
      <img src="{{ file.path | relative_url }}" class="collage-item" alt="Recuerdo GIDA">
    {% endif %}
  {% endfor %}
</div>

<script>
  const canvas = document.getElementById('starfield');
  const ctx = canvas.getContext('2d');
  let stars = [];

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = 300; // Misma altura que el header
  }

  class Star {
    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 2;
      this.speed = Math.random() * 0.4 + 0.1;
    }
    update() {
      this.y += this.speed;
      if (this.y > canvas.height) this.y = 0;
    }
    draw() {
      ctx.fillStyle = 'white';
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function initStars() {
    resize();
    stars = [];
    for (let i = 0; i < 100; i++) stars.push(new Star());
  }

  function animateStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(star => {
      star.update();
      star.draw();
    });
    requestAnimationFrame(animateStars);
  }

  document.addEventListener("DOMContentLoaded", function() {
    initStars();
    animateStars();

    // Barajado de tus fotos
    const container = document.getElementById('collage');
    const items = Array.from(container.children);
    for (let i = items.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [items[i], items[j]] = [items[j], items[i]];
    }
    items.forEach(item => container.appendChild(item));
  });
</script>