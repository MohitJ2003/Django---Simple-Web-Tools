@echo off
setlocal

:: Get the base directory where the script is located
set "BASEDIR=%~dp0"
:: echo Base Directory: %BASEDIR% - print base dir in terminal

:: Activate virtual environment
call "%BASEDIR%venv\Scripts\activate.bat"


pip install yt_dlp
pip install aspose-pdf
pip install pytube
pip install moviepy
pip install SpeechRecognition
pip install openpyxl
pip install pandas
pip install xlsxwriter


:: Confirm activation (optional)
if not defined VIRTUAL_ENV (
    echo Virtual environment activation failed. Exiting.
    exit /b
)

rem Run Django server
python manage.py runserver 8001