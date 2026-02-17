# Bible Reading Web Application

A comprehensive Bible reading desktop web application built with Django backend and vanilla JavaScript frontend.

## Features

- **Bible Reading**: Browse and read Bible text with book/chapter/verse navigation
- **Verse Highlighting**: Color-code verses with 5 color options (yellow, green, blue, pink, orange)
- **Personal Notes**: Add and manage personal notes on verses
- **Reading Plans**: Create and follow customized reading schedules
- **Full-Text Search**: Search across all Bible verses
- **Progress Tracking**: Automatically save reading progress
- **Toggle Verse Numbers**: Show/hide verse numbers for better reading experience

## Project Structure

```
bible_project/
├── README.md
├── requirements.txt
├── .gitignore
├── backend/
│   ├── manage.py
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── bible/
│   │   ├── models.py (Book, Verse, Highlight, Note, ReadingProgress)
│   │   ├── views.py (REST API ViewSets)
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── reading_plans/
│   │   ├── models.py (ReadingPlan, ReadingPlanDay, ReadingPlanVerse)
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   └── users/
│       └── apps.py
└── frontend/
    ├── index.html
    ├── css/
    │   └── styles.css
    └── js/
        ├── api.js (API communication layer)
        ├── reader.js (Bible reading functionality)
        ├── search.js (Search functionality)
        ├── plans.js (Reading plans management)
        └── main.js (Application initialization)
```

## Technology Stack

### Backend
- **Django 4.2+**: Web framework
- **Django REST Framework**: REST API
- **SQLite**: Database
- **django-cors-headers**: CORS support for frontend-backend communication

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with responsive design
- **Vanilla JavaScript**: No frameworks, pure JavaScript

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd bible_project
```

### Step 2: Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup Database
```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Admin User
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 5: Load Sample Data (Optional)
You can populate the Bible data through the Django admin panel or by creating a data fixture.

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

The backend API will be available at `http://localhost:8000`

### Step 7: Access the Application

1. **Admin Panel**: Navigate to `http://localhost:8000/admin/` to manage data
2. **Frontend**: Open `frontend/index.html` in a web browser, or serve it with:
   ```bash
   cd frontend
   python -m http.server 3000
   ```
   Then visit `http://localhost:3000`

## API Endpoints

### Bible API
- `GET /api/bible/books/` - List all books
- `GET /api/bible/books/{id}/chapters/` - Get chapter info for a book
- `GET /api/bible/verses/` - List verses (supports filtering by book and chapter)
- `GET /api/bible/verses/search/?q=query` - Search verses

### Highlights API
- `GET /api/bible/highlights/` - List user highlights
- `POST /api/bible/highlights/` - Create a highlight
- `DELETE /api/bible/highlights/{id}/` - Delete a highlight

### Notes API
- `GET /api/bible/notes/` - List user notes
- `POST /api/bible/notes/` - Create a note
- `PUT /api/bible/notes/{id}/` - Update a note
- `DELETE /api/bible/notes/{id}/` - Delete a note

### Progress API
- `GET /api/bible/progress/` - Get reading progress
- `POST /api/bible/progress/` - Save reading progress

### Reading Plans API
- `GET /api/reading/plans/` - List reading plans
- `GET /api/reading/plans/{id}/` - Get plan details
- `POST /api/reading/plans/` - Create a plan
- `POST /api/reading/plans/{id}/complete_day/` - Mark a day as completed

## Usage Guide

### Reading the Bible
1. Select a book from the dropdown
2. Select a chapter
3. Click on verses to highlight them with different colors
4. Double-click on verses to add personal notes
5. Toggle verse numbers on/off as needed

### Searching
1. Navigate to the Search tab
2. Enter your search query
3. Click on results to jump to that verse in the reader

### Managing Reading Plans
1. Navigate to the Reading Plans tab
2. View existing plans and their progress
3. Click on a plan to see details and mark days as complete
4. Create new plans through the admin panel

### Admin Panel
Access `http://localhost:8000/admin/` to:
- Add Bible books and verses
- Manage user accounts
- Create reading plans
- View all highlights and notes

## Development

### Adding Bible Data
You can add Bible content through:
1. Django admin panel (manual entry)
2. Django management commands (bulk import)
3. REST API endpoints

### Customization
- **Colors**: Modify highlight colors in `frontend/css/styles.css`
- **API Base URL**: Update `API_BASE_URL` in `frontend/js/api.js`
- **Styling**: Customize appearance in `frontend/css/styles.css`

## Database Models

### Bible App
- **Book**: Bible books (name, testament, chapter count)
- **Verse**: Individual verses with text
- **Highlight**: User verse highlights with colors
- **Note**: User notes on verses
- **ReadingProgress**: Track what user has read

### Reading Plans App
- **ReadingPlan**: Reading plan metadata
- **ReadingPlanDay**: Individual days in a plan
- **ReadingPlanVerse**: Verses assigned to specific days

## CORS Configuration

The backend is configured to allow requests from:
- `http://localhost:8000`
- `http://127.0.0.1:8000`
- `http://localhost:3000`
- `http://127.0.0.1:3000`

Modify `CORS_ALLOWED_ORIGINS` in `backend/config/settings.py` to add more origins.

## Security Notes

⚠️ **For Production Deployment:**
- Change `SECRET_KEY` in settings.py
- Set `DEBUG = False`
- Configure proper `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Set up proper authentication (currently using demo user)
- Use a production-grade database (PostgreSQL)
- Configure proper HTTPS/SSL

## License

This project is provided as-is for educational and personal use.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues and questions, please open an issue on the GitHub repository.

