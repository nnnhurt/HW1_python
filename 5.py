#5
a = int(input())
b = int(input())
# проверяем положительное ли число. если нет, то выводим НЕТ
if (a == 0 or (b % a) != 0):
    print('NO')
else:
# иначе просто делим число на другое число. отрицательно, т.к. мы переносим через =
    print(int(-b // a))
