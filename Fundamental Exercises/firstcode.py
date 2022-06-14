# berikut ini adalah contoh penggunaan function print dari Python
print('Hello teman-teman semua, selamat datang di Purwadhika!')
# print('Hello teman-teman semua, selamat datang di Purwadhika!')
print('Hello!')

x = 5
print('nilai x pertama = ', x)

# penjumlahan
x += 2
# x = x + 2
print('x setelah penjumlahan = ', x)

# pengurangan
x -= 2
# x = x - 2
print('x setelah pengurangan = ', x)

# perkalian
x *= 2
# x = x * 2
print('x setelah perkalian = ', x)

# pembagian
x /=  2
# x = x / 2
print('x setelah pembagian = ', x)

# modulus
x %= 2 
# x = x % 2
print('x setelah modulus = ', x)

# pembagian kebawah
x = 19
x //= 5
# x = x // 5
print('x setelah pembagian kebawah = ', x)

# pemangkatan
x **= 2
# x = x ** 2
print('x setelah pemangkatan = ', x)

import math

# ceil method
print('ceil method')
x = 4.2
x = math.ceil(x)
print(x)
print(math.ceil(7.1))

# floor method
print('floor method')
x = 4.8
x = math.floor(x)
print(x)
print(math.floor(7.9))

# fabs method
print('fabs method')
x = -4.5
x = math.fabs(x)
print(x)
print(math.fabs(5.2))
print(math.fabs(7))
print(math.fabs(-7))

# pow method
print('pow method')
x = 4
y = 3
hasil = math.pow(x,y)
print(hasil)
print(math.pow(2,3))
print(2 ** 3)

# sqrt method
print('sqrt method')
x = 25
x = math.sqrt(x)
print(x)
print(math.sqrt(9))

# pi constant
print('pi constant')
radius = 3
luas = math.pi * math.pow(radius,2)
print(math.pi)
print(luas)

# membuat variable a dan isinya integer 20
a = 20
print("data dan tipe data variable a pertama kali")
print(a, type(a))

# ubah tipe data variable a jadi string
a = str(a)
print("data dan tipe data variable a menjadi string")
print(a, type(a))

# ubah tipe data variable a jadi float
a = float(a)
print("data dan tipe data variable a menjadi float")
print(a, type(a))

# tipe data a tidak berubah 
int(a)
print("data dan tipe data variable a tetap float")
print(a, type(a))

# ubah tipe data variable a jadi int kembali
a = int(a)
print("data dan tipe data variable a menjadi int")
print(a, type(a))

# data pada variable a tetap int 
# tetapi yang muncul menggunakan format float
print("data dan tipe data variable a tetap int, tapi yg muncul float")
print(float(a), type(float(a)))
print("pembuktian")
print(a, type(a))

kutipSatu = 'Kutip Satu ("Im Batman")'
kutipDua = "Kutip Dua (I'm Iron Man)"
kutipTiga = '''
    "Im Batman"
    I'm Iron Man

    
'''

print(kutipSatu, type(kutipSatu))
print(kutipDua, type(kutipDua))
print(kutipTiga, type(kutipTiga))

esc1 = "Salam kenal murid \"Purwadhika\", mari kita belajar bersama."
print(esc1)

esc2 = 'Hello I\'m Baron'
print(esc2)

esc3 = 'This is backslash => \\'
print(esc3)

esc4 = 'Hello Guys,\nSelamat datang di Purwadhika!'
print(esc4)

esc5 = '\tHello Guys!'
print(esc5)

esc6 = 'Hello Guy\bs!'
print(esc6)

text = 'Halo Apa Kabar?'

panjangString = len(text)
print(panjangString)

indexApa = text.index('Apa')
print(indexApa)

indexAPertama = text.index('a')
print(indexAPertama)

hasilSplit1 = text.split(' ')
print(hasilSplit1)

hasilSplit2 = text.split('a')
print(hasilSplit2)

versiHurufKecil = text.lower()
print(versiHurufKecil)

versiHurufBesar = text.upper()
print(versiHurufBesar)

hurufPertamaCapital =  text.capitalize()
print(hurufPertamaCapital)

text = "I'm Baron, nice to meet you"

print(text[1])      # '
print(text[2:])     # m Baron, nice to meet you
print(text[:4])     # I'm
print(text[2:5])    # m B
print(text[:])      # I'm Baron, nice to meet you
print(text[-1])     # u
print(text[-3:-1])  # yo

a = "Apel"
b = "Jeruk"

c = a + b
print(c) # ApelJeruk

d = a + " " + b + " Mangga"
print(d) # Apel Jeruk Mangga

e = a + " " + str(5)
print(e) # Apel 5

umur = 23
nama = "Baron"
txt = "Nama saya {}, saya berumur {}".format(nama,umur)

print(txt)

jumlahApel = 3
jumlahJeruk = 5
pembelian = "Saya mau beli {jmlApel} Apel, {jmlMangga} Mangga, dan {jmlJeruk} Jeruk"

print(pembelian.format(jmlMangga=7, jmlJeruk=jumlahJeruk, jmlApel=jumlahApel))
print(pembelian)

txt = "Nama saya Baron"
a = "aya" in txt
b = "maya" in txt

print(a, type(a))
print(b, type(b))

c = "aya" not in txt
d = "maya" not in txt

print(c, type(c))
print(d, type(d))

# hasilnya True
hasil1 = 5 == 5
hasil2 = 7 != 5
hasil3 = 5 > 2
hasil4 = 2 < 5
hasil5 = 5 >= 5
hasil6 = 5 <= 5


