import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

plt.style.use('classic')

# %% show() or no show()?
x = np.linspace(0, 10, 100)

# MATLAB-style plotting
plt.figure()  # create a plot figure
plt.subplot(2, 1, 1)   # same as MATLAB (rows, cols, subplot)
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.xlabel('x')
plt.ylabel('y')

# more powerful object oriented-style plotting
f1, ax = plt.subplots(2)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

plt.figure()
ax1 = plt.axes()
ax1.plot(x, np.sin(x))

plt.figure()
ax2 = plt.axes()
ax2.plot(x, np.cos(x))

# scatter plots with plt.scatter
plt.figure()
plt.style.use('seaborn-whitegrid')
rng = np.random.RandomState(0)
x = rng.randn(100)  # -1 to 1
y = rng.randn(100)  # -1 to 1
colors = rng.rand(100)  # 0 to 1
sizes = 1000 * rng.rand(100)  # 0 to 1 x 1000 so 0 to 1000

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar()

iris = load_iris()
features = iris.data.T
plt.scatter(features[0], features[1], alpha=0.2, s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# error bars
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

plt.figure()
plt.errorbar(x, y, yerr=dy, fmt='.k')

plt.figure()
plt.errorbar(x, y, yerr=dy, fmt='o', color='k', ecolor='lightgray', elinewidth=3, capsize=0)

## Density and contour plots


def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure()
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()

plt.figure()
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
plt.colorbar()

plt.figure()
contours = plt.contour(X, Y, Z, 3)
plt.clabel(contours, inline=True, fontsize=8)
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', alpha=0.5)
plt.colorbar()

## Histograms, binnings, and density
data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=100, alpha=0.5, histtype='stepfilled', color='steelblue')

x1 = np.random.normal(1, 1, 1000)  # normal(location, scale, size)
x2 = np.random.normal(2, 1, 1000)
x3 = np.random.normal(3, 1, 1000)
plt.figure()
plt.hist(x1)
plt.hist(x2)
plt.hist(x3)