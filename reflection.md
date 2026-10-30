# Project Reflection

## What I Built

I built SmartWrite AI, a simple web application that uses an AI model to improve user-written text. Users enter text, select a writing style, and receive an improved version. The application was built with Flask and the OpenAI API.

## What I Learned

The biggest lesson was that building an AI application is not only about calling an AI model. The project required thinking about the problem first, defining a focused MVP, designing the application flow, testing the application, and deploying it.

I also learned how to use AI-assisted development while still maintaining a basic software engineering workflow. Git commits, automated testing, environment variables, and CI/CD made the project more reliable and easier to manage.

## Challenges

The main technical challenges were setting up the development environment, connecting the Flask application to the OpenAI API, and configuring GitHub Actions. One issue occurred because the OpenAI client was initialized when the application was imported, causing the CI environment to require an API key even though the automated test did not use the API. Moving client initialization into the request flow resolved the problem.

Another challenge was managing API costs. Since the application uses a paid API, automated tests were deliberately designed not to make API calls.

## What I Would Improve

The current application is intentionally small and demonstrates the core functionality rather than being a production-ready product. If I continued developing it, I would add better error handling, loading states, input validation, authentication, usage limits, and more comprehensive tests.

I would also test the application with real users to determine whether improving writing style is a sufficiently valuable problem and which user groups would use the product regularly.

## Key Takeaway

The most important lesson is that a useful AI product does not need a complicated architecture. A focused problem, a simple user experience, a reliable AI integration, and disciplined engineering practices are enough to build and validate an initial AI-powered product.