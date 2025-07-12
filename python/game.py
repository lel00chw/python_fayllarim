class Adamlar:
    def __init__(self,name,power,weapon,health,strength):
        self.name = name
        self.power = power
        self.weapon = weapon
        self.strength = strength
        self.health = health


    def __str__(self):
        return f"""
Name:{self.name}
Power:{self.power}
Weapon:{self.weapon}
Health:{self.health}
Strength:{self.strength}
"""
    
    def attack(self, enemy):
        if self.health<=0:
            print(f"{self.name}in cani qalmadi")
            return
        if enemy.health<=0:
            print(f"{enemy.name} coxdan lıbırcıt olub")
            return
        if self.strength>=enemy.strength:
            enemy.health -= self.strength
            if enemy.health <= 0:
                print(f"{self.name},{enemy.name}-a {self.weapon} ile hucum etdi!")
                print(f"{enemy.name} badimcanliga getdi!!")
            else:
                print(f"{self.name},{enemy.name}-a {self.weapon} ile hucum etdi!")
                print(f"{enemy.name}in cani {enemy.health} oldu!")
        else:
            print(f"{self.name}in gücü{enemy.name}in gucunden azdi")  


adam1 = Adamlar("Mikayil","Reality warping","Time Blade",250,300)
adam2 = Adamlar("Kamran","Super Speed","Poison Blade",260,300)
adam3 = Adamlar("Ayxan","Invisibility","Knife",230,300)
adam4 = Adamlar("Sadiq","Destruction","Bomb",240,300)
adam5 = Adamlar("Shukran","One Above All","The Orb",270,300)

adam1.attack(adam2)
adam5.attack(adam1)

