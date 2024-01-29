import sys

sys.path.append(".")
print("Path added")
import random
from . import annen_fil

def ett():
    s = random.choice([1, 2, 3, "en", "to", "tre"])
    annen_fil.niceprint(s)

if __name__ == "__main__":
    ett()
