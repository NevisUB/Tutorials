import ROOT
import numpy as np

c1 = ROOT.TCanvas()
tg = ROOT.TGraph()

for i in xrange(1,10):
    tg.SetPoint(i-1,i,np.log(i))

tg.Draw("ALP")
c1.Update()
c1.Modified()


# YUCK! Get me the data quickly before I become a physicist

#from buffer to the rescue!
xy_pairs = np.vstack((np.frombuffer(tg.GetX(),
                                    count=tg.GetN()),
                      np.frombuffer(tg.GetY(),
                                    count=tg.GetN()))).T

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['font.family'] = 'serif'


fig,ax = plt.subplots(figsize=(10,6))

ax.plot(xy_pairs[:,0], #x
        xy_pairs[:,1], #y
        '-o',
        lw=2)

plt.show()
