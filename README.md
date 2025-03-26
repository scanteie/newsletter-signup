# Newsletter Subscription Service

A secure, lightweight newsletter subscription service built with Flask. Features include user subscription management, unsubscribe functionality, and an admin interface with CSV export capabilities.

## Features

- User-facing subscription flow with email validation
- Terms and conditions acceptance requirement
- Unsubscribe functionality
- Thank you and confirmation pages
- Admin interface with subscriber management
- CSV export functionality
- SQLite database for data storage
- Responsive design

## Requirements

- Python 3.7+
- Flask and dependencies (see requirements.txt)
- SQLite3

## Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd newsletter-signup
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Run the setup script:
```bash
./setup.sh  # On Windows: run setup commands manually
```

Or manually:
```bash
pip install -r requirements.txt
python3 -c "from app import app, db; app.app_context().push(); db.create_all()"
```

## Running the Application

1. Activate the virtual environment (if not already activated):
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Start the Flask development server:
```bash
flask run
```

3. Access the application at http://localhost:5000

## Routes

- `/subscribe` - Newsletter subscription page
- `/unsubscribe` - Unsubscribe page
- `/thank-you` - Subscription confirmation page
- `/terms` - Terms and conditions page
- `/admin` - Admin interface (password protected)
- `/admin/export` - CSV export endpoint (password protected)

## Admin Access

Default credentials:
- Username: admin
- Password: admin

To change the admin credentials, set the following environment variables:
```bash
export ADMIN_USER=your_username
export ADMIN_PASS=your_password
```

## Database

The application uses SQLite with the following schema:

```sql
CREATE TABLE subscriber (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(120) UNIQUE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'subscribed',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

## Security Features

- Email validation
- CSRF protection
- Password-protected admin interface
- SQL injection prevention through SQLAlchemy
- XSS protection through template escaping

## Development

To run the application in debug mode:
```bash
export FLASK_ENV=development
flask run
```

## License

MIT License - feel free to use this project for your own purposes.