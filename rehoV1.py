########################
#Import dependencies
########################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpld3
import MySQLdb

#~~~~~~~~~~~Importing mySQL Data~~~~~~~#
#db = MySQLdb.connect("database-1.cluster-ro-cagxsdx2k0ey.us-east-2.rds.amazonaws.com", "admin", "rehoboam")
#cursor = db.cursor()
#sql1 = "SELECT theta FROM rehoboamSchema.rehoboamFull"
#cursor.execute(sql1)

#thetaArray = list(cursor.fetchall())
#thetaSQL = np.array(thetaArray).ravel() #converts to contiguous list

#sql2 = "SELECT radii FROM rehoboamSchema.rehoboamFull"
#cursor.execute(sql2)

#radiiArray = list(cursor.fetchall())
#radiiSQL = np.array(radiiArray).ravel() #converts to contiguous list
#~~~~~~~~~~~mySQL~~~~~~~#

N = 2000    #Numbers of bars
bottom = 8  #Where bars bottoms begin
max_height = .5 
width = (8*np.pi) / N   #width of each bar

#~~~~~~Original Calculation of theta & radii~~~~~#
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False) #array of indexes for each bar
radii = max_height*np.random.rand(N)    #array of heights/radii for each bar
#~~~~~~~~~~~~~~~~~~~~#

#Sets bars and plot
fig, ax = plt.subplots()
ax = plt.subplot(111, polar=True) #sets to circle
bars = ax.bar(theta, radii, width=width, bottom=bottom, facecolor='black') 

#~~~~~~Animation Attempt~~~~~~#
def animate(i):
    radii = max_height*np.random.rand(N)
    for rect, y in zip(bars, radii):
        rect.set_height(y)
    return bars

#frames = 100
anim = animation.FuncAnimation(fig, animate, blit=True, interval=200, repeat=True)

#~~~~~#

# Plot Display
plt.title('Rehoboam', fontsize=22)
plt.axis('off')
plt.show()






#Printing radii values out to CSV
#file = open('radiiout.csv', 'a') 
#wtr = csv.writer(file, delimiter=' ', lineterminator='\n')
#for x in radii : wtr.writerow ([x])
#file.close()

#Printing theta values out to CSV
#file = open('thetaout.csv', 'a') 
#wtr = csv.writer(file, delimiter=' ', lineterminator='\n')
#for x in theta : wtr.writerow ([x])
#file.close()