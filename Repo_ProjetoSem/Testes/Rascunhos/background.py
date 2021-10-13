import numpy

l1 = 150
l2 = 160

res = 1000

alfa = linspace(10, 140, res)
beta = linspace(240, 360, res)

x = l1*cos(alfa)+l2*cos(beta)
y = l1*sin(alfa)+l2*cos(beta)

print(alfa)