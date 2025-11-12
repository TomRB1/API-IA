ul documentados automáticamente con Swagger.

Tecnologías utilizadas

FastAPI (framework backend en Python)

Supabase (base de datos PostgreSQL)

psycopg (driver para conexión a PostgreSQL)

Vercel (plataforma de despliegue serverless)

python-dotenv (manejo de variables de entorno)

Estructura del proyecto

API-IA/
├── main.py
├── routes/
│ ├── cliente.py
│ ├── marca.py
│ ├── categoria.py
│ ├── componente.py
│ └── pedido.py
├── managers/
│ ├── cliente_manager.py
│ ├── marca_manager.py
│ ├── categoria_manager.py
│ ├── componente_manager.py
│ └── pedido_manager.py
├── models/
│ ├── cliente_model.py
│ ├── marca_model.py
│ ├── categoria_model.py
│ ├── componente_model.py
│ └── pedido_model.py
├── utils/
│ └── db.py
├── vercel.json
├── requirements.txt
└── .env

Endpoints principales

Cliente → /clientes/
Marca → /marcas/
Categoría → /categorias/
Componente → /componentes/
Pedido → /pedidos/

Todos los endpoints cuentan con documentación automática en /docs.

Deploy

El proyecto está desplegado en Vercel con conexión directa a Supabase.
Documentación Swagger: https://tu-proyecto.vercel.app/docs

(reemplazar con la URL real de Vercel)

Cómo ejecutar localmente

Clonar el repositorio
git clone https://github.com/TuUsuario/API-IA.git

cd API-IA

Crear entorno virtual
python -m venv venv
source venv/bin/activate (Linux/Mac)
venv\Scripts\activate (Windows)

Instalar dependencias
pip install -r requirements.txt

Crear archivo .env
DATABASE_URL=postgresql://usuario:contraseña@host:5432/postgres

Ejecutar servidor
uvicorn main:app --reload

Abrir navegador
http://127.0.0.1:8000/docs

Estructura lógica

models → define los esquemas Pydantic (validación y respuesta)
managers → contiene la lógica de acceso a la base de datos (CRUD)
routes → define los endpoints que interactúan con los managers
utils/db.py → maneja la conexión a Supabase mediante psycopg

Créditos

Desarrollado por Tom, con asistencia de inteligencia artificial.
Proyecto final CRUD + API + IA, hecho con dedicación y muchas líneas de código.
