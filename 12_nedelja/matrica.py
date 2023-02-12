mat = [
    [1,   2,  3,  4],  # 0. red
    [5,   6,  7,  8],  # 1. red
    [9,  10, 11, 12],  # 2. red
    [13, 14, 15, 16]   # 3. red
]  # 0.  1.  2.  3. kolone

print(f'{mat = }')        # cela matrica
print(f'{mat[0] = }')     # 0-ti red
print(f'{mat[0][2] = }')  # element u redu 0, koloni 2

# ispisivanje redova matrice
for i, red in enumerate(mat):
    print(f'{i=} {red=}')
    for j, element in enumerate(red):
        print(f'  {j=} {element=}')
