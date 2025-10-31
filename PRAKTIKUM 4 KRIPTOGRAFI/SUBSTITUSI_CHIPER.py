import tkinter as tk
from tkinter import messagebox, ttk

# =============================
# Fungsi utama cipher
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
# Fungsi untuk enkripsi
# =============================
def proses_cipher():
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
        messagebox.showerror("Error", "Format aturan salah! Gunakan format A=B di setiap baris.")
        return
    
    ciphertext = substitusi_cipher(plaintext, aturan)
    hasil_var.set(ciphertext)


# =============================
# Desain GUI
# =============================
root = tk.Tk()
root.title("Substitusi Cipher - GUI")
root.geometry("520x520")
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
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TFrame", background=warna_bg)

# Header
header = tk.Frame(root, bg=warna_accent, height=70)
header.pack(fill="x", pady=(0, 20))
judul = tk.Label(
    header,
    text="Substitusi Cipher",
    font=("Segoe UI Semibold", 18, "bold"),
    bg=warna_accent,
    fg="white",
)
judul.pack(expand=True)

# Card utama (kontainer putih)
card = tk.Frame(root, bg=warna_card, bd=0, relief="flat", highlightthickness=1, highlightbackground="#cfd6f6")
card.pack(fill="both", expand=True, padx=25, pady=10, ipadx=10, ipady=10)

# Input plaintext
tk.Label(card, text="Masukkan Plaintext:", font=("Segoe UI", 11, "bold"), bg=warna_card).pack(anchor="w", pady=(10, 0), padx=10)
entry_plaintext = ttk.Entry(card, width=55)
entry_plaintext.pack(pady=8, padx=10)

# Input aturan substitusi
tk.Label(card, text="Masukkan Aturan Substitusi (format: A=B per baris):", font=("Segoe UI", 11, "bold"), bg=warna_card).pack(anchor="w", pady=(10, 0), padx=10)
text_aturan = tk.Text(card, height=7, width=55, font=("Consolas", 11), bg="#f7f9ff", bd=1, relief="solid", highlightthickness=0)
text_aturan.pack(pady=8, padx=10)

# Tombol proses dengan efek hover
def on_enter(e):
    btn_proses.config(bg="#3d6ae0")
def on_leave(e):
    btn_proses.config(bg=warna_accent)

btn_proses = tk.Button(
    card,
    text="Enkripsi",
    font=("Segoe UI", 11, "bold"),
    bg=warna_accent,
    fg="white",
    activebackground="#3d6ae0",
    activeforeground="white",
    relief="flat",
    padx=25,
    pady=8,
    cursor="hand2",
)
btn_proses.pack(pady=15)
btn_proses.bind("<Enter>", on_enter)
btn_proses.bind("<Leave>", on_leave)
btn_proses.config(command=proses_cipher)

# Hasil ciphertext
tk.Label(card, text="Hasil Ciphertext:", font=("Segoe UI", 11, "bold"), bg=warna_card).pack(anchor="w", pady=(5, 0), padx=10)
hasil_var = tk.StringVar()
hasil_entry = ttk.Entry(card, textvariable=hasil_var, width=55, state="readonly")
hasil_entry.pack(pady=8, padx=10)

root.mainloop()
