n = int(input())
A = list(map(int, input().split()))
B = sorted(A)
P = []
for i in range(n):
    idx = B.index(A[i])
    P.append(idx)
    B[idx] = -1
print(*P)