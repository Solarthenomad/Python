#if : 돈이 있으면 택시를 타고 돈이 없으면 걸어 간다
#위의 식을 표현하자면
from email import message


money=True
if money:
    print("택시를 타고 가라")
    
else:
    print("걸어가라")
    
#비교 연산자 if    
a=1
b=2
if a<b:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# ><   ==(a와 b가 같다) !=(a와 b가 같지 않다)

money=2000
if money>=3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
#|(or) and(&)
#x or y : x와 y 둘중 하나가 참이면 참이다
#x and y : x와 y 모두 참이어야 참이다 

money=2000
card=1

if 1 in [1,2,3]:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if 1 not in [1,2,3]:
    print("택시를 타고 가라")
    
else:
    print("걸어가라")
    

#elif : 다중 조건 판단(조건문들이 여러개 있을 때 사용)

pocket=['papaer', 'cellphone']
card=True #'card가 있다'라는 뜻. 조건문 쓸 때 기본이 되며 default 값이다. 
if 'money' in pocket: #조건 1. 주머니에 돈이 있으면 택시를 타고가라
    print("택시를 타고가라")
elif card: #주머니에 돈이없지만 card가 있으면 택시를 타고가라
    print("택시를 타고가라")
else : #둘다 없으면 걸어가라
    print("걸어가라")
    
score = 70 #디폴트값 설정
if score >=60 :
    message = "success"
else : 
    message = "failure"
message = "success" if score >=60 else "failure" #조건부 표현식
print(message)

#while = 나무를 10번찍는다. 10번 넘어가면 멈춘다.

treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    print("나무를 %d번 찍었습니다"%treeHit)
    if treeHit ==10:
        print("나무 넘어갑니다.")
        
coffee = 10
money = 300 #변수들먼저 만들어주기

while money : #money를 낸다는 조건 하에 
    print("돈을 받았으니 coffee를 줍니다.")
    coffee=coffee-1 #coffee위에서 줬으니까 하나를 빼준 게 남은 커피
    print("남은 커피의 양은 %d개입니다." %coffee)
    if not coffee: #coffee가 false가 된다. =coffee가 존재하지 않는다.
        print("커피가 다 떨어졌습니다. 판매를 중단하겠습니다.")
        break #break를 어디에 넣든 while을 빠져나가게 됨
    
marks =[90,25,67,45,80]
number=0
for mark in marks: #파이썬에서의 for문은 리스트에서의 원소들을 자동으로 하나씩 빼오는 역할함
    number = number+1
    if mark>=60:
        print("%d번 학생은 합격입니다." %number)
        
    else : 
        print("%d번 학생은 불합격입니다." %number)
        
#1번 학생은 합격입니다
#2번 학생은 불합격입니다.
#3번 학생은 합격입니다.

marks = [90, 25,67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark < 60 : continue
    #continue는 if 조건을 만족하게 되면 continue문 아래로 나오는 코드들을 실행하지 않고 처음부터 다시 시작하게 한다. 
    print("%d번 학생 축하합니다. 합격입니다" %number)
    
#range
sum=0
for i in range(1,11): #1이상 11미만의 숫자들 하나씩나하씩 가져오기
    sum=sum+i
print(sum)

#구구단 만들기
for i in range(2,10):
    for j in range(1,10):
        print(i *j, end="")
print('')







        
