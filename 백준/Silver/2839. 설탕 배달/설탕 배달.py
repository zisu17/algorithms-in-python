n = int(input())
bag = 0
while n > 0:
    if n % 5 == 0:
        bag += n // 5
        n -= (n // 5) * 5
        break
    else:
        n -= 3
        bag += 1
if n == 0:
    print(bag)
else:
    print(-1)