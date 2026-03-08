---
layout: single
title: "Convocatorias GIDA"
permalink: /convocatorias/
header:
  overlay_color: "#05070a"
  overlay_filter: 0.5
---

<style>
  .convocatorias-container {
    margin-top: 20px;
  }
  .card-gida {
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    background: #ffffff;
    transition: transform 0.3s ease;
    border-left: 10px solid #7f8c8d; /* Color por defecto (Cerrada) */
  }
  .card-gida:hover {
    transform: translateY(-5px);
  }
  .card-abierta {
    border-left-color: #27ae60 !important;
  }
  .status-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8em;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 10px;
  }
  .badge-abierta { background: #e8f5e9; color: #2e7d32; }
  .badge-cerrada { background: #f5f5f5; color: #616161; }
  
  .btn-postular {
    background: #950001;
    color: white !important;
    padding: 10px 25px;
    border-radius: 6px;
    text-decoration: none;
    display: inline-block;
    font-weight: bold;
    margin-top: 15px;
    border: none;
  }
  .btn-postular:hover {
    background: #7a0000;
  }
</style>

Aquí encontrarás las oportunidades vigentes y el histórico de procesos para unirte a nuestro grupo de investigación.

<div class="convocatorias-container">
{% if site.data.convocatorias %}
  {% for conv in site.data.convocatorias %}
    <div class="card-gida {% if conv.estado == 'Abierta' %}card-abierta{% endif %}">
      
      <div class="status-badge {% if conv.estado == 'Abierta' %}badge-abierta{% else %}badge-cerrada{% endif %}">
        {{ conv.estado }}
      </div>

      <h2 style="margin: 10px 0; color: #333;">{{ conv.titulo }}</h2>
      
      <p style="color: #666; font-size: 0.9em;">
        <i class="fas fa-calendar-alt"></i> <strong>Fecha de cierre:</strong> {{ conv.fecha_cierre }}
      </p>

      <p style="line-height: 1.6;">{{ conv.descripcion }}</p>

      {% if conv.estado == 'Abierta' %}
        <a href="{{ conv.link_inscripcion }}" class="btn-postular" target="_blank">
          <i class="fas fa-paper-plane"></i> Postularme ahora
        </a>
      {% else %}
        <div style="margin-top: 15px; color: #888; font-style: italic;">
          <i class="fas fa-lock"></i> Este proceso ha finalizado.
        </div>
      {% endif %}
    </div>
  {% endfor %}
{% else %}
  <div class="notice--warning">
    <p>Actualmente no hay convocatorias registradas en el sistema de datos.</p>
  </div>
{% endif %}
</div>