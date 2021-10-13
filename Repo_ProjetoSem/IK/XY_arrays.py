import numpy as np

l1 = 150
l2 = 160

res = 1000

alfa = np.linspace(10, 140, res)
beta = np.linspace(240, 360, res)

x = l1*np.cos(alfa)+l2*np.cos(beta)
y = l1*np.sin(alfa)+l2*np.cos(beta)

