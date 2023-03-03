#see peaks meile arvutama seda funktsiooni, mis peaks temp ja aja suhet kirjeldama.
import math
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

q = float(input("Mis aega sa sooviksid 38 kraadi juures kasutada? ") )
#q = 3.25
t = q - 3.25
#print(t)

def f(x_var):
    func = (167 + (252*t+32*t)) * np.exp((-1)*(0.02*t + 0.1)*x_var)
    return func
#print(f(3.25))

x = sy.symbols("x")     # siinkohas 'y' deklareerimine jama oligi
y = (167.0 + (252.0*t + 32.0*t)) * sy.exp((-1.0)*(0.02*t + 0.1)*x)
print("y =", sy.simplify(y))

# Graafiku jaoks
fig, ax = plt.subplots()
time = np.linspace(10, 45, 1000)
ax.plot(time, f(time))
plt.xlabel('Temperatuur(C)')
plt.ylabel('Aeg (min)')
ax.grid()
plt.show()