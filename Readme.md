![](https://i.ytimg.com/vi/kBbKf9wliuc/sddefault.jpg)

# FinanceApp usando FastAPI CRUD con SQLAlchemy, Alembic, PostgreSQL y React.js

FinanceApp es una apliacación que te ayuda a llevar un registro de los gastos e ingresos. Podrás crear trantos registros como quieras, editarlos y borrarlos.

###Recomendaciones

> Recuerda crear y activar tu entorno virtual antes de instalar los requerimientos.

## Setup

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Python (versión 3.9) o superior.
- Dependencias: se incluyen en el repo.

## Instalación

Sigue estos pasos para configurar el entorno y ejecutar el proyecto:

1. Clona el repositorio desde GitHub:

   ```
   git clone https://github.com/Margumedo/Practica-Finance-app-React-FastApi.git
   ```

2. Navega al directorio del proyecto:

   cd tu-repositorio

3. Crea un entorno virtual (recomendado):

   ```
   python -m virtual venv
   ```

4. Activa el entorno virtual:

- En Windows:

  ```
  venv\Scripts\activate
  ```

- En macOS y Linux:

  ```
  source venv/bin/activate
  ```

5. **Installation of Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

# Database Setup

Instalar PostgreSQL y arrancar el servidor de la base de datos. Crear una nueva base de datos PostgreSQL. Copiar `.env.example` a `.env` y llenar los valores de la variable de entorno de la URL de conexión a la base de datos y otros valores necesarios.

# Running the Application

Executar la aplicación con `uvicorn main:app --reload`:

```bash
 uvicorn main:app --reload
```

Esto iniciará tu aplicación FastAPI y estará disponible en la dirección http://localhost:8000 para interactuar con la API a través de la interfaz de documentación generada automáticamente por FastAPI.

# API Endpoints

## Transactions

Create: `POST /transaction/`

Read: `GET /transactions/`

Update: `PUT /transaction{transaction_id}`

Delete: `DELETE /transaction/{transaction_id}`

Create: `POST /orders/`

# Testing

Utilizar herramientas como curl o Postman para probar las solicitudes API. También se pueden agregar pruebas unitarias con pytest.

# React

Para arrancar el frontend del apliación es necesario instalar axios con el siguiente comando:
`npm install axios`

Executar la aplicación con
`npm start`

Esto iniciará tu aplicación React y estará disponible en la dirección http://localhost:3000 para interactuar
