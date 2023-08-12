# 01. 평균 점수 구하기.
국어= 80
영어 = 75
수학 = 55
print((국어 + 영어 + 수학)/3)
#홀수, 짝수 판별하기.
n=13
if n%2==1:
    print('홀수')
#주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd='19'+pin[:6]
print(yyyymmdd)
num=pin[7:]
print(num)
#주민등록번호 인덱싱
pin ="881120-1068234"
print(pin[7])
#문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
#리스트 역순 정렬하기.
a=[1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)
#리스트를 문자열로 만들기
a=['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
#튜플 더하기
a=(1,2,3)
a = a+(4,) #요소가 한개만 있을 때는 반드시 ,를 붙여야함
print(a)
#딕셔너리 값 추출
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)
#리스트에서 중복 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b= list(aSet)
print(b)
#파이썬 변수
a = b =[1,2,3]
a[1] = 4
print(b)