# 모험가 길드

# step 01. 모험가 수와 공포도 문자열을 입력받아 숫자로 변환
# step 02. 공포도를 오름차순정렬을 해준다.
# step 03. 총 그룹 수와 그룹에 포함된 모험가 수 저장할 변수 초기화
# step 04. 공포도를 돌면서 사람 수 추가하기
# step 05. 사람수가 공포도보다 크거나 같으면 그룹형성 끝 -> 총그룹수 플러스->사람수는 다시 초기화 



n=int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count +=1
    if count >= i:
        result +=1
        count = 0
print(result)
