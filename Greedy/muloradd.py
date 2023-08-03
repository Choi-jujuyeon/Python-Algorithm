#곱하기 혹은 더하기

# step 01. 받은 문자열의 첫번째 문자를 숫자로 변환해 result 값에 저장
# step 02. 두번째 숫자부터 끝까지 반복문 돌리기
# step 03. 두번째 숫자부터 하나씩 data에 값을 저장
# step 04. result(첫번째 문자)와 data(두번째부터~문자)를 비교

a = input()

result = int(a[0])

for i in range(1,len(a)):
    num = int(a[i])
    if num <= 1 or result <=1:
       result += num
    else:
        result *= num

print(result)