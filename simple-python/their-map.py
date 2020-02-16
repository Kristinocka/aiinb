import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.colors as colors
import random as random

longitude = input("Liczba punktow w poziomie")
latitude = input("Liczba punktow w pionie")


max = input("Maksymalna wysokosc na mapie")
min = input("Minimalna wysokosc na mapie")
pointStep = input("Zmiana wysokosci")
topo = [min, max]

longitudeArr = np.linspace(230, 240, int(longitude))
longitudeSorted = np.sort(longitudeArr)

latitudeArr = np.linspace(45, 48, int(latitude))
latitudeSorted = np.sort(latitudeArr)

lista = []

index = 0
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

topoArr = lista

def percentage(whole):
    minus = 0
    all = 0
    for x in whole:
        count = list(filter(lambda x: (x < 0), x))
        count = len(count)
        both = len(x)
        minus += count
        all += both
    print(minus, all)
    return 100 * float(minus)/float(all)



landToWater = percentage(topoArr)

print( landToWater)


fig, ax = plt.subplots(constrained_layout=True)


colors_undersea = plt.cm.terrain(np.linspace(0, 0.17, 256))
colors_land = plt.cm.terrain(np.linspace(0.25, 1, 256))
all_colors = np.vstack((colors_undersea, colors_land))
terrain_map = colors.LinearSegmentedColormap.from_list('terrain_map',
    all_colors)


divnorm = colors.DivergingNorm(vmin=int(min), vcenter=0, vmax=int(max))

pcm = ax.pcolormesh(longitudeArr, latitudeArr, topoArr, rasterized=True, norm=divnorm,
    cmap=terrain_map,)
ax.set_xlabel('Lon $[^o E]$')
ax.set_ylabel('Lat $[^o N]$')
fig.colorbar(pcm, shrink=0.6, extend='both', label='Elevation [m]')
plt.show()