from django.conf import settings
import string
import nltk
from collections import Counter


import pickle
with open(str(settings.BASE_DIR) + '\\sihpredict\\trained_models\\positive_negative_neutral_ex.pkl', 'rb') as f:
    MODEL = pickle.load(f)

useless_words = nltk.corpus.stopwords.words("english") + list(string.punctuation)

def build_bag_of_words_features_filtered(words):
    word_counter = Counter(words)
    return {
        word: count for word, count in word_counter.items()
        if word.lower() not in useless_words
    }

def preprocess_statement(statement):
    words = statement.split()
    filtered_words = [word for word in words if word.lower() not in useless_words]
    return build_bag_of_words_features_filtered(filtered_words)

def get_sentiment(sentence):
    input_features = preprocess_statement(sentence)
    sentiment = MODEL.classify(input_features)
    return sentiment
