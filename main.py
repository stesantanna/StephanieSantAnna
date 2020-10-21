import numpy as np
import matplotlib.pyplot as plt

tam = 60
repeticoes = 100


def update(arrVal, N):
    arrValUpdate = np.zeros([N, N], dtype=int)
    for x in range(tam):
        for y in range(tam):
            soma = 0
            if x == 0 and y == 0:
                somaVizinhos = arrVal[x][y + 1] + arrVal[x + 1][y] + arrVal[x + 1][y + 1]
            elif x == 0 and y < N - 1:
                soma = arrVal[x][y - 1] + arrVal[x][y + 1] + arrVal[x + 1][y - 1] + arrVal[x + 1][y] + \
                               arrVal[x + 1][y + 1]
            elif x == 0 and y == N - 1:
                soma = arrVal[x][y - 1] + arrVal[x + 1][y - 1] + arrVal[x + 1][y]

            elif x > 0 and x < N - 1 and y == 0:
                soma = arrVal[x - 1][y] + arrVal[x - 1][y + 1] + arrVal[x][y + 1] + arrVal[x + 1][y] + \
                               arrVal[x + 1][y + 1]
            elif x > 0 and x < N - 1 and y > 0 and y < N - 1:
                soma = arrVal[x - 1][y - 1] + arrVal[x - 1][y] + arrVal[x - 1][y + 1] + arrVal[x][y - 1] + \
                               arrVal[x][y + 1] + arrVal[x + 1][y - 1] + arrVal[x + 1][y] + arrVal[x + 1][y + 1]
            elif x > 0 and y < N - 1 and y == N - 1:
                soma = arrVal[x - 1][y - 1] + arrVal[x - 1][y] + arrVal[x][y - 1] + arrVal[x + 1][y - 1] + \
                               arrVal[x + 1][y]


            elif x == N - 1 and y == 0:
                soma = arrVal[x - 1][y] + arrVal[x - 1][y + 1] + arrVal[x][y + 1]
            elif x == N - 1 and y > 0 and y < N - 1:
                soma = arrVal[x - 1][y - 1] + arrVal[x - 1][y] + arrVal[x - 1][y + 1] + arrVal[x][y - 1] + \
                               arrVal[x][y + 1]
            elif x == N - 1 and y == N - 1:
                soma = arrVal[x - 1][y - 1] + arrVal[x - 1][y] + arrVal[x][y - 1]
            if arrVal[x][y] == 1 and soma < 2:
                arrValUpdate[x][y] = 0
            if arrVal[x][y] == 1 and soma > 3:
                arrValUpdate[x][y] = 0
            if arrVal[x][y] == 0 and soma == 3:
                arrValUpdate[x][y] = 1
            if arrVal[x][y] == 1 and (soma == 2 or soma == 3):
                arrValUpdate[x][y] = 1

    return (arrValUpdate)

arrVal = np.random.randint(0, 2, [tam, tam])

fig, ax = plt.subplots()
plt.axis(False)

for iter in range(repeticoes):
    arrVal = update(arrVal, tam)

    im = ax.imshow(arrVal, cmap='Greys', interpolation='none')
    plt.show()
    nameFig = 'C:\\Analytics\\Conway\\' + str(iter).zfill(3) + '.png'
    plt.savefig(nameFig)
