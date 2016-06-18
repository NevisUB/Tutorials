# simple script to make a plot with python's matplotlib

import matplotlib.pyplot as plt
import numpy as np

# set the font-size for the entire script
plt.rcParams['font.size'] = 16

# create an array of equally spaced points
# 1st argument: min x value
# 2nd argument: max x value
# 3rd argument: num. of points in-between
xarray = np.linspace(0,10,100)

# y points are cos^2 of xarray points:
yarray = np.cos(xarray)**2

# now let's plot

# first, make the figure object.
fig = plt.figure( figsize=(10,6) )

# plt.plot command
# first 2 arguments are the arrays of equal length
# then you can specify how to plot the image
# 'bo' -> blue data-points [o stands for a point]
# other colors are:
# b = blue
# r = red
# g = green
# c = cyan
# k = black
# m = magenta
# y = yellow
# label is what will be shown in the legend, if one is drawn
plt.plot( xarray, yarray, 'bo', label='Cos^2 [x]')
# legend.
# location argument determined where in the image the legend goes
# 1 -> upper right
# 2 -> upper left
# 3 -> lower left
# 4 -> lower right
# 5,6,7,8 upper/lower/left/right centered on the axis (possibly not in that order)
plt.legend(loc=1, fontsize=12)
# the axes:
plt.xlabel('x [unitless]')
plt.ylabel('Cos^2 [x]')
# and the title
plt.title('Example of Simple Matplotlib Plot')
# and the one command you will always want!
plt.grid(True)
# finally show the image
plt.show()
