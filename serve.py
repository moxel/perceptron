import random
import json

model1 = json.load(open('models/model1.json', 'r'))
model2 = json.load(open('models/model2.json', 'r'))
model = {}
model.update(model1)
model.update(model2)

def predict(sentence):
    words = sentence.split(' ')
    score = 0.
    for word in words:
        score += model.get(word, 0.)

    if score > 0: return {'sentiment': '+'}
    else: return {'sentiment': '-'}
