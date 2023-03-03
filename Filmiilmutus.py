import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

q = float(input("Mis aega tahad kasutada 38 kraadi juures?"))

def f(x_var):
    func = (0.7586*q**2-5.4749*q+64.55)*(x_var**(-0.0301*q**2+0.2719*q-0.8617))
    return func

x = sy.symbols("x")
y = (0.7586*q**2-5.4749*q+64.55)*(x**(-0.0301*q**2+0.2719*q-0.8617))
print("y =", sy.simplify(y))

fig, ax = plt.subplots()
time = np.linspace(0, 30, 1000)
ax.plot(time, (time))
plt.xlabel('Aeg (min)')
plt.ylabel('Temperatuur(C)')
ax.grid()
plt.show()

def y_lahend(y_var):
    return sy.solve((((0.7586*q**2-5.4749*q+64.55)*(x**(-0.0301*q**2+0.2719*q-0.8617)))-y_var), x)


p = float(input("\nMis temperatuuri juures on aega tarvis? "))
v = y_lahend(p)
print(v)