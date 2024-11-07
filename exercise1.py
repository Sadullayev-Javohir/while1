"""Foydalanuvchidan raqam so'rang va u 0 dan katta bo'lsa, uni yig'indiga 
qo'shib boring. 0 kiritilganda, yig'indini chiqaring."""


result = 0
while True:
    num = int(input("Raqam kiriting: "))
    if num >= 0:
        result = result + num
    if num == 0:
        result = result
        print(result)
        break
    print(result)