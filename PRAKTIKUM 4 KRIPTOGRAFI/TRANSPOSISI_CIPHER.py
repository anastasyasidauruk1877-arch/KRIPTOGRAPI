import tkinter as tk
from tkinter import ttk, messagebox


# =============================
# Fungsi Substitusi Cipher
# =============================
def substitusi_cipher(plaintext, aturan):
    ciphertext = ""
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


# =============================
# Fungsi Transposisi Cipher
# =============================
def transposisi_cipher(plaintext):
    part_length = len(plaintext) // 4
    if len(plaintext) % 4 != 0:
        part_length += 1

    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]
    ciphertext = ""

    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
    return ciphertext


# =============================
# Proses Enkripsi Lengkap
# =============================
def proses_enkripsi():
    plaintext = entry_plaintext.get().upper()
    aturan_input = text_aturan.get("1.0", tk.END).strip().upper()

    if not plaintext:
        messagebox.showwarning("Peringatan", "Masukkan plaintext terlebih dahulu!")
        return

    aturan = {}
    try:
        for baris in aturan_input.splitlines():
            if "=" in baris:
                huruf_asli, huruf_ganti = baris.split("=")
                aturan[huruf_asli.strip()] = huruf_ganti.strip()
    except:
        messagebox.showerror("Error", "Format aturan salah! Gunakan format A=B per baris.")
        return

    hasil_substitusi = substitusi_cipher(plaintext, aturan)
    hasil_transposisi = transposisi_cipher(hasil_substitusi)

    hasil_sub_var.set(hasil_substitusi)
    hasil_trans_var.set(hasil_transposisi)


# =============================
# Tampilan GUI
# =============================
root = tk.Tk()
root.title("Substitusi + Transposisi Cipher")
root.geometry("650x700")
root.configure(bg="#e8eefc")

# Warna tema
warna_bg = "#e8eefc"
warna_card = "#ffffff"
warna_accent = "#5d8bf4"
warna_teks = "#222222"

# Style ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 11), background=warna_bg, foreground=warna_teks)
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8, relief="flat", background=warna_accent, foreground="white")
style.map("TButton", background=[("active", "#3d6ae0")])
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TFrame", background=warna_bg)

# Frame utama
frame = ttk.Frame(root, padding=25, style="TFrame")
frame.pack(expand=True, fill="both")

# Header (judul)
header = tk.Frame(frame, bg=warna_accent, height=70)
header.pack(fill="x", pady=(0, 20))
judul = tk.Label(
    header,
    text="Substitusi + Transposisi Cipher",
    font=("Segoe UI Semibold", 18, "bold"),
    bg=warna_accent,
    fg="white",
)
judul.pack(expand=True)

# Card utama
card = tk.Frame(frame, bg=warna_card, bd=0, relief="flat", highlightthickness=1, highlightbackground="#cfd6f6")
card.pack(fill="both", expand=True, padx=10, pady=10, ipadx=10, ipady=10)

# Bagian input plaintext
tk.Label(card, text="Masukkan Plaintext:", font=("Segoe UI", 11, "bold"), bg=warna_card).pack(anchor="w", pady=(10, 0), padx=10)
entry_plaintext = ttk.Entry(card, width=60)
entry_plaintext.pack(pady=8, padx=10)

# Bagian aturan substitusi
tk.Label(card, text="Masukkan Aturan Substitusi (format: A=B per baris):", font=("Segoe UI", 11, "bold"), bg=warna_card).pack(anchor="w", pady=(10, 0), padx=10)
text_aturan = tk.Text(card, height=7, width=60, font=("Consolas", 11), bg="#f7f9ff", bd=1, relief="solid", highlightthickness=0)
text_aturan.pack(pady=8, padx=10)

# Tombol proses
btn_frame = tk.Frame(card, bg=warna_card)
btn_frame.pack(pady=20)
btn_proses = tk.Button(
    btn_frame,
    text="Proses Enkripsi",
    font=("Segoe UI", 11, "bold"),
    bg=warna_accent,
    fg="white",
    activebackground="#3d6ae0",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2",
    borderwidth=0
)
btn_proses.pack()
btn_proses.config(command=proses_enkripsi)

# Hasil substitusi
tk.Label(card, text="Hasil Substitusi Cipher:", font=("Segoe UI", 11, "bold"), bg=warna_card).pack(anchor="w", pady=(5, 0), padx=10)
hasil_sub_var = tk.StringVar()
hasil_sub_entry = ttk.Entry(card, textvariable=hasil_sub_var, width=60, state="readonly")
hasil_sub_entry.pack(pady=5, padx=10)

# Hasil transposisi
tk.Label(card, text="Hasil Transposisi Cipher:", font=("Segoe UI", 11, "bold"), bg=warna_card).pack(anchor="w", pady=(10, 0), padx=10)
hasil_trans_var = tk.StringVar()
hasil_trans_entry = ttk.Entry(card, textvariable=hasil_trans_var, width=60, state="readonly")
hasil_trans_entry.pack(pady=5, padx=10)




root.mainloop()
