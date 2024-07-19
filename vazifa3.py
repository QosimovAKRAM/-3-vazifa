from collections import Counter

def eng_kop_takrorlangan(matn):
    count = Counter(matn)
    eng_kop = count.most_common(1)[0]
    return eng_kop[0]

# Misollar
print(eng_kop_takrorlangan("vvj7vt5i744"))  # '7'
print(eng_kop_takrorlangan("??"))   # '?'
