import numpy as np
import matplotlib.pyplot as plt

def amplify(x):
    n = len(x)
    A = np.matrix(np.zeros((2*n,n)))
    b = np.matrix(np.zeros((2*n,1)))
    for i in range(n):
        A[i, i] = 1. # amplify the curvature
        A[i, (i+1)%n] = -1.
        b[i, 0] = (x[i] - x[(i+1)%n])*1.9

        A[n+i, i] =    1*.3 # light data fitting term
        b[n+i, 0] = x[i]*.3
    return (np.linalg.inv(A.T*A)*A.T*b).tolist()

x = [100,100,97,93,91,87,84,83,85,87,88,89,90,90,90,88,87,86,84,82,80,
     77,75,72,69,66,62,58,54,47,42,38,34,32,28,24,22,20,17,15,13,12,9,
     7,8,9,8,6,0,0,2,0,0,2,3,2,0,0,1,4,8,11,14,19,24,27,25,23,21,19]
y = [0,25,27,28,30,34,37,41,44,47,51,54,59,64,66,70,74,78,80,83,86,90,93,
     95,96,98,99,99,100,99,99,99,98,98,96,94,93,91,90,87,85,79,75,70,65,
     62,60,58,52,49,46,44,41,37,34,30,27,20,17,15,16,17,17,19,18,14,11,6,4,1]

plt.plot(x+[x[0]], y+[y[0]], 'g--')

x = amplify(x)
y = amplify(y)

plt.plot(x+[x[0]], y+[y[0]], 'k-', linewidth=3)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('silhouette-better.png', bbox_inches='tight')
plt.show()

