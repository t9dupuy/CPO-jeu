import json

def write_file(a, file):
    with open(file, "wb") as fichier:
        fichier.write(json.dumps(a))

def read_file(file):
    with open(file, "rb") as fichier:
        a = json.loads(fichier.read())
    return a

