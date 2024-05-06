def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def pembagi(a,b):
    return a / b

def pangkat(a,b):
    return a ** b 

def perkalian(a,b):
    return a * b

def bilangan(angka):
    if angka % 2 == 0:
        return 'Genap'
    else:
        return 'Ganjil'
    


def tampilan_menu():
    print(25*'=')
    print('''Pilih Operasi Matematika 
        1. penjumlahan
        2. Pengurangan
        3. Perkalian''')
    print(25*'=')

def operasi():
    angka = int(input('Masukkan pilihan anda : '))
    angka1 = int(input('Masukkan bilangan pertama : '))
    angka2 = int(input('Masukkan bilangan kedua : '))

    if angka == 1:
        print('Hasil Penjumlahan : ',penjumlahan(angka1,angka2))
    elif angka == 2:
        print('Hasil Pengurangan : ',pengurangan(angka1,angka2))
    elif angka == 3:
        print('Hasil Perkalian : ',perkalian(angka1,angka2))
    else:
        print('Tidak ada pilihan angka, Tolong masukkan pilihan angka yang tertera diatas')
        exit()