#불 자료형 (참과 거짓을 나타내는 자료형)
#True / False 값만을 얻을 수 있다.
a=True
b=False
print(type(a))
print(type(b))
#조건문의 리턴값으로도 사용된다.
print(1==1)#A==B A와 B가 같은가?
print(2>1)
print(2<1)
#문자열, 리스트, 튜플, 딕셔너리 등 값이 비어있으면 ("",[],(),{}) 거짓이 된다.
#숫자는 그 값이 0일때 거짓이 된다.
a=[1,2,3,4]
while a:#a가 참인 동안
    print(a.pop())#리스트의 마지막 요소를 하나씩 꺼낸다.
if []: #만약 []가 참이면
    print("참")
else: #만약 []가 거짓이면
    print("거짓")
#bool('a') : a 자료형의 참과 거짓을 판단한다.
print(bool([1,2,3]))
s1=(1,2,3)
print(s1)
print(bool(s1))
print(bool())