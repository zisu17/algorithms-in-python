n = int(input())
score_list = list(map(int, input().split(' ')))
max = max(score_list)
new_score_list = []
for i in range(n):
    new_score = score_list[i]/max*100
    new_score_list.append(new_score)
avg = sum(new_score_list)/n
print(avg)