# SmartWrite AI — Product Requirements Document

## 1. Problem

People often write messages quickly but struggle to make them clear, professional, friendly, or concise. Existing writing tools can be unnecessarily complex for a simple rewrite task.

## 2. Target User

Students and working professionals who frequently need to improve short emails, messages, and workplace communication.

## 3. Proposed Solution

SmartWrite AI is a simple web application that uses generative AI to improve user-written text.

The user:
1. Enters text.
2. Selects a writing style.
3. Clicks **Improve Text**.
4. Receives an improved version.

Available styles:
- Professional
- Friendly
- Shorter

## 4. Core User Story

**As a user, I want to enter a rough message and select a preferred writing style so that I can quickly produce clearer and more appropriate communication.**

## 5. AI Functionality

The application sends the user's text and selected style to an OpenAI language model.

The model is instructed to:
- Improve the original text.
- Follow the selected style.
- Return only the improved version.

The application does not make decisions on behalf of the user. The user reviews the generated text before using it.

## 6. Success Criteria

The MVP is successful if:

- A user can enter text through the web interface.
- A user can select one of the three styles.
- The application successfully calls the AI model.
- The improved text is displayed to the user.
- The application can be deployed as a publicly accessible web application.
- Automated tests pass in the project CI pipeline.