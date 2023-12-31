#반복문 while
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무를 무찔렀습니다.")
#조건문이 거짓이 될 때, while문을 빠져나간다.

prompt = '''
    1.Add
    2.Del
    3.List
    4.Quit

    Enter number: '''

number = 0
while number != 4:
    print(prompt)
    number = int(input())#정수값을 input할 수 있도록 띄운다.

#Break문. while문 강제로 빠져나가기.
#커피가 없을 때 판매를 중지하고, 판매 중지 문구를 사용자에게 보여준다.
coffee = 10 # 자판기에 커피가 10개 있음
money = 300 #자판기에 넣을 돈은 300원
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요!"))
    if money == 300:
        print ("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print ("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다" % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#continue문 : while문을 빠져나가지 않고, 맨 처음으로 다시 돌아가기.
a = 0
while a < 10:
    a = a+1
    if a%2 == 0: continue #a를 2로 나누었을 때 나머지가 0이면 맨 처음으로 돌아간다.
    print(a)

a = 0
while a < 10:
    a = a+1
    if a%3 == 0: continue
    print(a)

# 무한루프
while True:
    print("ctrl+C")
