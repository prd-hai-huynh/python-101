import json

# read content from a file
with open('workfile', 'r') as f:
    data = f.read()
    print(data)
print(f.closed)

# dump content as json and save to data.json
with open('data.json', 'w') as f:
    x = [1, 'simple', 'list', 2, 3, 4]
    json.dump(x, f)

# load json content from data.json
with open('data.json', 'r') as f:
    x = json.load(f)
    print(x)
