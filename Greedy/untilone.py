# 1이 될 때까지
# step 01. 입력받는 값 n, k를 공백으로 구분해 정수로 변환한다.
# step 02. result 초기화 == 최종 계산 결과를 저장한다.
# step 03. while문
# N이 K로 나누어 떨어지는 수가 될 때까지 빼기
# N이 K 보다 작은지 체크 !
# 루프를 계속 돌 경우(위 조건 불만족), K로 나누기
# step 04. 남은 수는 1씩 빼주기

n, k = map(int, input().split())

result = 0

while True:
  target = (n // k) * k
  result += (n - target)
  n = target

  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)
