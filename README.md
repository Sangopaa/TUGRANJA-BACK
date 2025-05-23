# TU GRANJA - BACKEND

Este es el backend de TU GRANJA, una API RESTful construida con Flask, SQLAlchemy y Marshmallow para la gestión de granjas, usuarios, animales, variables y grupos.

## Características

- API RESTful con Flask y Flask-RESTful
- ORM con SQLAlchemy
- Serialización y validación con Marshmallow
- Migraciones de base de datos con Alembic
- Pruebas automatizadas con Pytest y Factory Boy
- Docker y Docker Compose para desarrollo y despliegue
- Soporte para múltiples entornos (producción y testing)

## Estructura del Proyecto

```
.
├── app.py
├── config.py
├── core/
├── models/
├── model_queries/
├── schemas/
├── shared/
├── views/
├── tests/
├── migrations/
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── Makefile
└── README.md
```

## Configuración

1. **Variables de entorno**  
   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

   ```
   MYSQL_DATABASE_USER=
   MYSQL_DATABASE_PASSWORD=
   MYSQL_DATABASE_HOST=
   MYSQL_DATABASE_PORT=
   MYSQL_DATABASE_DB=
   MYSQL_DATABASE_DB_TEST=
   TESTING=
   ```

2. **Instalación de dependencias**

   ```sh
   pip install -r requirements.txt
   ```

3. **Uso con Docker**

   - Levanta los servicios:

     ```sh
     make up
     ```

   - Crea la base de datos:

     ```sh
     make create_db
     ```

   - Ejecuta migraciones:

     ```sh
     make run_migrations
     ```

   - Ejecuta las pruebas:

     ```sh
     make test
     ```

## Endpoints Principales

- `GET /ping` — Verifica que el servicio está activo.
- `GET /farms` — Lista paginada de granjas.
- `GET /farm/<farm_id>` — Detalle de una granja.
- `POST /farm` — Crea una nueva granja.

## Pruebas

Las pruebas están en el directorio [`tests/`](tests/). Puedes ejecutarlas con:

```sh
make test
```

## Migraciones

Las migraciones se gestionan con Alembic. Para crear una nueva migración:

```sh
make create_migration message="mensaje de la migración"
```

## Licencia

MIT

---

Desarrollado por TU GRANJA.