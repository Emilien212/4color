import numpy as np

def fourColor(graph):
    colors = np.arange(0, 4, 1)

    degrees = np.sum(graph == 1, axis=1)-1
    coloringOrder = np.argsort(-degrees)

    nRegion = len(degrees)

    coloredKnots = np.ones_like(degrees)*(-1)
    matrixColor = np.tile(colors, (nRegion, 1))

    i = 0
    n = 0
    while i < len(degrees):
        if i <= 1 and n>=2:
            print("Insolvable")
            return np.zeros_like(degrees)

        # Removing non available color by proximity
        for knotColor in coloredKnots[graph[coloringOrder[i]].astype(bool)]:

            if knotColor in matrixColor[i] and knotColor != -1: 
                matrixColor[i, knotColor] = -1
        
        # Searching for available color
        availableColor = colors[np.where(matrixColor[i] != -1)]

        # If there is an available color
        if len(availableColor) > 0:
            coloredKnots[coloringOrder[i]] = availableColor[0]
            i += 1
        
        # If there is no available color
        else:
            matrixColor[i] = colors

            i -= 1
            matrixColor[i, coloredKnots[coloringOrder[i]]] = -1
            coloredKnots[coloringOrder[i]] = -1
    n+=1
    
    return coloredKnots