print(hasil1, type(hasil1))
print(hasil2, type(hasil2))
print(hasil3, type(hasil3))
print(hasil4, type(hasil4))
print(hasil5, type(hasil5))
print(hasil6, type(hasil6))

# hasilnya False
print(4 == 5)
print(5 != 5)
print(2 > 5)
print(5 < 2)
print(5 >= 7)
print(5 <= 2)


print(True and True)
print(True and False)
print(False and True)
print(False and False)

hasil1 = 5 < 7 and 4 >= 4
hasil2 = 5 < 7 and 4 >= 5
hasil3 = 2 > 5 and 5 == 5
hasil4 = 5 != 5 and 4 == 7

print('hasil1 = ', hasil1, type(hasil1))
print('hasil2 = ', hasil2, type(hasil2))
print('hasil3 = ', hasil3, type(hasil3))
print('hasil4 = ', hasil4, type(hasil4))

print(True or True)
print(True or False)
print(False or True)
print(False or False)

hasil1 = 5 < 7 or 4 >= 4
hasil2 = 5 < 7 or 4 >= 5
hasil3 = 2 > 5 or 5 == 5
hasil4 = 5 != 5 or 4 == 7

print('hasil1 = ', hasil1, type(hasil1))
print('hasil2 = ', hasil2, type(hasil2))
print('hasil3 = ', hasil3, type(hasil3))
print('hasil4 = ', hasil4, type(hasil4))

print(not(True))
print(not(False))

hasil1 = not((5 > 2 or 4 == 5) and 5 != 5)
hasil2 = not('hello' == "hello")
hasil3 = not(4 > 3 and 'apa' == "Apa")
hasil4 = not(3 > 5 or (7 != 8 and "kari" != 'kuri'))
hasil5 = not(5 != 5 and 7 > 2)

print('hasil1 = ', hasil1, type(hasil1))
print('hasil2 = ', hasil2, type(hasil2))
print('hasil3 = ', hasil3, type(hasil3))
print('hasil4 = ', hasil4, type(hasil4))
print('hasil5 = ', hasil5, type(hasil5))

print('Selamat datang!')

umur = int(input("Masukkan Umurmu : "))

if(umur >= 17) :
    print('Anda sudah boleh bikin SIM')
    nama = input('Masukkan Namamu : ')
    if(len(nama) > 1) :
        print('Terima kasih {}'.format(nama))

print('Sampai jumpa!')

print('Selamat datang!')

umur = int(input("Masukkan Umurmu : "))

if(umur >= 17) :
    print('Anda sudah boleh bikin SIM')
    nama = input('Masukkan Namamu : ')
    if(len(nama) > 1) :
        print('Terima kasih {}'.format(nama))
    else :
        print('Nama harus diatas 1 huruf')
else :
    print('Anda belum boleh bikin SIM')

print('Sampai jumpa!')

print('Pengecheckan Ujian')

nilai = int(input("Masukkan nilai : "))
grade = ''

if(nilai >= 90 and nilai <= 100) :
    grade = 'A'
elif(nilai >= 80 and nilai <= 89) :
    grade = 'B'
elif(nilai >= 70 and nilai <= 79) :
    grade = 'C'
elif(nilai >= 60 and nilai <= 69) :
    grade = 'D'
else :
    grade = 'F'

print('Grade = {}'.format(grade))

i = 0
while (i < 5) :
    print('Angka {}'.format(i))
    i += 1

# contoh 1
print('Contoh 1 :')
data1 = range(5)
print(data1, type(data1))

listData1 = list(data1)
print(listData1, type(listData1), '\n')

# contoh 2
print('Contoh 2 :')
data2 = range(5, 9)
print(data2, type(data2))

listData2 = list(data2)
print(listData2, type(listData2), '\n')

# contoh 3
print('Contoh 3 :')
data3 = range(7, 3)
print(data3, type(data3))

listData3 = list(data3)
print(listData3, type(listData3), '\n')

# contoh 4
print('Contoh 4 :')
data4 = range(7, 3, -1)
print(data4, type(data4))

listData4 = list(data4)
print(listData4, type(listData4), '\n')

# contoh 5
print('Contoh 5 :')
data5 = range(2, 14, 3)
print(data5, type(data5))

listData5 = list(data5)
print(listData5, type(listData5), '\n')

# contoh 1

for angka in range(5) :
    print(angka)

# contoh 2

# for angka in range(10,1,-3) :
#     print('angka = {}'.format(angka))

# contoh 3

# for char in 'Hello Guys!' :
#     print('char = ', char) 

# contoh 1

jmlPutaran = 0
while(True) :
    jmlPutaran += 1
    print('Putaran {}'.format(jmlPutaran))
    
    inputan = input('Masukkan yes untuk keluar : ')
    if(inputan == 'yes') :
        break

# contoh 2

text = 'Halo apa kabar?'
hurufYgDicari = input('Masukkan huruf yang ingin dicari pada text ({}) : '.format(text))
index = 0

for c in text :
    if(c == hurufYgDicari) :
        break

    index += 1

if(index == len(text)) :
    print('Huruf {} tidak ditemukan'.format(hurufYgDicari))
else :
    print('Huruf {} pertama ditemukan pada index ke {}'.format(hurufYgDicari, index))

text = 'Halo apa kabar?'
hurufYgInginDilewati = input('Masukkan huruf yang ingin dilewati pada text ({}) : '.format(text))

for c in text :
    if(c == hurufYgInginDilewati) :
        continue
    print(c)
    
stars = ''

