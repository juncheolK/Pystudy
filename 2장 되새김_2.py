#1
a=80
b=75
c=55
print((a+b+c)/3)
#2
n = 13
if n%2!=1:
    print("짝수")
else:
    print("홀수")
#3
PIN = "881120-1068234"
YYYYMMDD = PIN[:6]
NUM = PIN[-7:]
print(YYYYMMDD)
print(NUM)
#4
print(PIN[7])
#5 replace
a = "a:b:c:d"
b = a.replace(":","#")
print(b)
#6
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)
#7 "X".join(a) : X를 a리스트 사이에 추가한다.
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
#8 : 요소가 하나만 있을 때는 (,) 붙야아함
a =(1,2,3)
a = a + (4,)
print(a)
#10
a={'A':90, 'B':80, 'C':70}
result = a.pop('C')
print(a)
print(result)
#
a=[1,1,1,1,1,2,2,2,2,3,3,3,4,4,5,6,6,7]
aset= set(a)
b= list(aset)
print(b)
#