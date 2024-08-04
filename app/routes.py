from flask import request, jsonify, render_template
from .chatbot.main import ChatBot
from .chatbot.data_loader import load_data
from .chatbot.utils import preprocess_and_vectorize
from .config import Config
import logging

intents = load_data(Config.DATA_PATH)
X, tags, vectorizer = preprocess_and_vectorize(intents)
chatbot = ChatBot(intents, X, tags, vectorizer)


def init_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/get_response", methods=["POST"])
    def respond():
        user_input = request.json.get("user_input", "")
        logging.info(f"User input: {user_input}")

        if not user_input:
            return jsonify({"response": "Please provide an input."})

        response = chatbot.get_response(user_input)
        logging.info(f"Response: {response}")
        return jsonify({"response": response})

    @app.route("/reload_data", methods=["POST"])
    def reload_data():
        global intents, X, tags, vectorizer
        intents = load_data(Config.DATA_PATH)
        X, tags, vectorizer = preprocess_and_vectorize(intents)
        chatbot = ChatBot(intents, X, tags, vectorizer)
        return jsonify({"status": "Data reloaded successfully"})
