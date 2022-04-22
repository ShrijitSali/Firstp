from typing import List

g = {'i': 1}
print(g.keys())

# add 2 lists
import numpy as np

x = [1, 4, 6, 9]
y = [2, 4, 6, 5]
z = []
for i in range(0, len(x)):
    z.append(x[i] + y[i])
print(z)
print(np.add(x, y))
