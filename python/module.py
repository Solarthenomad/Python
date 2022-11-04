#모듈
#미리 만들어 놓은 .py파일(함수, 클래스, 변수 모두 포함)
#형식 : from 모듈이름 import 모듈안에 포함된 함수나 클래스 

from distutils.command.build_scripts import first_line_re


class Calculator(self, first, second):
    def __init__(self, first, second) :
        self.first = first
        self.second = second 
    def dataset(self, first, second):
        self. first = first
        self.second = second
    def add(self):
        result = self.first +self.second 
        return result
    def sub(self):
        result =self.first -self.second
        return result
##__어쩌구__는 특별한 함수들임
#__name__ == "__main__"은 파일의 name이 main일 때만 아래의 코드들이 실행된다. 
if __name__ == "__main__":
    print(add(1,4))
    print(add(4,2))
