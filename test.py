import moxel

model = moxel.Model('strin/test:latest', where='localhost')

output = model.predict(x1="-1", x2=1.5)
print(output['out'])
