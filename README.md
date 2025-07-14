
# ✈️ Airport API

### 👨‍✈️ View flights and book tickets with ease!

---

## ⚙️ Requirements

- 🐍 **Python** 3.12  
- 🌐 **Django** 5.x  
- 🧰 **Django REST Framework**  
- 🐘 **PostgreSQL** (via Docker)  
- 🐳 **Docker** & **Docker Compose**  
- 🧪 **Pytest** / Django TestCase  
- 📃 **Swagger** / drf-spectacular  
- 🔑 **JWT Authentication**  
- ✅ **Custom permissions** & throttling  
- 👤 **Custom user model** (email as username)  

---

## 🚀 Features

- 🛡️ Authentication via email & password  
- 🔍 View:
  - Your orders  
  - All flights  
  - All crews  
  - Aircraft and aircraft types  
- 🔎 Advanced filtering for journeys:
  - By route  
  - By departure/arrival time  
- ⚒️ Custom filters  
- 📚 Swagger-powered API docs  
- 🔬 Tests for all core business logic  
- 🐳 Full Docker support for local development  

---

## 🚴‍♂️ Getting Started

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/Miwacer/Airport.git
cd Airport
```

---

### 2. 🛠️ Set Up the Environment

Create and activate a virtual environment, then install the dependencies:

<details>
<summary>🪟 Windows</summary>

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

</details>

<details>
<summary>🐧 macOS / Linux</summary>

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

</details>

---

### 3. ⚙️ Create a `.env` File

At the project root, create a `.env` file and add the following:

```env
SECRET_KEY=your_secret_key
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=your_db_name
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

### 4. ✅ Final Steps

Apply migrations and run the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser 🌍

---

✅ You're good to go — happy coding!

---

## 🐳 Docker Setup

1. Build and start the containers:
```bash
docker-compose up --build
```

2. The app will be available at:
[http://localhost:8001](http://localhost:8001)

3. Default ports:
- App: `8001`
- DB: `5432`

.env file is used for all environment variables.
