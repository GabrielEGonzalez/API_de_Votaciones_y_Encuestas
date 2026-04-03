---

# Sistema de Votaciones y Encuestas API

API RESTful para la gestión de encuestas y votaciones. Permite a los usuarios crear encuestas, votar y consultar resultados en tiempo real, replicando funcionalidades presentes en sistemas de opinión pública.

---

## Objetivo del proyecto

Este proyecto tiene como finalidad implementar un sistema backend completo que abarque:

* Diseño de base de datos relacional
* Definición de relaciones entre tablas
* Implementación de operaciones CRUD
* Desarrollo de lógica de negocio
* Construcción de endpoints con FastAPI
* Generación de estadísticas mediante consultas SQL

---

## Tecnologías utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite (compatible con otros motores SQL)

---

## Modelo de datos

### Usuarios

Tabla: `usuarios`

Campos:

* id
* nombre
* correo
* password
* fecha_creacion

---

### Encuestas

Tabla: `encuestas`

Campos:

* id
* titulo
* descripcion
* creador_id (FK usuario)
* fecha_creacion
* activa (boolean)

Relación:

* Un usuario puede crear múltiples encuestas (1:N)

---

### Opciones

Tabla: `opciones`

Campos:

* id
* encuesta_id (FK)
* texto

Cada encuesta contiene múltiples opciones.

Ejemplo:

¿Cuál lenguaje prefieres?

1. Python
2. JavaScript
3. Go
4. Rust

---

### Votos

Tabla: `votos`

Campos:

* id
* usuario_id (FK)
* opcion_id (FK)
* fecha

Restricción:

* Un usuario solo puede votar una vez por encuesta

---

## Endpoints

### Usuarios

* POST `/usuarios`
  Crea un nuevo usuario

* POST `/login`
  Autenticación básica (retorna token o identificador)

---

### Encuestas

* POST `/encuestas`
  Crea una nueva encuesta junto con sus opciones

Ejemplo de entrada:

```json
{
  "titulo": "Lenguaje favorito",
  "descripcion": "Encuesta de programación",
  "opciones": [
    "Python",
    "JavaScript",
    "Go",
    "Rust"
  ]
}
```

Funcionalidad:

* Crea la encuesta
* Genera automáticamente las opciones

---

* GET `/encuestas`
  Lista todas las encuestas

* GET `/encuestas/{id}`
  Obtiene una encuesta con sus opciones

Ejemplo de respuesta:

```json
{
  "titulo": "Lenguaje favorito",
  "descripcion": "Encuesta de programación",
  "opciones": [
    {"id": 1, "texto": "Python"},
    {"id": 2, "texto": "JavaScript"}
  ]
}
```

---

### Votación

* POST `/votar`

Ejemplo de entrada:

```json
{
  "usuario_id": 2,
  "opcion_id": 5
}
```

Validaciones:

* El usuario existe
* La opción existe
* El usuario no ha votado previamente en esa encuesta

---

### Resultados

* GET `/encuestas/{id}/resultados`

Ejemplo de salida:

```
Python: 15 votos  
JavaScript: 10 votos  
Go: 4 votos  
Rust: 2 votos  
```

Implementación basada en consultas SQL con `GROUP BY`.

---

## Funcionalidades avanzadas

* GET `/encuestas/top`
  Obtiene las encuestas más votadas

* Conteo de votos por encuesta mediante `JOIN` y `COUNT`

* GET `/usuarios/{id}/encuestas`
  Lista encuestas creadas por un usuario

* Consulta de encuestas sin votos

---

## Estructura del proyecto

```bash
app/
│
├── routers/
│   ├── usuarios_router.py
│   ├── encuestas_router.py
│   └── votos_router.py
│
├── services/
│   ├── usuario_service.py
│   ├── encuesta_service.py
│   └── voto_service.py
│
├── repositories/
│   ├── usuario_repo.py
│   ├── encuesta_repo.py
│   └── voto_repo.py
│
├── models/
│   ├── usuario_model.py
│   ├── encuesta_model.py
│   ├── opcion_model.py
│   └── voto_model.py
│
├── schemas/
│   ├── usuario_schema.py
│   ├── encuesta_schema.py
│   └── voto_schema.py
│
├── database.py
└── main.py
```

Arquitectura basada en separación de responsabilidades:

* Routers: definición de endpoints
* Services: lógica de negocio
* Repositories: acceso a datos
* Models: definición de tablas
* Schemas: validación de datos

---

## Consultas SQL implementadas

* JOIN
* COUNT
* GROUP BY
* EXISTS
* UNIQUE
* FOREIGN KEY
* INDEX

---

## Mejoras propuestas

* Autenticación mediante JWT
* Encuestas con fecha de cierre (`fecha_fin`)
* Validación de encuestas activas/inactivas
* Ranking de opciones por número de votos
* Optimización de consultas
* Escalabilidad hacia motores como PostgreSQL

---

## Ejecución del proyecto

```bash
uvicorn main:app --reload
```

---

## Licencia

Este proyecto está bajo la licencia MIT.

---
