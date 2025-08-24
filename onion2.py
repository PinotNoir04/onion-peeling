from base64 import a85decode


def process(payload):
    b_decoded = a85decode(payload[:-1], adobe=True)
    res = bytearray()
    for b in b_decoded:
        b ^= 85
        odd = (b & 1)
        b >>= 1
        b |= 128 if odd else 0
        res.append(b)
    return res.decode("utf-8")


with open("onion-2.txt", "r") as f:
    text = f.read()

with open("onion-3.txt", "w") as f:
    f.write(process(text))
