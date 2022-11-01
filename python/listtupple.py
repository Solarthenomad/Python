# 파이썬 리스트를 사용하기 전(불편한 점 위주로 파악하기)
a="python"
b="javascript"
c="c++"
d="html/css"
e="java"

print(e)
#하나의 변수를 출력하려면 일일이 다 처야하는 번거로움이 있음 => 하나의 변수 안에 내가 넣고 싶은 것들을 다 넣으면?

a = ["python", "javascript", "c++", "html/css", "java"]
a = [1,2,"life", "too"]  #숫자 변수랑 문자 변수 같이 써도 됨
a=[1,2, "life", [3,4,"life", "is"]]  #리스트 안에 리스트 넣어도됨

print(a[3]) #[3,4,"life","is"]가 출력된다.
print(a[3][2]) #life가 출력된다.
#4번째 변수의 3번째 변수를 꺼내서 출력한다.
print(a[-1]) #[3,4,"life", "is"]가 출력된다.
print(a[-2]) #"life"가 출력된다.

a = [1,2,3]
b = [4,5,6]
print(a+b)   #1,2,3,4,5,6이 출력된다.
print(a*10)   #1,2,3 10번 출력

a=["박주하", "잠수", "수강신청 노노", "코딩공부"]
a[0] = "한재성"

print(a) #한재성이 출력된다.
a[0:2] = ["앵무새","퍼랭이"]#리스트 변수 a의 0번째부터 1번째까지의 변수를 위의 것으로 바꿔주기

print(a) #앵무새, 퍼랭이, 수강신청 노노, 코딩공부가 출력된다.
#리스트 삭제하기 
a[0:2] = []   #a의 0~1번째 변수를 삭제한다. 
del a[0] #a의 0번째 변수를 삭제한다.
#리스트에 변수 추가하기
a.append("시우버") #시우버를 리스트의 맨끝 원소로 추가해주기 
#알파벳순, 가나다순, 123 순으로 자동정렬해주기 
a.sort() 
a.reverse()
a.index(3) #a의 4번째 변수를 불러오기. 즉 a[3]과 똑같음 
a.insert(0,4) #0번째 인덱스에 4라는 변수를 추가해라 
a.remove("앵무새") #앵무새라는 값의 변수를 삭제해라

a=[1,5,3,1,1]
a.extend([2,3]) #a 변수에 2,3이라는 값을 뒤에 추가해라 
print(a) #1,5,3,1,1,2,3이 출력된다. 

#tupple
#tupple의 길이와 key에 해당되는 vlaue가 정해져 있음 - 삭제 추가 value, key의 값 변동 불가능 
#인덱싱이랑 슬라이싱만 가능하다

tupple = (1,2,'a', 'b')
print(tupple[0])   #1이 출력된다.
print(tupple[3])   #b가 출력된다. (인덱싱)

print(tupple[0:2]) #1,2,a가 출력된다. (슬라이싱)

#tupple끼리 합치기 
t1 = (1,2,'a', 'b')
t2 = (3,4)
print(t1 + t2)
print(t1 *3)
print(t1[0] + 1)
