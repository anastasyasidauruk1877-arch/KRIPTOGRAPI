import tkinter as tk
from tkinter import messagebox

# FUNGSI MATEMATIKA 
def mod_inverse(a, p):
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return None


#ENKRIPSI 
def encrypt():
    try:
        p = int(entry_p.get())
        g = int(entry_g.get())
        x = int(entry_x.get())
        k = int(entry_k.get())
        plaintext = entry_plain.get()

        if plaintext == "":
            messagebox.showwarning("Peringatan", "Masukkan plaintext!")
            return

        text_log.delete("1.0", tk.END)
        text_cipher.delete("1.0", tk.END)

        y = pow(g, x, p)
        a = pow(g, k, p)
        yk = pow(y, k, p)

        text_log.insert(tk.END, "=== PROSES ENKRIPSI ===\n")
        text_log.insert(tk.END, f"p = {p}, g = {g}, x = {x}, k = {k}\n")
        text_log.insert(tk.END, f"y = g^x mod p = {y}\n")
        text_log.insert(tk.END, f"a = g^k mod p = {a}\n")
        text_log.insert(tk.END, f"y^k mod p = {yk}\n\n")

        for ch in plaintext:
            m = ord(ch)
            b = (yk * m) % p
            text_log.insert(
                tk.END,
                f"Karakter '{ch}' → ASCII {m}\n"
                f"b = ({yk} × {m}) mod {p} = {b}\n\n"
            )
            text_cipher.insert(tk.END, f"({a},{b}) ")

    except ValueError:
        messagebox.showerror("Error", "Parameter harus berupa angka!")


#DEKRIPSI
def decrypt():
    try:
        p = int(entry_p.get())
        x = int(entry_x.get())
        cipher = text_cipher.get("1.0", tk.END).strip()

        if cipher == "":
            messagebox.showwarning("Peringatan", "Cipherteks kosong!")
            return

        text_log.delete("1.0", tk.END)

        pairs = cipher.replace("(", "").replace(")", "").split()
        a = int(pairs[0].split(",")[0])

        ax = pow(a, x, p)
        inv = mod_inverse(ax, p)

        text_log.insert(tk.END, "=== PROSES DEKRIPSI ===\n")
        text_log.insert(tk.END, f"a = {a}\n")
        text_log.insert(tk.END, f"a^x mod p = {ax}\n")
        text_log.insert(tk.END, f"Invers = {inv}\n\n")

        plaintext = ""

        for pair in pairs:
            _, b = pair.split(",")
            b = int(b)
            m = (b * inv) % p
            ch = chr(m)

            text_log.insert(
                tk.END,
                f"b = {b}\n"
                f"m = ({b} × {inv}) mod {p} = {m}\n"
                f"ASCII {m} → '{ch}'\n\n"
            )

            plaintext += ch

        entry_plain.delete(0, tk.END)
        entry_plain.insert(0, plaintext)

    except ValueError:
        messagebox.showerror("Error", "Format cipherteks salah!")


#  GUI
root = tk.Tk()
root.title("ElGamal")
root.geometry("850x650")
root.configure(bg="#FADADD")

# Judul
tk.Label(
    root, text="ELGAMAL CRYPTOSYSTEM",
    font=("Arial", 20, "bold"),
    bg="#FADADD", fg="#B03060"
).pack(pady=10)

# Frame Parameter
frame_param = tk.Frame(root, bg="#FADADD")
frame_param.pack()

labels = ["p", "g", "x", "k"]
entries = []

for i, lab in enumerate(labels):
    tk.Label(frame_param, text=lab, bg="#FADADD", font=("Arial", 11, "bold")).grid(row=0, column=i)
    e = tk.Entry(frame_param, width=8)
    e.grid(row=1, column=i, padx=5)
    entries.append(e)

entry_p, entry_g, entry_x, entry_k = entries

# Plaintext
tk.Label(root, text="Plaintext", bg="#FADADD", font=("Arial", 12, "bold")).pack(pady=5)
entry_plain = tk.Entry(root, width=60, font=("Arial", 12))
entry_plain.pack()

# Tombol
frame_btn = tk.Frame(root, bg="#FADADD")
frame_btn.pack(pady=10)

tk.Button(
    frame_btn, text="ENKRIPSI",
    command=encrypt,
    bg="#FFB6C1", width=15,
    font=("Arial", 11, "bold")
).grid(row=0, column=0, padx=10)

tk.Button(
    frame_btn, text="DEKRIPSI",
    command=decrypt,
    bg="#FFB6C1", width=15,
    font=("Arial", 11, "bold")
).grid(row=0, column=1, padx=10)

# Ciphertext
tk.Label(root, text="Cipherteks (a, b)", bg="#FADADD", font=("Arial", 12, "bold")).pack()
text_cipher = tk.Text(root, height=4, width=85, font=("Arial", 11))
text_cipher.pack()

# Log proses
tk.Label(root, text="Proses Enkripsi / Dekripsi", bg="#FADADD", font=("Arial", 12, "bold")).pack(pady=5)
text_log = tk.Text(root, height=12, width=95, font=("Courier New", 10))
text_log.pack()

root.mainloop()
