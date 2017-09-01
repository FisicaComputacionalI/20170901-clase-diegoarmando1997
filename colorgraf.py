# lineplot.py
import numpy as np
import pylab as pl
# Make an array of x values
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pl.xlabel('tiempo')
# Make an array of y values for each x value
y = [0,0,0,0,1,1,0,1,0,1,1,2,1,1,0,2,3,0,4,6]
pl.ylabel('Mascotas')
# use pylab to plot x and y
pl.plot(x,y, 'mo')
# show the ploton the screen
pl.savefig('tempmod.png')
