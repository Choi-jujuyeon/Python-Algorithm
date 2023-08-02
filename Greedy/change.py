# 거스름돈 알고리즘

# step 01. 입력할 거스름돈을 담을 변수 n과 결과값을 담을 count 변수  초기화
# step 02. array 내림차순으로 화폐 넣기
# step 03. array 각 요소의 값을 coin에 할당
# step 04. 거스름돈을 array에 저장된 화폐로 나눠준다.== 동전의 개수를 구할 수 있다.
# step 05. 다음화폐로 연산해야할 거스름돈 업데이트를 해준다.

n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
  count += n // coin
  n %= coin

print(count)
