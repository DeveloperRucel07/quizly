## Project Description

Quizly is an intelligent quiz generation platform that leverages cutting-edge AI technology to transform YouTube videos into interactive learning experiences. The application automatically extracts audio from videos, transcribes content using advanced speech recognition, and generates comprehensive quizzes with 10 carefully crafted questions. This platform is perfect for educators, students, and learners who want to enhance their knowledge retention through interactive assessment tools.

## Technologies Required

- **Python** (3.11+) - Core programming language
- **Django** (5.2.7) - Web framework for building the backend
- **Django REST Framework** (3.16.1) - For building RESTful APIs
- **ffmpeg** - Multimedia framework for audio/video processing
- **OpenAI Whisper** - Speech-to-text transcription
- **Google GenAI** - AI model for quiz generation
- **PyJWT & djangorestframework-simplejwt** - JWT authentication
- **python-dotenv** - Environment variable management
- **Torch & TensorFlow dependencies** - Machine learning operations

## Installation

### Prerequisites

Before you begin, ensure you have Python 3.11+ installed on your system.

### Install ffmpeg

**Windows:**
1. Download ffmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract to a folder (e.g., `C:\ffmpeg`)
3. Add the bin folder to your system PATH environment variable
4. Verify installation: `ffmpeg -version`

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

### Prerequisites (API Keys)

You will need the following API keys:
- **Google Generative AI API Key** - For quiz generation using Google's GenAI models

Store these in a `.env` file in the project root (see Getting Started section).

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/DeveloperRucel07/quizly.git
cd quizly
```

### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root directory:
```
DEBUG=True
SECRET_KEY=your-django-secret-key-here
GOOGLE_API_KEY=your-google-gemini-ai-api-key

```

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

### 7. Create Admin user for Database overview
```bash
python manage.py createsuperuser # and follow the instructions.
```

The application will be available at `http://127.0.0.1:8000`

## Project Structure

- `auth_app/` - User authentication and authorization
- `quizz_app/` - Quiz generation and management
- `core/` - Django project settings and configuration
- `media/` -  quiz media


### Endpoints


POST  `/api/register/`,  Create new Account 
POST  `/api/login/`,  Login with User and Password (after login the user cookies are store in the browser)
POST  `/api/logout/`,  logout user by deleting all cookies.
POST  `/api/token/refresh/`,  refresh the access token for the user 
POST  `/api/CreateQuiz/`,  Create a new quiz (only authenticated User)
GET  `/api/quizzes/` ,List of Quizzes the current user created  (only authenticated User)
GET  `/api/quizzes/<pk>/`,  Get quiz details  (only authenticated User and the user should be the owner of the quiz)


