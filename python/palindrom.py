def palindrom(cumle):
    a = "".join(c.lower() for c in cumle if c.isalnum())
    return a == a[::-1]

cumle = input("Cümləni daxil edin: ")
print("Bu cümlə palindromdur!" if palindrom(cumle) else "Bu cümlə palindrom deyil.")