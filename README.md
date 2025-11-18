# UroKolpo

A Django-based social media platform where users can share posts, photos, and connect with others.

## Features

- 🔐 **User Authentication** - Register, login, and logout functionality
- 📝 **Create Posts** - Share your thoughts with text and photos
- 🖼️ **Photo Upload** - Attach images to your posts
- ✏️ **Edit Posts** - Update your posts anytime
- 🗑️ **Delete Posts** - Remove posts with confirmation
- 🔍 **Search** - Search posts by content or username
- 👤 **User Profiles** - See posts from different users
- 📱 **Responsive Design** - Mobile-friendly interface with Bootstrap
- 🌙 **Dark Theme** - Modern dark mode interface

## Tech Stack

- **Backend**: Django 5.2.8
- **Frontend**: Bootstrap 5.3.8
- **Database**: SQLite3
- **Font**: Google Fonts (Poppins)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dipurajasaha/UroKolpo.git
   cd UroKolpo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### For Users

1. **Register**: Click "Register" in the navbar to create an account
2. **Login**: Use your credentials to log in
3. **Create Post**: Click "Create New Post" to share content
4. **Search**: Use the search bar to find posts by keywords or usernames
5. **Edit/Delete**: Manage your own posts with Edit and Delete buttons

### Project Structure

```
UroKolpo/
├── post/                    # Main app
│   ├── models.py           # Post model
│   ├── views.py            # View functions
│   ├── forms.py            # Django forms
│   ├── urls.py             # App URLs
│   └── templates/          # App templates
├── templates/              # Global templates
│   ├── layout.html         # Base template
│   └── registration/       # Auth templates
├── UroKolpo/              # Project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URLs
├── static/                # Static files
├── media/                 # User uploads
├── manage.py             # Django management
└── requirements.txt      # Dependencies
```

## Configuration

### Important Settings

- **SECRET_KEY**: Change this in production (in `settings.py`)
- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Add your domain in production
- **MEDIA_ROOT**: Location for uploaded files
- **STATIC_ROOT**: Location for static files

## Features in Detail

### Authentication
- User registration with username and password
- Secure login/logout system
- Password hashing and validation
- Protected routes with `@login_required` decorator

### Posts
- Rich text content
- Optional photo uploads
- Timestamp for each post
- User ownership and permissions
- Only post owners can edit/delete their posts

### Search Functionality
- Search by post content (case-insensitive)
- Search by username
- Real-time results display

## Security Notes

⚠️ **Before deploying to production:**
- Change `SECRET_KEY` in `settings.py`
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Set up proper database (PostgreSQL recommended)
- Configure static file serving
- Enable HTTPS

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Dipurajasaha**
- GitHub: [@Dipurajasaha](https://github.com/Dipurajasaha)

## Acknowledgments

- Django framework
- Bootstrap for responsive design
- Google Fonts for typography
