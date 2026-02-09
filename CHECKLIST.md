# Setup Checklist ✓

Use this checklist to track your setup progress:

## Initial Setup
- [ ] Navigate to project directory
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Create migrations: `python manage.py makemigrations`
- [ ] Apply migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Create media directories

## Optional Setup
- [ ] Add sample data: `python manage.py shell < add_sample_data.py`
- [ ] Collect static files: `python manage.py collectstatic`

## Testing
- [ ] Start server: `python manage.py runserver`
- [ ] Visit homepage: http://127.0.0.1:8000/
- [ ] Test user registration
- [ ] Test user login
- [ ] Browse flights page
- [ ] Test search functionality
- [ ] Test booking a flight
- [ ] Upload profile photo
- [ ] View booking history
- [ ] Access admin panel (if superuser)
- [ ] View admin dashboard (if staff)

## Customization (Optional)
- [ ] Change colors in style.css
- [ ] Update logo in base.html
- [ ] Add your own flights via admin
- [ ] Add packages via admin
- [ ] Add deals via admin
- [ ] Customize email settings
- [ ] Configure production settings

## Production Checklist (When Ready)
- [ ] Change SECRET_KEY
- [ ] Set DEBUG = False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up PostgreSQL database
- [ ] Configure email backend
- [ ] Set up static file serving
- [ ] Enable HTTPS
- [ ] Set up backup system
- [ ] Configure logging
- [ ] Set up monitoring

## Notes
Write any issues or customizations here:

_____________________________________________________________________________

_____________________________________________________________________________

_____________________________________________________________________________

_____________________________________________________________________________

## Completed! 🎉
Once everything is checked off, your flight ticket management system is ready!

Date Completed: _______________
