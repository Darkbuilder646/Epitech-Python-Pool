import random as rd
import time as t
sT = t.time()
mL = []
mL = [rd.randint(0,100) for i in range(1000000)]
d = t.time() - sT
print(d)