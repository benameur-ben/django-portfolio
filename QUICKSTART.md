# Django Portfolio - Quick Start Commands

## 🚀 Quick Setup (Copy & Paste)

### Step 1: Navigate to Project
```bash
cd C:\Users\Admin\.gemini\antigravity\scratch\django-portfolio
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Create Environment File
```bash
copy .env.example .env
```

**IMPORTANT**: Open `.env` and change `SECRET_KEY` to something unique!

### Step 6: Initialize Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Admin User
```bash
python manage.py createsuperuser
```
Follow prompts to set username, email, and password.

### Step 8: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 9: Run Server
```bash
python manage.py runserver
```

## 🎉 Access Your Portfolio

- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **API**: http://localhost:8000/api/projects/

## 📝 Next Steps

1. Login to admin panel with your superuser credentials
2. Add some projects (Projects → Add Project)
3. Add services (Services → Add Service)
4. View your portfolio at http://localhost:8000
5. Test the contact form

## 🐳 Docker Alternative (Optional)

If you prefer Docker:

```bash
# Build and run
docker-compose up --build

# Access at http://localhost:8000
```

## 🛑 Stop Server

Press `Ctrl + C` in the terminal

## 🔄 Restart Server

```bash
python manage.py runserver
```

## 📊 Useful Commands

### Create sample data
```bash
python manage.py shell
```

Then in the shell:
```python
from portfolio.models import Project, Service

# Create a sample project
Project.objects.create(
    title="Django Portfolio",
    description="A production-ready portfolio website",
    tech_stack=["Python", "Django", "Tailwind CSS"],
    role="Full Stack Developer",
    featured=True
)

# Create a sample service
Service.objects.create(
    name="Web Development",
    category="web",
    description="Custom web applications with Django",
    icon="🌐",
    is_active=True,
    order=1
)

exit()
```

### View all projects
```bash
python manage.py shell
```
```python
from portfolio.models import Project
for p in Project.objects.all():
    print(f"{p.title} - {p.tech_stack}")
exit()
```

### Reset database (if needed)
```bash
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```
