import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file.")

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.6-flash"

SYSTEM_PROMPT = """
You are GK Buddy, a fast and friendly General Knowledge AI chatbot.
Answer questions from general knowledge: science, technology, history,
geography, space, sports, inventions, computers, nature, education,
current affairs when the model has reliable knowledge, and everyday facts.

Rules:
- Give the direct answer first.
- Keep normal answers concise and easy to understand.
- For questions that need explanation, use short headings and bullet points.
- If the user asks in Tamil/Thanglish, reply in Tamil/Thanglish.
- If the user asks in English, reply in English.
- Do not pretend to know real-time information you cannot verify.
- If a question is unclear, ask one short clarification.
- Be friendly and interactive.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"answer": "Please type a question."}), 400

    prompt = f"{SYSTEM_PROMPT}\n\nUser question: {message}"

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        answer = getattr(response, "text", None) or "Sorry, I couldn't generate an answer."
        return jsonify({"answer": answer})
    except Exception as e:
        print("Gemini error:", e)
        return jsonify({
            "answer": "Sorry, something went wrong. Please check your Gemini API key and try again."
        }), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
