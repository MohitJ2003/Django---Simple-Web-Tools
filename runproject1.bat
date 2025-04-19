@echo off
setlocal

:: Get the base directory where the script is located
set "BASEDIR=%~dp0"
:: echo Base Directory: %BASEDIR% - print base dir in terminal

:: Activate virtual environment
call "%BASEDIR%webtoolenv\Scripts\activate.bat"

pip install yt_dlp


:: Confirm activation (optional)
if not defined VIRTUAL_ENV (
    echo Virtual environment activation failed. Exiting.
    exit /b
)

rem Run Django server
python manage.py runserver 8001