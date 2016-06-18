# www.larbys.com
# vgenty@larbys.com

import ROOT
import numpy as np

# Make a canvas with tgraph
c1 = ROOT.TCanvas()
tg = ROOT.TGraph()

# Put on a few points
for i in xrange(1,10):
    tg.SetPoint(i-1,i,np.log(i))

# Draw A(ll) L(ine) P(oints)
tg.Draw("ALP")

# Remember this? tell the canvas there is something on it
c1.Update()
c1.Modified()


# YUCK! Get me the data quickly before I turn into a physicist !

# np from buffer to the rescue! Carefull though if TGraph gets
# destroyed then we lose this memory
xy_pairs = np.vstack((np.frombuffer(tg.GetX(),            #X data
                                    count=tg.GetN()),     #how much x data
                      np.frombuffer(tg.GetY(),            #Y data
                                    count=tg.GetN()))).T  #how much y data

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['font.family'] = 'serif'


fig,ax = plt.subplots(figsize=(10,6))

ax.plot(xy_pairs[:,0], #x
        xy_pairs[:,1], #y
        '-o',          #lines with points
        lw=2)          #width of the line

ax.set_xlabel("X",fontweight='bold')
ax.set_ylabel("Y",fontweight='bold')

plt.show()
