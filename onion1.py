from base64 import a85decode

with open("onion-1.txt", "r") as fopen:
    text = fopen.read()

text = text[:-1]

decoded = a85decode(text, adobe=True).decode("utf-8")

with open("onion-2.txt", "w") as fopen:
    fopen.write(decoded)
