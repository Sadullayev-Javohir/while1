"""List yaratiladi va ekrandan son kiritiladi. Kiritilgan son listning ichida bor bo'lsa 'Element bor'
aks holda 'Element yo'q' kabi so'zlarni chiqaring."""

num = int(input("Son kiriting: "))
numList = [21, 15, 16, 90, 19, 53, 23, 89, 64]
i = 0
text = ''
check = False
while i < len(numList):
    if num == numList[i]:
        check = True
        break
    i += 1

if check:
    print("Element bor")
else:
    print("Element yo'q")