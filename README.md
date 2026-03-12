GidaWebPage
Officiall Web page for GIDA UN vamos a usar una plantilla llamada jekyll de minimal mistakes , para las personas que mas adelante desarrollen codigo, posteriormente , quizas nos toque hacer nmodificaciones , voy a crear un repo de prueba en Github , actualizare el link, para que clonen la plantilla y adicional , pues trabajen sobre algo , ya mas sugerido para GIDA link https://github.com/nherreno/GIDAWEBPAGE_test- link visualizar: https://nherreno.github.io/GIDAWEBPAGE_test-/ si hay algun problema para editar o acceder a este repo , escribir a nherreno@unal.edu.co, posdata mas adelante generaremos el link de la pagina oficial 

1. Configuración del Motor (Gemfile)
Lo primero que se realizó fue modificar el archivo Gemfile para asegurar la compatibilidad con los servidores de GitHub.

Se definieron las librerías base: github-pages y el plugin jekyll-include-cache.

Esto permitió que las GitHub Actions dejaran de marcar error y pudieran compilar el sitio correctamente.

2. Identidad y Rutas (_config.yml)
Posteriormente, modificamos el archivo maestro de configuración para darle identidad al grupo:

Identidad: Se cambió el título a "GIDA UNAL" y se ajustó la biografía del autor con los datos del grupo.

Skin: Se seleccionó el tema visual air, que ofrece un fondo gris claro más profesional que el predeterminado.

Rutas Críticas: Se configuró el baseurl como "/GIDAWEBPAGE_test-". Sin este paso, el navegador no encontraba los archivos de estilo y la página se veía como texto plano.

3. Estructura de Navegación (_data/navigation.yml)
Para organizar la información, creamos un sistema de pestañas en la parte superior derecha:

Se eliminaron los links de ejemplo del tema original (como el "Quick-Start Guide").

Se añadieron los accesos directos estratégicos: Profesores, Proyectos de Investigación, Miembros, Publicaciones, Convocatorias y Semilleros.

NOTA:index  permite modificar como la pantallaza de inicio por partes , ya de manera mas tecnica hace parte del front 
------------------------------------------------------------------------------------------------------------------------------------------

🛠️ Estado Actual: Refinando el Inicio
Actualmente, nos encontramos en la fase de pulir la Página de Inicio (index.md).

El objetivo es pasar de una lista simple de entradas a un diseño de alto impacto visual con cabeceras y una biografía de autor completa en la barra lateral.

Nota: El paso de creación de archivos individuales para cada pestaña del menú aún no se ha ejecutado, priorizando la estabilidad y estética de la fachada principal.



se creo una carpeta en assets que guarda las imagenes de recuerdos , y se implemento recuerdos.md la parte de container es la que vamos a modificar para que sea dinamica cada vez que cargemos va a generarse de manera aleatoria el orden de las imagenes 
Aquí tienes el README.md actualizado. He mantenido la estructura de tu archivo original, pero en lugar de tratarlo como un proyecto nuevo, lo he redactado como una bitácora de progreso continuo, documentando cómo evolucionamos desde la plantilla base hasta el sistema automatizado y corregido que tienes ahora.

GIDA WebPage - Bitácora de Desarrollo y Evolución
Este proyecto es la evolución oficial del portal del GIDA, desarrollado sobre Jekyll con el tema Minimal Mistakes. A continuación, se detalla el progreso técnico alcanzado, integrando las soluciones a los problemas de migración y las nuevas automatizaciones.

📈 Progreso y Mejoras Implementadas
1. Estabilidad de Infraestructura (Post-Migración)
Tras las primeras pruebas en el repositorio GIDAWEBPAGE_test-, el despliegue oficial presentó retos de configuración que fueron resueltos:

Corrección de Rutas Críticas: Se identificó que el baseurl en el _config.yml causaba que la página perdiera sus estilos CSS al cambiar de repositorio. Actualmente, el archivo _config.yml tiene comentadas las rutas del sitio de prueba para permitir una transición rápida si se requiere volver a testear.

Sincronización del Menú: Se restauraron las secciones de Profesores, Miembros y Recuerdos vinculando correctamente el archivo _data/navigation.yml con el motor de Jekyll, evitando que las pestañas desaparecieran en el sitio oficial.

2. Automatización "Todoterreno" (Python + GitHub Actions)
Para que el grupo pueda actualizar datos sin tocar el código fuente, se implementó un flujo de trabajo inteligente:

Script de Conversión Dinámica: Se creó convertir_datos.py, un script que procesa archivos CSV/Excel ignorando errores de formato comunes (como el uso de comas vs puntos y comas).

Blindaje de Caracteres: El sistema fuerza la codificación UTF-8, permitiendo que los nombres con tildes o caracteres especiales no bloqueen el proceso de construcción de la web (Build error).

Actualización Silenciosa: Al subir un CSV, GitHub Actions ejecuta el script, genera el YAML y actualiza la web automáticamente.

3. Lógica Avanzada de Convocatorias
La sección de convocatorias dejó de ser una lista estática para convertirse en un sistema de semáforo visual:

Normalización con Downcase: El código ahora es "insensible" a mayúsculas. Detecta estados como "ABIERTA" o "abierta" por igual, eliminando errores de visualización.

Sistema de Colores Dinámico:

Verde: Abierta con link de inscripción.

Amarillo: Abierta pero con link pendiente (el recuadro muestra "⚠️ No hay link disponible todavía").

Rojo: Convocatoria cerrada.

Coherencia Visual: Se sincronizó el color del Status Badge (recuadro de arriba) con el borde lateral de la tarjeta para una estética profesional.

4. Estética Aeroespacial (Header Espacial)
Para mantener la identidad del GIDA en todas las pestañas:

Canvas de Estrellas Sincronizado: Se integró el script de JavaScript que genera partículas animadas en Profesores, Miembros y Recuerdos.

Inyección de DOM: La lógica se ajustó para que el canvas se inyecte directamente en el elemento .page__hero--overlay, asegurando que el efecto espacial se vea detrás del título en cualquier tamaño de pantalla.

📁 Guía de Mantenimiento para Desarrolladores
Para continuar con el desarrollo sin romper la estabilidad lograda:

En el _config.yml: Si el repositorio cambia de nombre o de cuenta, actualiza inmediatamente el baseurl y la url. Los valores de prueba están marcados para referencia.

En _data/: Los archivos CSV deben mantener los encabezados originales (titulo, estado, link_inscripcion, etc.) para que el script de Python pueda procesarlos.

Sección Recuerdos: Para añadir fotos, súbelas a assets/images/recuerdos/. El código en recuerdos.md se encarga de barajarlas aleatoriamente en cada carga de página.

⚠️ Nota Técnica Final: La arquitectura actual prioriza la autonomía de los coordinadores. El uso de Python como puente entre Excel y Jekyll asegura que la página sea escalable y fácil de mantener a largo plazo.