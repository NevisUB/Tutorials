# new histogram lesson
# how to use histograms in matplotlib
# in this script we focus on representing histogrammed data
# as data-points w/ error bars
import matplotlib.pyplot as plt
import numpy as np

# set the font-size for the entire script
plt.rcParams['font.size'] = 16

# 1st generate a dataset of random numbers [this is ideally your data-set. But we are just testing]

mu = 5.
sigma = 1.5
gauss_v = np.random.normal(mu,sigma,700)

# now histogram these values
fig = plt.figure(figsize=(10,7))
# prepare bins:
xmin = -0.5 # minimum bin entry 
xmax = 10.5 # maximum bin entry:
nbin = 11   # number of bins
bin_v = np.linspace(xmin, xmax, nbin+1)
# use numpy to bin the information
values, bins = np.histogram(gauss_v,bin_v)
# calculate the bin-centers
bin_centers = 0.5*(bins[1:]+bins[:-1])
print 'values returned : ',values
print 'bins   returned : ',bins
print 'bin centers are : ',bin_centers

plt.errorbar(bin_centers,values,yerr=np.sqrt(values),fmt='o',color='b',lw=2,label=r'$\mu = %.01f$ $\sigma = %.01f$'%(mu,sigma),markersize=8)
plt.grid(True)
plt.xlabel('X [random draw]')
plt.ylabel('Y [frequency]')
plt.legend(loc=1)
plt.title('Simple histogram example')
plt.show()
