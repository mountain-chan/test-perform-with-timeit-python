import timeit

setup = """
import re
from data_test import message
words = message.split()
"""

ex1 = """ 
i = 0
for word in words:
    rep = re.sub(r"[.,?!:()“”]", "", word).lower()
    words[i] = rep
    i += 1
"""

ex2 = """ 
i = 0
for word in words:
    rep = word
    if "," in rep:
        rep = rep.replace(",", "")
    if "." in rep:
        rep = rep.replace(".", "")
    if "?" in rep:
        rep = rep.replace("?", "")
    if "(" in rep:
        rep = rep.replace("(", "")
    if ")" in rep:
        rep = rep.replace(")", "")
    if ":" in rep:
        rep = rep.replace(":", "")
    if "!" in rep:
        rep = rep.replace("!", "")
    if "“" in rep:
        rep = rep.replace("“", "")
    if "”" in rep:
        rep = rep.replace("”", "")
    if not rep.islower():
        rep = rep.lower()
    words[i] = rep
    i += 1
"""

long = timeit.timeit(ex1, setup=setup, number=10)
print(long)

long = timeit.timeit(ex2, setup=setup, number=10)
print(long)
