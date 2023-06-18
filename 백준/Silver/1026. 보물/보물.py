def minimize_S(num, A, B):
    A.sort()
    B.sort(reverse=True)
    total = 0
    for i in range(num):
        total += A[i] * B[i]
    return total
num=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(minimize_S(num, A, B))