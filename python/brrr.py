
#class Cars:
#    def __init__(self,brand,model,year,price):
#        self.brand = brand
#        self.model = model
#        self.year = year
#        self.price = price
#
#    def __str__(self):
#        return f"""
#Brand:{self.brand}
#Model:{self.model}
#Year:{self.year}
#Price:{self.price}
#"""
#    
#car1 = Cars("Toyota","Corolla","2024","24.500 USD")
#car2 = Cars("Honda","Civic","2024","16.300 USD")
#
#print(car1)
#print(car2)


#a=float(input("Ilk eded:"))
#b=float(input("Ikinci eded:"))
#
#print(a+b)

#a=int(input("Yasinizi daxil edin:"))
#if a<18:
#    print("Balacasan.")
#if a>=18:
#    print("Boyuksen.")

#a=int(input("Eded daxil edin:"))
#if a%2==0:
#    print("Cut ededdir.")
#else:
#    print("Tek ededdir.")

#a=float(input("Ilk eded:"))
#b=float(input("Ikinci eded:"))
#
#if a>b:
#    print(a)
#else:
#    print(b)


#DOVRLER

#for i in range (1, 101):
#    print(i)

#numbers = []
#
#for i in range(10):
#    num = float(input(f"{i+1}-ci ədədi daxil edin: "))
#    numbers.append(num)
#
#total = sum(numbers)
#
#print(f"Daxil edilən ədədlər: {numbers}")
#print(f"Ədədlərin cəmi: {total}")

#a = int(input("Eded daxil edin: "))
#
#def sade_eded(num):
#    if num <= 1:
#        return False
#    for i in range(2, num):
#        if num % i == 0:
#            return False
#    return True
#
#if sade_eded(a):
#    print("Sade ededdir.")
#else:
#    print("Murekkeb ededdir.")

#class BankAccount:
#    def __init__(self, initial_balance=0):
#        self.balance = initial_balance
#
#    def deposit(self, amount):
#        if amount > 0:
#            self.balance += amount
#            return f"{amount} AZN hesabınıza əlavə edildi. Cari balans: {self.balance} AZN"
#        return "Əlavə ediləcək məbləğ müsbət olmalıdır."
#
#    def withdraw(self, amount):
#        if amount > self.balance:
#            return "Balansda kifayət qədər vəsait yoxdur."
#        elif amount > 0:
#            self.balance -= amount
#            return f"{amount} AZN hesabınızdan çıxarıldı. Cari balans: {self.balance} AZN"
#        return "Çıxarılacaq məbləğ müsbət olmalıdır."
#
#
#account = BankAccount(100)  
#print(account.deposit(50))  
#print(account.withdraw(30)) 
#print(account.withdraw(150))  