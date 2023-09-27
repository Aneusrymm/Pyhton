for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

"""
Output:
1,1
1,2
2,1
2,2
"""

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1


"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""

for huruf in 'Muhamad Nabil':
    if huruf == '  ':
        break
    print('Huruf saat ini: {}'.format(huruf))

for huruf in 'Muhamad Nabil Firdaus':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))
