#Mahmoud Tamer
import matplotlib.pyplot as plt         #import plot from matplot library 
from matplotlib import animation        #import animation from matplot library
#from gpiozero import DistanceSensor    #import Ultrasonic sensor from gpiozero library
import numpy as np                      #import numpy library      
#import Adafruit_DHT                    #import DHT11 library
import random
#Ultrasonic_sensor= DistanceSensor(echo=18, trigger=17)     #setup Ultra sonic sensor
#DHT_sensor= Adafruit_DHT.DHT11                             #setup DHT temperture sensor
#pin=20                                                     #configuration for data pin of DHT

f = open('./Sensor_log.txt','w')                            #open the file for Sensor readings recording
fig= plt.figure()                                           #intialize the figure
ax = plt.axes(xlim=(0, 30), ylim=(0, 60), xlabel='Time [s]', ylabel='Sensors Readings')     #intiliaze the Axis of the graph
#the first values on the graph for temperture will be non so nothing will be visable with some proprites for the line
line_temp, = ax.plot(np.arange(30), np.ones(30, dtype=float)*np.nan, lw=1, c='blue', marker='d', ms=2, label = 'Temperture')
#the first values on the graph for distance will be non so nothing will be visable with some proprites for the line
line_distance, = ax.plot(np.arange(30), np.ones(30, dtype=float)*np.nan, lw=1, c='red', marker='o', ms=2, label = 'Distance')
ax.legend(loc='upper left') #To add a box defining each line and the box will on the upper left
t= random.randrange(0,30)
#humidity, temp= Adafruit_DHT.read_retry(DHT_sensor, pin) #read the DHT sensor
#distance= Ultrasonic_sensor.distance*100   #read the ultrasonic sensor
def init():  #A function called init to return the intial lines
    return line_temp,line_distance

def animate(i):  #A function called animate to change the values of the lines accroding to the readings and return the lines
    #humidity, temp= Adafruit_DHT.read_retry(DHT_sensor, pin)
    temp= random.randrange(0,25)
    y_temp=temp
    old_y_temp= line_temp.get_ydata()
    new_y_temp= np.r_[old_y_temp[1:], y_temp]
    line_temp.set_ydata(new_y_temp)
    #distance= Ultrasonic_sensor.distance*100
    distance= random.randrange(25,50)
    y_distance=distance
    old_y_distance= line_distance.get_ydata()
    new_y_distance= np.r_[old_y_distance[1:], y_distance]
    line_distance.set_ydata(new_y_distance)
    f.write(f"Temperature:{temp}   Distance:{distance}\n")
    return line_temp,line_distance
anim = animation.FuncAnimation(fig, animate, init_func=init, frames = 30, interval=100, blit=False) #To start the animation of the graph for 30 frames
anim.save(f"animated_graph.gif", writer='pillow') #To save the graph as a gif
plt.show()  #To show the graph with updated readings
f.close()  #To clos the log file