import tkinter as tk
from tkinter import ttk, messagebox
import itertools
import math

# ======================================================
# FUNGSI PERMUTASI DASAR
# ======================================================
def permutasi_menyeluruh(n):
    return math.factorial(n)

def permutasi_sebagian(n, r):
    return math.factorial(n) // math.factorial(n - r)

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil

def permutasi_keliling(n):
    if n <= 0:
        return 0
    return math.factorial(n - 1)

# ======================================================
# FUNGSI PENEMPATAN BUKU DI RAK
# ======================================================
def penempatan_buku(n, r):
    bagian_rak = [str(i + 1) for i in range(r)]
    buku = [f"Buku-{i + 1}" for i in range(n)]
    kombinasi = list(itertools.product(bagian_rak, repeat=n))
    hasil = []
    for k in kombinasi:
        posisi = ", ".join([f"{buku[j]} di Rak-{k[j]}" for j in range(n)])
        hasil.append(posisi)
    return hasil

# ======================================================
# LOGIKA TOMBOL PROSES
# ======================================================
def proses():
    mode = combo_mode.get()
    output_text.delete(1.0, tk.END)

    try:
        if mode == "Permutasi Menyeluruh":
            n = ent_n_seluruh.get().strip()
            if not n.isdigit() or int(n) <= 0:
                messagebox.showwarning("Peringatan", "Masukkan nilai n yang valid!")
                return
            hasil = permutasi_menyeluruh(int(n))
            output_text.insert(tk.END, f"Permutasi Menyeluruh dari {n} elemen = {hasil}")

        elif mode == "Permutasi Sebagian":
            n = ent_n_sebagian.get().strip()
            r = ent_r_sebagian.get().strip()
            if not n.isdigit() or not r.isdigit() or int(r) > int(n) or int(n) <= 0:
                messagebox.showwarning("Peringatan", "Pastikan n dan r valid serta n ≥ r.")
                return
            hasil = permutasi_sebagian(int(n), int(r))
            output_text.insert(tk.END, f"Permutasi Sebagian dari {n} elemen diambil {r} = {hasil}")

        elif mode == "Permutasi Keliling":
            n = ent_n_keliling.get().strip()
            if not n.isdigit() or int(n) <= 0:
                messagebox.showwarning("Peringatan", "Masukkan nilai n yang valid!")
                return
            hasil = permutasi_keliling(int(n))
            output_text.insert(tk.END, f"Permutasi Keliling dari {n} elemen = {hasil}")

        elif mode == "Permutasi Berkelompok":
            jumlah = ent_jumlah_grup.get().strip()
            if not jumlah.isdigit() or int(jumlah) <= 0:
                messagebox.showwarning("Peringatan", "Masukkan jumlah kelompok yang valid!")
                return
            
            grup = []
            total = int(jumlah)
            for i in range(total):
                nilai = ent_grup[i].get().strip()
                if not nilai:
                    messagebox.showwarning("Peringatan", f"Isi kelompok ke-{i+1} belum diisi!")
                    return
                grup.append(nilai.split())

            hasil = permutasi_berkelompok(grup)
            output_text.insert(tk.END, f"Hasil Permutasi Berkelompok:\n")
            for i, h in enumerate(hasil, 1):
                output_text.insert(tk.END, f"{i}. {h}\n")
            output_text.insert(tk.END, f"\nTotal permutasi: {len(hasil)}")

        elif mode == "Penempatan Buku di Rak":
            n = ent_n_buku.get().strip()
            r = ent_r_rak.get().strip()
            if not n.isdigit() or not r.isdigit() or int(n) <= 0 or int(r) <= 0:
                messagebox.showwarning("Peringatan", "Masukkan nilai n dan r yang valid!")
                return
            hasil = penempatan_buku(int(n), int(r))
            output_text.insert(tk.END, f"Semua Cara Penempatan Buku:\n")
            for i, h in enumerate(hasil, 1):
                output_text.insert(tk.END, f"{i}. {h}\n")
            output_text.insert(tk.END, f"\nTotal cara: {len(hasil)}")

        else:
            messagebox.showinfo("Info", "Silakan pilih mode terlebih dahulu.")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# ======================================================
