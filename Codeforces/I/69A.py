x, a, b, c = int(input()), 0, 0, 0
for i in range(x):
    x, y, z = map(int, input().split())
    a += x
    b += y
    c += z
print('YES' if a == 0 and b == 0 and c == 0 else 'NO')
