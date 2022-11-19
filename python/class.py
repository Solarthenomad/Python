#class = 반복되는 변수나 메서드(함수)를 미리 설계해놓은 틀
#클래스가 필요한 이유
from distutils.command.build_scripts import first_line_re
from pickletools import read_uint1
from readline import set_completion_display_matches_hook


result = 0
def add(num):
    global result
    result += num   # result = result + num
                    # result-= result - num
                    # result *= result *num
    return result
print(add(3))
print(add(4))
#3,7이 나오면 왜냐면 result가 위에서 0으로 초기값 설정된게 global result로 선언되서 add로 넘어와서 3이 나온뒤 result =3 + number4를 더했으니까 7이 됨
#각각 하려면 각각 변수를 선언하고 각각 return을 해주어야 함...겁나 번거로워짐 
result = 0
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result1 += num
    return result2

#class 명은 맨 앞에 문자를 대문자로 써야함
#class의 구조
class Calculator:
    def __init__(self) : #def __init__(self)는 함수의 변수의 초기값을 설정해주는 역할을 한다. 
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cla2 = Calculator()

print(cal1.add(3))   #cal1의 add함수에 3을 넣었을 때의 결과물을 출력해라 
print(cal2.add(4))   #cal2의 add함수에 4을 넣었을 때의 결과물을 출력해라 

class FourCal:
    pass #아무것도 안한다는 것 

a = FourCal()
print(a)
#걍 a만 나옴 

class FourCal:
    def __init__(self,first, second):
        self.first = first 
        self.second = second
        #변수 초기값을 class에서 설정해준다. 
        
    def setdata(self, first, second): #setdata 인자 즉 객체 
        self.first = first #a의 first 변수 = first
        self.second = second #a의 second 변수 = second
        
        def add(self): #아래에서 a.add이므로 a를 그대로 받아서 사용함 a= self but b.add이면 b를 받아서 사용하게 됨
            result = self.first + self.second
            return result
        
class MoreFourCal(FourCal):
    pass  #MoreFourCal이라는 클래스가 FourCla의 클래스의 함수들을 그대로 상속받는 것


#a 변수에 함수 적용하기 
a = FourCal(1,2) #a라는 객체가 위의 클래스를 쓰겠다고 말하기 
a.setdata(1,2)   #변수.클래스의 쓰고 싶은 함수(인자1,인자2,인자3...)
print(a.first)
print(a.second)
print(a.add())

a=MoreFourCal(4,2)
print(a.add()) #MoreFourCal의 add함수를 활용하는 것

#Calculator 최종으로 만들기 (사칙연산)

from math import math

class FourCal() :
    def __init__(self,first,second) :
        self.first = first
        self.second = second
    def setdata(self, first, second) :
        self.first=first
        self.second=second
    
    def add(self):
        result = self.first+self.second
        return result #return something은 
    def min(self):
        result = self.first -self.second
        return result
    def mul(self):
        result = self.first *self.second
        return result
    def sub(self):
        result = self.first /self.second
    

    