# FUNGSI UNTUK MENGUBAH INPUT SESUAI MODE
# ======================================================
def ubah_mode(event=None):
    for frame in semua_frame:
        frame.pack_forget()
    mode = combo_mode.get()
    if mode == "Permutasi Menyeluruh":
        frame_menyeluruh.pack(fill="x", pady=10)
    elif mode == "Permutasi Sebagian":
        frame_sebagian.pack(fill="x", pady=10)
    elif mode == "Permutasi Berkelompok":
        frame_input_permutasi.pack(fill="x", pady=10)
    elif mode == "Permutasi Keliling":
        frame_keliling.pack(fill="x", pady=10)
    elif mode == "Penempatan Buku di Rak":
        frame_input_rak.pack(fill="x", pady=10)

def buat_input_grup():
    for widget in frame_daftar_grup.winfo_children():
        widget.destroy()
    ent_grup.clear()
    try:
        total = int(ent_jumlah_grup.get().strip())
        for i in range(total):
            lbl = tk.Label(frame_daftar_grup, text=f"Kelompok ke-{i+1}:", bg=warna_frame, fg=warna_teks, font=("Segoe UI", 10, "bold"))
            lbl.pack(pady=(3, 0))
            ent = ttk.Entry(frame_daftar_grup, font=("Consolas", 11))
            ent.pack(pady=2, ipadx=40, ipady=3)
            ent_grup.append(ent)
    except:
        messagebox.showerror("Error", "Masukkan jumlah kelompok yang valid!")

# ======================================================
# TEMA WARNA
# ======================================================
warna_bg = "#fff0f5"
warna_frame = "#ffffff"
warna_accent = "#f7a8c3"
warna_teks = "#333333"
warna_hover = "#fcbad3"

# ======================================================
# ANTARMUKA UTAMA
# ======================================================
root = tk.Tk()
root.title("Program Permutasi & Penempatan Buku")
root.geometry("850x720")
root.configure(bg=warna_bg)

# Judul
lbl_judul = tk.Label(root, text="PROGRAM PERMUTASI & PENEMPATAN BUKU",
                     font=("Segoe UI", 18, "bold"), bg=warna_bg, fg=warna_teks)
lbl_judul.pack(pady=15)

# Frame utama
frame_main = tk.Frame(root, bg=warna_frame, bd=2, relief="groove",
                      highlightbackground=warna_accent, highlightthickness=2)
frame_main.pack(padx=25, pady=10, fill="both", expand=True)

# Bagian atas: pilihan mode dan input
frame_top = tk.Frame(frame_main, bg=warna_frame)
frame_top.pack(fill="x", pady=10)

lbl_mode = tk.Label(frame_top, text="Pilih Mode:", font=("Segoe UI", 11, "bold"),
                    bg=warna_frame, fg=warna_teks)
lbl_mode.pack(anchor="w", padx=10, pady=(5, 3))
combo_mode = ttk.Combobox(frame_top, state="readonly", font=("Segoe UI", 11))
combo_mode["values"] = [
    "Permutasi Menyeluruh",
    "Permutasi Sebagian",
    "Permutasi Berkelompok",
    "Permutasi Keliling",
    "Penempatan Buku di Rak"
]
combo_mode.current(0)
combo_mode.bind("<<ComboboxSelected>>", ubah_mode)
combo_mode.pack(padx=10, pady=5, anchor="w")

# Frame input untuk setiap mode
frame_menyeluruh = tk.Frame(frame_top, bg=warna_frame)
lbl_n_seluruh = tk.Label(frame_menyeluruh, text="Masukkan n:", font=("Segoe UI", 10, "bold"), bg=warna_frame)
lbl_n_seluruh.pack(anchor="w", padx=10, pady=(5, 3))
ent_n_seluruh = ttk.Entry(frame_menyeluruh, font=("Consolas", 11))
ent_n_seluruh.pack(padx=10, pady=3, ipadx=40, ipady=3)

