@echo off
rem Change directory to your Django project
cd "C:\Users\dell pc\PycharmProjects\pythonProject1\djangoProjects\project1"
rem Activate virtual environment if you're using one
call "C:\Users\dell pc\PycharmProjects\pythonProject1\venv\Scripts\activate.bat"
rem Run Django server
python manage.py runserver