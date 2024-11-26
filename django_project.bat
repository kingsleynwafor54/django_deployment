@echo off
REM Activate the virtual environment
cd /d C:\Users\user\blogProject\blog_project
call C:\Users\user\blogProject\blog_env\Scripts\activate.bat
REM Start the Django development server
python manage.py runserver 0.0.0.0:8001
