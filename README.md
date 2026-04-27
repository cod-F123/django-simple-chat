# Simple Chat Project with Django Channels

This is a simple, real-time chat application developed using the Django framework and the Django Channels library. Django Channels enables WebSocket communication for building real-time applications.

## Features

*   **Real-time Messaging:** Users can send and receive messages instantly.
*   **Multiple Chat Rooms:** Support for several distinct chat rooms.
*   **Authenticated Users:** Messages are attributed to logged-in users.
*   **Simple UI:** A clean and user-friendly interface for chatting.

## Requirements

*   Python 3.8+
*   Django 3.2+
*   Django Channels 3.0+
*   Redis (for Channels to function correctly)

## Installation and Setup

1.  **Clone the Repository:**
```bash
git clone https://github.com/cod-F123/django-simple-chat.git
cd django-simple-chat
```

2. **Create and Activate a Virtual Environment (Optional but Recommended):**
```bash
cd core
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure Redis:**

Ensure Redis is installed and running on your system. It’s typically started with the command redis-server.

5. **Create .env file and set Environment valuable**
```env
SECRET_KEY = 'youre_secret_key'
DEBUG = True # in production False
ALLOWED_HOSTS = 'localhost,127.0.0.1' # seprate with ,
CHANNEL_HOST = #default redis://127.0.0.1:6379
```

7. **Run Django Migrations:**
```bash
pyhton manage.py migrate
```
7. **Create a Superuser (Optional):**
```bash
python manage.py createsuperuser
```
8. **Run the Django Development Server:**
```bash
python manage.py runserver
```


