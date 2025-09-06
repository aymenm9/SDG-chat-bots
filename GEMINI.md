# GEMINI.md

## Project Overview

This project hosts a set of chatbots focused on the Sustainable Development Goals (SDGs). It is built using Python with the FastAPI framework and integrates with the Gemini API for its conversational AI capabilities. The application is designed to receive chat messages, maintain a history of the conversation, and generate relevant responses using the Gemini language model.

The project is structured as a web service, with plans to have three distinct chatbots, each with its own API endpoint. It uses Pydantic for data validation and to define the structure of the chat messages.

## Building and Running

To get the project up and running, you will need to have Python and the dependencies installed.

**1. Install Dependencies:**

It is recommended to use a virtual environment. Once your environment is activated, you can install the required packages using pip:

```bash
pip install -r requirements.txt
```

**2. Set Up Environment Variables:**

The application uses the Gemini API, which requires an API key. You will need to create a `.env` file in the root of the project and add your Gemini API key to it:

```
GOOGLE_API_KEY="your_gemini_api_key"
```

**3. Running the Application:**

The application can be run using `uvicorn`, an ASGI server. From the root of the project, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server, and you should see output indicating that the application is running. The `--reload` flag will automatically restart the server when you make changes to the code.

The API will be available at `http://127.0.0.1:8000`.

**4. Docker:**

The project also includes a `Dockerfile` and `docker-compose.yaml`, which can be used to build and run the application in a Docker container.

To build and run with Docker Compose:

```bash
docker-compose up --build
```

## Development Conventions

*   **Code Style:** The project follows the standard Python PEP 8 style guide.
*   **API:** The project uses FastAPI to build the API. The initial endpoint is `/api/chatbot/sdg`. The plan is to have a separate API endpoint for each of the three chatbots.
*   **Data Models:** Pydantic is used to define the data models for the API. The main data models are `Msg` and `Message` (defined as `Massage` in `schemas.py`, which is likely a typo).
*   **Dependencies:** Project dependencies are managed with a `requirements.txt` file.
*   **Configuration:** The Gemini API key is managed through an `.env` file.

### Chatbot Architecture

The application will be structured to support three individual chatbots. For each chatbot, there will be a dedicated set of functions to manage its behavior:

*   **System Instructions:** A function will be responsible for generating the specific system instructions for each chatbot. This will define the chatbot's persona, its knowledge domain, and its expected behavior.
*   **Tool Generation:** A separate function will define the tools available to each chatbot for function calling. This will allow each chatbot to have its own unique set of capabilities and integrations.