for i in range(5) :
    stars += '* '

print(stars)

# result => * * * * *

stars = ''

for i in range(5) :
    stars += '*\n'

print(stars)

# result => *
#           *
#           *
#           *
#           *

stars = ''
size = 5

for i in range(size) :
    for j in range(size) :
        stars += '* '
    stars += '\n'

print(stars)

# result => * * * * * 
#           * * * * *
#           * * * * *
#           * * * * *
#           * * * * *


stars = ''
size = 5

for i in range(size) :
    for j in range(1 + i) :
        stars += '* '
    stars += '\n'

print(stars)

# result => * 
#           * *
#           * * *
#           * * * *
#           * * * * *

# index =>     0/-5    1/-4   2/-3   3/-2    4/-1
listContoh = ['hello',    1,     1,     3,   True]

print(listContoh, type(listContoh))

print(listContoh[0]) # hello
print(listContoh[2]) # 1
print(listContoh[4]) # True

print(listContoh[-1]) # True
print(listContoh[-2]) # 3
print(listContoh[-5]) # hello

print(listContoh[-4:-1]) # [1, 1, 3]
print(listContoh[1:4]) # [1, 1, 3]
print(listContoh[-5:2]) # ['hello', 1]
print(listContoh[0:-2]) # ['hello', 1, 1]
print(listContoh[2:]) # [1, 3, True]

# index =>     0/-5    1/-4   2/-3   3/-2    4/-1
listContoh = ['hello',    1,     1,     3,   True]

listContoh[1] = 'test'
listContoh[-2] = 'coba'

print(listContoh) # ['hello', 'test', 1, 'coba', True]

# index =>     0/-5    1/-4   2/-3   3/-2    4/-1
listContoh = ['hello',    1,     1,     3,   True]

listContoh.append('coba')
listContoh.insert(1, 'boleh')

print(listContoh) # ['hello', 'boleh', 1, 1, 3, True, 'coba']

# index =>     0/-5      1/-4      2/-3    3/-2    4/-1
listContoh = ['hello',  'coba',   'coba',     3,   True]

listContoh.remove('coba') # remove first coba
listContoh.pop() # remove last item
del listContoh[1] # remove item at index 1

print(listContoh) # ['hello', 3]

listContoh.clear() # remove all items

print(listContoh) # []

# index =>     0/-5    1/-4   2/-3   3/-2    4/-1
listContoh = ['hello',    1,     1,     3,   True]

for item in listContoh : 
    print(item)

# hello
# 1
# 1
# 3
# True

# index =>     0/-5    1/-4   2/-3   3/-2    4/-1
listContoh = ['hello',    1,     1,     3,   True]

check = 2 in listContoh
print(check) # False

if "hello" in listContoh :
    print("Ada string hello di listContoh")
else :
    print('string hello tidak ditemukan di listContoh')

# Ada string hello di listContoh

# index =>     0/-5      1/-4      2/-3    3/-2    4/-1
listContoh = ['hello',  'coba',   'coba',     3,   True]

newList1 = listContoh
newList1[1] = 'test'

newList2 = listContoh.copy()
newList2[2] = 'baru'

print(listContoh) # ['hello', 'test', 'coba', 3, True]
print(newList1) # ['hello', 'test', 'coba', 3, True]
print(newList2) # ['hello', 'test', 'baru', 3, True]

# index =>     0/-5      1/-4      2/-3    3/-2    4/-1
listContoh = ['hello',  'coba',   'coba',     3,   True]
listBaru = [5, 'test', False]
listCoba = ['tarik', 8]

listGabungan = listBaru + listContoh
print(listGabungan) # [5, 'test', False, 'hello', 'coba', 'coba', 3, True]

listGabungan.extend(listCoba)
print(listGabungan) # [5, 'test', False, 'hello', 'coba', 'coba', 3, True, 'tarik', 8]

# index =>     0/-5      1/-4       2/-3    3/-2      4/-1
listContoh = ['eddie', 'baron',   'andi', 'charlie', 'samson']
indexYgDicari1 = listContoh.index('andi')

print(indexYgDicari1, type(indexYgDicari1)) # 2 <class 'int'>

indexYgDicari2 = listContoh.index('bernard')  # error
print(indexYgDicari2) 

# index =>     0/-5      1/-4       2/-3    3/-2      4/-1
listContoh = ['eddie', 'baron',   'andi', 'charlie', 'samson']
listContoh.sort()

print(listContoh) # ['andi', 'baron', 'charlie', 'eddie', 'samson']

listAngka = [4, 3, 1, 5, 2]
listAngka.sort(reverse=True)

print(listAngka) # [5, 4, 3, 2, 1]

# index =>     0/-5      1/-4       2/-3    3/-2      4/-1
listContoh = ['eddie', 'baron',   'andi', 'charlie', 'samson']
listContoh.reverse()

print(listContoh) # ['samson', 'charlie', 'andi', 'baron', 'eddie']

things = [
    ['red pen', 'blue pen'],
    ['analog clock', 'digital clock'],
    ['futsal shoes', 'badminton shoes']
]

print(things) # [['red pen', 'blue pen'], ['analog clock', 'digital clock'], ['futsal shoes', 'badminton shoes']]
print(things[1]) # ['analog clock', 'digital clock']
print(things[2]) # ['futsal shoes', 'badminton shoes']
print(things[1][1]) # digital clock
print(things[2][0]) # futsal shoes
print(things[0][1]) # blue pen

contoh = [
    [
        ['hello', 'apa', 'kabar'],
        [1, 2, 3]
    ],
    [
        [True, False, [1, [2, 3]]]
    ]
]

