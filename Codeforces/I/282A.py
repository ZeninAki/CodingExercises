x, ans = int(input()), 0
for i in range(x):
    s = input()
    ans += s[0] == '+' or s[-1] == '+'
    ans -= s[0] == '-' or s[-1] == '-'
print(ans)
