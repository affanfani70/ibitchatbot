import random
import logging
from sklearn.metrics.pairwise import cosine_similarity
from .utils import preprocess_and_vectorize, strip_greetings, correct_spelling
from .gpt_service import get_gpt_response


class ChatBot:
    def __init__(self, intents, X, tags, vectorizer):
        self.intents = intents
        self.X = X
        self.tags = tags
        self.vectorizer = vectorizer

    def get_response(self, user_input):
        if len(user_input) <= 1:
            return "Input is too small. Please enter a more detailed query."

        user_input = strip_greetings(user_input.lower())
        corrected_input = correct_spelling(user_input, self.intents)
        input_vec = self.vectorizer.transform([corrected_input])
        similarities = cosine_similarity(input_vec, self.X)
        closest = similarities.argmax()

        logging.debug(f"Similarity scores: {similarities}")
        logging.debug(
            f"Highest similarity score: {similarities[0, closest]} for tag: {self.tags[closest]}"
        )

        threshold = 0.3

        if similarities[0, closest] < threshold:
            gpt_response = get_gpt_response(corrected_input)
            if gpt_response:
                return gpt_response
            else:
                fallback_responses = [
                    intent.get("responses", [])
                    for intent in self.intents
                    if intent.get("tag") == "fallback"
                ]
                if fallback_responses and fallback_responses[0]:
                    return random.choice(fallback_responses[0])
                else:
                    return "I'm sorry, I didn't understand that. Could you please rephrase?"

        tag = self.tags[closest]
        intent = next(
            (intent for intent in self.intents if intent.get("tag") == tag), None
        )
        if intent:
            return random.choice(
                intent.get(
                    "responses",
                    ["I'm sorry, I didn't understand that. Could you please rephrase?"],
                )
            )
        else:
            fallback_responses = [
                intent.get("responses", [])
                for intent in self.intents
                if intent.get("tag") == "fallback"
            ]
            if fallback_responses and fallback_responses[0]:
                return random.choice(fallback_responses[0])
            else:
                return "I'm sorry, I didn't understand that. Could you please rephrase?"
