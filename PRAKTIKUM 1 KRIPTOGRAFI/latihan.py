import tkinter as tk
from tkinter import messagebox

# ==========================
# Fungsi Aritmatika Dasar
# ==========================
def aritmatika_form():
    win = tk.Toplevel()
    win.title("Fungsi Aritmatika Dasar")

    tk.Label(win, text="Angka 1:").grid(row=0, column=0, padx=10, pady=5)
    angka1_entry = tk.Entry(win)
    angka1_entry.grid(row=0, column=1, pady=5)

    tk.Label(win, text="Angka 2:").grid(row=1, column=0, padx=10, pady=5)
    angka2_entry = tk.Entry(win)
    angka2_entry.grid(row=1, column=1, pady=5)

    def hitung(op):
        try:
            a = float(angka1_entry.get())
            b = float(angka2_entry.get())
            if op == '+':
                hasil = a + b
            elif op == '-':
                hasil = a - b
            elif op == '*':
                hasil = a * b
            elif op == '/':
                hasil = a / b if b != 0 else "Error: Bagi 0"
            messagebox.showinfo("Hasil", f"Hasil: {hasil}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka valid!")

    # fungsi khusus untuk masing-masing tombol (tanpa lambda)
    def tambah(): hitung('+')
    def kurang(): hitung('-')
    def kali():   hitung('*')
    def bagi():   hitung('/')

    tk.Button(win, text="+", width=5, command=tambah).grid(row=2, column=0, pady=5)
    tk.Button(win, text="-", width=5, command=kurang).grid(row=2, column=1, pady=5)
    tk.Button(win, text="*", width=5, command=kali).grid(row=3, column=0, pady=5)
    tk.Button(win, text="/", width=5, command=bagi).grid(row=3, column=1, pady=5)


# ==========================
# Kalkulator Sederhana
# ==========================
def kalkulator_form():
    win = tk.Toplevel()
    win.title("Kalkulator Sederhana")

    tk.Label(win, text="Angka 1:").grid(row=0, column=0, padx=10, pady=5)
    angka1_entry = tk.Entry(win)
    angka1_entry.grid(row=0, column=1, pady=5)

    tk.Label(win, text="Operator (+ - * /):").grid(row=1, column=0, padx=10, pady=5)
    operator_entry = tk.Entry(win)
    operator_entry.grid(row=1, column=1, pady=5)

    tk.Label(win, text="Angka 2:").grid(row=2, column=0, padx=10, pady=5)
    angka2_entry = tk.Entry(win)
    angka2_entry.grid(row=2, column=1, pady=5)

    def hitung():
        try:
            a = float(angka1_entry.get())
            b = float(angka2_entry.get())
            op = operator_entry.get()
            if op == '+':
                hasil = a + b
            elif op == '-':
                hasil = a - b
            elif op == '*':
                hasil = a * b
            elif op == '/':
                hasil = a / b if b != 0 else "Error: Bagi 0"
            else:
                hasil = "Operator tidak valid"
            messagebox.showinfo("Hasil", f"Hasil: {hasil}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka valid!")

    tk.Button(win, text="Hitung", command=hitung, bg="lightgreen").grid(row=3, column=0, columnspan=2, pady=10)


# ==========================
# Hitung Nilai Akademik
# ==========================
def nilai_form():
    win = tk.Toplevel()
    win.title("Hitung Nilai Akhir Akademik")

    tk.Label(win, text="Nilai Sikap (10%)").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_sikap = tk.Entry(win)
    entry_sikap.grid(row=0, column=1, pady=5)

    tk.Label(win, text="Nilai Tugas (30%)").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entry_tugas = tk.Entry(win)
    entry_tugas.grid(row=1, column=1, pady=5)

    tk.Label(win, text="Nilai UTS (25%)").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entry_uts = tk.Entry(win)
    entry_uts.grid(row=2, column=1, pady=5)

    tk.Label(win, text="Nilai UAS (35%)").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entry_uas = tk.Entry(win)
    entry_uas.grid(row=3, column=1, pady=5)

    def hitung_nilai():
        try:
            sikap = float(entry_sikap.get())
            tugas = float(entry_tugas.get())
            uts = float(entry_uts.get())
            uas = float(entry_uas.get())
            total_nilai = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

            if 81 <= total_nilai <= 100:
                huruf, bobot = "A", 4
            elif 76 <= total_nilai <= 80:
                huruf, bobot = "B+", 3.5
            elif 71 <= total_nilai <= 75:
                huruf, bobot = "B", 3
            elif 66 <= total_nilai <= 70:
                huruf, bobot = "C+", 2.5
            elif 56 <= total_nilai <= 65:
                huruf, bobot = "C", 2
            elif 46 <= total_nilai <= 55:
                huruf, bobot = "D", 1
            else:
                huruf, bobot = "E", 0

            ket = "Lulus" if total_nilai >= 56 else "Tidak Lulus"

            hasil = (
                f"Total Nilai Akhir : {total_nilai:.2f}\n"
                f"Nilai Huruf       : {huruf}\n"
                f"Bobot Nilai       : {bobot}\n"
                f"Keterangan        : {ket}"
            )
            messagebox.showinfo("Hasil Perhitungan", hasil)
        except ValueError:
            messagebox.showerror("Error", "Input harus berupa angka!")

    tk.Button(win, text="Hitung Nilai", command=hitung_nilai, bg="lightblue").grid(row=4, column=0, columnspan=2, pady=10)


# ==========================
# Menu Utama GUI
# ==========================
root = tk.Tk()
root.title("Program Multi-Menu")

tk.Label(root, text="=== MENU UTAMA ===", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="1. Fungsi Aritmatika Dasar", width=30, command=aritmatika_form).pack(pady=5)
tk.Button(root, text="2. Kalkulator Sederhana", width=30, command=kalkulator_form).pack(pady=5)
tk.Button(root, text="3. Hitung Nilai Akademik", width=30, command=nilai_form).pack(pady=5)
tk.Button(root, text="Keluar", width=30, command=root.destroy, bg="salmon").pack(pady=10)

root.mainloop()
