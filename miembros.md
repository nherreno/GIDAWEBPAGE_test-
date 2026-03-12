---
# BLOQUE 1: CONFIGURACIÓN (Front Matter)
# No cambiar a menos que quieras otra URL o Título.
layout: single
title: "Miembros del GIDA"
permalink: /miembros/
author_profile: true
header:
  overlay_color: "#05070a" 
---

<div id="mi-header-espacial" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;">
  <canvas id="canvas-estrellas"></canvas>
</div>

<style>
  /* BLOQUE 3: ESTILOS CSS (Diseño de Tarjetas) */
  /* Cámbialo si quieres que las tarjetas se vean distintas */
  .page__hero--overlay { position: relative !important; background-color: #05070a !important; overflow: hidden; }
  .seccion-titulo { border-bottom: 2px solid #d35400; margin: 50px 0 30px; color: #2c3e50; font-size: 1.8em; }
  
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); 
    gap: 25px;
  }

  .member-card {
    background: #ffffff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    text-align: center; overflow: hidden; border: 1px solid #e1e1e1; transition: 0.3s;
  }
  .member-card:hover { transform: translateY(-10px); }
  .member-img { width: 100%; height: 220px; object-fit: cover; }
</style>

<h2 class="seccion-titulo">Estudiantes de Pregrado</h2>
<div class="team-grid">
  {% assign pregrado = site.data.miembros | where: "tipo", "pregrado" %}
  {% for miembro in pregrado %}
  <div class="member-card">
    <img src="{{ miembro.foto | relative_url }}" class="member-img">
    <div style="padding:15px;">
      <div style="font-weight:bold;">{{ miembro.nombre }}</div>
      <div style="color:#d35400; font-weight:bold;">{{ miembro.area }}</div>
      <div style="font-size:0.85em;">{{ miembro.carrera }}</div>
      <a href="mailto:{{ miembro.correo }}" style="font-size:0.8em; color:#2980b9;">{{ miembro.correo }}</a>
    </div>
  </div>
  {% endfor %}
</div>
<h2 class="seccion-titulo">Estudiantes de Posgrado</h2>
<div class="team-grid">
  {% assign posgrado = site.data.miembros | where: "tipo", "posgrado" %}
  {% for miembro in posgrado %}
  <div class="member-card">
    <img src="{{ miembro.foto | relative_url }}" class="member-img">
    <div style="padding:15px;">
      <div style="font-weight:bold;">{{ miembro.nombre }}</div>
      <div style="color:#2980b9; font-weight:bold;">{{ miembro.area }}</div>
      <div style="font-size:0.85em;">{{ miembro.carrera }}</div>
      <a href="mailto:{{ miembro.correo }}" style="font-size:0.8em; color:#2980b9;">{{ miembro.correo }}</a>
    </div>
  </div>
  {% endfor %}
</div>
<h2 class="seccion-titulo">Egresados</h2>
<div class="team-grid">
  {% assign egresados = site.data.miembros | where: "tipo", "egresado" %}
  {% for miembro in egresados %}
  <div class="member-card">
    <img src="{{ miembro.foto | relative_url }}" class="member-img">
    <div style="padding:15px;">
      <div style="font-weight:bold;">{{ miembro.nombre }}</div>
      <div style="color:#7f8c8d; font-weight:bold;">{{ miembro.area }}</div>
      <div style="font-size:0.85em;">{{ miembro.carrera }}</div>
    </div>
  </div>
  {% endfor %}
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