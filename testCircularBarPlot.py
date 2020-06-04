import numpy as np
import matplotlib.pyplot as plt
import csv

#~~~~~~~~~~~Test~~~~~~~#
import pandas as pd
import seaborn as sns
# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
#~~~~~~~~~~~Test~~~~~~~#

N = 2000
bottom = 8
max_height = .5
#max_height_array = [.5, 1, 2, 4]
#max_height_random = np.random.choice(a = max_height_array, p = [.25, .25, .25, .25])

theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = max_height*np.random.rand(N)
width = (8*np.pi) / N

#Printing radii values out to CSV
file = open('radiiout.csv', 'a') 
wtr = csv.writer(file, delimiter=' ', lineterminator='\n')
for x in radii : wtr.writerow ([x])
file.close()

#Printing theta values out to CSV
#file = open('thetaout.csv', 'a') 
#wtr = csv.writer(file, delimiter=' ', lineterminator='\n')
#for x in theta : wtr.writerow ([x])
#file.close()

ax = plt.subplot(111, polar=True)
bars = ax.bar(theta, radii, width=width, bottom=bottom)



# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor('000000')
    #bar.set_facecolor(plt.cm.jet(r / 10.))
    #bar.set_alpha(0.9)

plt.title('Rehoboam', fontsize=22)
plt.axis('off')
plt.show()