print(contoh) # [[['hello', 'apa', 'kabar'], [1, 2, 3]], [[True, False, [1, [2]]]]]
print(contoh[0][1][1]) # 2
print(contoh[1][0][2][1][1]) # 3

# index =>       0/-5   1/-4   2/-3   3/-2    4/-1
tupleContoh = ('hello',    1,     1,     3,   True)

# tupleContoh[1] = 50 # TypeError: 'tuple' object does not support item assignment
# del tupleContoh[2] # TypeError: 'tuple' object doesn't support item deletion
# tupleContoh.append('test') # AttributeError: 'tuple' object has no attribute 'append'

listContoh = list(tupleContoh)

listContoh[1] = 50
del listContoh[2]
listContoh.append('test')

tupleContoh = tuple(listContoh)
print(tupleContoh) # ('hello', 50, 3, True, 'test')

tuple1 = ('hello',)
print(tuple1) # ('hello',)
print(len(tuple1)) # 1
print(type(tuple1)) # <class 'tuple'>

# cara salah/bukan tuple
tuple2 = ('hello') 
print(tuple2) # hello
print(type(tuple2)) # <class 'str'> 

things = (
    ('red pen', 'blue pen'),
    ('analog clock', 'digital clock'),
    ['futsal shoes', 'badminton shoes']
)

print(things) # (('red pen', 'blue pen'), ('analog clock', 'digital clock'), ['futsal shoes', 'badminton shoes'])
print(things[1]) # ('analog clock', 'digital clock')
print(things[2]) # ['futsal shoes', 'badminton shoes']
print(things[1][1]) # digital clock
print(things[2][0]) # futsal shoes

things[2][0] = 'basketball shoes'

print(things) # (('red pen', 'blue pen'), ('analog clock', 'digital clock'), ['basketball shoes', 'badminton shoes'])
print(things[2]) # ['basketball shoes', 'badminton shoes']
print(things[2][0]) # basketball shoes

# things[2] = 'test' # TypeError: 'tuple' object does not support item assignment
# things[0][0] = 'green pen' # TypeError: 'tuple' object does not support item assignment

# cara 1
dictionaryContoh1 = {
    'nama' : 'Budi',
    'usia' : 25,
    'pekerjaan' : 'Developer'
}
print(dictionaryContoh1) # {'nama': 'Budi', 'usia': 25, 'pekerjaan': 'Developer'}

# cara 2
dictionaryContoh2 = dict(nama='Andi', usia=27, pekerjaan='Data Scientist')
print(dictionaryContoh2) # {'nama': 'Andi', 'usia': 27, 'pekerjaan': 'Data Scientist'}

dictionaryContoh = {
    'nama' : 'Budi',
    'usia' : 25,
    'pekerjaan' : 'Developer',
    'menikah' : False
}

print(dictionaryContoh['nama']) # Budi
print(dictionaryContoh['usia']) # 25
print(dictionaryContoh.get('pekerjaan')) # Developer
print(dictionaryContoh.get('menikah')) # False

dictionaryContoh = {
    'nama' : 'Budi',
    'usia' : 25,
    'pekerjaan' : 'Developer',
    'menikah' : False
}

dictionaryContoh['usia'] = 27
print(dictionaryContoh)

# {'nama': 'Budi', 'usia': 27, 'pekerjaan': 'Developer', 'menikah': False}

dictionaryContoh = {
    'nama' : 'Budi',
    'usia' : 25,
    'pekerjaan' : 'Developer',
    'menikah' : False
}

dictionaryContoh['kelamin'] = 'Pria'
print(dictionaryContoh)

# {'nama': 'Budi', 'usia': 25, 'pekerjaan': 'Developer', 'menikah': False, 'kelamin': 'Pria'}

dictionaryContoh = {
    'nama' : 'Budi',
    'usia' : 25,
    'pekerjaan' : 'Developer',
    'menikah' : False,
    'kelamin' : 'Pria'
}

del dictionaryContoh['kelamin'] # removes key-value pair for kelamin key
dictionaryContoh.pop('usia') # removes key-value pair for usia key
dictionaryContoh.popitem() # removes the last inserted item

print(dictionaryContoh) # {'nama': 'Budi', 'pekerjaan': 'Developer'}

dictionaryContoh.clear() # empties the dictionary

print(dictionaryContoh) # {}

dictionaryContoh = {
    'nama' : 'Budi',
    'usia' : 25,
    'pekerjaan' : 'Developer',
    'menikah' : False
}

for key in dictionaryContoh :
    print("{} = {}".format(key,dictionaryContoh[key]))

hasil = dictionaryContoh.keys()
print(hasil, type(hasil))

for key in dictionaryContoh.keys() :
    print("{} = {}".format(key,dictionaryContoh[key]))

hasil = dictionaryContoh.values()
print(hasil, type(hasil))

for val in dictionaryContoh.values() :
    print(val)

hasil = dictionaryContoh.items()
print(hasil, type(hasil))

for key,val in dictionaryContoh.items() :
    print("{} = {}".format(key,val))


dictionaryContoh = {
    'nama' : 'Budi',
    'usia' : 25,
    'pekerjaan' : 'Developer',
    'menikah' : False
}

check = 'kelamin' in dictionaryContoh
print(check)

if 'usia' in dictionaryContoh :
    print('Ada key usia pada dictionaryContoh')
else :
    print('Tidak ada key usia pada dictionaryContoh')

# Ada key usia pada dictionaryContoh

