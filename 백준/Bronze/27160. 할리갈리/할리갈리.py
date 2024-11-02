from collections import defaultdict

def solutions():
    n = int(input())
    fruit_counts = defaultdict(int)
    for _ in range(n):
        s = input().split(" ")
        fruit_counts[s[0]] += int(s[1])
    if 5 in fruit_counts.values():
        print("YES")
    else:
        print("NO")

solutions()
