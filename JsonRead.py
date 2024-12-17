import json
import os

def read_Json(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            data = json.load(f)
            for item in data:
                yield item