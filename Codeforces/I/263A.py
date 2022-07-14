x, y = -1, -1
for i in range(5):
    l = [int(k) for k in input().split()]
    if 1 in l:
        x = i
        y = l.index(1)
print(abs(x-2)+abs(y-2))