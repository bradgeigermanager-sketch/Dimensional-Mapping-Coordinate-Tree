import json
from .vector import Vector10D

def load_points(path):
    with open(path) as f:
        raw = json.load(f)

    return [Vector10D(*p["vector"]) for p in raw]
