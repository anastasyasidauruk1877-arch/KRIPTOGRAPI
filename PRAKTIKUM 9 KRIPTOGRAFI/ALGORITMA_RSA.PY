import tkinter as tk
from tkinter import messagebox
import random
from math import gcd

# ======================= RSA FUNCTIONS =========================

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def random_prime(min_val=50, max_val=200):
    primes = [x for x in range(min_val, max_val) if is_prime(x)]
    return random.choice(primes)

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def mod_inverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception("Inverse modular tidak ada!")
    return x % phi

# ======================= GUI PROGRAM ===========================

window = tk.Tk()
window.title("RSA Encryption")
window.geometry("850x600")
window.configure(bg="#FFD6E7")   

# GLOBAL FONTS
FONT_L = ("Segoe UI", 12)
FONT_M = ("Segoe UI", 10)

# Title Label
tk.Label(
    window,
    text="RSA ENCRYPTION",
    font=("Segoe UI", 18, "bold"),
    bg="#FFD6E7",
    fg="#C2185B"   
).pack(pady=10)


# ======================= FRAME INPUT ===========================
input_frame = tk.Frame(window, bg="#FFF0F6", bd=2, relief="groove", highlightbackground="#F48FB1", highlightthickness=2)
input_frame.pack(pady=10, padx=10, fill="x")

tk.Label(input_frame, text="Plaintext (teks bebas):", font=FONT_L, bg="#FFF0F6").grid(row=0, column=0, padx=10, pady=10)
entry_plaintext = tk.Entry(input_frame, width=50, font=FONT_L, bd=2, relief="solid", bg="#FFFFFF")
entry_plaintext.grid(row=0, column=1, padx=10, pady=10)


# RSA Variables
p = q = e = d = n = phi = None
cipher_list = []

# ======================= BUTTON STYLE ==========================

def styled_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=FONT_M,
        fg="white",
        bg="#EC407A",          
        activebackground="#D81B60",
        activeforeground="white",
        width=25,
        height=1,
        bd=0,
        relief="flat",
        highlightbackground="#F48FB1",
        highlightcolor="#F48FB1"
    )


# ======================= FUNCTIONS =============================

def latihan1():
    global p, q, e, n, phi, d
    p, q, e = 17, 11, 7
    n = p * q
    phi = (p-1) * (q-1)
    d = mod_inverse(e, phi)

    txt.delete("1.0", tk.END)
    txt.insert(tk.END, " === LATIHAN 1: RSA NILAI TETAP === \n")
    txt.insert(tk.END, f"p = {p}\nq = {q}\ne = {e}\n")
    txt.insert(tk.END, f"n = {n}\nphi(n) = {phi}\n")
    txt.insert(tk.END, f"d = {d}\n\n")
    messagebox.showinfo("Info", "algoritam RSA berhasil dibuat!")


def generate_random_rsa():
    global p, q, e, n, phi, d
    p = random_prime()
    q = random_prime()
    while q == p:
        q = random_prime()

    n = p * q
    phi = (p-1) * (q-1)

    while True:
        e = random.randint(2, phi-1)
        if gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)

    txt.delete("1.0", tk.END)
    txt.insert(tk.END, " === LATIHAN 2: RSA ACAK === \n")
    txt.insert(tk.END, f"p = {p}\nq = {q}\ne = {e}\n")
    txt.insert(tk.END, f"n = {n}\nphi = {phi}\n")
    txt.insert(tk.END, f"d = {d}\n\n")

    messagebox.showinfo("Info", "RSA acak berhasil dibuat!")


def encrypt():
    global cipher_list

    if None in (p, q, e, n):
        messagebox.showerror("Error", "Generate RSA dahulu!")
        return

    text = entry_plaintext.get()
    if text == "":
        messagebox.showerror("Error", "Plaintext kosong!")
        return

    cipher_list = []
    txt.insert(tk.END, " === ENKRIPSI STRING === \n")

    for ch in text:
        m = ord(ch)
        c = pow(m, e, n)
        cipher_list.append(c)
        txt.insert(tk.END, f"'{ch}' → ASCII {m} → Cipher {c}\n")

    txt.insert(tk.END, f"\nCiphertext List = {cipher_list}\n\n")


def decrypt():
    if cipher_list == []:
        messagebox.showerror("Error", "Belum ada ciphertext untuk didekripsi!")
        return

    txt.insert(tk.END, " === DEKRIPSI STRING === \n")

    result = ""
    for c in cipher_list:
        m = pow(c, d, n)
        ch = chr(m)
        result += ch
        txt.insert(tk.END, f"Cipher {c} → ASCII {m} → '{ch}'\n")

    txt.insert(tk.END, f"\nHasil Dekripsi = {result}\n\n")


# ======================= BUTTON FRAME ==========================

btn_frame = tk.Frame(window, bg="#FFD6E7")
btn_frame.pack(pady=5)

styled_button(btn_frame, "Latihan 1 (p=17,q=11,e=7)", latihan1).grid(row=0, column=0, padx=10, pady=5)
styled_button(btn_frame, "Generate RSA Acak", generate_random_rsa).grid(row=0, column=1, padx=10, pady=5)
styled_button(btn_frame, "Enkripsi Teks", encrypt).grid(row=1, column=0, padx=10, pady=5)
styled_button(btn_frame, "Dekripsi Teks", decrypt).grid(row=1, column=1, padx=10, pady=5)


# ======================= TEXTBOX OUTPUT ==========================

txt = tk.Text(
    window,
    width=100,
    height=20,
    font=("Consolas", 10),
    bg="#FFF0F6",                 # pink soft
    bd=2,
    relief="solid",
    highlightbackground="#F06292",
    highlightthickness=2
)
txt.pack(pady=10, padx=10)


window.mainloop()
