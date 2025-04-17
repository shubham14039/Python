import matplotlib.pyplot as plt

nval = []
linear = []
quadratic = []
cubic = []
exponential = []

for i in range(1, 101):
    nval.append(i)
    linear.append(i)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.3**i)

plt.plot(nval,linear)
plt.plot(nval,quadratic)
plt.plot(nval,cubic)
plt.plot(nval,exponential)
plt.xlabel("N")
plt.ylabel("Function")
plt.show()
