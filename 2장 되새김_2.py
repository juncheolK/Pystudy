#3번째 복습
'''
헷갈린 부분들
당연한거지만 아직 각 자료형에 대한 함수가 어떤게 있는 지 바로 나오지 않는다.
join함수의 활용법이 미숙하다. "추가하고 싶은 변수 x".join(x를 추가 하고 싶은 변수)
'''
#1
a=80
b=75
c=55
d=a+b+c
print(d//3)
#2
a = 14
if a%2 == 0:
    print("a is even")
else :
    print("a is odd")
#3, 4
pin = "881120 - 1068234"
a= pin.split("-")
yyyymmdd = a[0]
print(yyyymmdd)
num = a[1][1]
print(num)
if int(num)%2 == 0:
    print("woman")
else:
    print("man")
#5
a = "a:b:c:d:e"
b = a.replace(":", "#")
print(b)
#6
a = [1,5,4,3,7]
a.sort()
a.reverse()
print(a)
#7
a = ['life', 'is', 'a', 'great', 'day']
result = " ".join(a)

print(result)
#8
a = (1,2,3)
a = a + (4,)
print(a)
#9
a = dict() 
print(a)
#10
a = {'A':90, 'B':80, 'C':70, 'D':60}
result = a.pop('B')
print(a)
print(result)
#11
a = [1,1,1,1,2,3,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
aSet = set(a)
b = list(aSet)
print(b)
#12