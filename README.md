# 🧪 Práctica: El Explorador del Multiverso (APIs + Pandas)

**Asignatura:** Tecnología y Digitalización  
**Nivel:** 3º ESO  
**Objetivo:** Aprender a descargar datos reales de Internet y analizarlos.

---

## 1. Introducción: ¿Qué vamos a hacer?

Hoy dejamos de inventarnos datos. Vamos a conectarnos a una base de datos mundial para obtener información en tiempo real.

```text
datos_json (OBJETO / DICCIONARIO)  --> { }
│
├── "info": { ... }   (Otro objeto con info de paginación)
│
└── "results": [      (ARRAY / LISTA) --> [ ]
       │
       ├── { "id": 1, "name": "Rick Sanchez"... },  (Posición 0)
       ├── { "id": 2, "name": "Morty Smith"... },   (Posición 1)
       ├── { "id": 3, "name": "Summer Smith"... }   (Posición 2)
       ...
    ]
```

Para ello, usaremos dos herramientas nuevas:

1.  **`requests` (El Mensajero):** Una librería que "llama" a una página web y se trae la información.
2.  **`pandas` (El Excel con Esteroides):** Una herramienta profesional para ordenar datos desordenados y convertirlos en tablas perfectas.

**La Misión:** Crear una App que descargue los personajes de la serie **Rick y Morty**, nos permita filtrar quién está vivo o muerto, y analizar las especies.

---

## 2. Preparación del Entorno

Si estás en Replit o en tu ordenador, asegúrate de instalar las librerías necesarias escribiendo esto en la terminal (Shell):

```bash
pip install streamlit pandas requests