things = {
    'food1' : {
        'name' : 'Ramen',
        'price' : 25000
    },
    'food2' : {
        'name' : 'Pizza',
        'price' : 30000
    },
    'food3' : {
        'name' : 'Spaghetti',
        'price' : 20000
    }
}

print(things['food1'])
print(things['food2']['name'])

contoh = {
    'anggota' : [
        {
            'nama' : 'Andi',
            'usia' : 21,
            'hobby' : ('Main Basket', 'Nonton Film Marvel', 'Dengerin Musik K-Pop')
        },
        {
            'nama' : 'Budi',
            'usia' : 22,
            'hobby' : ('Nonton Drama Korea', 'Main Futsal', 'Makan Sushi')
        }
    ],
    'ketua' : {
        'nama' : 'Sultan',
        'usia' : 27,
        'hobby' : ('Main Kelereng', 'Nonton Anime', 'Makan Keripik Kentang')
    }
}

print(contoh['ketua']['nama']) # Sultan
print(contoh['anggota'][1]) # {'nama': 'Budi', 'usia': 22, 'hobby': ('Nonton Drama Korea', 'Main Futsal', 'Makan Sushi')}
print(contoh['anggota'][0]['hobby']) # ('Main Basket', 'Nonton Film Marvel', 'Dengerin Musik K-Pop')
print(contoh['anggota'][1]['hobby'][2]) # Makan Sushi

setContoh = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Iron Man 3', 20, False }
print(setContoh, type(setContoh)) 

# {False, 'Iron Man 3', 'Avengers: Age of Ultron', 'The Avengers', 20} <class 'set'>
# The order of the items will always be random

list1 = ['Budi', 2, 2, 'Ceci']
tuple1 = (False, 1, 'Andi', False)
dictionary1 = {
    'nama' : 'Coder',
    'usia' : 25,
    'pekerjaan' : 'Coder',
    'menikah' : False
}

setList = set(list1)
setTuple = set(tuple1)
setDictionary = set(dictionary1)
setDictionaryValues = set(dictionary1.values())

print(setList) # {'Ceci', 2, 'Budi'}
print(setTuple) # {False, 1, 'Andi'}
print(setDictionary) # {'nama', 'usia', 'pekerjaan', 'menikah'}
print(setDictionaryValues) # {False, 25, 'Coder'}

setContoh = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron' }

for item in setContoh :
    print(item)

# Iron Man 3
# The Avengers
# Avengers: Age of Ultron

# print(setContoh[1]) # TypeError: 'set' object is not subscriptable

setContoh = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron' }

setContoh.add('Iron Man')
print(setContoh)
# {'Avengers: Age of Ultron', 'The Avengers', 'Iron Man 3', 'Iron Man'}

setContoh.update({ 'Iron Man 3', 'Hulk' })
print(setContoh)
# {'Hulk', 'Iron Man 3', 'Avengers: Age of Ultron', 'The Avengers', 'Iron Man'}

setContoh = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk', 'Wonder Woman' }

setContoh.remove('The Avengers')
print(setContoh)
# {'Wonder Woman', 'Hulk', 'Iron Man 3', 'Avengers: Age of Ultron'}

setContoh.discard('Hulk')
print(setContoh)
# {'Wonder Woman', 'Iron Man 3', 'Avengers: Age of Ultron'}

setContoh.pop()
print(setContoh)
# {'Iron Man 3', 'Avengers: Age of Ultron'}

setContoh.clear()
print(setContoh)
# set()

setMovie1 = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk' }
setMovie2 = { 'Titanic', 'The Avengers' }

setGabungan = setMovie1.union(setMovie2)
print(setGabungan)
# {'Iron Man 3', 'Hulk', 'Titanic', 'The Avengers', 'Avengers: Age of Ultron'}

setMovie1 = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk' }
setMovie2 = { 'Titanic', 'The Avengers', 'Hulk' }

setMovie3 = setMovie1.difference(setMovie2)
print(setMovie3)
# {'Avengers: Age of Ultron', 'Iron Man 3'}
print(setMovie1)
# {'Avengers: Age of Ultron', 'Iron Man 3', 'Hulk', 'The Avengers'}

setMovie1.difference_update(setMovie2)
print(setMovie1)
# {'Avengers: Age of Ultron', 'Iron Man 3'}

setMovie1 = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk' }
setMovie2 = { 'Titanic', 'The Avengers', 'Hulk' }

setMovie3 = setMovie1.symmetric_difference(setMovie2)
print(setMovie3)
# {'Iron Man 3', 'Avengers: Age of Ultron', 'Titanic'}
print(setMovie1)
# {'The Avengers', 'Hulk', 'Iron Man 3', 'Avengers: Age of Ultron'}

setMovie1.symmetric_difference_update(setMovie2)
print(setMovie1)
# {'Iron Man 3', 'Avengers: Age of Ultron', 'Titanic'}

setMovie1 = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk' }
setMovie2 = { 'Titanic', 'The Avengers', 'Hulk' }

setMovie3 = setMovie1.intersection(setMovie2)
print(setMovie3)
# {'The Avengers', 'Hulk'}
print(setMovie1)
# {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}

setMovie1.intersection_update(setMovie2)
print(setMovie1)
# {'The Avengers', 'Hulk'}

setMovie1 = { 'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk' }
setMovie2 = { 'The Avengers', 'Hulk' }

checkDisjoint = setMovie1.isdisjoint(setMovie2)
checkSubset = setMovie2.issubset(setMovie1)
checkSuperset = setMovie1.issuperset(setMovie2)

