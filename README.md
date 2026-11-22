# Python Backend Project

A product inventory application with a **FastAPI backend**, **SQLAlchemy ORM**, and a **PostgreSQL** database. This repository also contains a React frontend that integrates with the API.

> **Project contributions:** I built the backend, including the REST API and database integration. The frontend was created by its contributor; their name or profile was not identifiable from the repository, so please replace **[Frontend contributor]** with the correct name or GitHub link.

## Features

- Create, list, retrieve, update, and delete products.
- Persist product records using SQLAlchemy and PostgreSQL.
- Seed the database with sample products when it is empty.
- Browse the interactive API documentation provided by FastAPI.
- React frontend in the `frontend/` directory.

## Technology Stack

- **Backend:** Python, FastAPI, Pydantic, SQLAlchemy
- **Database:** PostgreSQL
- **Frontend:** React, Axios, CSS

## Repository Structure

```text
.
├── database.py          # Database engine and session configuration
├── db_models.py         # SQLAlchemy database models
├── main.py              # FastAPI app and product endpoints
├── models.py            # Pydantic request/response model
└── frontend/            # React frontend application
```

## Getting Started

### Prerequisites

- Python 3.9 or newer
- Node.js and npm (to run the frontend)
- A running PostgreSQL database

### 1. Configure the database

Create a PostgreSQL database, then add a `.env` file in the repository root with its SQLAlchemy connection URL:

```env
db_url=postgresql+psycopg2://USERNAME:PASSWORD@HOST:5432/DATABASE_NAME
```

Replace the placeholders with your database credentials and database name. Keep `.env` private and do not commit credentials.

### 2. Install backend dependencies

From the repository root, create and activate a virtual environment, then install the packages:

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the backend packages:

```bash
pip install fastapi uvicorn sqlalchemy python-dotenv psycopg2-binary
```

### 3. Start the backend

From the repository root:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. FastAPI's interactive documentation is at `http://localhost:8000/docs` (ReDoc: `http://localhost:8000/redoc`).

### 4. Start the frontend (optional)

In a separate terminal:

```bash
cd frontend
npm install
npm start
```

The frontend development server runs at `http://localhost:3000` and is configured to proxy API requests to `http://localhost:8000`.

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Basic service response |
| `GET` | `/products` | List all products |
| `GET` | `/products/{id}` | Get a product by ID |
| `POST` | `/products` | Create a product |
| `PUT` | `/products/{id}` | Update a product by ID |
| `DELETE` | `/products/{id}` | Delete a product by ID |

### Product request example

Use this JSON body when creating or updating a product:

```json
{
  "id": 10,
  "name": "Wireless mouse",
  "description": "Ergonomic mouse",
  "price": 29,
  "quantity": 15
}
```

## Database Initialization

On startup, the application creates the product table if it does not exist. If the table is empty, it inserts a small set of sample products.

## Credits

- **Backend and API:** Sarvesh-029
- **Frontend:** [Frontend contributor] — frontend contribution. Add the contributor's name or GitHub profile here.

## License

No license is currently specified. Contact the repository owner before reusing or distributing this project.
