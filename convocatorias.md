---
layout: single
title: "Convocatorias GIDA"
permalink: /convocatorias/
header:
  overlay_color: "#05070a"
---

<style>
  .convocatoria-card {
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    border-left: 8px solid;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    background: #fff;
  }
  .estado-abierta { border-left-color: #27ae60; } /* Verde */
  .estado-cerrada { border-left-color: #7f8c8d; opacity: 0.7; } /* Gris */
  .btn-gida {
    background: #950001;
    color: white !important;
    padding: 8px 15px;
    border-radius: 5px;
    text-decoration: none;
    display: inline-block;
    margin-top: 10px;
  }
</style>

Aquí encontrarás las oportunidades vigentes para unirte a nuestros proyectos de investigación.

{% for conv en site.data.convocatorias %}
  <div class="convocatoria-card {% if conv.estado == 'Abierta' %}estado-abierta{% else %}estado-cerrada{% endif %}">
    <h3 style="margin-top: 0;">{{ conv.titulo }}</h3>
    <p><strong>Estado:</strong> {{ conv.estado }} | <strong>Cierre:</strong> {{ conv.fecha_cierre }}</p>
    <p>{{ conv.descripcion }}</p>
    
    {% if conv.estado == 'Abierta' %}
      <a href="{{ conv.link_inscripcion }}" class="btn-gida" target="_blank">Postularme ahora</a>
    {% else %}
      <span style="color: #888; font-style: italic;">Convocatoria finalizada</span>
    {% endif %}
  </div>
{% endfor %}