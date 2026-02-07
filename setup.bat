@echo off
REM Django Portfolio Setup Script for Windows
REM This script automates the local setup process

echo ========================================
echo Django Portfolio - Automated Setup
echo ========================================
echo.

REM Step 1: Create virtual environment
echo [1/9] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment created
echo.

REM Step 2: Activate virtual environment
echo [2/9] Activating virtual environment...
call venv\Scripts\activate
echo ✓ Virtual environment activated
echo.

REM Step 3: Upgrade pip
echo [3/9] Upgrading pip...
python -m pip install --upgrade pip
echo ✓ Pip upgraded
echo.

REM Step 4: Install dependencies
echo [4/9] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed
echo.

REM Step 5: Create .env file
echo [5/9] Creating environment file...
if not exist .env (
    copy .env.example .env
    echo ✓ .env file created - PLEASE EDIT IT TO SET YOUR SECRET_KEY!
) else (
    echo ✓ .env file already exists
)
echo.

REM Step 6: Run migrations
echo [6/9] Creating database tables...
python manage.py makemigrations
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)
echo ✓ Database tables created
echo.

REM Step 7: Collect static files
echo [7/9] Collecting static files...
python manage.py collectstatic --noinput
echo ✓ Static files collected
echo.

REM Step 8: Create superuser
echo [8/9] Creating superuser account...
echo.
echo Please enter your admin credentials:
python manage.py createsuperuser
echo ✓ Superuser created
echo.

REM Step 9: Complete
echo [9/9] Setup complete!
echo.
echo ========================================
echo Setup Complete! 🎉
echo ========================================
echo.
echo Your Django portfolio is ready to run!
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then visit:
echo   - Website: http://localhost:8000
echo   - Admin: http://localhost:8000/admin
echo   - API: http://localhost:8000/api/projects/
echo.
echo ========================================
pause
