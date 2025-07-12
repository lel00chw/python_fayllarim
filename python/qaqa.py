limit = 10
streak = 0
duzgun = 0
yanlis = 0

suallar = [
    {"sual": "Dəyişən nədir?", "cavab": "deyeri deyise bilen simvoldur"},
    {"sual": "Python-da dəyişənlər hansı tiplərdə ola bilər?", "cavab": "int float str list tuple dict set bool"},
    {"sual": "İf-şərti nədir?", "cavab": "sertli ifade"},
    {"sual": "İf-şərtində 'else' nə işə yarayır?", "cavab": "if serti dogru olmadigi zaman kodu icra edir"},
    {"sual": "Döngü nədir?", "cavab": "tekrarlanan emrler toplusu"},
    {"sual": "Python-da 'for' döngüsü necə işləyir?", "cavab": "iterable icerisindeki her bir elementi dovr etmeye imkan verir"},
    {"sual": "Funksiyalar nədir?", "cavab": "giris deyerlerine esaslanaraq cixisa cavab veren alt-proqramdir"},
    {"sual": "Funksiyaların istifadəsi nə üçün vacibdir?", "cavab": "kodun tekrar istifadesi ve teskilatlanmasi ucun vacibdir"},
    {"sual": "Python-da bir funksiyanı necə yarada bilərik?", "cavab": "def() vasitesi ile"},
    {"sual": "Funksiyaya arqument göndərmək nə deməkdir?", "cavab": "funksiyanin ise salinmasinda ona deyer teqdim etmek"}
]

for i, sual in enumerate(suallar, 1):
    cavab = input(f"{i}. {sual['sual']}\nCavab: ")
    if cavab.strip().lower() == sual["cavab"].lower():
        duzgun += 1
        streak += 1
        print("Duzgun Cavab!")
    else:
        yanlis += 1
        streak = 0
        print("Yanlis Cavab!")

print("Suallar bitdi!")
print("Streak:", streak)
print("Dogrularin sayi:", duzgun)
print("Yanlislarin sayi:", yanlis)