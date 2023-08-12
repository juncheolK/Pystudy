#자료형의 값을 저장하는 공간, 변수 = 객체
#변수 이름_ = 변수에 저장할 값 
a=[1,2,3]
print(id(a)) #객체의 주솟 값, 컴퓨터가 프로그램에서 사용하는 데이터를 기억하는 공간.
#객체의 주솟 값이 필요한 때가 있나?
b=a
print(id(b))#메모리의 주솟 값은 고정값이 아니다.
#A is B:A와 B가 가리키는 객체는 같은가?
print(a is b) 
#b 변수를 생성할 때 a 변수의 값을 가져오면서 a와 다른 주소를 가리키도록 하는 방법

#리스트 복사. [:] 
a=[1,2,3]
b=a[:]#리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
a[1]=4
print(a)
print(b)
#copy 모듈 #모듈과 함수의 차이점이 뭐지 #모듈은 함수나 변수, 클래스를 모아 놓은 파이썬 파일.
from copy import copy#copy 모듈에 있는 copy 함수 import
a=[1, 2, 3]
b= copy(a) # == b=a[:]
print(b)
print(b is a)
#리스트 자료형의 copy함수 사용하기.
b=a.copy() #파이썬 리스트에 내장된 copy 함수 사용.
print(b is a)
#튜플로 a, b 값에 대입
a, b=('python', 'life')
(a, b)='python', 'life' #튜플은 괄호를 생략해도 된다.
[a, b]= ['python', 'life'] #리스트로 변수를 만들 수도 있으며
a = b = 'python' #여러 개의 변수에 같은 값을 대입할 수 있다.
a=3
b=5
a,b=b,a #a와 b의 값을 바꿈.
print(a, b)
a=[1,2,3]
b=[1,2,3]
print(a is b) #서로 메모리가 다르므로 false
