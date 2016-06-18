# www.larbys.com
# vgenty@larbys.com

import ROOT
from ROOT import TRandom3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rand = TRandom3(0)

# Make TCanvas + TH2D
c1 = ROOT.TCanvas()
c1.cd()
th2d = ROOT.TH2D("th",";;",15,0,5,10,0,2)

# Fill with TRandom data
for i in xrange(1000):
    th2d.Fill(rand.Gaus(3,0.9),
              rand.Gaus(.5,0.6))

# Draw TH2D with the usual COLZ option
th2d.Draw("COLZ")
c1.Update()

# numpy read raw TArray buffer that TH2D is sitting on, +2 on box nBins...
data  = np.frombuffer(th2d.GetArray(),count=th2d.GetSize())

# split the data on Y, since frombuffer returned a contiguous set of memory
data  = np.array(np.split(data,th2d.GetNbinsY()+2))

# remove overflow/underflow
data = data[1:-1,1:-1]

# draw in pyplot
fig,ax = plt.subplots(figsize=(10,6))
matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['font.family'] = 'serif'

# matshow mimics output of TH2D.Draw("COLZ"), put the origin a the bottom like ROOT
cb = ax.matshow(data,
                extent=[0,5,0,2],
                origin='lower',
                aspect='auto')

# Move the xticks down there too!
ax.xaxis.set_ticks_position('bottom')

# Z axis scale like root
plt.colorbar(cb)

#Draw
plt.show()


