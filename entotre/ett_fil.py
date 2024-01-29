import sys

sys.path.append(".")
print("Path added")
import random
from annen_fil import niceprint

def ett():
    s = random.choice([1, 2, 3, "en", "to", "tre"])
    niceprint(s)

if __name__ == "__main__":
    ett()
