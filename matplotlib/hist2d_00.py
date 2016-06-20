# new histogram lesson
# how to use histograms in matplotlib
# this lesson: simple 2d histogram
import matplotlib.pyplot as plt
import numpy as np

# set the font-size for the entire script
plt.rcParams['font.size'] = 16

# normal distribution center at x=0 and y=5
x = np.random.randn(100000)
y = np.random.randn(100000) + 5

# first attempt at a simple 2d histogram
fig = plt.figure(figsize=(10,8))
plt.hist2d(x, y, bins=40)
plt.colorbar()
plt.show()


#now let's try and dress up the color bar
fig = plt.figure(figsize=(10,8))
plt.hist2d(x, y, bins=40)
bar = plt.colorbar()
bar.ax.set_ylabel('Color Bar Title')
plt.show()


# let's play around with the binning
fig = plt.figure(figsize=(10,8))
binx = np.linspace(-5,5,25)
biny = np.linspace(0,10,5)
plt.hist2d(x, y, bins=[binx,biny])
bar = plt.colorbar()
bar.ax.set_ylabel('Color Bar Title')
plt.show()


# log-scale in Z
from matplotlib.colors import LogNorm

fig = plt.figure(figsize=(10,8))
plt.hist2d(x, y, bins=40,norm=LogNorm())
plt.colorbar()
plt.show()
