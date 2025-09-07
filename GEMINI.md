# GEMINI.md

## Project Overview

This project hosts a chatbot for the **Setif Development Group (SDG)**, a student scientific and development group at the University of Setif. It is built using Python with the FastAPI framework and integrates with the Gemini API for its conversational AI capabilities. The application is designed to receive chat messages, maintain a history of the conversation, and generate relevant responses using the Gemini language model.

The project is structured as a web service with a single chatbot, but it is designed to be easily extendable to support multiple chatbots in the future. It uses Pydantic for data validation and to define the structure of the chat messages.

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
*   **API:** The project uses FastAPI to build the API. The main endpoint is `/api/chatbot/sdg`.
*   **Data Models:** Pydantic is used to define the data models for the API. The main data models are `Msg` and `Massage` (defined in `schemas.py`). **Note:** `Massage` is likely a typo and should be renamed to `Message`.
*   **Dependencies:** Project dependencies are managed with a `requirements.txt` file.
*   **Configuration:** The Gemini API key is managed through an `.env` file.

## Project Structure

The project is organized into the following files:

*   **`main.py`**: The main entry point of the application. It defines the FastAPI app and the chatbot endpoint.
*   **`chat_bots.py`**: Contains the core logic for the SDG chatbot. It orchestrates the process of building the request for the Gemini API and processing the response.
*   **`chat_bot.py`**: Handles the direct interaction with the Gemini API, including making the API calls and managing function calling.
*   **`schemas.py`**: Defines the Pydantic data models used for API requests and responses.
*   **`system_instructions.py`**: Contains the system prompts that define the chatbot's persona and behavior.
*   **`tools_declarations.py`**: Declares the functions that the chatbot can use (tools) for the Gemini API.
*   **`tools.py`**: Provides the implementation for the tools declared in `tools_declarations.py`.
*   **`util.py`**: A collection of utility functions that help in building the configuration, content, and tools for the Gemini API.
*   **`summary.py`**: Implements the logic for summarizing the conversation history to manage context length.
*   **`requirements.txt`**: Lists the Python dependencies for the project.
*   **`Dockerfile` and `docker-compose.yaml`**: Used for building and running the application in Docker containers.
*   **`GEMINI.md`**: This file, providing an overview of the project.

## Chatbot Architecture

The application is designed around a modular architecture that separates concerns and allows for easy extension.

*   **API Layer (`main.py`)**: The FastAPI application serves as the entry point for incoming requests. It receives the user's message and passes it to the chatbot logic.
*   **Chatbot Orchestration (`chat_bots.py`)**: This layer is responsible for managing the overall flow of the conversation. It builds the necessary components for the Gemini API call, including the system instructions, tools, and conversation history.
*   **Gemini API Interaction (`chat_bot.py`)**: This layer handles the direct communication with the Gemini API. It sends the request and processes the response, including handling function calls.
*   **Tooling (`tools.py`, `tools_declarations.py`)**: The chatbot is equipped with tools that allow it to access external information or perform specific actions. The tools are declared in `tools_declarations.py` and implemented in `tools.py`.
*   **Data Management (`schemas.py`, `summary.py`)**: Pydantic models in `schemas.py` ensure data integrity, while `summary.py` provides a mechanism for managing the conversation history and preventing it from becoming too long.
