# new histogram lesson
# how to fit using scipy.curve_fit
from scipy.optimize import curve_fit
# in this script we focus on representing histogrammed data
# as data-points w/ error bars
import matplotlib.pyplot as plt
import numpy as np

# set the font-size for the entire script
plt.rcParams['font.size'] = 16

# define the function we are interested in fitting to
def gauss(x,A,mu,sigma):

    return A * np.exp( - ((x-mu)**2) / (2 * sigma**2) )


# generate a dataset of random numbers [this is ideally your data-set. But we are just testing]
mu = 5.
sigma = 1.5
gauss_v = np.random.normal(mu,sigma,2000)

# prepare bins:
xmin = -0.5 # minimum bin entry 
xmax = 10.5 # maximum bin entry:
nbin = 31   # number of bins
bin_v = np.linspace(xmin, xmax, nbin+1)
# use numpy to bin the information
values, bins = np.histogram(gauss_v,bin_v)

# calculate the bin-centers
bin_centers = 0.5*(bins[1:]+bins[:-1])

# fit this data and extract constants
# try with a guess
guess = [np.sum(values), 3.0, 2.0]
popt,popv = curve_fit(gauss,bin_centers,values)#,p0=guess)
print popt

# now histogram these values
fig = plt.figure(figsize=(10,7))

# draw data-points
plt.errorbar(bin_centers,values,yerr=np.sqrt(values),fmt='o',color='b',lw=2,label=r'$\mu = %.01f$ $\sigma = %.01f$'%(mu,sigma),markersize=8)
# draw fitted curve
xvals = np.linspace(xmin,xmax,100)
plt.plot(xvals,gauss(xvals,*popt),'r-',lw=2,label='Fitted curve')

plt.grid(True)
plt.xlabel('X [random draw]')
plt.ylabel('Y [frequency]')
plt.legend(loc=1)
plt.title('Simple histogram example')
plt.show()
