n, k = map(int, input().split())
ans = 0
l = [int(i) for i in input().split()]
for i in range(n):
    ans += (l[i] > 0 and i < k) or (l[i] > 0 and i >= k and l[i] == l[k-1])
print(ans)
