"""x = [1, 2, 0, 14, 5, -6] berilgan list ning katta elementi va kichik elementini toping."""

x = [1, 2, 0, -14, 5, 66]
i = 0

minimum = x[0]
maximum = x[0]

while i < len(x):
    if x[i] > maximum:
        maximum = x[i]
    elif x[i] < minimum:
        minimum = x[i]
    i += 1
print(f"Maksimum: {maximum}, Mimimum: {minimum}")