# SDG Chat Bots

A FastAPI-based project that provides multiple chatbot endpoints for different purposes: SDG (Sustainable Development Goals), Events, and Podcast information. The project uses Google's Gemini API for generating responses.

## Features

- **Multiple Specialized Chatbots:**
  - SDG Chatbot: Provides information about Sustainable Development Goals
  - Event Chatbot: Handles event-related queries and workshop registrations
  - Podcast Chatbot: Manages podcast-related information

- **Rate Limiting:**
  - Implements request rate limiting to prevent abuse
  - Different limits for different endpoints
  - 100 requests per hour and 10 requests per minute for chatbot endpoints

- **CORS Security:**
  - Configured with specific allowed origins
  - Supports both production and development environments

## API Endpoints

### Base Endpoint
- `GET /`: Basic health check endpoint (Rate limit: 10/hour)

### Chatbot Endpoints
- `POST /api/chatbot/sdg`: SDG information chatbot
- `POST /api/chatbot/event`: Event management chatbot
- `POST /api/chatbot/podcast`: Podcast information chatbot

All chatbot endpoints have the following rate limits:
- 100 requests per hour
- 10 requests per minute

## Request/Response Schema

### Message Schema
```python
class Massage {
    summary?: string
    history: [
        {
            role: "user" | "model"
            content: string
        }
    ]
    message: string
}
```

## Setup and Installation

### Prerequisites
- Python 3.x
- Docker (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/setif-developers-group/SDG-chat-bots.git
cd SDG-chat-bots
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file in the root directory with your Gemini API credentials and other necessary environment variables.

### Running the Application

#### Using Python
```bash
uvicorn main:app --reload
```

#### Using Docker
```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`

## Technology Stack

- **Framework:** FastAPI
- **AI Model:** Google Gemini API
- **Rate Limiting:** slowapi
- **Container:** Docker
- **ASGI Server:** Uvicorn
- **Dependencies Management:** pip

## API Documentation

Once the application is running, you can access the automatic API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Error Handling

The application includes robust error handling for:
- Model unavailability
- Function call errors
- Rate limit exceeded errors
- General exceptions

## Project Structure

- `main.py`: FastAPI application entry point and route definitions
- `chat_bots.py`: Implementation of different chatbot functionalities
- `schemas.py`: Pydantic models for request/response validation
- `tools.py`: Utility functions for chatbot operations
- `models_manager.py`: Manages AI model interactions
- `system_instructions.py`: Contains system prompts for different chatbots
- `docker-compose.yaml`: Docker composition configuration
- `requirements.txt`: Python dependencies

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License


