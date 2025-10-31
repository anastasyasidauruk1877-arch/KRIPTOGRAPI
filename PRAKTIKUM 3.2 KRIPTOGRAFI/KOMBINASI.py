import tkinter as tk
from tkinter import ttk, messagebox
import itertools

# ==============================
# FUNGSI LOGIKA KOMBINASI
# ==============================
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# ==============================
# FUNGSI TOMBOL KONVERSI
# ==============================
def hitung_kombinasi():
    try:
        n = int(ent_n.get())
        r = int(ent_r.get())

        if n < 0 or r < 0:
            messagebox.showwarning("Peringatan", "Masukkan angka positif!")
            return
        if r > n:
            messagebox.showerror("Error", "r tidak boleh lebih besar dari n!")
            return

        hasil = kombinasi(n, r)
        text_hasil.delete(1.0, tk.END)

        text_hasil.insert(tk.END, f"Jumlah kombinasi C({n}, {r}) = {hasil}\n\n")

        if n <= 26:
            huruf = [chr(65 + i) for i in range(n)]
            semua_kombinasi = list(itertools.combinations(huruf, r))
            text_hasil.insert(tk.END, "Daftar kombinasi huruf:\n")
            for i, komb in enumerate(semua_kombinasi, 1):
                text_hasil.insert(tk.END, f"{i}. {' '.join(komb)}\n")
        else:
            text_hasil.insert(tk.END, "Nilai n terlalu besar untuk huruf (maks 26).")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def hapus_semua():
    ent_n.delete(0, tk.END)
    ent_r.delete(0, tk.END)
    text_hasil.delete(1.0, tk.END)

def salin_hasil():
    root.clipboard_clear()
    root.clipboard_append(text_hasil.get(1.0, tk.END))
    messagebox.showinfo("Salin", "Hasil kombinasi disalin ke clipboard!")

# ==============================
# DESAIN ANTARMUKA
# ==============================
root = tk.Tk()
root.title("Program Kombinasi Huruf")
root.geometry("650x600")
root.configure(bg="#ffe6ee")  # Pink muda pastel

# Warna tema
warna_bg = "#ffe6ee"
warna_frame = "#ffffff"
warna_teks = "#333333"
warna_accent = "#f28db2"
warna_hover = "#f6aac8"
warna_input = "#fff9fb"

# ==============================
# JUDUL
# ==============================
lbl_judul = tk.Label(root, text="Program Kombinasi C(n, r)",
                     font=("Segoe UI", 18, "bold"), bg=warna_bg, fg=warna_teks)
lbl_judul.pack(pady=20)

# FRAME UTAMA
frame = tk.Frame(root, bg=warna_frame, bd=2, relief="groove", highlightbackground=warna_accent, highlightthickness=2)
frame.pack(pady=10, padx=25, fill="both", expand=True)

# INPUT SECTION
lbl_n = tk.Label(frame, text="Masukkan jumlah total objek (n):",
                 font=("Segoe UI", 11, "bold"), bg=warna_frame, fg=warna_teks)
lbl_n.pack(pady=(20, 5))
ent_n = ttk.Entry(frame, font=("Consolas", 12), justify="center")
ent_n.pack(pady=5, ipadx=40, ipady=5)

lbl_r = tk.Label(frame, text="Masukkan jumlah objek yang dipilih (r):",
                 font=("Segoe UI", 11, "bold"), bg=warna_frame, fg=warna_teks)
lbl_r.pack(pady=(15, 5))
ent_r = ttk.Entry(frame, font=("Consolas", 12), justify="center")
ent_r.pack(pady=5, ipadx=40, ipady=5)

# ==============================
# TOMBOL
# ==============================
def on_enter(e): e.widget["bg"] = warna_hover
def on_leave(e): e.widget["bg"] = warna_accent

frame_btn = tk.Frame(frame, bg=warna_frame)
frame_btn.pack(pady=20)

def buat_tombol(teks, perintah):
    btn = tk.Button(frame_btn, text=teks, command=perintah,
                    bg=warna_accent, fg="white",
                    activebackground=warna_hover, activeforeground="white",
                    font=("Segoe UI", 10, "bold"),
                    relief="flat", bd=0, padx=20, pady=8)
    btn.pack(side="left", padx=8)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

buat_tombol("Hitung Kombinasi", hitung_kombinasi)
buat_tombol("Hapus", hapus_semua)
buat_tombol("Salin", salin_hasil)

# ==============================
# HASIL
# ==============================
lbl_hasil = tk.Label(frame, text="Hasil:", font=("Segoe UI", 11, "bold"),
                     bg=warna_frame, fg=warna_teks)
lbl_hasil.pack(pady=(10, 5))

frame_scroll = tk.Frame(frame, bg=warna_frame)
frame_scroll.pack(fill="both", expand=True, padx=15, pady=5)

scrollbar = ttk.Scrollbar(frame_scroll)
scrollbar.pack(side="right", fill="y")

text_hasil = tk.Text(frame_scroll, height=10, wrap="word", yscrollcommand=scrollbar.set,
                     font=("Consolas", 11), bg=warna_input, fg=warna_teks,
                     relief="flat", bd=2, padx=10, pady=10)
text_hasil.pack(fill="both", expand=True)
scrollbar.config(command=text_hasil.yview)

# Jalankan program
root.mainloop()
