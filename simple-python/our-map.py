import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import matplotlib.animation as anim
import mpl_toolkits.mplot3d
from matplotlib.colors import LightSource
from matplotlib import cm
import random as random

longitude = input("Liczba punktow w poziomie")
# longitude = 200
latitude = input("Liczba punktow w pionie")
# latitude = 200
max = input("Maksymalna wysokosc na mapie")
# max = 100
min = input("Minimalna wysokosc na mapie")
# min = -100
pointStep = input("Zmiana wysokosci")
# pointStep = 10
woda = int(input('woda'))
# woda = 500
ziemia = int(input('ziemia'))
topo = [min, max]
longitudeArr = np.linspace(230, 240, int(longitude))
longitudeSorted = np.sort(longitudeArr)
latitudeArr = np.linspace(45, 48, int(latitude))
latitudeSorted = np.sort(latitudeArr)
lista = []
index = 0

#TODO: SPRAWDZAC PUNKT NIE TYLKO PO PRAWEJ ALE ZAROWNO TEN NA DOLE.
for x in longitudeArr:
    lista.append([])
    index1 = 0
    for i in latitudeArr:
        if (len(lista[index]) > 0):
            poprzednia = lista[index][index1 - 1]
            temp = np.random.uniform(poprzednia - float(pointStep), poprzednia + float(pointStep))
            lista[index].append(temp)
        else:
            temp = np.random.uniform(float(min), float(max) - 600)
            lista[index].append(temp)
        index1 += 1
    index += 1
print(lista)
topoArr = lista
# minusNums = list(filter(lambda x: (x < 0), topoArr))
# def percentage(part, whole):
#   return 100 * float(part)/float(whole)
# landToWater = percentage(len(minusNums), len(topoArr))
# print(lista)


fig, ax = plt.subplots(constrained_layout=True)
ax = plt.axes(projection='3d')


srodek = int(0)

colors_undersea = plt.cm.terrain(np.linspace(0, 0.17, woda))
colors_land = plt.cm.terrain(np.linspace(0.25, 1, ziemia))
all_colors = np.vstack((colors_undersea, colors_land))
terrain_map = colors.LinearSegmentedColormap.from_list('terrain_map',
                                                       all_colors)
# make the norm:  Note the center is offset so that the land has more
# dynamic range:
divnorm = colors.DivergingNorm(vmin=float(min), vcenter=float(srodek), vmax=float(max))
print(longitude)
print(latitude)
print(topo)
X, Y = np.meshgrid(longitudeArr, latitudeArr)
ls = LightSource(270, 45)
rgb = ls.shade(np.array(topoArr), cmap=cm.ocean, vert_exag=0.1, blend_mode='soft')
pcm = ax.plot_surface(np.array(X), np.array(Y), np.array(topoArr), rstride=1, cstride=1, linewidth=0,  cmap=terrain_map, antialiased=False)
# cmap=terrain_map,)
ax.set_xlabel('Longitude $[^o E]$')
ax.set_ylabel('Latitude $[^o N]$')
# ax.set_aspect(1 / np.cos(np.deg2rad(49)))
fig.colorbar(pcm, shrink=0.6, extend='both', label='Elevation [m]')
plt.show()
