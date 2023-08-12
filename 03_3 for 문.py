#for문은 문장 구조가 한눈에 들어온다는 장점이 있다.
test_list = ['one','two','three']
for a in test_list: #one, two, three를 순서대로 a에 대입
    print(a)

a=[(1,2), (3,4), (5,6)]
for (x, y) in a:
    print(x + y) #리스트의 요솟값이 튜플이라서 각각의 요소가 자동으로 x, y에 대입됨.

a = [90, 25, 67, 45, 80]
b = 0
for x in a:
    b = b + 1
    if x >= 60:
        print("%d번 학생은 합격" %b)
    else:
        print("%d번 학생은 불합격" %b)

#continue 문은 for문에도 사용할 수 있다.
a = [90, 25, 67, 45, 80]
b = 0
for x in a:
    b = b+1
    if x < 60: continue
    print("%d번 축하합니다. 합격입니다." %b)

for x in range(len(a)): #len은 리스트 안의 요소 개수를 리턴하는 함수
    if a[x] < 60:
        continue
    print("%d번 축하합니다. 합격입니다." %(x+1))

#range 함수 : 숫자 리스트를 자동으로 만들어 주는 함수.
a = range(10)
# range(0, 10) == 0~9까지.
a = 0
for b in range(1, 11):
    a = a + b 

print(a)

##for과 range를 이용한 1부터 100까지 더하기
a = range(100) # == a = range(0,101) == 1부터 100까지
b = 0
for c in a:
    b = b + c
print(b)

#for과 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")#print함수에 end파라미터를 정한 이유는 결과값을 출력할 때, 다음줄로 넘기지 않고 그 줄에 계속 출력하기 위해서임.
    print('') #칸 바꾸기, 두번째 for문이 끝나면 결괏값을 다음 줄부터 출력하게 하는 역할을 한다.

#리스트 컴프리헨션 #컴프리헨션이 뭐지
a=[1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

a=[1,2,3,4]
result = [num*3 for num in a if num%2 == 0]
print(result)
#[표현식 for 항목 in 반복_가능_객체 if 조건문]
'''[표현식 for 항목 in 반복_가능_객체 if 조건문1
         for 항목 in 반복_가능_객체 if 조건문2] '''

result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)
#while문을 for문으로 바꿀수도 있고, for문을 while문으로 바꿀수도 있다.
a = 1
while a in range(1, 50):
    a = a + 1
print(a)

for a in range(1, 50):
    a = a + 1
print(a)
