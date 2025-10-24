# ============================================================
# PROGRAM KONVERSI BERBAGAI JENIS BILANGAN
# (Biner, Oktal, dan Heksadesimal)
# ============================================================

def konversi_biner(biner):
    """Konversi Biner ke Desimal dan Heksadesimal"""
    if not all(bit in '01' for bit in biner):
        return None, None
    desimal = int(biner, 2)
    heksa = hex(desimal).upper()[2:]
    return desimal, heksa


def konversi_oktal(oktal):
    """Konversi Oktal ke Desimal, Biner, dan Heksadesimal"""
    if not all(digit in '01234567' for digit in oktal):
        return None, None, None
    desimal = int(oktal, 8)
    biner = bin(desimal)[2:]
    heksa = hex(desimal).upper()[2:]
    return desimal, biner, heksa


def konversi_heksa(heksa):
    """Konversi Heksadesimal ke Desimal, Biner, dan Oktal"""
    try:
        desimal = int(heksa, 16)
    except ValueError:
        return None, None, None
    biner = bin(desimal)[2:]
    oktal = oct(desimal)[2:]
    return desimal, biner, oktal


# ============================================================
# PROGRAM UTAMA
# ============================================================
while True:
    print("\n==============================")
    print("   PROGRAM KONVERSI BILANGAN  ")
    print("==============================")
    print("1. Biner ke Desimal & Heksadesimal")
    print("2. Oktal ke Desimal, Biner & Heksadesimal")
    print("3. Heksadesimal ke Desimal, Biner & Oktal")
    print("4. Keluar")
    
    pilihan = input("\nPilih menu (1-4): ")

    if pilihan == '1':
        biner = input("Masukkan bilangan biner: ")
        desimal, heksa = konversi_biner(biner)
        if desimal is None:
            print("❌ Input tidak valid! Hanya boleh berisi angka 0 dan 1.")
        else:
            print(f"\nHasil Konversi:")
            print(f"Biner       : {biner}")
            print(f"Desimal     : {desimal}")
            print(f"Heksadesimal: {heksa}")

    elif pilihan == '2':
        oktal = input("Masukkan bilangan oktal: ")
        desimal, biner, heksa = konversi_oktal(oktal)
        if desimal is None:
            print("❌ Input tidak valid! Bilangan oktal hanya boleh berisi 0–7.")
        else:
            print(f"\nHasil Konversi:")
            print(f"Oktal        : {oktal}")
            print(f"Desimal      : {desimal}")
            print(f"Biner        : {biner}")
            print(f"Heksadesimal : {heksa}")

    elif pilihan == '3':
        heksa = input("Masukkan bilangan heksadesimal: ")
        desimal, biner, oktal = konversi_heksa(heksa)
        if desimal is None:
            print("❌ Input tidak valid! Bilangan heksadesimal hanya boleh mengandung 0-9 dan A-F.")
        else:
            print(f"\nHasil Konversi:")
            print(f"Heksadesimal : {heksa.upper()}")
            print(f"Desimal      : {desimal}")
            print(f"Biner        : {biner}")
            print(f"Oktal        : {oktal}")

    elif pilihan == '4':
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih 1-4.")
