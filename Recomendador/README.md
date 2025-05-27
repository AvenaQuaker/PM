# Recomendador de Canciones 🎵

Este proyecto es una aplicación web de recomendación de canciones, desarrollada con **FastAPI**, **MongoDB** y un frontend moderno usando **TailwindCSS** y **SwiperJS**. Permite a los usuarios registrarse, iniciar sesión y recibir recomendaciones personalizadas de música según sus preferencias, emociones y artistas favoritos.

## Características principales

- Registro e inicio de sesión de usuarios.
- Recomendaciones de canciones basadas en géneros, emociones y artistas.
- Visualización de playlist personal y canciones recientes.
- Interfaz moderna y responsiva.
- Integración con MongoDB para almacenamiento de usuarios y canciones.

## Estructura del proyecto

```
Recomendador/
├── app/
│   ├── static/           # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/        # Plantillas HTML (Jinja2)
│   ├── models/           # Modelos y acceso a base de datos
│   ├── main.py           # Punto de entrada FastAPI
│   └── ...
├── requirements.txt      # Dependencias del backend
├── package.json          # Dependencias del frontend (opcional)
└── README.md             # Este archivo
```

## Instalación

1. **Clona el repositorio:**
   ```
   git clone [https://github.com/AvenaQuaker/PM.git]
   cd Recomendador
   ```

2. **Instala las dependencias de Python:**
   ```
   pip install -r requirements.txt
   ```

3. **Configura la base de datos MongoDB:**
   - Asegúrate de tener una instancia de MongoDB en ejecución.
   - Actualiza la cadena de conexión en los archivos correspondientes si es necesario.

4. **Ejecuta la aplicación:**
   ```
   .venv\Scripts\Activate.ps1          
   uvicorn app.main:app --reload
   ```

5. **Accede a la aplicación:**
   - Abre tu navegador en [http://localhost:8000](http://localhost:8000)

## Tecnologías utilizadas

- **Backend:** FastAPI, Motor (MongoDB async), Pydantic
- **Frontend:** HTML, TailwindCSS, SwiperJS, JavaScript
- **Base de datos:** MongoDB

## Créditos

Desarrollado por Jaime Aquino y Mario Alberto   
Proyecto académico para la materia de Programación Multiparadigma.

