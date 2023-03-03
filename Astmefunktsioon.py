#Niisiis. Nüüd võib olla võimalus, et ma sain lõpuks asjale pihta:)
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

q = float(input("Mis aega tahad kasutada 38 kraadi juures?"))
t = q-3.25

def f(x_var):
    func = (51.75 + t)*(x_var**(-0.26 + 0.04*t))
    return func

x = sy.symbols("x")
y = ((51.75 + t)*x**(-0.26 + 0.04*t))
print("y =", sy.simplify(y))

fig, ax = plt.subplots()
time = np.linspace(0, 30, 1000)
ax.plot(time, f(time))
plt.xlabel('Aeg (min)')
plt.ylabel('Temperatuur(C)')
ax.grid()
plt.show()

def y_lahend(y_var):
    return sy.solve(((51.75 + t)*(x**(-0.26 + 0.04*t))-y_var), x)

p = float(input("\nMis temperatuuri juures on aega tarvis? "))
v = y_lahend(p)
print(v)
