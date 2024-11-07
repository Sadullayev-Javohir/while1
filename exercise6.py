"""Ekranda kiritilgan sonning necha xonali ekanligini aniqlang."""

n = int(input("n sonini kiriting: "))
string = str(n)
i = 1

while i < len(string):
    i += 1
print(f"{n} {i} xonali son")