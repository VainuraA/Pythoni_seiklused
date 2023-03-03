import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

#oletame, et kõikide kraadide suhe on neljakordne.
#algtingimusteks võtan DEV 1-2 andmed.
#seega 24C-16min, 30C-8min, 38C-3.25 ja 45C-2min
a = 16
b = 8
c = 3.25
d = 2
z = float(input("Kaua sa tahad ilmutada 38 kraadi juures? "))
f = z - c

Uus_aeg_24 = f*16 + a
Uus_aeg_30 = f*4 + b
Uus_aeg_45 = f/4 + d

#Funktsiooni leidmiseks kasutame Lagrange'i interpolatsioonipolünoomi.
x,y = sy.symbols("x,y")

def func(x):
    func = 24*( ((x-z)*(x-Uus_aeg_30)*(x-Uus_aeg_45))/((Uus_aeg_24-z)*(Uus_aeg_24-Uus_aeg_30)*(Uus_aeg_24-Uus_aeg_45) ) ) +\
           30 * ( ((x-Uus_aeg_24)*(x-z)*(x-Uus_aeg_45))/((Uus_aeg_30-Uus_aeg_24)*(Uus_aeg_30-z)*(Uus_aeg_30-Uus_aeg_45))) + \
           38 * ( ((x-Uus_aeg_24)*(x-Uus_aeg_30)*(x-Uus_aeg_45))/((z-Uus_aeg_24)*(z-Uus_aeg_30)*(z-Uus_aeg_45)) ) +\
           45 *( ((x-Uus_aeg_24)*(x-Uus_aeg_30)*(x-z))/((Uus_aeg_45-Uus_aeg_24)*(Uus_aeg_45-Uus_aeg_30)*(Uus_aeg_45-z)))
    return func
y = 24*( ((x-z)*(x-Uus_aeg_30)*(x-Uus_aeg_45))/((Uus_aeg_24-z)*(Uus_aeg_24-Uus_aeg_30)*(Uus_aeg_24-Uus_aeg_45) ) ) +\
           30 * ( ((x-Uus_aeg_24)*(x-z)*(x-Uus_aeg_45))/((Uus_aeg_30-Uus_aeg_24)*(Uus_aeg_30-z)*(Uus_aeg_30-Uus_aeg_45))) + \
           38 * ( ((x-Uus_aeg_24)*(x-Uus_aeg_30)*(x-Uus_aeg_45))/((z-Uus_aeg_24)*(z-Uus_aeg_30)*(z-Uus_aeg_45)) ) +\
           45 *( ((x-Uus_aeg_24)*(x-Uus_aeg_30)*(x-z))/((Uus_aeg_45-Uus_aeg_24)*(Uus_aeg_45-Uus_aeg_30)*(Uus_aeg_45-z)))

print("y =", sy.simplify(y))
"""
TO DO
Esialgsesse funktiooni vaja y asemele panna temperatuuri väärtus!
"""

# Graafiku jaoks
fig, ax = plt.subplots()
t = np.linspace(0, 50, 100)
plt.ylim([0, 50])
plt.xlim([0, 20])
ax.plot(t, func(t))
plt.xlabel('Aeg (min)')
plt.ylabel('Temperatuur (C)')
ax.grid()
#plt.show()

#print(sy.solve(y, x, dict = True))
#print(inversefunc(y,y_values=38,open_domain=True))


def y_lahend(y):
    return sy.solve(24*( ((x-z)*(x-Uus_aeg_30)*(x-Uus_aeg_45))/((Uus_aeg_24-z)*(Uus_aeg_24-Uus_aeg_30)*(Uus_aeg_24-Uus_aeg_45) ) ) +\
           30 * ( ((x-Uus_aeg_24)*(x-z)*(x-Uus_aeg_45))/((Uus_aeg_30-Uus_aeg_24)*(Uus_aeg_30-z)*(Uus_aeg_30-Uus_aeg_45))) + \
           38 * ( ((x-Uus_aeg_24)*(x-Uus_aeg_30)*(x-Uus_aeg_45))/((z-Uus_aeg_24)*(z-Uus_aeg_30)*(z-Uus_aeg_45)) ) +\
           45 *( ((x-Uus_aeg_24)*(x-Uus_aeg_30)*(x-z))/((Uus_aeg_45-Uus_aeg_24)*(Uus_aeg_45-Uus_aeg_30)*(Uus_aeg_45-z))) - y, x)

q = float(input("\nMis temperatuuri juures on aega tarvis? "))
t = y_lahend(q)
print(t)

#print(sy.solve( 0.0338051009877635*x**3 - 0.396789768538993*x**2 - 4.22887365472506*x + 54.774465575704 - 38, x))
"""
Answers should ne
x == -8.82105464365 || x == 3.250000000000 || x == 17.30862551151
"""
