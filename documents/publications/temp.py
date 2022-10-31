# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file 
"""

# cours pyton
for i in range (1, 10):
    print("Hello")
    print("Word")
    
    
import test
test.puissance(2, 3)




L =  range(1000)
import numpy as rp
Lnp = rp.array(1000)
L =  range(1000)




import numpy as np
data = np.loadtxt('zoo.txt')
year, hares, lynxes, carrots = data.T


np.savetxt('zoo3.txt', data)

import matplotlib.pyplot as plt

plt.ylabel('Label')
plt.plot(data)
plt.savefig("test")




from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


m = Basemap(projection='merc',llcrnrlat=-30,urcrnrlat=50,\
            llcrnrlon=-80,urcrnrlon=80,lat_ts=20,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='green')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='blue')
plt.title("Mercator Projection")
plt.show()



m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
m.bluemarble()
plt.show()