print(checkDisjoint) # False
print(checkSubset) # True
print(checkSuperset) # True

def salam() :
    print('Hello selamat datang di Purwadhika!')
    print('Semoga hari anda menyenangkan!')

salam()
# Hello selamat datang di Purwadhika!
# Semoga hari anda menyenangkan!     

salam()
# Hello selamat datang di Purwadhika!
# Semoga hari anda menyenangkan!   

# test = salam()
# # Hello selamat datang di Purwadhika!
# # Semoga hari anda menyenangkan!  
   
# print(test,type(test))
# # None <class 'NoneType'>

def salamBalik(nama,usia) :
    print('Hello perkenalkan nama saya {}, dan usia saya {}'.format(nama,usia))
    print('Senang bertemu dengan anda!')

salamBalik('Andi', 25)
# Hello perkenalkan nama saya Andi, dan usia saya 25
# Senang bertemu dengan anda!

salamBalik('Budi', 27)
# Hello perkenalkan nama saya Budi, dan usia saya 27
# Senang bertemu dengan anda!

salamBalik(30, 'Dedi')
# Hello perkenalkan nama saya 30, dan usia saya Dedi
# Senang bertemu dengan anda!

# salamBalik('Ceci')
# TypeError: salamBalik() missing 1 required positional argument: 'usia'

# salamBalik()
# TypeError: salamBalik() missing 2 required positional arguments: 'nama' and 'usia'

# def salamBalik(nama = 'Unknown',usia = 0) :
#     if(nama == 'Unknown' and usia > 0) :
#         print('Saya berusia {}'.format(usia))
#     elif(nama != 'Unknown' and usia == 0) :
#         print('Hello nama saya {}'.format(nama))
#     elif(nama != 'Unknown' and usia > 0) :
#         print('Hello perkenalkan nama saya {}, dan usia saya {}'.format(nama,usia))
    
#     print('Senang bertemu dengan anda!')

# salamBalik(usia=25)
# # Saya berusia 25
# # Senang bertemu dengan anda!

# salamBalik('Budi')
# # Hello nama saya Budi
# # Senang bertemu dengan anda!

# salamBalik(usia=21,nama='Andi')
# # Hello perkenalkan nama saya Andi, dan usia saya 21
# # Senang bertemu dengan anda!

# salamBalik()
# # Senang bertemu dengan anda!

# contoh 1
def tambah(angka1,angka2) :
    return angka1 + angka2

hasil1 = tambah(5,4)
print(hasil1) # 9

print(tambah(10,2)) # 12

# contoh 2
# def coba(nama) :
#     print('Selamat Datang {} di Toko Kue Bahagia!'.format(nama))
#     print('Kuenya dijamin bikin bahagia loh!')

#     while(True) :
#         mau = input('Mau coba kue ini? : ')
#         if(mau == 'yes') :
#             print('Thank You! silahkan ini kuenya')
#             return 'Kue Coklat'
#         elif(mau == 'saya sudah bilang tidak mau') :
#             break
#         print('Anda yakin?')

#     print('Semoga anda sudah bahagia, dan sampai jumpa lagi!')

# kue = coba('Baron')
# print(kue,type(kue))

# def coba() :
#     print(x + 2)
#     return x + 3

# x = 5
# print(coba(), x)
# # 7
# # 8 5

# def coba() :
#     x = 8
#     print(x + 2)
#     return x + 3

# x = 5
# print(coba(), x)
# # 10
# # 11 5

# def coba() :
#     x += 8
#     print(x + 2)
#     return x + 3

# x = 5
# print(coba(), x)
# # UnboundLocalError: local variable 'x' referenced before assignment

# def coba() :
#     x = 2
#     x += 8
#     print(x + 2)
#     return x + 3

# x = 5
# print(coba(), x)
# # 12
# # 13 5

# def coba() :
#     global x
#     x += 8
#     print(x + 2)
#     return x + 3

# x = 5
# print(coba(), x)
# # 15
# # 16 13

def tambah(num1, num2) :
    return num1 + num2

def kurang(num1, num2) :
    return num1 - num2

def hitung(fnOperator, angka1, angka2) :
    hasil = fnOperator(angka1, angka2)
    return hasil

print(hitung(tambah, 9, 5)) # 14
print(hitung(kurang, 9, 5)) # 4

def tampilkanJawaban(jawaban) :
    print('Jawaban = {}'.format(jawaban))

def pertambahan(angka1, angka2) :
    hasil = angka1 + angka2
    tampilkanJawaban(hasil)

def pengurangan(angka1, angka2) :
    hasil = angka1 - angka2
    tampilkanJawaban(hasil)

def perkalian(angka1, angka2) :
    hasil = angka1 * angka2
    tampilkanJawaban(hasil)

def pembagian(angka1, angka2) :
    hasil = angka1 / angka2
    tampilkanJawaban(hasil)

pertambahan(10, 5) # Jawaban = 15
pengurangan(10, 5) # Jawaban = 5
perkalian(10, 5) # Jawaban = 50
pembagian(10, 5) # Jawaban = 2.0

def countdown(counter) :
    print(counter)
    counter -= 1

    if(counter >= 0) :
        countdown(counter)
        print('counter = {}'.format(counter))

countdown(3)
# 3
# 2
# 1
# 0
# counter = 0
# counter = 1
# counter = 2

kali2 = lambda angka : angka * 2
print(kali2(7)) # 14

tambah = lambda angka1, angka2 : angka1 + angka2
print(tambah(15,2)) # 17

