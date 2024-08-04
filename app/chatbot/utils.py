import spacy
from spellchecker import SpellChecker
from sklearn.feature_extraction.text import TfidfVectorizer
import logging

nlp = spacy.load("en_core_web_sm")
spell = SpellChecker()
unique_words = {"ibit", "bbit", "mbit", "cafe", "fyp"}


def custom_tokenize(text):
    doc = nlp(text.lower())
    return [
        token.lemma_ for token in doc if not token.is_stop and not token.is_punct
    ] or ["emptytoken"]


def correct_spelling(text, intents):
    words = text.split()
    corrected_words = []
    for word in words:
        if word.lower() in unique_words or any(
            word.lower() in pattern.lower()
            for intent in intents
            for pattern in intent["patterns"]
        ):
            corrected_words.append(word)
        else:
            corrected_words.append(spell.correction(word) or word)
    corrected_text = " ".join(corrected_words)
    logging.debug(f"Corrected spelling from '{text}' to '{corrected_text}'")
    return corrected_text


def preprocess_and_vectorize(intents):
    sentences, tags = [], []
    for intent in intents:
        for pattern in intent.get("patterns", []):
            sentences.append(pattern.lower())
            tags.append(intent["tag"])
    vectorizer = TfidfVectorizer(tokenizer=custom_tokenize, stop_words="english")
    X = vectorizer.fit_transform(sentences)
    logging.debug(f"Vectorized sentences: {sentences}")
    logging.debug(f"Vectorized matrix shape: {X.shape}")
    return X, tags, vectorizer


def strip_greetings(text):
    greetings = ["hi", "hello", "hey"]
    words = text.split()
    if words and words[0].lower() in greetings:
        return " ".join(words[1:])
    return text
