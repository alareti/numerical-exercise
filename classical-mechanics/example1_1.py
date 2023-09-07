# %%
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

g = 9.80665


def position(t, theta, mu, length):
    pos = 0.5 * g * (np.sin(theta) - mu * np.cos(theta)) * t**2
    return np.fmin(pos, length)


def height(t, theta, mu, length):
    x = length - position(t, theta, mu, length)
    return x * np.sin(theta)


mu = 0
theta = np.pi / 2
length = 1

t = np.linspace(0, 1, 100)
y_t = height(t, theta, mu, length)

fig, ax = plt.subplots()
ax.set_xlabel("Time (s)")
ax.set_ylabel("Height (m)")
ax.plot(t, y_t)
plt.show()


# %%
def integrand(t, theta, mu):
    return g * (np.sin(theta) - mu * np.cos(theta))


def first_integral(t):
    return integrate.quad(integrand, 0, t, args=(theta, mu))[0]


def integral(t):
    return integrate.quad(first_integral, 0, t)[0]


def height_integral(length, position):
    x = np.fmax(length - position, 0)
    return x * np.sin(theta)


t = np.linspace(0, 1, 100)
pos_t = np.vectorize(integral)(t)
y_t = height_integral(length, pos_t)

fig, ax = plt.subplots()
ax.set_xlabel("Time (s)")
ax.set_ylabel("Height (m)")
ax.plot(t, y_t)
plt.show()
