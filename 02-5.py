#딕셔너리 자료형 : 자료의 카테고리라고 생각하면 됨.
#리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다.
#{key1: Value1, key2: Value2, key3: Value3, ...}
dic = {'name': 'pey', 'phone':'010-9999-1234', 'birth': '1118'}
a = {'a': [1, 2, 3]} #Value에 리스트도 넣을 수 있다.
#딕셔너리에 쌍을 추가, 삭제하기
a={1: 'a'}#딕셔너리는 {중괄호}
a[2]='b'# = {2:'b'} 추가 a의 2번째 키는 'b'다.
print(a)
del a[1] #리스트의 값을 지울때와 표시는 똑같이 쓴다. 'del a[key]' a의 1번 키와 밸류 삭제
print(a)
#키를 사용해 밸류 얻기
grade={'pey':10,'julliet':99}
print(grade['pey'])
print(grade['julliet'])
#딕셔너리에는 리스트와 튜플에 있는 인덱싱 방법을 적용할 수 없다.
#딕셔너리에서 Key는 고유한 값으로, 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지는 모두 무시된다.
a={1:'a', 1:'b'}
print(a)
#Key는 변하지 않는 값으로, 튜플은 쓸 수 있지만, 리스트는 쓸 수 없다.
'''
a={[1,2]:'hi'}
print(a)
>> TypeError: unhashable type: 'list'
'''
#딕셔너리 관련 함수
#keys : Key 리스트 만들기.
a={'name':'pey', 'phone':'010-1234-5678', 'birth':'1118'}
print(a.keys()) #dict_keys 객체 = dict.keys()
for k in a.keys():
    print(k)
list(a.keys()) #dict_keys 객체를 리스트로 변환 #언제 dict_keys객체를 리스트로 변환하게 될까?
#Values : Value 리스트 만들기 
print(a.values())
#Items : Key, value 쌍 얻기
print(a.items())
#Clear : Key:Value 쌍 모두 지우기
a.clear()
print(a)
#get : Key로 Value 얻기
a={'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a.get('name'))
#a.get('name')=a['name']
#a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 None을 리턴한다.
#문자열의 find와 index함수같은 느낌.
print(a.get('nonono'))
'''
print(a['nonono'])
KeyError : 'nonono'
'''
#딕셔너리 a에 A가 없을 경우 default값을 출력하는 방법.
print(a.get('A','default'))
#in : 해당 Key가 딕셔너리 안에 있는지 조사하기
print('name' in a)
print('email' in a)
dic={'name':'홍길동', 'birth':'1128', 'age':30}
