# Metode isalnum() mengembalikan nilai True jika karakter dalam string adalah alfanumerik, 
# yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.
# Jika ada Spasi Maka dianggaap False

kata = 'Nabil123'
print(kata.isalnum())
# True


kata = 'Nabil 123'
print(kata.isalnum())
# False

kata = '123'
print(kata.isalnum())
# True


kata = '1 2 3'
print(kata.isalnum())
# False