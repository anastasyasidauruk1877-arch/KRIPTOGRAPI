Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def tambah(a, b):     return a + b def kurang(a, b):     return a - b def kali(a, b):     return a * b def bagi(a, b):     if b != 0: 
...         return a / b     else: 
...         return  
... angka1 = float(input("Masukkan angka pertama: ")) angka2 = float(input("Masukkan angka kedua: ")) print(f"Hasil penjumlahan: {tambah(angka1, angka2)}") print(f"Hasil pengurangan: {kurang(angka1, angka2)}") print(f"Hasil perkalian: {kali(angka1, angka2)}") print(f"Hasil pembagian: {bagi(angka1, angka2)}") 
