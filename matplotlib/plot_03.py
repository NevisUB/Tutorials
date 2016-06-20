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
    os.system('wget http://www.nevis.columbia.edu/~dcaratelli/showandtell/larlite_opdigit.root data/')

f = ROOT.TFile('data/larlite_opdigit.root')
t = f.Get("opdigit_pmtreadout_tree")
trig = f.Get("trigger_daq_tree")


for entry in xrange(t.GetEntries()):

    #ax.cla()
    #fig.gca()
    
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

        #if (ch < 100 or ch >= 132):
        #if (ch != 109):
        #    continue
        
        print 'Channel number: ',ch

        ax.cla()
        fig.gca()

        adc_v = []
        for adc in opdigit:
            adc_v.append(adc)
        
        plt.plot(adc_v)
        plt.grid(True)
        #plt.axvspan(baseline_start,baseline_end,facecolor='k',alpha=0.5,label='Baseline Region')
        #plt.axvspan(pulse_start,pulse_end,facecolor='r',alpha=0.5,label='Pulse Region')
        plt.title('Wf for Chan %i, Entry %i'%(ch,entry))
        #plt.xlim([baseline_start-100,pulse_end+100])
        #plt.xlim([0,30])
        #plt.ylim([2000,4100])
        plt.xlabel('Tick Number [64 MHz - 15.625 ns]')
        plt.ylabel('ADC Counts')
        #plt.legend(loc=2)
        
        fig.canvas
        fig.canvas.draw()
        
        usrinput = raw_input("Hit Enter: next evt  || int: go to event number ||  q: exit viewer\n")            
        if ( usrinput == "q" ):                                             
            sys.exit(0)
            
sys.exit(0)