frame_sebagian = tk.Frame(frame_top, bg=warna_frame)
lbl_n_sebagian = tk.Label(frame_sebagian, text="Masukkan n:", font=("Segoe UI", 10, "bold"), bg=warna_frame)
lbl_n_sebagian.pack(anchor="w", padx=10, pady=(5, 3))
ent_n_sebagian = ttk.Entry(frame_sebagian, font=("Consolas", 11))
ent_n_sebagian.pack(padx=10, pady=3, ipadx=40, ipady=3)
lbl_r_sebagian = tk.Label(frame_sebagian, text="Masukkan r:", font=("Segoe UI", 10, "bold"), bg=warna_frame)
lbl_r_sebagian.pack(anchor="w", padx=10, pady=(5, 3))
ent_r_sebagian = ttk.Entry(frame_sebagian, font=("Consolas", 11))
ent_r_sebagian.pack(padx=10, pady=3, ipadx=40, ipady=3)

frame_input_permutasi = tk.Frame(frame_top, bg=warna_frame)
lbl_jumlah_grup = tk.Label(frame_input_permutasi, text="Masukkan Jumlah Kelompok:", font=("Segoe UI", 10, "bold"), bg=warna_frame)
lbl_jumlah_grup.pack(anchor="w", padx=10, pady=(5, 3))
ent_jumlah_grup = ttk.Entry(frame_input_permutasi, font=("Consolas", 11))
ent_jumlah_grup.pack(padx=10, pady=3, ipadx=40, ipady=3)
ttk.Button(frame_input_permutasi, text="Buat Input Kelompok", command=buat_input_grup).pack(pady=5)
frame_daftar_grup = tk.Frame(frame_input_permutasi, bg=warna_frame)
frame_daftar_grup.pack(pady=5)
ent_grup = []

frame_keliling = tk.Frame(frame_top, bg=warna_frame)
lbl_n_keliling = tk.Label(frame_keliling, text="Masukkan n:", font=("Segoe UI", 10, "bold"), bg=warna_frame)
lbl_n_keliling.pack(anchor="w", padx=10, pady=(5, 3))
ent_n_keliling = ttk.Entry(frame_keliling, font=("Consolas", 11))
ent_n_keliling.pack(padx=10, pady=3, ipadx=40, ipady=3)

frame_input_rak = tk.Frame(frame_top, bg=warna_frame)
lbl_n_buku = tk.Label(frame_input_rak, text="Masukkan Jumlah Buku (n):", font=("Segoe UI", 10, "bold"), bg=warna_frame)
lbl_n_buku.pack(anchor="w", padx=10, pady=(5, 3))
ent_n_buku = ttk.Entry(frame_input_rak, font=("Consolas", 11))
ent_n_buku.pack(padx=10, pady=3, ipadx=40, ipady=3)
lbl_r_rak = tk.Label(frame_input_rak, text="Masukkan Jumlah Rak (r):", font=("Segoe UI", 10, "bold"), bg=warna_frame)
lbl_r_rak.pack(anchor="w", padx=10, pady=(5, 3))
ent_r_rak = ttk.Entry(frame_input_rak, font=("Consolas", 11))
ent_r_rak.pack(padx=10, pady=3, ipadx=40, ipady=3)

semua_frame = [frame_menyeluruh, frame_sebagian, frame_input_permutasi, frame_keliling, frame_input_rak]
frame_menyeluruh.pack(fill="x", pady=10)

# Tombol Proses di tengah
def on_enter(e): e.widget["bg"] = warna_hover
def on_leave(e): e.widget["bg"] = warna_accent

btn_proses = tk.Button(frame_main, text="Proses", command=proses,
                       bg=warna_accent, fg="white", font=("Segoe UI", 11, "bold"),
                       activebackground=warna_hover, bd=0, relief="flat", padx=20, pady=6)
btn_proses.pack(pady=15)

# Output di bawah
lbl_output = tk.Label(frame_main, text="Hasil:", font=("Segoe UI", 11, "bold"), bg=warna_frame)
lbl_output.pack(pady=(0, 3))
output_text = tk.Text(frame_main, font=("Consolas", 10), height=15, wrap="word",
                      bg="#fff8fb", fg="#333333", relief="flat")
output_text.pack(padx=15, pady=5, fill="both", expand=True)

btn_proses.bind("<Enter>", on_enter)
btn_proses.bind("<Leave>", on_leave)

root.mainloop()
