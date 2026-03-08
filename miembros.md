---
layout: single
title: "Miembros del GIDA"
permalink: /miembros/
author_profile: true
header:
  overlay_color: "#05070a" # Mantenemos el fondo negro para las estrellas
---

<div id="mi-header-espacial" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;">
  <canvas id="canvas-estrellas"></canvas>
</div>

<style>
  /* Ajustes del Header */
  .page__hero--overlay { position: relative !important; background-color: #05070a !important; overflow: hidden; }
  .page__hero-content { position: relative; z-index: 5; }

  /* 2. DISEÑO DE TARJETAS DE MIEMBROS */
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 25px;
    margin-top: 40px;
  }

  .member-card {
    background: #ffffff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    text-align: center;
    padding-bottom: 20px;
    border: 1px solid #e1e1e1;
  }

  .member-card:hover {
    transform: translateY(-10px); /* Efecto de elevación profesional */
  }

  .member-img {
    width: 100%;
    height: 200px;
    object-fit: cover; /* Ajusta la foto al contenedor */
    background: #eee;
  }

  .member-info { padding: 15px; }
  
  .member-name { font-weight: bold; font-size: 1.2em; color: #222; margin-bottom: 5px; }
  
  .member-role { 
    color: #d35400; /* Color distintivo para el área de trabajo */
    font-weight: 600; 
    font-size: 0.9em; 
    text-transform: uppercase;
    margin-bottom: 10px;
  }

  .member-detail { font-size: 0.85em; color: #666; margin: 2px 0; }
  
  .member-email { 
    display: inline-block;
    margin-top: 10px;
    font-size: 0.85em;
    color: #2980b9;
    text-decoration: none;
  }
</style>

Nuestro equipo está conformado por estudiantes y profesionales apasionados por el desarrollo aeroespacial en Colombia.

<div class="team-grid">
  
  <div class="member-card">
    <img src="{{ '/assets/images/miembros/foto1.jpg' | relative_url }}" class="member-img" alt="Nombre del Miembro">
    <div class="member-info">
      <div class="member-name">Nombre Apellido</div>
      <div class="member-role">Área de Propulsión</div>
      <div class="member-detail">Ingeniería Mecánica</div>
      <a href="mailto:correo@unal.edu.co" class="member-email">correo@unal.edu.co</a>
    </div>
  </div>

  </div>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('canvas-estrellas');
    const ctx = canvas.getContext('2d');
    const header = document.querySelector('.page__hero--overlay') || document.querySelector('header');
    const container = document.getElementById('mi-header-espacial');

    if (header && container) {
      header.appendChild(container);
      function resize() { canvas.width = header.offsetWidth; canvas.height = header.offsetHeight; }
      let stars = Array.from({length: 120}, () => ({
        x: Math.random() * window.innerWidth, y: Math.random() * 400, r: Math.random() * 1.5, v: Math.random() * 0.4
      }));
      function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); ctx.fillStyle = "white";
        stars.forEach(s => {
          ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2); ctx.fill();
          s.y += s.v; if (s.y > canvas.height) s.y = 0;
        });
        requestAnimationFrame(animate);
      }
      window.addEventListener('resize', resize); resize(); animate();
    }
  });
</script>