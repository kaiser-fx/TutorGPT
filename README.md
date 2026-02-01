# TutorGPT - AI-Powered Coding Tutor

An interactive web application that leverages Google's Gemini AI to provide personalized coding education. TutorGPT acts as a personal coding tutor with the personality of Harvey Specter from SUITS(or any character of your choice), guiding students through programming languages step-by-step.

## Features

- **Interactive Chat Interface**: Clean, modern chat UI for seamless student-tutor interaction
- **AI-Powered Tutoring**: Uses Google Gemini 2.5 Flash model for intelligent responses
- **Multi-Language Support**: Can teach various programming languages based on user preference
- **Adaptive Learning**: Offers structured courses with progressive difficulty levels (Beginner, Intermediate, Advanced)
- **Code Snippet Integration**: Provides practical coding examples with explanations
- **Knowledge Assessment**: Includes MCQ questions to test understanding with instant feedback
- **Markdown Support**: Renders formatted text and code blocks for better readability
- **CORS-Enabled**: Frontend and backend communicate seamlessly across origins

## Project Structure

```
WebAppProject/
├── frontend.html          # Interactive chat interface
└── backend/
    ├── app.py            # FastAPI backend server
    └── __pycache__/      # Python cache files
```

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
  - Marked.js for markdown rendering
  - Responsive design with flexbox layout
  
- **Backend**: Python
  - FastAPI for REST API
  - Google Generativeai SDK (Gemini API)
  - CORS middleware for cross-origin requests

## Prerequisites

- Python 3.8+
- Google Generative AI API key
- Modern web browser

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TutorGPT
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn google-generativeai python-multipart
   ```

3. **Set up API key** (already configured in `backend/app.py`, but consider using environment variables for production)

## Running the Application

1. **Start the backend server**
   ```bash
   cd backend
   python -m uvicorn app:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`

2. **Open the frontend**
   - Open `frontend.html` in your web browser
   - Or serve it with a local server (e.g., `python -m http.server 8080`)

3. **Begin learning**
   - The app will greet you with an introduction
   - Select your preferred programming language from the options provided
   - Choose your learning level
   - Follow the structured course content
   - Answer quiz questions to test your knowledge

## API Endpoints

### `GET /start`
- **Description**: Initializes a new chat session and displays the welcome message
- **Response**: `{"reply": "Welcome message from TutorGPT"}`

### `POST /chat`
- **Description**: Sends a user message and receives a tutored response
- **Request Body**: `{"message": "User's question or response"}`
- **Response**: `{"reply": "TutorGPT's response"}`

## Course Structure

The application guides learners through:

1. **Introduction** to the selected programming language
2. **Installation & IDE Setup** instructions
3. **Basic Syntax** fundamentals
4. **Control Flow** concepts
5. **Advanced Topics** (expanded based on language)
6. **Practical Examples** with code snippets
7. **Assessment** through MCQ questions

## Safety Features

Content filtering is enabled for:
- Harassment
- Hate speech
- Sexually explicit content
- Dangerous content

## Author

**Kushagra Tarun**
- [LinkedIn](https://www.linkedin.com/in/kushagra-tarun-1a809131b/)
- [GitHub](https://github.com/kaiser-fx)

## Future Enhancements

- User progress tracking and history
- Multiple language support for the UI
- Code execution sandbox
- Advanced analytics and performance metrics
- Chat history persistence
- Dark mode toggle
- Mobile-responsive improvements


---

**Note**: The API key is currently hardcoded for development purposes. For production, use environment variables to securely manage sensitive credentials.
