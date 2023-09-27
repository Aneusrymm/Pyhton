#strip()
#Metode ini bertugas untuk menghapus whitespace pada bagian awal dan akhir string.

print("         Muhamad Nabil Firdaus          ".strip())

# Jika tidak menggunakan strip() maka outputnya "    Muhamad Nabil Firdaus   "
# Jika menggunakan sstrip() maka outputnya "Muhamad Nabil Firdaus"

# Jika ingin menghilangkan karakter selain whitespace, Anda bisa mengikuti contoh berikut.

kata = 'Muhamad Nabil Firdaus'
print(kata.strip("Firdaus"))