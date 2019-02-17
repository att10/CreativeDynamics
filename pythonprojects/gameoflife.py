import matplotlib.pyplot as plt
import numpy as np

N = 100

G = np.zeros((N,N))
# G[5:8,5] = 1
# G[7,4] = 1
# G[6,3] = 1
copy = np.copy(G)


def check(x, y, G, N):
    return G[(x-1)%N,(y-1)%N] + G[(x-1)%N,y] + G[(x-1)%N,(y+1)%N] + G[x,(y-1)%N] + G[x,(y+1)%N] + G[(x+1)%N,(y-1)%N] + G[(x+1)%N,y] + G[(x+1)%N,(y+1)%N]

for i in range(N):
    for j in range(N):
        G[i,j] = np.random.randint(15)

# Display it
plt.axis("off")
p = plt.imshow(G, interpolation='nearest',vmin=-0.1,vmax=0.1)
plt.set_cmap('PuRd')
plt.pause(1)

for n in range(100000):

    for i in range(N):
        for j in range(N):
            neigh = check(i,j, G, N)
            if neigh > 65 or neigh < 3:
                copy[i,j] -= 1
            elif neigh < 66 or neigh > 2:
                copy[i,j] += 1

    G = np.copy(copy)
    p.set_data(G)
    plt.pause(.1)
