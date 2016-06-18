# simple script to make a plot with python's matplotlib
# now let's add our own function to use for plotting
import matplotlib.pyplot as plt
import numpy as np

# set the font-size for the entire script
plt.rcParams['font.size'] = 16

# plot neutrino osc. probability
# under sterile assumption w/ approx. of osc. prob.
# define mixing angle and mass splitting
# sin^(2 theta) = 0.01
angle = 0.01
# delta mass^2 = 1.0 eV^2
mass = 1.0
# function assumes L in km and E in GeV
def OscProb(L,E):
    return angle * ( np.sin( 1.27 * mass * L / E) )**2

# vectorize the funcion!
OscProb_v = np.vectorize(OscProb)

# use a baseline from 0 to 3 km
baseline_v = np.linspace(0,3,500)

# oscillation probability for 1 GeV neutrino
oscprob_001GeV_v = OscProb_v(baseline_v, 1.0)
# oscillation probability for 10 GeV neutrino
oscprob_010GeV_v = OscProb_v(baseline_v, 10.0)
# oscillation probability for 0.1 GeV neutrino
oscprob_200MeV_v = OscProb_v(baseline_v, 0.2)

# now let's plot

# first, make the figure object.
fig = plt.figure( figsize=(10,7) )

# plt.plot command
plt.plot( baseline_v, oscprob_001GeV_v, 'b-', label='Osc. Prob. 1 GeV', lw=3)
plt.plot( baseline_v, oscprob_010GeV_v, 'r-', label='Osc. Prob. 10 GeV', lw=3)
plt.plot( baseline_v, oscprob_200MeV_v, 'g-', label='Osc. Prob. 200 MeV', lw=3)
# legend.
plt.legend(loc=1, fontsize=14)
# the axes:
plt.xlabel('Baseline L [km]')
plt.ylabel('Osc. Probability')
# and the title
plt.title(r'$P_{\mu e}$ assuming $\sin^2{2\theta} = %.02f$ and $\Delta m^2 = %.01f eV^2$'%(angle,mass))
# and the one command you will always want!
plt.grid(True)
# finally show the image
plt.show()
