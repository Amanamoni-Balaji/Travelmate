# TravelMate

TravelMate is a Django-based travel and tourism web application.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd CRT_PROJECT_2
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   # Windows:
   .\env\Scripts\activate
   # macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   cd travelmate_dev/travelmate
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
