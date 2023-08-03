# 시각 문제
# 시 분 초를 str로 다 더해서 원하는 숫자가 포함되어 있는지 체크 !

h = int(input())

count = 0

for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1
print(count)
