'리스트는 서랍장이다. python에서는 list에 다양한 자료형을 넣을 수 있다.'
a = [1, 2, 3, ["Life", "is"], 6]
print(type(a))
print(a[3][0]) #[3]번째 인덱스의 속성에서 [0] 자리에 있는 값 ["Life", "is"][0]
a=[1, 2, 3, 4, 5]
a=[1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])
#리스트의 슬라이싱
print(a[0:2]) #[0이상:2미만][2:]=2부터 끝까지 [:5]=처음부터 5까지
print(a[0::2]) #[0이상: 미만:2칸씩 건너뛰기]
a=[1, 2, [3, 4, 5]]
print(a[2][:2])

print(len(a)) #리스트의 길이를 구할 때 사용, 문자열, 튜플, 딕셔너리에서도 사용 가능

#리스트 더하기
a=[1, 2 ,3]
b=[4, 5, 6]
print(a+b)
print(a*3)
print(len(a))

#리스트의 값 수정하기
a=[1, 2, 3]
a[2] = 4
print(a[0:1])
del a[1] #리스트의 값 삭제하기
#del a[x]는 x번째 요솟값을 삭제한다. del 객체
print(a)
a=[1, 2, 3, 4, 5, 6]
del a[2:]
print(a)
#a.append(x) : x를 리스트의 맨 마지막에 추가한다.
a.append(8)
print(a)
a.append(7)
print(a)
#a.sort() : 리스트의 요소를 순서대로 정렬해준다.
a.sort()
print(a)
#a.reverse() : 리스트를 역순으로 뒤집어준다.
a=[1, 2, 3]
a.reverse()
print(a)
#a.index(x) : 리스트에 x값이 있으면 x의 인덱스 값을 리턴한다.
print(a.index(3))
#a.insert(a, b) : 리스트의 a번째 위치에 b를 삽입한다.
a.insert(0,0)
print(a)
#a.remove(x) : 리스트에서 첫번째로 나오는 x를 삭제한다.
a.append(3)
print(a)
a.remove(3)
print(a)
#a.pop() : 리스트의 맨 마지막 요소를 리턴하고 그 요소를 삭제한다.
print(a.pop())
print(a)
#a.count(x) : 리스트 안에 x가 몇 개 있는제 조사하여 그 개수를 리턴
a.append(1)
print(a)
print(a.count(1))
#extend(x) : x에는 리스트만 올 수 있으며, 원래의 a리스트에 x를 더하게 된다.
a=[1, 2, 3]
a.extend([4,5])
print(a)
#a.extend([4, 5])는 a +=[4,5]와 동일.

a=['유','부','주','엉','붕','이']
b=a[0] + a[2] + a[4]
print(b)
if b:
    print("우흥")