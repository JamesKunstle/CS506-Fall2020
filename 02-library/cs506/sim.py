import math
from typing import List

def euclidean_dist(x, y):
<<<<<<< HEAD
    if (len(x) == 0) or (len(y) == 0) or (len(x) != len(y)):
        return 0
    dist: float = 0
    for x_i, y_i in zip(x, y):
        dist += (x_i - y_i) ** 2
    return math.sqrt(dist)
=======
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)
>>>>>>> a19297dd00e822f88b59df77a271525a8e9e3836

def manhattan_dist(x, y):
    if (len(x) == 0) or (len(y) == 0) or (len(x) != len(y)):
        return 0
    dist: float = 0
    for x_i, y_i in zip(x, y):
        dist += (x_i - y_i)
    return abs(dist)

def jaccard_dist(x, y):
    if (len(x) == 0) or (len(y) == 0) or (len(x) != len(y)):
        return 0

    intersection: int = len(list(set(x) & set(y)))
    union: int = len(list(set(x) | set(y)))

    if union == 0: return 0

    return 1 - (intersection / union)

    

def cosine_sim(x, y):
    if (len(x) == 0) or (len(y) == 0) or (len(x) != len(y)):
        return 0
    num: float = 0
    l_den: float =  0
    r_den: float =  0
    for x, y in zip(x, y):
        num += x * y
        l_den += x ** 2
        r_den += y ** 2
    
    return num / (math.sqrt(l_den) * math.sqrt(r_den))


# Feel free to add more


if __name__ == "__main__":
    print(jaccard_dist([0, 0, 0], [1, 1, 1]))