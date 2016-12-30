import matplotlib.pyplot as plt
import numpy as np

x_v = [0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5]
y_v = [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5]
c_v = [0,0,0,0,0,0,1,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

NROWS = 6
NCOLS = 6

print 'ROWS : ',NROWS
print 'COLS : ',NCOLS
print 'Entries : ',len(c_v)

c_v = np.array(c_v)

grid = c_v.reshape( (NROWS,NCOLS) )

# how to mask a value
grid = np.ma.masked_where(grid==5, grid)

fig = plt.figure(figsize=(15,6))

plt.imshow(grid, extent=(x_v[0], x_v[-1], y_v[-1], y_v[0]),
           interpolation='nearest')#, cmap=cm.gist_rainbow)

plt.colorbar(label='Value')
plt.xlabel('X [cm]')
plt.ylabel('Y [cm]')
plt.show()

