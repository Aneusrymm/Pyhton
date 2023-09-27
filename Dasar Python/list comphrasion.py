angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

angka = [1, 2, 3, 4]
pangkat = [n**n for n in angka]
print(pangkat)
