import sys, math

input = sys.stdin.readline

fin_score = []

prob = int(input().rstrip())

score = list(map(int, input().split()))

copy = tuple(score)

for i in copy:

    temp = score.pop(0)

    temp2 = temp / max(copy) * 100

    fin_score.append(temp2)

avg = sum(fin_score) / len(fin_score)

print(avg)

