# serve.py
import random
import json

model = json.load(open('model.json', 'r'))

def predict(x1, x2):
    if model['w1'] * x1 + model['w2'] * x2 > 0:
        return {'answer': 1.}
    else:
        return {'answer': 0.}

