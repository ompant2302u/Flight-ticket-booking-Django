@echo off
echo Setting up Flight Ticket Management System...
echo.

cd myProject

echo Creating media directories...
if not exist "media\profiles" mkdir media\profiles
if not exist "media\packages" mkdir media\packages
if not exist "media\deals" mkdir media\deals

echo Creating database migrations...
python manage.py makemigrations

echo Applying migrations...
python manage.py migrate

echo.
echo Create a superuser account for admin access:
python manage.py createsuperuser

echo.
echo Setup complete!
echo.
echo To start the server, run:
echo   cd myProject
echo   python manage.py runserver
echo.
echo Then visit: http://127.0.0.1:8000/
echo.
pause
