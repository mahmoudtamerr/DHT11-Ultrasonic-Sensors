import matplotlib.pyplot as plt 
from matplotlib import animation
#from gpiozero import DistanceSensor
import numpy as np
#import Adafruit_DHT
import random
import time
from datetime import datetime

f = open('./Sensor.txt','w')
fig= plt.figure()
ax = plt.axes(xlim=(0, 30), ylim=(0, 45), xlabel='Time [s]', ylabel='Output')
line1, = ax.plot(np.arange(30), np.ones(30, dtype=float)*np.nan, lw=1, c='blue', marker='d', ms=2)
line2, = ax.plot(np.arange(30), np.ones(30, dtype=float)*np.nan, lw=1, c='red', marker='o', ms=2)
t= random.randrange(0,30)
def init():
    return line1,line2

def animate(i):
    t= random.randrange(0,25)
    y=t
    old_y= line1.get_ydata()
    new_y= np.r_[old_y[1:], y]
    line1.set_ydata(new_y)
    t2= random.randrange(25,50)
    y2=t2
    old_y2= line1.get_ydata()
    new_y2= np.r_[old_y2[1:], y2]
    line2.set_ydata(new_y2)
    f.write(f"Temperature:{t}   Distance:{t2}\n")
    return line1,line2
anim = animation.FuncAnimation(fig, animate, init_func=init, frames = 30, interval=100, blit=False)
#anim.save(f"anim{int(time.time())}.gif", writer='pillow')
plt.show()
f.close()