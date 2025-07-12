eded = float(input('Eded daxil edin:'))
def yuvarla_eded(eded):
    kesr_hissesi = eded % 1
    if kesr_hissesi < 0.5:
        return int(eded // 1)
    else:
        return int(eded // 1 + 1)
print(yuvarla_eded(eded))