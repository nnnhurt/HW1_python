#6
a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - (4 * a * c)
if d > 0:
#0.5 так как ищем корень.
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    print(x1, x2)
if d < 0:
    print('')
elif d == 0:
    print((-b) / (2 * a))


