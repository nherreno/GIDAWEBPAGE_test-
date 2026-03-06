---
layout: single
title: "Recuerdos GIDA"
permalink: /recuerdos/
author_profile: true
header:
  overlay_color: "transparent"
---

<div id="starfield-rec" style="position: absolute; top: 0; left: 0; width: 100%; height: 300px; z-index: 0; background: #05070a; overflow: hidden;">
  <canvas id="canvas-rec"></canvas>
</div>

<style>
  .page__hero--overlay {
    background-color: transparent !important;
    height: 300px;
    position: relative;
    z-index: 1;
  }
  .page__hero-title {
    color: white !important;
  }
</style>

<script>
  const cRec = document.getElementById('canvas-rec');
  const ctxRec = cRec.getContext('2d');
  cRec.width = window.innerWidth; cRec.height = 300;
  let sRec = Array.from({length: 80}, () => ({x: Math.random()*cRec.width, y: Math.random()*cRec.height, s: Math.random()*1.5}));
  function animRec() {
    ctxRec.clearRect(0,0,cRec.width,cRec.height);
    ctxRec.fillStyle = 'white';
    sRec.forEach(s => {
      ctxRec.beginPath(); ctxRec.arc(s.x, s.y, s.s, 0, Math.PI*2); ctxRec.fill();
      s.y += 0.3; if(s.y > 300) s.y = 0;
    });
    requestAnimationFrame(animRec);
  }
  animRec();
</script>

*(Aquí debajo pegas tu código de la galería y el texto que ya tenías)*