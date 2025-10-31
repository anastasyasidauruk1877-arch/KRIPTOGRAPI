# kalkulator_loop.py
def hitung(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            return "Error: pembagian dengan nol"
        return a / b
    return "Operator tidak dikenali. Gunakan hanya +, -, *, /"

def main():
    print("=== Kalkulator Sederhana ===")
    print("Operator yang tersedia: +  -  *  /")

    while True:
        try:
            a = float(input("Masukkan nilai a: "))
            b = float(input("Masukkan nilai b: "))
        except ValueError:
            print("⚠️ Input harus berupa angka. Coba lagi.")
            continue
    
        op = input("Masukkan operator (+, -, *, /): ").strip()
        hasil = hitung(a, b, op)
        print("Hasil:", hasil)

        lagi = input("Apakah Anda ingin melakukan operasi lagi? (y/t): ").strip().lower()
        if lagi == 't' or lagi == 'n':
            print("Terima kasih. Program selesai.")
            break

if __name__ == "__main__":
    main()
