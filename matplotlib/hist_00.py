# 1st histogram lesson
# how to use histograms in matplotlib
import matplotlib.pyplot as plt
import numpy as np

# set the font-size for the entire script
plt.rcParams['font.size'] = 16

# 1st generate a dataset of random numbers [this is ideally your data-set. But we are just testing]

gauss_v = np.random.normal(10,2,1000)

# now histogram these values
fig = plt.figure(figsize=(10,7))
# prepare bins:
xmin = -0.5 # minimum bin entry 
xmax = 20.5 # maximum bin entry:
nbin = 21   # number of bins
bin_v = np.linspace(xmin, xmax, nbin+1)

print 'Bins are : ',bin_v
plt.hist(gauss_v,bins=bin_v)
plt.grid(True)
plt.xlabel('X [random draw]')
plt.ylabel('Y [frequency]')
plt.title('Simple histogram example')
plt.show()


# now let's make our histogram a bit pretiter and add some additional distributions

mu_00    = 10.
sigma_00 = 2.
gauss_v_00 = np.random.normal(mu_00,sigma_00,1000)
mu_01    = 7.
sigma_01 = 3.
gauss_v_01 = np.random.normal(mu_01,sigma_01,1000)
mu_02    = 9.
sigma_02 = 1.
gauss_v_02 = np.random.normal(mu_02,sigma_02,1000)

# now histogram these values
fig = plt.figure(figsize=(10,7))
# prepare bins:
xmin = -0.5 # minimum bin entry 
xmax = 20.5 # maximum bin entry:
nbin = 21   # number of bins
bin_v = np.linspace(xmin, xmax, nbin+1)

plt.hist(gauss_v_00,bins=bin_v,label=r'$\mu = %i$ $\sigma = %i$'%(mu_00,sigma_00),histtype='stepfilled',alpha=0.5,color='b')
plt.hist(gauss_v_01,bins=bin_v,label=r'$\mu = %i$ $\sigma = %i$'%(mu_01,sigma_01),histtype='stepfilled',alpha=0.5,color='r')
plt.hist(gauss_v_02,bins=bin_v,label=r'$\mu = %i$ $\sigma = %i$'%(mu_02,sigma_02),histtype='stepfilled',alpha=0.5,color='g')
plt.grid(True)
plt.legend(loc=2,fontsize=16)
plt.xlabel('X [random draw]')
plt.ylabel('Y [frequency]')
plt.title('Simple histogram example')
plt.show()
