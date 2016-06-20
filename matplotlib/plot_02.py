# simple script to make a plot with python's matplotlib
# learn how to use multiple axes.
import matplotlib.pyplot as plt
import numpy as np

# set the font-size for the entire script
plt.rcParams['font.size'] = 16

# lifetime correction (vs. drift time)

xpos = np.linspace(0,2.56,1000)
attn8 = np.exp( -xpos / (0.008 * 1103) )
attn7 = np.exp( -xpos / (0.007 * 1103) )
attn9 = np.exp( -xpos / (0.009 * 1103) )



fig, ax = plt.subplots(figsize=(10,8))

# Add some extra space for the second axis at the bottom
fig.subplots_adjust(bottom=0.2)


plt.plot(xpos,attn8,'b-',lw=2,label='8 ms electron lifetime')
plt.plot(xpos,attn7,'b--',lw=1,label='7 ms electron lifetime')
plt.plot(xpos,attn9,'b-.',lw=1,label='9 ms electron lifetime')
ax.grid()
ax.set_xlabel('Distance from TPC Anode [m]')
ax.set_ylabel('Frac. of Charge Reaching Anode')
ax.set_xlim([0,2.56])
ax.legend(fontsize=16)

ax2 = ax.twiny()
ax2.xaxis.set_ticks_position("bottom")
ax2.xaxis.set_label_position("bottom")
ax2.spines["bottom"].set_position(("axes", -0.15))
new_tick_locations = np.array([0., .64, 1.28, 1.92, 2.56])
new_tick_values    = new_tick_locations / 1.103
new_tick_values    = ['%.1f'%v for v in new_tick_values]
ax2.set_xticks(new_tick_locations)
ax2.set_xticklabels(new_tick_values)
ax2.set_xlabel("Drift Time [ms]")
ax2.spines['bottom'].set_color('red')
ax2.xaxis.label.set_color('red')
ax2.tick_params(axis='x', colors='red')

plt.title('Lifetime Attenuation for Charge Drifting in TPC')


plt.show()
