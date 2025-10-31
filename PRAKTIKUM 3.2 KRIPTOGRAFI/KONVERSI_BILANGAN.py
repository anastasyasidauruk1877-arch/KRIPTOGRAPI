import tkinter as tk
from tkinter import ttk, messagebox

# ==========================
# FUNGSI KONVERSI
# ==========================
def konversi():
    nilai = ent_input.get().strip()
    mode = combo_mode.get()

    if not nilai:
        messagebox.showwarning("Peringatan", "Masukkan nilai terlebih dahulu!")
        return

    try:
        if mode == "Biner ➜ Desimal, Heksadesimal":
            desimal = int(nilai, 2)
            heksa = hex(desimal)[2:].upper()
            hasil.set(f"""
Biner        : {nilai}
Desimal      : {desimal}
Heksadesimal : {heksa}
""")

        elif mode == "Oktal ➜ Desimal, Biner, Heksadesimal":
            desimal = int(nilai, 8)
            biner = bin(desimal)[2:]
            heksa = hex(desimal)[2:].upper()
            hasil.set(f"""
Oktal        : {nilai}
Desimal      : {desimal}
Biner        : {biner}
Heksadesimal : {heksa}
""")

        elif mode == "Heksadesimal ➜ Desimal, Biner, Oktal":
            desimal = int(nilai, 16)
            biner = bin(desimal)[2:]
            oktal = oct(desimal)[2:]
            hasil.set(f"""
Heksadesimal : {nilai.upper()}
Desimal      : {desimal}
Biner        : {biner}
Oktal        : {oktal}
""")

        else:
            hasil.set("Pilih mode konversi yang sesuai.")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid untuk mode yang dipilih!")


# ==========================
# FUNGSI TAMBAHAN
# ==========================
def hapus_semua():
    ent_input.delete(0, tk.END)
    hasil.set("")

def salin_hasil():
    root.clipboard_clear()
    root.clipboard_append(hasil.get())
    messagebox.showinfo("Disalin", "Hasil konversi berhasil disalin ke clipboard!")


# ==========================
# DESAIN JENDELA UTAMA
# ==========================
root = tk.Tk()
root.title("Konversi Bilangan - Tema Pastel Pink")
root.geometry("580x520")
root.configure(bg="#fceef5")

# ==========================
# WARNA & STYLE
# ==========================
warna_bg = "#fceef5"       # Latar belakang pink lembut
warna_card = "#ffffff"     # Putih lembut untuk area utama
warna_accent = "#f7a8c3"   # Pink pastel utama
warna_btn_hover = "#f48fb1"
warna_teks = "#3d3d3d"

# Gunakan ttk style modern
style = ttk.Style()
style.theme_use("clam")
style.configure("Rounded.TButton",
                font=("Segoe UI", 10, "bold"),
                padding=8,
                background=warna_accent,
                foreground="white",
                relief="flat")
style.map("Rounded.TButton",
          background=[("active", warna_btn_hover)],
          relief=[("pressed", "flat")])

# ==========================
# HEADER
# ==========================
header = tk.Frame(root, bg=warna_accent, height=70)
header.pack(fill="x", pady=(0, 15))
lbl_judul = tk.Label(header, text="KONVERSI BILANGAN",
                     font=("Segoe UI", 20, "bold"),
                     bg=warna_accent, fg="white")
lbl_judul.pack(expand=True)

# ==========================
# FRAME UTAMA (CARD)
# ==========================
frame = tk.Frame(root, bg=warna_card, bd=0, relief="flat",
                 highlightthickness=1, highlightbackground="#f6c6da")
frame.pack(pady=10, padx=20, fill="both", expand=True, ipadx=10, ipady=10)

# Label Mode
lbl_mode = tk.Label(frame, text="Pilih Mode Konversi:",
                    font=("Segoe UI", 11, "bold"), bg=warna_card)
lbl_mode.pack(pady=(20, 5))

combo_mode = ttk.Combobox(frame, state="readonly", font=("Segoe UI", 11))
combo_mode["values"] = [
    "Biner ➜ Desimal, Heksadesimal",
    "Oktal ➜ Desimal, Biner, Heksadesimal",
    "Heksadesimal ➜ Desimal, Biner, Oktal"
]
combo_mode.current(0)
combo_mode.pack(pady=5)

# Input
lbl_input = tk.Label(frame, text="Masukkan Nilai:",
                     font=("Segoe UI", 11, "bold"), bg=warna_card)
lbl_input.pack(pady=(20, 5))
ent_input = ttk.Entry(frame, font=("Consolas", 12), justify="center")
ent_input.pack(pady=5, ipadx=40, ipady=5)

# ==========================
# TOMBOL CUSTOM
# ==========================
def gaya_tombol(btn, warna_bg, warna_hover):
    btn.configure(bg=warna_bg, fg="white", relief="flat", bd=0, padx=20, pady=8,
                  font=("Segoe UI", 10, "bold"), cursor="hand2", activebackground=warna_hover)
    btn.bind("<Enter>", lambda e: btn.config(bg=warna_hover))
    btn.bind("<Leave>", lambda e: btn.config(bg=warna_bg))

frame_btn = tk.Frame(frame, bg=warna_card)
frame_btn.pack(pady=15)

btn_konversi = tk.Button(frame_btn, text="Konversi", command=konversi)
gaya_tombol(btn_konversi, warna_accent, warna_btn_hover)
btn_konversi.grid(row=0, column=0, padx=6)

btn_hapus = tk.Button(frame_btn, text="Hapus", command=hapus_semua)
gaya_tombol(btn_hapus, "#f7b6cc", "#f59ab6")
btn_hapus.grid(row=0, column=1, padx=6)

btn_salin = tk.Button(frame_btn, text="Salin", command=salin_hasil)
gaya_tombol(btn_salin, "#f8c3d3", "#f7a5bc")
btn_salin.grid(row=0, column=2, padx=6)

# ==========================
# HASIL KONVERSI
# ==========================
lbl_hasil_title = tk.Label(frame, text="Hasil Konversi:",
                           font=("Segoe UI", 11, "bold"), bg=warna_card)
lbl_hasil_title.pack(pady=(15, 5))
hasil = tk.StringVar()
lbl_hasil = tk.Label(frame, textvariable=hasil, font=("Consolas", 11),
                     bg=warna_card, fg="#333", justify="left", anchor="w")
lbl_hasil.pack(pady=10, padx=20, fill="x")

root.mainloop()
