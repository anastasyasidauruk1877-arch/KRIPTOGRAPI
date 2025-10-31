# kalkulator_ops_module.py
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '**': operator.pow,
}

def main():
    print("Kalkulator (operator module).")
    while True:
        try:
            a = float(input("Masukkan nilai a: "))
            b = float(input("Masukkan nilai b: "))
        except ValueError:
            print("Input harus angka.")
            continue

        op = input("Masukkan operator (+, -, *, /, %, **): ").strip()
        func = ops.get(op)
        if func is None:
            print("Operator tidak valid.")
        else:
            try:
                hasil = func(a, b)
                print(f"Hasil {a} {op} {b} = {hasil}")
            except ZeroDivisionError:
                print("Error: pembagian dengan nol.")

        lagi = input("Mulai operasi perhitungan lagi? (y/n): ").strip().lower()
        if lagi != 'y':
            print("Program selesai. Terima kasih!")
            break

if __name__ == "__main__":
    main()
