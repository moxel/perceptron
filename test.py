import moxel

model = moxel.Model('strin/hello:latest', where='localhost')

output = model.predict(sentence="hello, i am happy")
print(output['sentiment'])
