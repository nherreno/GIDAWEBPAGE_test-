---
layout: single
title: "Convocatorias GIDA"
permalink: /convocatorias/
---

Aquí encontrarás las oportunidades para unirte a nuestros proyectos.

<div class="convocatorias-lista">
{% if site.data.convocatorias %}
  {% for item in site.data.convocatorias %}
    <div style="border-left: 10px solid {% if item.estado contains 'Abierta' %}#27ae60{% else %}#7f8c8d{% endif %}; padding: 20px; margin: 20px 0; background: #fff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
      <h3 style="margin-top: 0;">{{ item.titulo }}</h3>
      <p><strong>Estado:</strong> {{ item.estado }} | <strong>Cierre:</strong> {{ item.fecha_cierre }}</p>
      <p>{{ item.descripcion }}</p>
      {% if item.estado contains 'Abierta' %}
        <a href="{{ item.link_inscripcion }}" style="background: #950001; color: white !important; padding: 10px 15px; border-radius: 5px; text-decoration: none; font-weight: bold;">Postularme</a>
      {% endif %}
    </div>
  {% endfor %}
{% else %}
  <p>Esperando a que el robot genere los datos... (Sube tu CSV a la carpeta _data).</p>
{% endif %}
</div>