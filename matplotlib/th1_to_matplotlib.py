#www.larbys.com
import ROOT

xmin=-10.0
xmax= 10.0
div =0.2

c1 = ROOT.TCanvas()
th1d = ROOT.TH1D("",";;",int((xmax-xmin)/div),xmin,xmax)
th1d.FillRandom("gaus",10000)
th1d.Draw()
c1.Update()
c1.Modified()


#Ew... how can physicists live with that... right, dirty TTree->Draw()...


import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['font.family'] = 'serif'

#give numpy the Double_t* to bin heights from TH1
bin_heights = np.frombuffer(th1d.GetArray(),        #buffer
                            dtype=np.float64,       #the type
                            count=th1d.GetNbinsX()) #how many bins


fig,ax = plt.subplots(figsize=(10,6))

his = ax.hist(np.arange(xmin,xmax,div),           
              bins=np.arange(xmin,xmax+div,div),
              weights=bin_heights)
plt.show()
