from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)

# Local knowledge base
knowledge_base = {
    "hello": "Hello! Welcome to SmartAssist. How can I help you?",
    "hi": "Hi! What would you like to learn today?",
    "good morning": "Good morning! How can I assist you today?",
    "your name": "I am SmartAssist, your knowledge assistant.",
    "who are you": "I am SmartAssist, a retrieval-based knowledge chatbot.",
    "thank you": "You're welcome! Feel free to ask another question.",
    "bye": "Goodbye! Have a wonderful day."
}
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()


# Search local knowledge
def search_knowledge(question):

    question = clean_text(question)

    if question in knowledge_base:
        return knowledge_base[question]

    # Match a known topic inside the question
    for topic, answer in knowledge_base.items():

        if topic in question:
            return answer

    return None


# Retrieve information from Wikipedia
def search_wikipedia(question):

    try:
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": question,
            "format": "json"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10,
            headers={"User-Agent": "SmartAssistChatbot/1.0"}
        )

        response.raise_for_status()

        results = response.json()["query"]["search"]

        if not results:
            return None

        title = results[0]["title"]

        summary_url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + requests.utils.quote(title, safe="")
        )

        summary_response = requests.get(
            summary_url,
            timeout=10,
            headers={"User-Agent": "SmartAssistChatbot/1.0"}
        )

        summary_response.raise_for_status()

        data = summary_response.json()

        return data.get("extract")

    except requests.RequestException as error:
        print("Wikipedia connection error:", error)
        return None

    except (KeyError, ValueError):
        return None


# Main chatbot response
def get_bot_response(message):

    if not message.strip():
        return "Please enter a question."

    # First search local knowledge
    answer = search_knowledge(message)

    if answer:
        return answer

    # If not found, search Wikipedia
    answer = search_wikipedia(message)

    if answer:
        return answer

    return (
        "Sorry, I couldn't find reliable information about this question. "
        "Please try another question or use different keywords."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():

    data = request.get_json(silent=True) or {}

    message = data.get("message", "")

    reply = get_bot_response(message)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)