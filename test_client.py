import moxel

model = moxel.Model('bot/ci-perceptron-dir:latest', where='dev')

output = model.predict(sentence='happy')['sentiment']
print('outpout:', output)

if output == '+':
    exit(0)

exit(1)
