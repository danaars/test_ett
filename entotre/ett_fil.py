#import sys

#sys.path.append(".")
#print("Path added")
import random
#from . import annen_fil
from entotre.submodule.submodfile import submodfunc
#print("submod import succ")
from entotre.annen_fil import niceprint

def ett():
    s = random.choice([1, 2, 3, "en", "to", "tre"])
    #annen_fil.niceprint(s)
    niceprint(s)
    if isinstance(s, int):
        print(f"SubModFunc of {s}: {submodfunc(s)}")

if __name__ == "__main__":
    ett()
