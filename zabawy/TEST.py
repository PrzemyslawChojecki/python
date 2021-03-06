import random
import math
import matplotlib.pyplot as plt


def los(K):
    l = 0
    for k in range(K):
        r = random.uniform(0, 1)
        if r > 1 / (math.fabs(l / 30) + 2):
            if l < 0:
                l += 1
            elif l > 0:
                l -= 1
            else:
                r = random.randint(0, 1)
                if r:
                    l += 1
                else:
                    l -= 1
        else:
            if l > 0:
                l += 1
            else:
                l -= 1
    return l


dic = {}

for d in range(300):
    l = los(100)
    try:
        dic[l] += 1
    except:
        dic[l] = 1

print(dic)