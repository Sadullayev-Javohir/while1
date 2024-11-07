"""x = [1, 2, 3, 14, 5, 6, 6, 7] berilgan list ning katta elementini toping."""

x = [1, 2, 233, 114, -5, 6, 6]

i = 1
maximum = x[0]

while i < len(x):
    if x[i] > maximum:
        maximum = x[i]
    i += 1
print(f"Katta element: {maximum}")