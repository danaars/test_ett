import sys

sys.path.append(".")
import random
from annen_fil import niceprint

def ett():
    s = random.choice([1, 2, 3, "en", "to", "tre"])
    niceprint(s)

if __name__ == "__main__":
    ett()
