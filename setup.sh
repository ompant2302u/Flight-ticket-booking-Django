#!/bin/bash

echo "🚀 Setting up Flight Ticket Management System..."
echo ""

# Navigate to project directory
cd "$(dirname "$0")/myProject"

# Create media directories
echo "📁 Creating media directories..."
mkdir -p media/profiles media/packages media/deals

# Make migrations
echo "🔄 Creating database migrations..."
python manage.py makemigrations

# Apply migrations
echo "💾 Applying migrations..."
python manage.py migrate

# Create superuser prompt
echo ""
echo "👤 Create a superuser account for admin access:"
python manage.py createsuperuser

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the server, run:"
echo "  cd myProject"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000/"
echo ""
