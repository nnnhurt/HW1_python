n = int(input())
K = int(input())
r = int(input())
variant = int(input())
V = (r - 1) * 2 + variant % K
if n - ((r - 1) * 2 + variant) > K:
    if (((r - 1) * 2 + variant + V) % 2) == 0:
        print(((r - 1) * 2 + variant + V) // 2 + 1, 2)
    else:
        print(str(((r - 1) * 2 + variant + V) // 2 + 1) + ' ' + '1')
else:
    print(-1)