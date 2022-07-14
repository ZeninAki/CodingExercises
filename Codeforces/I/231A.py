x, ans = int(input()), 0
for i in range(x):
    a, b, c = map(int, input().split())
    ans += (a+b+c >= 2)
print(ans)