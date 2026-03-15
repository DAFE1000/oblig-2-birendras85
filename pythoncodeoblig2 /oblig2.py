import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# original function
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# equation from derivative
def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

# find root
x_guess = 1.5
x_max = fsolve(g, x_guess)[0]
y_max = f(x_max)

print("Toppunkt x:", round(x_max,4))
print("Toppunkt y:", round(y_max,4))

# create x values
x = np.linspace(0,6,500)
y = f(x)

# plot
plt.plot(x,y,label="f(x)=e^(-x/4) arctan(x)")
plt.plot(x_max,y_max,"ro",label="Toppunkt")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot av funksjonen")
plt.grid(True)
plt.legend()

plt.savefig("graf.png")
plt.show()