file = open("adamlar.txt", "a")

adamlar = ["Shookrun", "Sadiq", "Comerun", "Ay-Khan", "Murad", "Dream", "Zaur", "Kamal", "Aqshin", "Firudin", "Adam", "Adem", "Mikayil", "Rasim", "Arzu", "Ilqar", "Malik", "Lale", "Salman", "Habil"]

for i, adam in enumerate(adamlar, 1):
    file.write(f"{i}. {adam}\n")
