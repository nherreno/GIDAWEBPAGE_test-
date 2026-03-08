---
layout: single
title: "Convocatorias GIDA"
permalink: /convocatorias/
---

Aquí encontrarás las oportunidades para unirte a nuestros proyectos.

<div class="convocatorias-container">
{% if site.data.convocatorias %}
  {% for conv in site.data.convocatorias %}
    <div style="border-radius: 10px; padding: 20px; margin: 20px 0; border-left: 8px solid {% if conv.estado == 'Abierta' %}#27ae60{% else %}#7f8c8d{% endif %}; box-shadow: 0 2px 10px rgba(0,0,0,0.1); background: #ffffff; color: #333;">
      <h3 style="margin-top: 0; color: #000;">{{ conv.titulo }}</h3>
      <p style="margin-bottom: 5px;">
        <strong>Estado:</strong> 
        <span style="color: {% if conv.estado == 'Abierta' %}#27ae60{% else %}#7f8c8d{% endif %}; font-weight: bold;">
          {{ conv.estado }}
        </span> 
        | <strong>Cierre:</strong> {{ conv.fecha_cierre }}
      </p>
      <p>{{ conv.descripcion }}</p>
      
      {% if conv.estado == 'Abierta' %}
        <a href="{{ conv.link_inscripcion }}" style="background: #950001; color: white !important; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block; font-weight: bold;" target="_blank">Postularme ahora</a>
      {% else %}
        <p style="color: #888; font-style: italic; margin-top: 10px;">🚫 Convocatoria finalizada</p>
      {% endif %}
    </div>
  {% endfor %}
{% else %}
  <p>No hay convocatorias registradas en este momento.</p>
{% endif %}
</div>