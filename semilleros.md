---
layout: single
title: "Semilleros GIDA"
permalink: /semilleros/
author_profile: true
header:
  overlay_color: "#05070a"
  caption: "Formación y Divulgación Aeroespacial"
---

<div id="mi-header-espacial" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;">
  <canvas id="canvas-estrellas"></canvas>
</div>

<style>
  header.page__hero--overlay, .page__hero--overlay {
    position: relative !important;
    background-color: #05070a !important;
    overflow: hidden;
  }
  .page__hero-content, .wrapper { position: relative; z-index: 5; }

  /* TABLA DE PROGRAMACIÓN */
  .tabla-semillero {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 10px;
    overflow: hidden;
    margin: 30px 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  }
  .tabla-semillero th {
    background: #950001;
    color: white;
    padding: 15px;
    text-align: left;
  }
  .tabla-semillero td { padding: 12px 15px; border-bottom: 1px solid #eee; }

  /* GRID DE YOUTUBE */
  .yt-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 20px;
  }
  .yt-card {
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    transition: 0.3s;
    border: 1px solid #eee;
  }
  .yt-card:hover { transform: translateY(-5px); border-color: #ff0000; }
  .yt-thumb {
    width: 100%; height: 150px;
    background-size: cover;
    background-position: center;
    display: flex; align-items: center; justify-content: center;
  }
  .yt-overlay {
    background: rgba(255,0,0,0.8);
    color: white; padding: 4px 10px;
    border-radius: 4px; font-size: 0.75em; font-weight: bold;
  }
  .yt-info { padding: 15px; }
  .yt-title { font-weight: bold; color: #333; text-decoration: none; font-size: 0.95em; }
  
  .btn-yt {
    background: #ff0000; color: white !important;
    padding: 12px 25px; border-radius: 30px;
    text-decoration: none; display: inline-block;
    font-weight: bold; margin-top: 30px;
  }
</style>

El semillero es la puerta de entrada al GIDA. Aquí formamos a los próximos ingenieros y científicos mediante sesiones teórico-prácticas.

## 📅 Próximas Sesiones Presenciales
*Las fechas se actualizan semestralmente según el calendario académico.*

<table class="tabla-semillero">
  <thead>
    <tr>
      <th>Fecha</th>
      <th>Tema</th>
      <th>Conferencista</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>TBD</td><td>Introducción y Bienvenida</td><td>Líderes GIDA</td></tr>
    <tr><td>TBD</td><td>Principios de Propulsión</td><td>Área de Motores</td></tr>
    <tr><td>TBD</td><td>Diseño y Simulación</td><td>Área de Estructuras</td></tr>
    <tr><td>TBD</td><td>Electrónica y Telemetría</td><td>Área de Control</td></tr>
    <tr><td>TBD</td><td>Lanzamiento Experimental</td><td>Equipo de Logística</td></tr>
  </tbody>
</table>

---

## 📺 Playlists Principales
Explora el contenido estructurado de nuestros semilleros anteriores.

<div class="yt-grid">
  <div class="yt-card">
    <div class="yt-thumb" style="background-image: url('https://img.youtube.com/vi/E8WInJ_wXzE/0.jpg');">
       <div class="yt-overlay">PLAYLIST OFICIAL</div>
    </div>
    <div class="yt-info">
      <a href="https://www.youtube.com/playlist?list=PLW-x_Z6ObeI0u0m_E7vAia5mREOAtRk5p" class="yt-title" target="_blank">Semillero Ciencias Aeroespaciales</a>
    </div>
  </div>

  <div class="yt-card">
    <div class="yt-thumb" style="background-image: url('https://img.youtube.com/vi/v5u7p0z_oA0/0.jpg');">
       <div class="yt-overlay">CURSO COMPLETO</div>
    </div>
    <div class="yt-info">
      <a href="https://www.youtube.com/playlist?list=PLW-x_Z6ObeI3PqZzX6I_7zUv75E9Z8S7k" class="yt-title" target="_blank">Semillero Ciencia y Tecnología</a>
    </div>
  </div>

  <div class="yt-card">
    <div class="yt-thumb" style="background-image: url('https://img.youtube.com/vi/p8kM7AueW48/0.jpg');">
       <div class="yt-overlay">TALLER PRÁCTICO</div>
    </div>
    <div class="yt-info">
      <a href="https://www.youtube.com/playlist?list=PLW-x_Z6ObeI0Vp7X7u_eS_L-v0YV_mPZ4" class="yt-title" target="_blank">Cohetería de Agua (Kits GIDA)</a>
    </div>
  </div>
</div>

## 🎥 Contenido Adicional
Videos de lanzamientos, eventos y tutoriales rápidos.

<div class="yt-grid">
  <div class="yt-card">
    <div class="yt-thumb" style="background-image: url('https://img.youtube.com/vi/Yf84U0A7x60/0.jpg');">
       <div class="yt-overlay">EXTRAS</div>
    </div>
    <div class="yt-info">
      <a href="https://www.youtube.com/@CohetesdeaguaGIDAUN/videos" class="yt-title" target="_blank">Videos y Lanzamientos Recientes</a>
    </div>
  </div>
</div>

<center>
  <a href="https://www.youtube.com/@CohetesdeaguaGIDAUN" class="btn-yt" target="_blank">
    <i class="fab fa-youtube"></i> SUSCRÍBETE AL CANAL
  </a>
</center>

<script>
  document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('canvas-estrellas');
    const ctx = canvas.getContext('2d');
    const header = document.querySelector('.page__hero--overlay') || document.querySelector('header');
    const container = document.getElementById('mi-header-espacial');

    if (header && container) {
      header.appendChild(container);
      function resize() {
        canvas.width = header.offsetWidth;
        canvas.height = header.offsetHeight;
      }
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
          ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2); ctx.fill();
          s.y += s.v;
          if (s.y > canvas.height) s.y = 0;
        });
        requestAnimationFrame(animate);
      }
      window.addEventListener('resize', resize);
      resize(); animate();
    }
  });
</script>