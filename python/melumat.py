import tkinter as tk
from tkinter import messagebox

def on_button_click():

    ad = ad_entry.get()
    soyad = soyad_entry.get()
    yas = yas_entry.get()
    ata_adi = ata_adi_entry.get()

    messagebox.showinfo("Daxil edilmis melumatlar", f"Ad: {ad}\nSoyad: {soyad}\nYas: {yas}\nAta adi: {ata_adi}")


root = tk.Tk()
root.title("Melumatlari daxil edin")
root.geometry("250x250")  

tk.Label(root, text="Ad").grid(row=0, column=0, padx=10, pady=5)
ad_entry = tk.Entry(root)
ad_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Soyad").grid(row=1, column=0, padx=10, pady=5)
soyad_entry = tk.Entry(root)
soyad_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Yas").grid(row=2, column=0, padx=10, pady=5)
yas_entry = tk.Entry(root)
yas_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Ata Adi").grid(row=3, column=0, padx=10, pady=5)
ata_adi_entry = tk.Entry(root)
ata_adi_entry.grid(row=3, column=1, padx=10, pady=5)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.grid(row=4, columnspan=2, pady=10)


root.mainloop()