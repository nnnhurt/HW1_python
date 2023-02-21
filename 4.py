#4
x = int(input())
# делим число на десятки t и единицы e
t = x // 10
e = x % 10
#начнем с десятков
if t == 10:
    result = "C"
elif t == 9:
    result = "XC"
elif t == 4:
    result = "XL"
elif t >= 5:
    result = "L" + (t - 5)*"X"
else:
    result = t*"X"
# теперь единицы
if e == 9:
    result += "IX"
elif e == 4:
    result += "IV"
elif e >= 5:
    result += "V" + (e - 5)*"I"
else:
    result += e*"I"
print(result)