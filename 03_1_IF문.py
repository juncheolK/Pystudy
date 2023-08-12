# IF 조건문에서 '조건문'은 참과 거짓을 판단하는 문장.
money = True
if money:
    print("A")
else:
    print("B")
# 파이썬의 IF문에서는 들여쓰기 규칙을 잘 지켜야 한다.
# 조건문 뒤에는 반드시 콜론(:)이 붙는다.
#비교 연산자. <, >, ==, !=(같지 않다.), >=, <=
x=3
y=2
print(x > y)
x != y
money = 2000
if money >= 3000:
    print("택시 가능")
else:
    print("뚜벅")
# and, or, not
# x or y : x와 y 둘 중 하나만 참이어도 참이다.
# x and y : x와 y 모두 참이어야 참이다.
# not x : x가 거짓이면 참이다.
money = 2000
card = True
if money >= 3000 or card:
    print("택시")
else:
    print("뚜벅")
# in / in not : X in Y ==X가 Y안에 있다면 참, X not in Y == X가 Y안에 없다면 참
print(1 in [1,2,3])
print(1 not in [1,2,3])
print('a' in('a','b','c'))
print('j' not in 'python')
pocket = ['지갑', '참치']
if '돈' in pocket:
    print("택시를 타라")
else:
    print("걸어")

주머니=['카드', '버스', '지하철']
if '카드' not in 주머니:
    print('걸어')
else:
    print('버스')
#pass : 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때나 아무런 일도 하지 않도록 설정하고 싶을 때 사용
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드 꺼내")
#다양한 조건을 판단하는 elif
#주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시")
else:
    if card:
        print("택씨")
    else:
        print("걷자")

if 'money' in pocket:#주머니에 돈이 있으면
    print("택시a")
elif card: #주머니에 돈이 없고 카드가 있으면
    print("택시b")
else: #주머니에 돈이 없고 카드도 없으면
    print("걸어")
#elif는 이전 조건문이 거짓일 때 수행된다.
#elif는 개수 제한 없이 사용할 수 있다.
#if문을 한 줄로 작성하기
if 'money' in pocket:
    pass
else:
    print('카드')
pocket =['paper', 'money', 'phone']
if 'money' in pocket: pass
else: print(카드)
score = 70
if score >=60: message = 'success'
else : message = 'failure'
print(message)
message = 'success' if score >= 60 else "failure"
print(message)
#변수 = 조건문이 참인 경우의 값 if 조건문 else 조건문이 거짓인 경우의 값

