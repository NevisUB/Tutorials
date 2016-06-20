import ROOT
import larlite
import numpy as np
import matplotlib.pyplot as plt
from pylab import polyfit
import sys, os

plt.ion()
plt.rcParams.update({'font.size':16})
fig, ax = plt.subplots(figsize=(15,7))

# load file
if not(os.path.isfile('data/larlite_opdigit.root')):
    os.system('wget http://www.nevis.columbia.edu/~dcaratelli/showandtell/larlite_opdigit.root data/.')
    cmd =  'mv larlite_opdigit.root data/.'
    os.system(cmd)

# open the root file
f = ROOT.TFile('data/larlite_opdigit.root')
t = f.Get("opdigit_pmtreadout_tree")
trig = f.Get("trigger_daq_tree")


# loop through the entries in this TTree
for entry in xrange(t.GetEntries()):

    t.GetEntry(entry)
    trig.GetEntry(entry)

    trig_obj = trig.trigger_daq_branch
    print 'TRIGGER Bits : ',trig_obj.TriggerBits()

    opdigit_v = t.opdigit_pmtreadout_branch

    for opdigit in opdigit_v:

        # only use beam-gate waveforms
        if (opdigit.size() < 200):
            continue
        
        ch = opdigit.ChannelNumber()

        # skip waveforms not coming from physical PMTs
        if (ch < 100 or ch >= 132):
            continue
        
        print 'Channel number: ',ch

        # clear the axes
        ax.cla()
        fig.gca()

        adc_v = []
        for adc in opdigit:
            adc_v.append(adc)
        
        plt.plot(adc_v)
        plt.grid(True)
        plt.title('Wf for Chan %i, Entry %i'%(ch,entry))
        plt.xlabel('Tick Number [64 MHz - 15.625 ns]')
        plt.ylabel('ADC Counts')
        
        fig.canvas
        fig.canvas.draw()
        
        usrinput = raw_input("Hit Enter: next evt  || int: go to event number ||  q: exit viewer\n")            
        if ( usrinput == "q" ):                                             
            sys.exit(0)
            
sys.exit(0)
