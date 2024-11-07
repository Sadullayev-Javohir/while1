"""x = [1, 2, 3, 14, 5, 6, 6, 7] berilgan list ning katta elementi nechani indexda ekanligini chiqaring."""

x = [1, 2, 3, 14, 5, 6, 4, 7]

i = 1
maximum = x[0]
maxIndex = 0
index = 0
while i < len(x):
    if x[i] > maximum:
        maximum = x[i]
        maxIndex = i
    i += 1
print(f"{maximum} sonning indeksi {maxIndex}")