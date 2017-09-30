import moxel

model = moxel.Model('strin/ci-perceptron:latest', where='dev')

output = model.predict(sentence='happy')['sentiment']
print('outpout:', output)

if output == '+':
    exit(0)

exit(1)
