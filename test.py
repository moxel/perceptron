import moxel

model = moxel.Model('moxel/hello:latest', where='localhost')

output = model.predict(sentence="hello, i am happy")
print(output['sentiment'])
