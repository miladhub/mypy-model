import sys
import json
import base64
import mymodel

def b64_to_string(line):
    b64 = line.encode("utf-8")
    str_encoded = base64.b64decode(b64)
    return str_encoded.decode("utf-8")

if __name__ == "__main__":
    for line in sys.stdin:
        js = b64_to_string(line)
        args = json.loads(js)
        mymodel.predict(args)
