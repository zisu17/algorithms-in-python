n = int(input())
people = list(map(int, input().split()))
people.sort()
time=0
for idx, person in enumerate(people):
    time += (n-idx)*person
print(time)