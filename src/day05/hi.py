a = 0
b = 6

c = 2 * (a < b) - 1
d = 2 * (b < a) - 1
print(list(range(a, b+c, c)))

print(list(zip(range(a, b+c, c), range(b, a+d, d))))