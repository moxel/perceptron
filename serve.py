import random
import json
import argparse

parser = argparse.ArgumentParser('Parser')
parser.add_argument('-m','--model', default='model.json', type=str)
args = parser.parse_args()

model = json.load(open(args.model, 'r'))

def predict(sentence):
    words = sentence.split(' ')
    score = 0.
    for word in words:
        score += model.get(word, 0.)

    if score > 0: return {'sentiment': '+'}
    else: return {'sentiment': '-'}
