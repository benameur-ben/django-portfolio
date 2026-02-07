# Django Portfolio - Production-Ready

A high-end, production-ready portfolio website for a Software Engineer specializing in Python & Django. Optimized for low-bandwidth environments with a Cyber-Professional UI design.

## 🚀 Features

- **Database**: SQLite with optimized indexing (Projects, Services, LeadCapture)
- **Backend**: Django 5.0+ with RESTful API
- **Frontend**: Tailwind CSS with Cyber-Professional theme and Bento Grid layout
- **Admin**: Custom Django admin for lead management
- **DevOps**: Docker containerization + GitHub Actions CI/CD
- **Performance**: Lazy loading, compression, WhiteNoise for static files

## 📋 Prerequisites

- Python 3.11+
- pip (Python package manager)
- Git (for version control)
- Docker (optional, for containerization)

## 🛠️ Local Setup

### 1. Clone or Navigate to Project
```bash
cd C:\Users\Admin\.gemini\antigravity\scratch\django-portfolio
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Create Environment File
```bash
copy .env.example .env
```

Edit `.env` and set your SECRET_KEY:
```
SECRET_KEY=your-unique-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000

## 🎨 Admin Panel

Access the admin panel at: http://localhost:8000/admin

Use the superuser credentials you created to:
- Add projects with tech stack and links
- Manage services (Automation, Trading, Web)
- View and manage leads from contact form

## 📡 API Endpoints

- `GET /api/projects/` - List all projects
- `GET /api/projects/?featured=true` - Featured projects only
- `GET /api/projects/?tech=Python` - Filter by technology
- `GET /api/services/` - List active services
- `POST /api/leads/` - Submit contact form

## 🐳 Docker Setup

### Build and Run with Docker Compose
```bash
docker-compose up --build
```

### Build Docker Image
```bash
docker build -t django-portfolio .
```

### Run Container
```bash
docker run -p 8000:8000 django-portfolio
```

## 🚢 Deployment

### Render Deployment

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set environment variables:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-domain.com`
4. Deploy command: `gunicorn portfolio_project.wsgi:application`

### Railway Deployment

1. Create new project on Railway
2. Add PostgreSQL database (optional, or use SQLite)
3. Set environment variables
4. Deploy from GitHub

## 📁 Project Structure

```
django-portfolio/
├── portfolio_project/      # Main Django project
│   ├── settings.py        # Configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
├── portfolio/            # Main app
│   ├── models.py        # Database models
│   ├── views.py         # Views and API
│   ├── admin.py         # Custom admin
│   └── serializers.py   # DRF serializers
├── templates/
│   └── index.html       # Frontend template
├── static/              # Static files
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose
├── requirements.txt     # Python dependencies
└── .github/workflows/   # CI/CD pipeline
```

## 🎯 Tech Stack

- **Backend**: Django 5.0.2, Django REST Framework 3.14.0
- **Database**: SQLite with WAL mode
- **Frontend**: Tailwind CSS (CDN), Vanilla JavaScript
- **Server**: Gunicorn 21.2.0
- **Static Files**: WhiteNoise 6.6.0
- **Deployment**: Docker, GitHub Actions

## 📝 License

MIT License - Feel free to use for your own portfolio!

## 🤝 Contributing

This is a personal portfolio template. Feel free to fork and customize!

## 📧 Contact

For questions or support, use the contact form on the website.
