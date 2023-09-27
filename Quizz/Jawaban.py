panjang = len(var_list)
print("Panjang List Adalah: ",panjang)

maksimal = max(var_list)
print("Nilai Maksimal Nya adalah :",maksimal)

minimal = min(var_list)
print("Nilai Minum Nya Adalah : ",minimal)

banyak = var_list.count(605132)
print("Nilai Minum Nya Adalah : ",banyak)

# Bonus
for indeks, nilai in enumerate(var_list):
    if nilai == 605132:
        print(f"Nilai 605132 ditemukan pada indeks ke-{indeks}: {nilai}") 