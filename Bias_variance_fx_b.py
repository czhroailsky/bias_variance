## Bias and variance

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from numpy import arange, pi, sin
import numpy as np
import random 
import math
import os

# Iterations

experiments = 200

# Bias list
b_list = []

for i in range(experiments):
    # Random points
    x1 = random.uniform(0, 1.0)
    x2 = random.uniform(0, 1.0)
    y1 = sin(2*x1*pi)
    y2 = sin(2*x2*pi)
    
    # Mean between two random points
    dis = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    b = max(y1, y2) - dis/2
    b_list.append(b)

# Sin() function
t = arange(0, 1, 0.01)
ft = sin(2*t*pi)

# Bias iteration to list (One element)
aux = []
reci = []
for number in b_list:
	reci.append(number)
	aux.append(reci)
	reci = []

# Constant hypothesis h(x) = b
imprimir = []
for element in aux:
	imprimir.append(element*len(t))
    
# Mean bias (mean between all the bias lines)
mean_b = sum(b_list)/len(b_list)
g_bar = mean_b

# Mean bias (list size to plot)
g_bar_imp = [g_bar]*len(t)

# Mean squared error from mean bias and Sin() function
lista_bias = []
for element in t:
	bias_x = math.pow(mean_b - sin(2*element*pi), 2)
	lista_bias.append(bias_x)

# Bias
pro_bias = sum(lista_bias)/len(lista_bias)
print('Bias = %f' % pro_bias)

# Variance
promedio_b = sum(b_list)/len(b_list)
interior = [x-promedio_b for x in b_list]
cuadrado = [math.pow(x, 2) for x in interior]
suma = sum(cuadrado)
variance = suma/(len(b_list)-1)
print('Variance = %f' % variance)

# Plot
plt.plot(t, ft)
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(0, 1)
##ax1.plot(x1, y1, 'ro')
##ax1.plot(x2, y2, 'ro')
for element in imprimir:
	plt.plot(t, element, alpha = 0.5, color = 'g')
plt.plot(t, g_bar_imp, alpha = 0.5, color = 'r', linewidth = 2)
"""ax2 = fig.add_subplot(212)
ax2.plot(t, ft)
ax2.grid(True)
ax2.set_ylim(-2, 2)"""
plt.text(0.5, 1.75, 'Bias = '+str(pro_bias))
plt.text(0.5, 1.64, 'Variance = '+str(variance))
plt.show()
#plt.savefig(os.path.join('Sinusoidal_uno.png'), dpi = 300, format = 'png', bbox_inches = 'tight')