# GK Buddy - General Knowledge AI Chatbot

A responsive, interactive General Knowledge chatbot built with Flask and Gemini.

## Project structure

- app.py - Flask backend + Gemini API
- templates/index.html - complete frontend (HTML/CSS/JS)
- requirements.txt - dependencies
- .env.example - API key template

## Run locally

1. Install Python 3.10+.
2. Open this folder in VS Code / PowerShell.
3. Install dependencies:
   `python -m pip install -r requirements.txt`
4. Create a file named `.env`.
5. Copy the line from `.env.example` and replace it with your Gemini API key.
6. Run:
   `python app.py`
7. Open http://127.0.0.1:5000

Never upload your real `.env` or API key to GitHub.
