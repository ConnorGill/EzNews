import numpy as np
import matplotlib.pyplot as plt

#~~~~~~~~~~~Test~~~~~~~#
import pandas as pd
import seaborn as sns
# Import Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")
#~~~~~~~~~~~Test~~~~~~~#

N = 1000
bottom = 8
max_height = 4

theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = max_height*np.random.rand(N)
width = (2*np.pi) / N

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
