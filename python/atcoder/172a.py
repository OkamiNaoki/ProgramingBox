from itertools import product as pd

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = 0
for i, j in pd(range(1 << h), range(1 << w)):
    temp = 0
    for x, y in pd(range(h), range(w)):
        if 1 << x & i and 1 << y & j:
            if c[x][y] == "#":
                temp += 1
    ans += temp == k
print(ans)
