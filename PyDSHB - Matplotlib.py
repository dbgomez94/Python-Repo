import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

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
fig, ax = plt.subplots(2)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

fig1 = plt.figure()
ax1 = plt.axes()
ax1.plot(x, np.sin(x))

fig2 = plt.figure()
ax2 = plt.axes()
ax2.plot(x, np.cos(x))

# this line is from pycharm
# this line is also from pycharm
