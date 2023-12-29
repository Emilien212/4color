import matplotlib.pyplot as plt
from fourColor import fourColor
from geometrics import *
import numpy as np
import datetime
import time

t0 = time.time()




# Parameters
nFig = 16
grid = 500
adjacencyLimit = 1 # To increase when the grid/nFig is increased
width = 1024  # [px]
height = 1024 # [px]

# Window size adjustement
px = 1/plt.rcParams['figure.dpi']
plt.subplots(figsize=(width*px, height*px))

# Meshing
X = np.linspace(0, 1, grid)
Y = np.linspace(0, 1, grid)
mX, mY = np.meshgrid(X, Y)

# Add random figures
figures = []
for i in range(nFig):
    figure = np.random.choice([Circle(), Square(), Line()])
    figures.append(figure)
    plt.plot(figure.X, figure.Y, color="black")

print(f"{datetime.timedelta(seconds=time.time()-t0)} - Randoms figures generated, creating Map ...")


# Create the map
position = np.zeros(((grid, grid, nFig)))
for i, x in enumerate(X):
    for j, y in enumerate(Y):
        for k, figure in enumerate(figures):
            position[i, j, k] = figure.isIn(x, y)

position2D = position.reshape(-1, position.shape[-1]) 
unique_indices, inverse_indices = np.unique(position2D, axis=0, return_inverse=True)

nRegion = np.max(inverse_indices) + 1
mapRegion = np.transpose(inverse_indices.reshape((grid, grid)))

print(f"{datetime.timedelta(seconds=time.time()-t0)} - Map created, creating Graph... ")

# Create the graph
graph = np.zeros((nRegion, nRegion), dtype=int)
for i in range(1, grid-1):
    for j in range(1, grid-1):
        adjacent = [mapRegion[i-1][j-1], mapRegion[i-1][j], mapRegion[i-1][j+1],
                    mapRegion[i  ][j-1], mapRegion[i  ][j],  mapRegion[i  ][j+1],
                    mapRegion[i+1][j-1], mapRegion[i+1][j], mapRegion[i+1][j+1]
                    ]
        for k in adjacent:
            graph[k][mapRegion[i][j]] += 1
            graph[mapRegion[i][j]][k] += 1
graph = np.where(graph-2*adjacencyLimit > 0, 1, 0)

print(f"{datetime.timedelta(seconds=time.time()-t0)} - Graph created, applying four colors theorem... ")


# four colors theorem
coloredKnots = fourColor(graph)

print(f"{datetime.timedelta(seconds=time.time()-t0)} - Four colors theorem applied, coloring map... ")

# Coloring region and plotting figures
coloredKnots = np.take(["red", "blue", "green", "yellow"], coloredKnots)
for i in range(nRegion):
    plt.plot(mX[np.where(mapRegion==i)], mY[np.where(mapRegion==i)], ".", c=coloredKnots[i])

for figure in figures:
    plt.plot(figure.X, figure.Y, "black")

plt.xlim(0, 1)
plt.ylim(0, 1)

print(f"{datetime.timedelta(seconds=time.time()-t0)} - Map colored, displaying map ... ")



print(f"Regions # : {nRegion}")
plt.show()