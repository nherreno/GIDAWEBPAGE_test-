---
# CONFIGURACIÓN JEKYLL: Define el diseño y la URL (/miembros/)
layout: single
title: "Miembros del GIDA"
permalink: /miembros/
author_profile: true
header:
  overlay_color: "#05070a" # Color de respaldo si falla el script de estrellas
---

<div id="mi-header-espacial" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;">
  <canvas id="canvas-estrellas"></canvas>
</div>

<style>
  /* ESTILOS DEL ENCABEZADO: Fuerza el fondo negro y la altura */
  .page__hero--overlay { 
    position: relative !important; 
    background-color: #05070a !important; 
    overflow: hidden; 
  }

  /* ESTILOS DE LAS TARJETAS (CARDS): Controla sombras, bordes y animaciones */
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); /* Auto-ajusta columnas */
    gap: 25px;
    margin-top: 40px;
  }

  .member-card {
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease; /* Suavidad del efecto hover */
    text-align: center;
    overflow: hidden;
    border: 1px solid #e1e1e1;
  }

  .member-card:hover {
    transform: translateY(-10px); /* Efecto de levitación al pasar el mouse */
  }

  .member-img {
    width: 100%;
    height: 220px;
    object-fit: cover; /* Mantiene la proporción de la foto sin deformarla */
  }
</style>

<div class="team-grid">
  {% for miembro in site.data.miembros %}
  <div class="member-card">
    <img src="{{ miembro.foto | relative_url }}" class="member-img" alt="{{ miembro.nombre }}">
    <div class="member-info">
      <div class="member-name">{{ miembro.nombre }}</div>
      <div class="member-role" style="color: #d35400; font-weight: bold;">{{ miembro.area }}</div>
      <div class="member-detail">{{ miembro.carrera }}</div>
      <a href="mailto:{{ miembro.correo }}" class="member-email" style="color: #2980b9;">{{ miembro.correo }}</a>
    </div>
  </div>
  {% endfor %}
</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('canvas-estrellas');
    const ctx = canvas.getContext('2d');
    // Buscamos el header original del tema para inyectar nuestro código
    const header = document.querySelector('.page__hero--overlay') || document.querySelector('header');
    const container = document.getElementById('mi-header-espacial');

    if (header && container) {
      header.appendChild(container); // Inyección dinámica del canvas en el header

      function resize() {
        canvas.width = header.offsetWidth;
        canvas.height = header.offsetHeight;
      }

      // Lógica de dibujo: Crea partículas blancas (estrellas) con movimiento vertical
      let stars = Array.from({length: 120}, () => ({
        x: Math.random() * window.innerWidth,
        y: Math.random() * 400,
        r: Math.random() * 1.5,
        v: Math.random() * 0.4
      }));

      function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "white";
        stars.forEach(s => {
          ctx.beginPath();
          ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
          ctx.fill();
          s.y += s.v; // Controla la velocidad de caída
          if (s.y > canvas.height) s.y = 0; // Reinicia la estrella arriba
        });
        requestAnimationFrame(animate);
      }

      window.addEventListener('resize', resize);
      resize();
      animate();
    }
  });
</script>