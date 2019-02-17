import matplotlib.pyplot as plt
import numpy as np

N = 100

G = np.zeros((N,N))
targetX = 50
targetY = 50
copy = np.copy(G)

def check(x, y, G, N, targetX, targetY):
    if G[x,y] == 1:

        if x > targetX:
            x += 1
        elif x < targetX:
            x -= 1

        if y > targetY:
            y += 1
        elif y < targetY:
            y -= 1

    elif G[x,y] == 2:
        x += np.random.randint(-1,1)
        y += np.random.randint(-1,1)

    return [x,y]

for i in range(N):
    for j in range(N):
        if np.random.randint(5) == 0:
            G[i,j] = np.random.randint(2)

G[targetX,targetY] = 2

# Display it)
plt.axis("off")
p = plt.imshow(G)
plt.pause(1)

for i in range(10000):

    for x in range(N):
        for y in range(N):
            n = G[x,y]
            point = check(x,y,G,N,targetX, targetY)
            copy[point[0]%N, point[1]%N] = n
            if G[x,y] == 2:
                targetX = point[0]%N
                targetY = point[1]%N
                
    G = np.copy(copy)
    p.set_data(G)
    plt.pause(.01)
