import tkinter as tk
from tkinter import messagebox

def hitung_nilai():
    try:
        # Ambil input dari entry
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())

        # Hitung total nilai dengan bobot
        total_nilai = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

        # Tentukan huruf mutu & bobot
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

        # Keterangan
        keterangan = "Lulus" if total_nilai >= 56 else "Tidak Lulus"

        # Tampilkan hasil
        hasil = (
            f"Total Nilai Akhir : {total_nilai:.2f}\n"
            f"Nilai Huruf       : {huruf}\n"
            f"Bobot Nilai       : {bobot}\n"
            f"Keterangan        : {keterangan}"
        )
        messagebox.showinfo("Hasil Perhitungan", hasil)

    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

# === GUI ===
root = tk.Tk()
root.title("Form Hitung Nilai Akhir Akademik")

# Label dan Entry
tk.Label(root, text="Nilai Sikap/Kehadiran (10%)").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_sikap = tk.Entry(root)
entry_sikap.grid(row=0, column=1, pady=5)

tk.Label(root, text="Nilai Tugas (30%)").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_tugas = tk.Entry(root)
entry_tugas.grid(row=1, column=1, pady=5)

tk.Label(root, text="Nilai UTS (25%)").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_uts = tk.Entry(root)
entry_uts.grid(row=2, column=1, pady=5)

tk.Label(root, text="Nilai UAS (35%)").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_uas = tk.Entry(root)
entry_uas.grid(row=3, column=1, pady=5)

# Tombol
btn_hitung = tk.Button(root, text="Hitung Nilai", command=hitung_nilai, bg="lightblue")
btn_hitung.grid(row=4, column=0, columnspan=2, pady=10)

btn_exit = tk.Button(root, text="Exit", command=root.destroy, bg="salmon")
btn_exit.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
