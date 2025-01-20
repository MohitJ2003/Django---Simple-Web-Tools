@echo off
rem Navigate to your Django project directory
cd "D:\Projects\PycharmProjects\pythonProject1\djangoProjects\project1"

rem Activate virtual environment
call "audiotrnas\Scripts\activate"

rem Confirm activation (optional)
if not defined VIRTUAL_ENV (
    echo Virtual environment activation failed. Exiting.
    exit /b
)

rem Run Django server
python manage.py runserver 8001