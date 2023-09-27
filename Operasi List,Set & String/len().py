# Fungsi len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string. 
# Khusus pada string, program akan menghitung jumlah karakternya.

contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))

"""
Output:
[1, 3, 3, 5, 5, 5, 7, 7, 9]
9
"""
# atau juga bisa menuliskan kode sebagai berikut

panjang_list = len(contoh_list)
print("Panjang Elemen pada contoh_list adalah :", panjang_list)


# Contoh Set
contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))

"""
Pada kode di atas, Anda mengonversi list menjadi set terlebih dahulu.
Hal ini menyebabkan anggota list berubah menjadi anggota set yang tidak memiliki duplikat.
Setelah itu, Anda mencetak jumlah anggota dari set. Hasilnya adalah anggota set berjumlah 5.
"""
"""
Output:
{1, 3, 5, 7, 9}
5
"""


# String
contoh_list = "Belajar Python"

print(contoh_list)
print(len(contoh_list))

"""
Output:
Belajar Python
14
"""

# Pada kode di atas, Anda menghitung jumlah karakter string yang ada pada variabel "contoh_list". 
# Perhatikan bahwa karakter space dihitung sebagai karakter string.