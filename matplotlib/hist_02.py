# 1st histogram lesson
# how to use histograms in matplotlib
# in this example we present how to share one axis
# so that we can draw two curves with different scales
import matplotlib.pyplot as plt
import numpy as np

# set the font-size for the entire script
plt.rcParams['font.size'] = 16

# 1st generate a dataset of random numbers [this is ideally your data-set. But we are just testing]

mu = 5.
sigma = 1.5
gauss_v = np.random.normal(mu,sigma,1000)

# now histogram these values
fig, ax = plt.subplots(figsize=(10,7))
# now create a second axis which shares the x-axis
ax2 = ax.twinx()

# prepare bins:
xmin = -3.5 # minimum bin entry 
xmax = 13.5 # maximum bin entry:
nbin = 25   # number of bins
bin_v = np.linspace(xmin, xmax, nbin+1)
# use numpy to bin the information
values, bins = np.histogram(gauss_v,bin_v)
# calculate the bin-centers
bin_centers = 0.5*(bins[1:]+bins[:-1])

ax.errorbar(bin_centers,values,yerr=np.sqrt(values),fmt='o',color='b',lw=2,label=r'$\mu = %.01f$ $\sigma = %.01f$'%(mu,sigma),markersize=8)
plt.grid(True)
plt.xlabel('X [random draw]')
# for axis object, we have the same functions but instead we use 'set_'.
ax.set_ylabel('Y [frequency]')
ax.tick_params(axis='y',color='blue')
for t in ax.yaxis.get_ticklabels():
    t.set_color('b')



# in this axis we will show the cumulative distribution of the data-points
cumulative_v = []
for val in values:
    if ( len(cumulative_v)  == 0):
        cumulative_v.append(val)
    else:
        cumulative_v.append( cumulative_v[-1] + val)
cumulative_v = np.array(cumulative_v)
# this array has integers. cast as float so that we can normalize
cumulative_v =  cumulative_v.astype(float)
# normalize
cumulative_v /= float(np.sum(values))
ax2.step(bin_centers,cumulative_v, label='Cumulative Distrib.',lw=3,color='r')
ax2.set_ylabel('Frac. of Total Events')
ax2.set_ylim([-0.01,1.01])
for t in ax2.yaxis.get_ticklabels():
    t.set_color('r')
ax2.tick_params(axis='y',color='red')


plt.legend(loc=2)
plt.xlim([-4,14])
plt.title('Simple histogram example')
plt.show()
