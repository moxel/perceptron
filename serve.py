import random
import json

model = json.load(open('model.json', 'r'))

def predict(sentence):
    words = sentence.split(' ')
    score = 0.
    for word in words:
        score += model.get(word, 0.)

    if score > 0: return {'sentiment': '+'}
    else: return {'sentiment': '-'}
