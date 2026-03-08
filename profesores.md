---
layout: single
title: "Cuerpo Docente"
permalink: /profesores/
header:
  overlay_color: "#05070a"
---

<style>
  .profesor-card {
    max-width: 950px;
    margin: 40px auto;
    background: #fff;
    border-radius: 15px;
    display: flex;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    border-left: 10px solid #950001;
  }
  .profesor-sidebar { background: #fdfdfd; padding: 40px; text-align: center; flex: 1; border-right: 1px solid #eee; }
  .profesor-main { padding: 40px; flex: 2; }
  .profesor-photo { width: 180px; height: 180px; border-radius: 50%; object-fit: cover; border: 4px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
  .tag-is { background: #950001; color: #fff; padding: 4px 12px; border-radius: 20px; font-size: 0.75em; font-weight: bold; }
</style>

{% for profe in site.data.profesores %}
<div class="profesor-card">
  <div class="profesor-sidebar">
    <img src="{{ profe.foto | relative_url }}" class="profesor-photo">
    <h2 style="margin: 15px 0 5px;">{{ profe.nombre }}</h2>
    <span class="tag-is">{{ profe.cargo }}</span>
    <p style="margin-top: 15px; font-size: 0.9em; color: #333;">{{ profe.correo }}</p>
  </div>

  <div class="profesor-main">
    <h3 style="color: #950001; margin-top: 0;">Perfil Profesional</h3>
    <p style="text-align: justify; line-height: 1.6;">{{ profe.perfil }}</p>
    
    <h4 style="border-bottom: 1px solid #eee; padding-bottom: 5px;">Formación Académica</h4>
    <ul style="list-style: none; padding: 0; font-size: 0.9em;">
      {% for estudio in profe.estudios %}
      <li style="margin-bottom: 15px;">
        <i class="fas fa-graduation-cap"></i> <strong>{{ estudio.grado }}</strong><br>
        <span style="color: #666;">{{ estudio.institucion }}</span><br>
        <small style="font-style: italic;">Tesis: {{ estudio.tesis }}</small>
      </li>
      {% endfor %}
    </ul>
  </div>
</div>
{% endfor %}