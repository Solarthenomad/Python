#함수(def 함수이름(){코드

def sum_many(*args):    #args = 아규먼트(인자들)를 붙이면 모든 인자들
    sum = 0
    for i in args: #아규먼트들의 모든 인자들을
        sum = sum+i #sum에다가 더해줌
    return sum

print(sum_many(1,2,3,4,5,6,7))


def print_kwargs(**kwargs):         #def 함수이름(아규먼트)  #**이므로 이 친구는 딕셔너리 형태의 아규먼트들을 처리해준다.     
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은:" + k)
print(print_kwargs(name="int 조수", age=16))

def sum_an_mul(a,b):
    return a+b, a*b

print(sum_andm_mul)

def say_myself(name, old, man = True):   #man의 기본갑은 True이다. 즉 남자 맞다가 기본값으로 설정되어 있음
    print("나의 이름은 %s 입니다." %name)
    print("나의 나이는 %s입니다." %age)
    if man :
        print("남자입니다.")
    else:
        print("여자입니다.")
        
say_myself("솔라", 24, True) #위의 아규먼트들 맞는 파라미터들 설정해줌

#함수 안에 선언된 변수의 효력범위 
a=1
def vartest(a): #def vartest안의 a는 밖의 a와 다름. 즉 vartest 안의 변수들은 지역변수라고 하여 외부의 영향을 받지 않는다. 
    a=a+1

vartest(a)
print(a)
#1이 출력된다.

a=1
def vartest():
    global a
    a= a+1
    
vartest()
print(a)


#함수를 다르게 표현하기 (간단하게 표현하기) = lambda
def add(a,b):
    return a+b

add = lambda a,b : a+b #위의 함수를 lambda라는 함수를 통해서 한다. 

myList = [lambda a,b :a+b, lambda a,b : a*b]
myList[0] #lambda a,b:a+b가 불러와짐
myList[0](1,2) #lambda a,b:a+b가 불러와지고 a,b 인자에 각각 1,2가 넣어진다. 

#내장함수 vs 사용자 정의 함수
a=input()
a.append(3)
a.pop()

#이렇게 
def 사용자정의함수


#사용자 입력과 출력 함수
#input
a= input() #내장함수라고 정의된다. 
#콘솔창에 1이라고 입력하면 자동으로 a에 1이 입력된다. 
print(a) #1이 출력되게 된다. 

number = input("숫자를 입력하세요 : ")
print(number) #출력 함수 = print()

#파일 생성하기 & 닫기(변수 = open() & 변수.close)

f = open("새파일.txt", 'w')
f.close

#파일 열기 모드 
#'r' : 읽기모드 : 파일을 읽기만 할 때 사용함(read)
#'w' : 쓰기모드 : 파일의 내용을 쓸 때 사용함(write)
#'a' : 추가모드 : 파일의 마지막에 새로운 내용을 추가 시킬 때 사용함(add)

#파일을 쓰기 모두로 열어 출력값 적기 
f = open("C:/python/새파일.txt", "w")
for i in range(1,11):
    data="%d번째 줄입니다.\n" %i
    #for range는 보통 몇 번 출력할지를 표현하는 식임 그냥 이렇게 해석해주자 
    f.write(data)
f.close()


#쓴 파일이 있으면 읽어서 뭔가를 처리해야 함 = 읽자 
f = open("C:/python/새파일.txt", "r", encoding="UTF-8")
line=f.readline()   #f.readline()에서 readline()함수는 한 줄씩 읽어오는 애 딱 처음의 한 줄만 읽어옴
print(line)
f.close()

#모든 줄 다 읽어오고 싶을 때는 
#첫 번쨰 방법 : while true 사용하기
f=open("새파일.txt", "r", encoding="UTF-8")
while True: #while true는 break 나오기 전까지 계속 무한대로 실행해줌
    line = f.readline()    #f 파일을 한줄씩 읽은 걸 line이라 하자
    if not line : break #line이 아니면 끝내
    print(line)
f.close()

#두 번쨰 방법 : readlines
f = open("새파일.txt", "r", encoding="UTF-8")
lines= f.readlines()
for line in lines :
    print(line)
f.close()

f = open("새파일.txt", "r", encoding="UTF-8")
lines= f.readlines()
for line in lines :
    print("첫 번쨰 줄입니다.\n")
f.close()

f = open("새파일.txt", "r", encoding="UTF-8")
lines= f.readlines()
for line in lines :
    print(line, end="")        #print(line, end="")=print(line.strip("\n"))
    #strip(a) : 문자열 끝의 a를 제거해주는 함수
    #print(line.strip("\n"),end="")에서 end는 한줄로 다나오게 하는 함수이다.
f.close()


#파일 쓰고 읽기 - (with open(파일명) as 파일변수) 사용하기 
with open("foo.txt", "w") as f:  #f 파일은 foo.txt이고 이친구를 롸이트 모드로 열어준다. 
#
    f.write("Life is too short, you need python")
    
#Immutable(정수,실수,문자열,튜플) vs Mutable(리스트, 딕셔너리, 집합)
#Immutable =변하지 않는 자료형
a=1
def vartest(a):
    a=a+1
    
vartest(a)
print(a)
#지역변수가 변한다고 해서 전역변수가 바뀌지 않음. 즉 함수를 벗어나면 변하지 않는다. 왜냐하면 print(a) 했을 떄 1출력되기 때문에

#Mutable = 변하는 자료형
b=[1,2,3] #리스트 
def vartest2(b): #b리스트에 대한 함수 vartest2는
    b=b.append(4) #b리스트에다가 4를 추가해준다. 
    
vartest2(b)
print(b)




    