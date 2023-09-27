def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Nabil", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Nabil"))

"""
Output:
Halo, Dicoding! Selamat pagi!
Halo, Dicoding! Selamat sore!
"""

def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3, 4, 5, 6, 7, 8))

"""
Output:
<class 'tuple'>
6
"""