age = int(input("Yasinizi daxil edin:"))
pensiya_yasi = 65

def yasi_yoxla(age, pensiya_yasi):
    if age >= pensiya_yasi:
        return "Siz artiq pensiya yasina catmisiniz ve ya onu kecmisiniz."
    else:
            qalan_il = pensiya_yasi - age
    return "Sizin pensiya yasina " + str(qalan_il) + " il qalib."
    
print(yasi_yoxla(age, pensiya_yasi))  
