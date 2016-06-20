# new histogram lesson
# how to use histograms in matplotlib
# in this script we load data from a text file
# and make several histograms in the same image
import numpy as np
import matplotlib.pyplot as plt

# set the font-size for the entire script
plt.rcParams['font.size'] = 14

# load some files with data
dbmap = open("data/mapRun95_GoodDB.txt","r")
tvals = open("data/writeTension.txt","r")
badch = open("data/bad_Run95.txt","r")

bad_crate = []
bad_slot  = []
bad_femch = []

# go thorugh the data-files and save to arrays
for lbad in badch:
    badvals = lbad.split(" ")
    bad_crate.append(int(badvals[0]))
    bad_slot.append(int(badvals[1]))
    bad_femch.append(int(badvals[2]))

bad_tension = []
badv_tension = []
badu_tension = []
u_tension = []
v_tension = []
y_tension = []

# get tension values
for ltens in tvals:
            
    tensV = ltens.split(" ")
    tenswire = int(tensV[0])
    tensplane = int(tensV[1])
    tension = float(tensV[2])/1.0
    
    if ( tensplane == 0 ):
        u_tension.append(tension)
    if ( tensplane == 1 ):
        v_tension.append(tension)
    if ( tensplane == 2 ):
        y_tension.append(tension)
                
tvals.seek(0,0)


for lmap in dbmap:

    mapvals = lmap.split("\t")

    crate = int(mapvals[3])
    slot  = int(mapvals[4])
    femch = int(mapvals[5])
    plane = int(mapvals[2])
    wiren = int(mapvals[1])

    found = False
    for x in xrange(len(bad_crate)):
        if ( (bad_crate[x] == crate) and
             (bad_slot[x] == slot) and
             (bad_femch[x] == femch) ):
            found = True
            break

    special = 0
    if (crate==9 and slot==16 and femch==19):
        special = 1
    if (found):

        
        #print "Bad Channel: [{0}, {1}, {2}]".format(crate,slot,femch)
        
        for ltens in tvals:
            
            tensV = ltens.split(" ")
            tenswire = int(tensV[0])
            tensplane = int(tensV[1])
            tension = float(tensV[2])

            if ( (tenswire == wiren) and
                 (tensplane == plane) ):

                #print "with tension: {0}".format(tension)

                if (plane==0):
                    badu_tension.append(tension)

                if (special == 1):
                    badv_tension.append(tension)
                else:
                    bad_tension.append(tension)
                
                break

        tvals.seek(0,0)
            
tensnp_bad = np.array(bad_tension)
tensnp_badv = np.array(badv_tension)
tensnp_badu = np.array(badu_tension)
u_tens = np.array(u_tension)
v_tens = np.array(v_tension)
y_tens = np.array(y_tension)

binT = np.linspace(2,10,100)

fig = plt.figure(figsize=(15,15))


ax1 = plt.subplot(4,1,1)
plt.title("Tension Values for Run 95 Noisy Channels & for U,V,Y Plane Wires",fontsize=18)
plt.ylabel("Frequency",fontsize=18)
plt.hist(tensnp_badv,bins=binT,normed=True,alpha=0.5,color='magenta',label='Intersting V Wire')
plt.hist(tensnp_bad,bins=binT,normed=True,alpha=0.5,color='black',label='Noisy Channels - Run 95')
plt.xlim([2,10])
plt.ylim([0,3.5])
plt.grid(True)
plt.legend(loc=2,fontsize=18)
ax2 = plt.subplot(4,1,2)
plt.hist(u_tens,bins=binT,normed=True,alpha=0.5,color='blue',label='U Wires')
plt.ylabel("Frequency",fontsize=18)
plt.xlim([2,10])
plt.legend(loc=2,fontsize=18)
plt.grid(True)
ax3 = plt.subplot(4,1,3)
plt.hist(v_tens,bins=binT,normed=True,alpha=0.5,color='green',label='V Wires')
plt.ylabel("Frequency",fontsize=18)
plt.xlim([2,10])
plt.legend(loc=2,fontsize=18)
plt.grid(True)
ax4 = plt.subplot(4,1,4)
plt.hist(y_tens,bins=binT,normed=True,alpha=0.5,color='red',label='Y Wires')
plt.xlim([2,10])
plt.xlabel("Tension [N]",fontsize=18)
plt.ylabel("Frequency",fontsize=18)
plt.legend(loc=2,fontsize=18)
plt.grid(True)

plt.show()
