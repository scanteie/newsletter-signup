#!/bin/bash

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Initialize the database
echo "Initializing database..."
python3 -c "from app import app, db; app.app_context().push(); db.create_all()"

echo "Setup complete! Run 'source venv/bin/activate' to activate the virtual environment,"
echo "then 'flask run' to start the application."