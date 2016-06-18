# This script does nothing.
# It checks and sees if you are able to
# import matplotlib and numpy, which are
# required for plotting.

try:
    import matplotlib.pyplot as plt
except:
    print 'Cannot import MATPLOTLIB.'
try:
    import numpy
except:
    print 'Cannot import NUMPY'
