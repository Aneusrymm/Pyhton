# Metode ini mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet. 
# Jika ada satu huruf lain yang bukan alfabet, seperti angka atau spasi nilai False akan dikembalikan.

kata = 'MuhamadNabilFirdaus'
print(kata.isalpha())
# True

spasi = "Muhamad Nabil Firdaus"
print(spasi.isalpha())
# False

angka = "Nabil 123"
print(angka.isalpha())
# False