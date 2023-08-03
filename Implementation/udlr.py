# 상하좌우 문제

n = int(input())
x, y = 1, 1
plans = input().split()

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# plans에 있는 변수를 plan 변수를 활용해 하나씩 확인
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      # nx,ny를 사용하기 전에 초기화하지 않아도 된다 !
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny

print(x, y)
