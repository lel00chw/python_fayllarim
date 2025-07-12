#import string
#
#first_char = input("Enter the first character:")
#second_char = input("Enter the second character:")
#
#def check_characters():
#   if first_char.islower() and second_char.islower():
#      return 1
#   if first_char.isupper() or first_char.islower() and second_char.isupper() or second_char.islower():
#      return 0
#   if first_char and second_char != string.ascii_letters:
#      return -1
#   
#answer = check_characters()
#print(answer)



#first_char = input("Enter the first character:")
#second_char = input("Enter the second character:")
#letters_lower = "abcdefghijklmnopqrstuvwxyz"
#letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
#def check_characters():
#   if first_char.islower() and second_char.islower():
#      return 1
#   if first_char.isupper() or first_char.islower() and second_char.isupper() or second_char.islower():
#      return 0
#   if first_char and second_char != letters_lower and letters_upper:
#      return -1
#   
#answer = check_characters()
#print(answer)



#a=0
#my_list = [1, 2, 3, -2, -9, 89, 12, -121, -65]
#for eded in my_list:
#    if eded<0:
#        a=a+eded
#print(a)



#age = int(input("Yasinizi daxil edin:"))
#pensiya_yasi = 65
#
#def yasi_yoxla(age, pensiya_yasi):
#    if age >= pensiya_yasi:
#        return "Siz artiq pensiya yasina catmisiniz ve ya onu kecmisiniz."
#    else:
#            qalan_il = pensiya_yasi - age
#    return "Sizin pensiya yasina " + str(qalan_il) + " il qalib."
#    
#print(yasi_yoxla(age, pensiya_yasi))  



#class Characters:
#    def __init__(self,name,surname,job,wealth,weapon):
#        self.name = name
#        self.surname = surname
#        self.job = job
#        self.wealth = wealth
#        self.weapon = weapon
#
#    def __str__(self):
#        return f"""
#Name:{self.name}
#Surname:{self.surname}
#Job:{self.job}
#Wealth:{self.wealth}
#Weapon:{self.weapon}
#"""
#    
#character1 = Characters("Tim","Cheese","Hitman","Two Hundred Thousand",".338 Lapua Magnum")
#character2 = Characters("John","Pork","Businessman","Ten Million","Glock 23")
#
#print(character1)
#print(character2)



import tkinter as tk
def on_button_click():
    print(f"Ad: {ad_entry.get()}, Soyad: {soyad_entry.get()}, Yas: {yas_entry.get()}, Ata adi: {ata_adi_entry.get()}")

root = tk.Tk()
root.title("BANAN")

tk.Label(root, text="Ad:").pack()
ad_entry = tk.Entry(root)
ad_entry.pack()

tk.Label(root, text="Soyad:").pack()
soyad_entry = tk.Entry(root)
soyad_entry.pack()

tk.Label(root, text="Yas:").pack()
yas_entry = tk.Entry(root)
yas_entry.pack()

tk.Label(root, text="Ata adi:").pack()
ata_adi_entry = tk.Entry(root)
ata_adi_entry.pack()

root.mainloop()