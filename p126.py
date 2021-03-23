# 함수 정의
def checkEven0dd(n):
    if n % 2 == 0:
        return "짝수"
    else:
        return "홀수"

number = int(input("정수 입력해라: "))

#함수 호출
print(f'결과값 {} 다', checkEven0dd(number))









