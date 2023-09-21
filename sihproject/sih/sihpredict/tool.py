def get_sentiment(sentence):
    if(sentence[-1] == '.'):
        return "positive"
    elif sentence[-1] == ' ':
        return "negative"
    else:
        return "neutral"