kurang = lambda angka1, angka2, angka3 : angka1 - angka2 - angka3
print(kurang(20, 4, 6)) # 10

list1 = [1,2,3,4,5]

def kali2(angka) :
    return angka * 2

hasilMap = map(kali2, list1)
print(hasilMap, type(hasilMap)) 
# <map object at 0x0000027509756640> <class 'map'>

hasilMapList = list(hasilMap)
print(hasilMapList)
# [2, 4, 6, 8, 10]

hasilMapList1 = list(map(lambda angka : angka * 2, list1))
print(hasilMapList1) 
# [2, 4, 6, 8, 10]


def mapDuplikat(fn,collection) :
    newCollection = []
    for item in collection :
        newCollection.append(fn(item))
    
    return newCollection

list1 = [1,2,3,4,5]

def ubah(angka) :
    return 'Angka {}'.format(angka)

newList = mapDuplikat(ubah,list1)
print(newList)
# ['Angka 1', 'Angka 2', 'Angka 3', 'Angka 4', 'Angka 5']

print(mapDuplikat(lambda angka : 'Angka {}'.format(angka), list1))
# ['Angka 1', 'Angka 2', 'Angka 3', 'Angka 4', 'Angka 5']

list1 = [1,2,3,4,5]

def angkaGenap(angka) :
    return angka % 2 == 0

hasilFilter = filter(angkaGenap, list1)
print(hasilFilter, type(hasilFilter)) 
# <filter object at 0x000001199E6E6640> <class 'filter'>

hasilFilterList = list(hasilFilter)
print(hasilFilterList)
# [2, 4]

hasilFilterList1 = list(filter(lambda angka : angka % 2 == 0, list1))
print(hasilFilterList1) 
# [2, 4]


def filterDuplikat(fn, collection) :
    newCollection = []
    for item in collection :
        if(fn(item)) :
            newCollection.append(item)
    
    return newCollection

list1 = [1,2,3,4,5]

def angkaGenap(angka) :
    return angka % 2 == 0

newList = filterDuplikat(angkaGenap,list1)
print(newList)
# [2, 4]

print(filterDuplikat(lambda angka: angka % 2 == 0, list1))
# [2, 4]

class KueCoklatManusia :
    warnaMata = 'Biru'
    warnaMulut = 'Putih'
    warnaBaju = 'Putih'
    warnaKancing = 'Merah'

kue1 = KueCoklatManusia()
kue2 = KueCoklatManusia()
kue3 = KueCoklatManusia()

print(kue1, type(kue1))
print(kue2, type(kue2))
print(kue3, type(kue3))

print(kue1.warnaMata, type(kue1.warnaMata))
print(kue2.warnaMata, type(kue2.warnaMata))
print(kue3.warnaMata, type(kue3.warnaMata))

kue2.warnaMata = 'Hitam'

print(kue1.warnaMata, type(kue1.warnaMata))
print(kue2.warnaMata, type(kue2.warnaMata))
print(kue3.warnaMata, type(kue3.warnaMata))

class KueCoklatManusia :
    def __init__(myObject, eyeColor, buttonsColor) :
        print('1 kue sedang dibuat')
        myObject.warnaMata = eyeColor
        myObject.warnaMulut = 'Putih'
        myObject.warnaBaju = 'Putih'
        myObject.warnaKancing = buttonsColor

kue1 = KueCoklatManusia('Biru', 'Merah')
kue2 = KueCoklatManusia(eyeColor='Hitam', buttonsColor='Merah')
kue3 = KueCoklatManusia(buttonsColor='Coklat', eyeColor='Green')

print(kue1, type(kue1))
print(kue2, type(kue2))
print(kue3, type(kue3))

print(kue1.__dict__, type(kue1.__dict__))
print(kue2.__dict__, type(kue2.__dict__))
print(kue3.__dict__, type(kue3.__dict__))

class KueCoklatManusia :
    def __init__(self, eyeColor, buttonsColor) :
        print('1 kue sedang dibuat')
        self.warnaMata = eyeColor
        self.warnaMulut = 'Putih'
        self.warnaBaju = 'Putih'
        self.warnaKancing = buttonsColor
    
    def infoWarnaKue(self, nama='Unknown') :
        print('''
        Info Warna Kue untuk {} :

        Warna Mata = {}
        Warna Mulut = {}
        Warna Baju = {}
        Warna Kancing = {}
        '''.format(nama, self.warnaMata, self.warnaMulut, self.warnaBaju, self.warnaKancing))

kue1 = KueCoklatManusia('Biru', 'Merah')
kue2 = KueCoklatManusia(eyeColor='Hitam', buttonsColor='Merah')
kue3 = KueCoklatManusia(buttonsColor='Coklat', eyeColor='Green')

kue1.infoWarnaKue()
kue2.infoWarnaKue('Andi')
kue3.infoWarnaKue(nama='Budi')

class Manusia :
    def __init__(self, name, age, alive, job) :
        self.nama = name
        self.umur = age
        self.masihHidup = alive
        self.pekerjaan = job
    
    def bernafas(self) :
        print('{} sedang bernafas'.format(self.nama))

class Hewan :
    def __init__(self, name, age, alive, canFly) :
        self.nama = name
        self.umur = age
        self.masihHidup = alive
        self.dapatTerbang = canFly
    
    def bernafas(self) :
        print('{} sedang bernafas'.format(self.nama))

class Tumbuhan :
    def __init__(self, name, age, alive, rootType) :
        self.nama = name
        self.umur = age
        self.masihHidup = alive
        self.jenisAkar = rootType
    
    def bernafas(self) :
        print('{} sedang bernafas'.format(self.nama))

