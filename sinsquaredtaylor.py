import math
from matplotlib import pyplot as plt
import numpy as np


def sinsquaredtaylor(x, a=50, b=49):
    return sum([sum([(((-1)**(n+m))*x**(2*n + 2**(m+1)))/(math.factorial(2*n +1)*math.factorial(2*m+1)) for n in range(b)]) for m in range(a)])



x = np.linspace(0, 1, 1000)
plt.plot(x, sinsquaredtaylor(x))
plt.plot(x, np.sin(x)**2)

plt.show()
