# SmartWrite AI — Technical Specification

## 1. System Overview

SmartWrite AI is a lightweight web application that accepts user-written text, sends it to an OpenAI language model with a selected writing style, and displays the generated improvement.

## 2. Architecture

```text
User
  |
  v
Flask Web Application
  |
  v
Prompt Construction
  |
  v
OpenAI API
  |
  v
Generated Improved Text
  |
  v
Web Interface
```

## 3. Components

### Web Application

- Framework: Flask
- Language: Python
- Provides the user interface and HTTP request handling.
- Runs locally during development and will be deployed using a production WSGI server.

### AI Module

- Provider: OpenAI API
- Input:
  - Original user text
  - Selected writing style
- Output:
  - Improved text

The AI module is instructed to return only the rewritten version.

### Configuration

The OpenAI API key is stored in an environment variable:

`OPENAI_API_KEY`

The API key is stored in `.env` during local development and is excluded from Git using `.gitignore`.

## 4. Request Flow

1. User opens the SmartWrite AI web page.
2. User enters text.
3. User selects a style.
4. Flask receives the POST request.
5. Flask constructs an AI prompt.
6. The OpenAI API generates the improved text.
7. Flask returns the result to the browser.

## 5. Testing Strategy

The MVP includes an automated test that verifies:

- The Flask application starts successfully.
- The homepage returns HTTP 200.
- The expected SmartWrite AI interface is present.

The test does not call the OpenAI API, avoiding unnecessary API cost during automated testing.

## 6. Security

- API credentials are stored in environment variables.
- `.env` is excluded from source control.
- API keys must never be committed to GitHub.
- Generated content is treated as user-provided output and should be reviewed before use.

## 7. Deployment

The application will be deployed using a cloud platform capable of running a Python Flask application.

The production server will use Gunicorn:

`gunicorn app:app`

The OpenAI API key will be configured as a secure environment variable on the deployment platform.