"""A dan B gacha bo'lgan sonlarni yig'indisini ekranga chiqaring."""

A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))

result = 1

while A <= B:
    print(result)
    A = A + 1
    result += A
    
    