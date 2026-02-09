# ✈️ SkyVoyage - Flight Ticket Management System

A modern, responsive, and fully functional flight ticket booking platform built with Django.

![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### For Users
- 🔍 **Search & Filter** - Find flights by destination, date, airline, and price
- 🎫 **Easy Booking** - Simple booking process with instant confirmation
- 📱 **QR Codes** - Digital tickets with QR codes for easy check-in
- 👤 **Profile Management** - Manage your profile with photo upload
- 📊 **Booking History** - Track all your past and upcoming flights
- 🎁 **Deals & Packages** - Browse special offers and travel packages

### For Admins
- 📈 **Analytics Dashboard** - View booking statistics and trends
- ✏️ **Content Management** - Manage flights, packages, and deals
- 👥 **User Management** - View and manage user accounts
- 📊 **Reports** - Track popular destinations and booking patterns

### Design & UX
- 🎨 **Modern UI** - Clean, professional design with smooth animations
- 📱 **Fully Responsive** - Works perfectly on desktop, tablet, and mobile
- ⚡ **Fast & Smooth** - Optimized performance with loading animations
- 🎭 **Interactive** - Hover effects, transitions, and micro-interactions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project:**
   ```bash
   cd "Django project"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run setup (Windows):**
   ```cmd
   setup.bat
   ```
   
   **Or on Linux/Mac:**
   ```bash
   ./setup.sh
   ```

4. **Add sample data (optional):**
   ```bash
   cd myProject
   python manage.py shell < add_sample_data.py
   ```

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser:**
   ```
   http://127.0.0.1:8000/
   ```

## 📚 Documentation

- **[Setup Instructions](SETUP_INSTRUCTIONS.md)** - Detailed setup guide
- **[Quick Start Guide](QUICK_START.md)** - Quick reference for common tasks
- **[Features List](FEATURES.md)** - Complete list of implemented features

## 🎯 Usage

### For Regular Users

1. **Browse Flights:**
   - Visit the homepage or flights page
   - Use search and filters to find your flight
   - Click "Book Now" on your preferred flight

2. **Book a Ticket:**
   - Fill in passenger details
   - Confirm booking
   - Download/print your e-ticket with QR code

3. **Manage Profile:**
   - Click on your profile picture in the navbar
   - Select "Edit Profile"
   - Upload photo and update information

### For Administrators

1. **Access Admin Panel:**
   - Go to http://127.0.0.1:8000/admin/
   - Login with superuser credentials
   - Manage flights, packages, deals, and bookings

2. **View Dashboard:**
   - Go to http://127.0.0.1:8000/admin-dashboard/
   - View statistics and analytics
   - Monitor recent bookings

## 🛠️ Technology Stack

- **Backend:** Django 4.0+
- **Database:** SQLite (development) / PostgreSQL (production ready)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Styling:** Custom CSS with Flexbox/Grid
- **Fonts:** Google Fonts (Inter, Outfit)
- **Icons:** Unicode Emojis
- **Image Processing:** Pillow
- **QR Codes:** qrcode library

## 📁 Project Structure

```
Django project/
├── myProject/                 # Main Django project
│   ├── myApp/                # Main application
│   │   ├── static/          # CSS, JS, images
│   │   ├── templates/       # HTML templates
│   │   ├── models.py        # Database models
│   │   ├── views.py         # View functions
│   │   └── urls.py          # URL routing
│   ├── myProject/           # Project settings
│   ├── media/               # User uploads
│   └── manage.py            # Django CLI
├── setup.sh                 # Linux/Mac setup script
├── setup.bat                # Windows setup script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🎨 Customization

### Change Colors
Edit `myApp/static/css/style.css`:
```css
:root {
    --primary: #ff6b6b;      /* Main color */
    --secondary: #4ecdc4;    /* Secondary color */
    --dark: #2d3436;         /* Text color */
}
```

### Change Logo
Edit `myApp/templates/base.html`:
```html
<a href="{% url 'index' %}" class="logo">Your Logo</a>
```

### Add Custom Pages
1. Create template in `myApp/templates/`
2. Add view function in `myApp/views.py`
3. Add URL pattern in `myApp/urls.py`

## 🔒 Security

- ✅ CSRF protection enabled
- ✅ User authentication required for bookings
- ✅ Password hashing
- ✅ SQL injection protection (Django ORM)
- ✅ XSS protection

**For Production:**
- Change `SECRET_KEY` in settings.py
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use PostgreSQL instead of SQLite
- Enable HTTPS
- Use environment variables for sensitive data

## 📊 Database Models

- **User** - Django's built-in user model
- **Profile** - Extended user information with photo
- **Flight** - Flight details (number, route, time, price, seats)
- **Package** - Travel packages with pricing
- **Deal** - Special offers with discounts
- **Ticket** - Booking records with status

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created with ❤️ for flight booking enthusiasts

## 🙏 Acknowledgments

- Django framework and community
- Google Fonts for typography
- All open-source contributors

## 📞 Support

For issues or questions:
1. Check the documentation files
2. Review Django official docs
3. Check error messages in terminal

## 🎉 What's Next?

Potential enhancements:
- [ ] Email notifications for bookings
- [ ] Payment gateway integration (Stripe/PayPal)
- [ ] Seat selection interface
- [ ] Multi-city flights
- [ ] Flight reviews and ratings
- [ ] Loyalty points system
- [ ] Mobile app (React Native/Flutter)
- [ ] Real-time flight tracking
- [ ] Weather information
- [ ] Hotel booking integration

---

**Happy Flying! ✈️**

Made with Django and lots of ☕
