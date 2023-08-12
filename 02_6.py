#집합 자료형
s1=set([1,2,3])
print(s1)
s2=set('Hello')
print(s2)
#집합 자료형은 중복을 허용하지 않으며, 순서가 없다. >> 인덱싱을 지원하지 않음.
l1 = list(s1) #s1을 리스트로 변환, 튜블로 변환은 tuple(s1)
print(l1)
print(l1[0])
#교집합, 합집합, 차집할을 구할 때 set 자료형이 유용하게 쓰인다.
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
# A&B : 교집합 구하기 
print(s1 & s2) # = s1.intersection(s2) or s2.intersection(s1)
# A|B : 합집합 구하기
print(s1|s2) # = s1.union(s2) or s2.union(s1)
# A-B : 차집합 구하기
print(s1-s2) # = s1.difference(s2)
print(s2-s1) # = s2.difference(s1)
#add : 값 1개 추가하기
s1=set([1,2,3])
s1.add(4)
print(s1)
#update :값 여러개 추가하기
s1.update([4,5,6,7,8])
print(s1)# 중복을 허용하지 않으므로 4는 추가되지 않음.
#remove : 특정 값 제거하기
s1=set([1,2,3])
s1.remove(2)
print(s1)
