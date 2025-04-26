#def ters_cevir(s):
#    return s[::-1]
#metn = input("Bir cumle ve ya soz daxil edin:")
#print("Metnin tersine cevrilmis hali:", ters_cevir(metn))


cumle=input("tez nese yaz vaxtim yoxdu:")
def sozleri_ters_sirala(cumle):
    return '  '.join(cumle.split()[::-1])

print("cumlenin eks duzulusu:",sozleri_ters_sirala(cumle))