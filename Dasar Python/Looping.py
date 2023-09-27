for i in range(10):
    print(i)

#contoh yang salah
"""
for i in range(10):
print(i)
"""

for i in range(1,11,2):
    print(i)

''''
Pada program di atas, kita menampilkan bilangan ganjil yang dimulai dari 1 hingga 10.
 Perhatikan bahwa program di atas mendefinisikan nilai "1" sebagai "start", nilai "10" sebagai "stop", dan nilai "2" sebagai "step". 
 Ingat bahwa "stop" bersifat eksklusif, yang artinya nilai terakhirnya tidak akan disertakan. 
Dengan begitu, program di atas akan menampilkan kode dari 1 hingga 10 
dengan setiap bilangan ke-2 dan kelipatannya akan dilewati atau tidak dicetak.
'''

#While
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

"""
Output:
1
2
3
4
5
"""

# For Bersarang
for i in range(1, 3):
    print("*")
    for j in range(2, 3):
        print("*")

