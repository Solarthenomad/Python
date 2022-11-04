#dictionary : AI에서 자주 사용됨 
#다음은 한 사람에 관한 정보를 갖는 json 객체이다. 키-값 쌍의 패턴으로 표현된다. 
"""{
    "이름" : "홍길동",
    "나이" : 25,
    "성별" : "여",
    "주소" : "서울특별시 양천구 목동",
    "가족관계"}"""
    
    #key를 통해 value를 얻는다. 
    #연관 배열 또는 해쉬
    
dictionary = {'name' : 'Eric', 'age' : '15'}

print(dictionary['name']) #딕셔너리의 이름이 dictionary인 것의 key name의 value를 출력 해서 Eric이 출력됨 

a= {1 : 'a'}
a['name'] = "익명" #a 딕셔너리에 key가 name이고 value가 익명인 원소를 추가해줌

print(a)
#{1: 'a', 'name' : '익명'}이 출력된다. 


grade = {'pay' : 10, 'juliet' : 99}
print(grade['pay'])  #10이 출력되게 된다. key의 value를 출력해달라는 것
print(grade['juliet']) #99출력

a={1:'파랑구름', 2:'이현준', 3: '민MIN준JUN'}
#key값만을 뽑아내기 
print(a.keys()) #.은 ~의라는 뜻으로 a의 keys를 print해준다는 의미 
print(a.values()) #.은 ~의라는 뜻으로 a의 values를 프린트해준다는 의미 
print(a.items()) #key와 value 모두 출력하자

for k in a.keys() :
    print(k) #a의 key값들의 임의의 k원소들을 출력하라 
    #1,2,3출력

for k in a.values() :
    print(k) #a의 value값들의 임의의 k 원소들을 출력하라 
    #파랑구름, 이현준 , 민MIN준JUN 출력 

for k,v in a.items() :
    print("키는: " + str(k))
    print("밸류는" : v)
    
print(a[4])
#이렇게 하면 error만 뜨고 
print(a.get(4))
#이렇게 하면 none이 뜨게 되는데 이런 get함수의 성질을 이용해서 default 지정까지 가능하다.
print(a.get(4,'없음'))
#

print(1 in a) #a안에 1이라는 key가 있냐 없냐 즉 참과 거짓 결과값을 표현해줌

#집합 자료형
#중복을 허용하지 않으며 순서가 없다. (인덱싱 ㄴㄴ)
set = set([1,2,3])  #set라는 변수 안에 12,3이라는 원소를 저장한다. 
print(set) #1,2,3출력
print(type(set))

1=[1,2,2,3,3]
newList = list(set(1))

