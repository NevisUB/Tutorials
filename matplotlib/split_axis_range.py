#vic
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['font.family'] = 'serif'

import numpy as np


# Lots of the time my histogram has a bin that really obscures
# the overall histogram feature. A great example histograming
# the single PE spectum. You will find that the spectum has a large
# bin near zero (this is the integrated baseline...) for example


# 10000 ``baseline" values
pedestal = np.zeros(100000)

# The actual signal we care about
npe = [np.random.normal(pe,pe,int(10000/float(pe))) for pe in xrange(1,5)]

# stack them (turn them from list of np.array to np.array)
npe = np.hstack(tuple(npe))

# add pedestal and signal together
data = np.concatenate((pedestal,npe),axis=0)

# make a figure
fig, ax = plt.subplots(figsize=(10,6))

#histogram them, explicitly give the bins
ax.hist(data,bins=np.arange(0,10+0.1,0.1),histtype='stepfilled',color='blue',lw=2)

#labels
ax.set_xlabel("V*s",fontweight='bold')
ax.set_ylabel("Count",fontweight='bold')

plt.grid()
#show it
plt.show()


# Looks annoying, we chould just restrict the range, or convert to the log scale
# but lets practice breaking the Y axis into two regions

# make a new figure
fig, (ax1,ax2) = plt.subplots(2,1,sharex=True,figsize=(10,6))

# plot it twice, on two difference axis
kwargs = {'bins' : np.arange(0,10+0.1,0.1),'histtype': 'stepfilled', 'color': 'blue', 'lw' :2}
ax1.hist(data,**kwargs)
ax2.hist(data,**kwargs)

# labels
ax1.set_ylabel("Count",fontweight='bold')
ax2.set_xlabel("V*s",fontweight='bold')

ax1.set_ylim(1e4,1.25e5)
ax2.set_ylim(0,800)

# remove the top and bottom lines
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)


plt.subplots_adjust(hspace=0.15)

# how big to make the diagonal lines in axes coordinates
d = .015 

# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax2.transAxes, color='k', clip_on=False)

# bottom-right diagonal
ax2.plot((1-d,1+d),(1-d,1+d), **kwargs)

# bottom-left diagonal
ax2.plot((-d,+d),(1-d,1+d), **kwargs) 

# switch to the bottom axes, update the dictionary key
kwargs.update(transform=ax1.transAxes) 

# top-right diagonal
ax1.plot((1-d,1+d),(-d,+d), **kwargs)

# top-left diagonal
ax1.plot((-d,+d),(-d,+d), **kwargs)


ax1.grid(True)
ax2.grid(True)
plt.show()