class MakhlukHidup :
    def __init__(self, name, age, alive) :
        self.nama = name
        self.umur = age
        self.masihHidup = alive
    
    def bernafas(self) :
        print('{} sedang bernafas'.format(self.nama))

class Manusia(MakhlukHidup) :
    def __init__(self, name, age, alive, job) :
        super().__init__(name, age, alive)
        self.pekerjaan = job

class Hewan(MakhlukHidup) :
    def __init__(self, name, age, alive, canFly) :
        super().__init__(name, age, alive)
        self.dapatTerbang = canFly

class Tumbuhan(MakhlukHidup) :
    def __init__(self, name, age, alive, rootType) :
        super().__init__(name, age, alive)
        self.jenisAkar = rootType
    
    def bernafas(self):
        print('{} bernafas menggunakan pori-pori stomata'.format(self.nama))

manusia1 = Manusia('Budi', 21, True, 'Teacher')
tumbuhan1 = Tumbuhan('Pohon Pisang', 1, True, 'Akar Serabut')

print(manusia1.__dict__)
print(tumbuhan1.__dict__)
manusia1.bernafas()
tumbuhan1.bernafas()

def fizzBuzz(num) :
    # i starts from 1 to num
    for i in range(1, num+1) :

        # Number divisible by 15,(divisible by both 3 & 5), 
        # print 'FizzBuzz' in place of the number 
        if (i % 15 == 0) :
            print('FizzBuzz')

        # Number divisible by 3, 
        # print 'Fizz' in place of the number
        elif (i % 3 == 0) :
            print('Fizz')

        # Number divisible by 5, 
        # print 'Buzz' in place of the number 
        elif (i % 5 == 0) :
            print('Buzz')
        
        # Print the number
        else :
            print(i)

fizzBuzz(20)

def fibonacci(num) :
    theList = []
    for i in range(num) :
        if(i < 2) :
            theList.append(1)
        else :
            theList.append(theList[i-1] + theList[i-2])
    
    return theList

print(fibonacci(0)) # []
print(fibonacci(5)) # [1, 1, 2, 3, 5]
print(fibonacci(7)) # [1, 1, 2, 3, 5, 8, 13]

import math

def reverseList(theList) :
    panjangList = len(theList)
    for i in range(math.floor(panjangList/2)) :
        theList[i], theList[panjangList-1-i] = theList[panjangList-1-i], theList[i]

    return theList

list1 = [True, False]
list2 = ['andi', 'budi', 'leli', 'dedi', 'ceci']
list3 = [1, 2, 3, 4, 5, 6]

reverseList(list1)
reverseList(list2)
reverseList(list3)

print(list1) # [False, True]
print(list2) # ['ceci', 'dedi', 'leli', 'budi', 'andi']
print(list3) # [6, 5, 4, 3, 2, 1]

print(reverseList([True, False])) # [False, True]
print(reverseList(['andi', 'budi', 'leli', 'dedi', 'ceci'])) # ['ceci', 'dedi', 'leli', 'budi', 'andi']
print(reverseList([1, 2, 3, 4, 5, 6])) # [6, 5, 4, 3, 2, 1]

# An optimized version of Bubble Sort 
def bubbleSort(theList): 
    panjangList = len(theList) 
   
    # Traverse through all array elements 
    for i in range(panjangList): 
        swapped = False
  
        # Last i elements are already in place
        for j in range(0, panjangList-i-1): 
   
            # traverse the array from 0 to panjangList-i-1.
            # Swap if the element found is greater than the next element 
            if (theList[j] > theList[j+1]) : 
                theList[j], theList[j+1] = theList[j+1], theList[j] 
                swapped = True
  
        # IF no two elements were swapped by inner loop, then break 
        if swapped == False: 
            break
  
listTest = [19, 41, 24, 50, 12] 
  
bubbleSort(listTest) 
  
print(listTest) # [12, 19, 24, 41, 50]

def getMean(theList) :
    sum = 0
    for item in theList :
        sum += item

    mean = sum / len(theList)
    return mean

list1 = [ 5, 2, 9, 5, 7 ]

print(getMean(list1))

from math import floor

def getMedian(theList) :
    theList.sort()
    median = None
    panjangList = len(theList)

    if (panjangList % 2 != 0) :
	    median = theList[floor(panjangList / 2)]
    else :
        mid1 = theList[floor(panjangList / 2) - 1]
        mid2 = theList[floor(panjangList / 2)]
        median = (mid1 + mid2) / 2

    return median

list1 = [ 5, 2, 9, 5, 7 ]
list2 = [ 8, 1, 4, 3, 6, 10 ]

print(getMedian(list1))
print(getMedian(list2))

def getMode(theList) :
    countDictionary = {}
    # create countDictionary
    for num in theList :
        if(num in countDictionary.keys()) :
            countDictionary[num] += 1
        else :
            countDictionary[num] = 1
    # create list of mode/s
    maxFrequency = 1
    modes = []
    for key in countDictionary.keys() :
        if (countDictionary[key] > maxFrequency) :
            modes = [key]
            maxFrequency = countDictionary[key]
        elif (countDictionary[key] == maxFrequency) :
            modes.append(key)
    # if every value appears same amount of times
    if (len(modes) == len(countDictionary.keys())) :
        modes = []
    return modes

list1 = [ 5, 2, 7, 5, 7 ]
list2 = [ 8, 1, 2, 1, 8, 2 ]

print(getMode(list1))
print(getMode(list2))

