# Contoh If Tunggal
temperature = 30
if temperature > 25:
    print("Cuaca panas, nyalakan AC")

# Contoh If-Else
password = "12345"
if password == "secret":
    print("Akses diterima")
else:
    print("Akses ditolak")

# Contoh If-Elif-Else
nilai = 85
if nilai >= 90:
    print("Anda mendapat nilai A")
elif nilai >= 80:
    print("Anda mendapat nilai B")
elif nilai >= 70:
    print("Anda mendapat nilai C")
else:
    print("Perbaiki Nilai")

# Contoh If Bersarang (nested if)
number = 10
if number > 0:
    print("Angka positif")
    if number % 2 == 0:
        print("Angka genap")
    else:
        print("Angka ganjil")
else:
    print("Angka negatif")

# Contoh If Dengan Operator Logika (and, or, not)
umur = 20
tinggi = 160
if umur >= 18 and tinggi >= 155:
    print("Anda memenuhi syarat")
else:
    print("Anda tidak memenuhi syarat")

day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Ini adalah akhir pekan.")
else:
    print("Ini adalah hari kerja.")

is_logged_in = False
if not is_logged_in:
    print("Silakan masuk untuk melanjutkan.")
else:
    print("Selamat datang kembali!")

# Contoh If Dengan Input
username = input("Masukkan nama pengguna: ")
if username == "admin":
    print("Selamat datang, admin!")
else:
    print(f"Selamat datang, {username}!")
