import pickle
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn as sns
import numpy as np

file = open('Elevation.pkl','rb')
data = pickle.load(file)
Z = np.array(data).reshape((35,65))
x = np.arange(17,52,1)
y = np.arange(71,136,1)
X,Y = np.meshgrid(y,x)

fig = plt.figure(figsize=(16,9))
ax = Axes3D(fig)

ls = LightSource(270,45)
#rgb = ls.shade(Z,cmap=cm.gist_earth, vert_exag = 0.1,blend_mode='soft')
ax.plot_surface(X,Y,Z,linewidth=0,
                cmap=cm.gist_earth,shade=False,vmin=-8000,vmax=8000,
                rstride = 1,cstride = 1)
ax.contourf(X,Y,Z,zdir='z',cmap='rainbow',
            stride=1,offset = -15000)     #projection
ax.contourf(X,Y,Z,zdir='y',cmap=cm.gist_earth,
            stride =1,offset = 100)
#ax.contour(X,Y,Z,zdir='z',colors = 'Black',mask=False,linewidth=10)
ax.set_ylim3d((15,55))
ax.set_xlim3d((70,138))
ax.set_zlim((-7000,8000))
plt.show()
