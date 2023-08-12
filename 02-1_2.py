line = "="*50
a=51
if a > 1:
    print("a는 1보다 크다")
print("="*50)
for a in [1, 2, 3]:
    print(a)
print("="*50)
i = 0
while i < 5:
    i = i + 1
    print(i)
print('='*50)
def add(a, b):
    return a + b
n = add(3, 4)
print(n)
print("="*50)
a=8.17e4
"e=10"
print(a)
print(0o27)
print(0x52)
"0o는 8진수 0x는 16진수"
a = 3
b = 4
print(a**b)
"**는 제곱을 뜻하는 표시"
while a < 10:
    a = a+1
    print(a**b)
"이렇게 쓰면 a값을 각각 구해서 b제곱을 해준다."
print(7%3)
print(3%7)
print(7/4)
print(6//4)
"%는 나머지를 /는 몫을 //는 몫 중 정수까지의 숫자만"
print("="*50)
print(14//3)
print(14%3)
'''
이스케이프 코드
\n : 문자열 안에서 줄을 바꿀 때 사용
\t : 문자열 사이에 탭 간격을 줄 때 사용
\\ : \를 그대로 표현할 때 사용
\' : '를 그대로 표현할 때 사용
\" : "를 그대로 표현할 때 사용
여기 아래부터 무슨소린지 모르겠다.
\r : 캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
\f : 폼 피드 (줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
'''
a='캐리지\t리턴이\n뭘까?'
print(a)
b=len(a)
print(b)
"인덱싱 : 무언가를 가리킨다 / 슬라이싱 : 무언가를 잘라낸다"
a = "life is too short, you need python"
print(a[3])
print(a[0:4])
"[a:b] 는 a에서 b까지를 의미한다. [a:]는 a부터 끝까지 [:b]는 처음부터 b까지 [:]는 처음부터 끝까지"
"[a:b]에서 b는 포함하지 않으므로, a~b-1까지의 값이 나온다."
print(a[0:3])
"문자열 자료는 슬라이싱 할 수 없다."
"문자열 포매팅"
num = 72
print("I eat %d apples." % num)
print("I eat %s apples." % "zero")
N=10
D="three"
c="I ate %d apples. so I was sick for %s days."
print(c % (N, D))
'''
문자열 포맷 코드
%s : 문자열 (string)
%c : 문자 1개 (character)
%d : 정수 (integer)
%f : 부동소수 (floating-point)
%o : 8진수
%x : 16진수
%% : Literal % (문자 % 자체) (연산자 %d와 %가 같은 문자열 안에 존재하는 경우 %는 무조건 %%로 써야한다.)
포맷팅이란? 문자열 안에 어떤 값을 삽입하는 것
포맷팅은 포멧 코드와 포멧 함수로 할 수 있다.
'''
a="A is %s%%." %92.124
print(a)
b="%10s" % "hi"#전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고, 그 앞의 나머지 공간은 공백으로 남겨둬라.
print(b)
A="%0.3f" %3.141592
print(A)
print(line)
"숫자 바로 대입하기"
print("I eat {0} apples".format(6))
print("I eat %d apples." % 33)
"2개 이상의 값"
숫자 = 3
날짜 = 2
print("I eat {0} apples and {1} day".format(숫자, 날짜))
"{0}, {1}, {2} 순의 순서로 .format(a, b, c)에서 a b c가 대입된다."
print("{0:<10}".format("hi")) # 총 10자릿수를 만들고 치환되는 문자열을 왼쪽에 정렬한다.
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi")) # 정렬 위치 앞에 오는 값으로 공백을 채운다.
print("{0:@^10}".format("hi"))
print("{0:10.4f}".format(3.42134234)) # 총 10자릿수를 만들고, 소수점 4번째 미만까지 표시한다.
print("{{   and   }}".format())
print(line)
"f문자열 포매팅 f'{}' > {}안의 값을 정의된 값으로 바꾼다."
name = "김준철"
age = 26
print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.')
d={'name':'김준철', 'age':30 }
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"python":!^12}')
'''
문자열 내장 함수
count : 문자 개수 세기
a = "hobby"
a.count('b')
>> 문자열 중 문자 b의 개수를 리턴 >> 2개가 됨.
'''
a = "hobby"
print(a.count('b'))
'''
a.find('b) : 위치 알려주기
a = "python is the best choice"
a.find('b')
a.find('k') > -1 : 문자열이 포함되지 않았다는 뜻.
'''
a = "python is the best choice"
print(a.find('b'))
'''
a.index('b') : 위치 알려주기.
find랑 기본적으로 같지만, 찾는 문자가 존재하지 않으면 오류가 발생함

join : 문자열 삽입
'''
print(",".join('abcd'))
'upper 소문자를 대문자로 바꾸기'
a="hi"
print(a.upper())
'lovwer 대문자를 소문자로 바꾸기'
a='HI'
print(a.lower())
'''
a.strip() : 공백 지우기
a.rstrip() : 오른쪽 공백 지우기
a.lstrip() : 왼쪽 공백 지우기
a.replace("A", "B") : "A"를 "B"로 문자열 대체하기
'''
a = "Life is too short"
print(a.replace("Life", "your leg"))
'''
a.split(b) : b를 기준으로 문자열 나누기
'''
print(a.split())
b="a:b:c:d"
print(b.split(':'))
