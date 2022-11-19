a=1 #a라는 변수 안에 오른쪽을 집어넣는다.
b=1

print(type(a))
#출력한다. a의 type을
#4.24e10은 4.24 * 10의 10승을 의미한다.

print(a/b) #나눈 결과값이 그대로 나오고
print(a//b)
#나눴을 때의 몫이 출력됨

#문자열

a="Hello world"
a="Python's favorite food is Perl "
print(type(a))

#줄 바꾸고 싶을 때는 백슬래쉬+n을 쳐야한다. 파이썬은 한줄씩만 인식하기 때문에 줄바꿈을 그냥 하게 되면 인식을 못함

b = 'life is too short \n You need python!'
print(b)

a="python"
b = "is fun!"
print(a*100)
/*a=python을 100번 출력하게 됨. 문자열에 곱하고 더하기가 가능하다.*/
print(a+b)
/*python is fun! 이 출력되게 됨*/

#문자열 처리 해주기 
#인덱싱(문자열 순서대로 출력하자.)
a="Life is too short, you need python"
print(a[0])   /*L이 출력됨. a[0]은 맨 첫번째 문자열이다.*/

print(a[-1]) 
# o가 출력된다. -가 붙으면 뒤에서부터 출력되는 것 

#슬라이싱(최대와 최소값을 설정간격대로 잘라서 원하는 범위만 출력해주자 )
c="12345678"
print(c[::2]) #[이상 : 미만 : 간격]
#위의 c[::2]에서는 이상값과 미만값이 정해지지 않고 간격만 나왔으니까 1357이 출력되게 된다.
print(c[:8:])
#8미만의 모든 값들을 출력하자
#print(c[:-1:])뒤에서 첫번째 값 미만의 모든 것들을 출력하게 되면 1~7까지의 값이 동일하게 출력됨

number = 10
day= "three"
a="I ate %s apples. so I was sick for %s days." %(1.2, day)

print(a)

#정렬과 공백 
a="%10s % hi"
print(a) #          hi가 출력된다. 앞에 있는 %s 10개만큼이 띄어진채로 출력됨 
a="%-10sjane % 'hi'"
print(a)     #hi            jane이 출력된다. 

#비슷하게 임의로 값을 주는 것중에서 format함수가 있는데, 이 format은 변수의 오른쪽 값에 사용한다. 

a="My age is {age}, My name is {name}".format(name="solarthenomad", age=3)
#다른 방식으로 format 함수를 축약해서 쓰면 f가 된다.
name="int"
a=f"나의 이름은 {name}입니다."
print(a)
a.lower() #모두 소문자로 바꾸기
a.upper() #모두 대문자로 바꾸기 
print(a[0].islower())
#islower, isupper은 이게 과연 대문자인지 소문자인지 true or false로 답변이 되는 것 
print(len(a)) #길이를 출력해주기 
print(a.replace("My age", "My sister")) #My age를 My sister로 바꿔줌 
index = a.index("n")
#n이 a에서 어느 위치에 있는지 확인이 가능함
index = a.index("n", index+1)
print(index)



#양쪽 공백지우기
a.strip()



#%d : 정수 %f : 실수 %s : 문자열(다 사용가능) 이 세개만 사용되니까 이 세개만 외워놓자

#소수점 계산할 때 너무 끝까지 많이 나오면 보기가 꺼려짐 그래서 몇번째 자리수까지만 남겨두고 자른다는 게 필요한데 이때 쓸수있는게 '간격'

d= "%0.4f" % 3.42134234
#%0.4f에서 0은 간격이고 4는 소수점 남기는 자리수이다.
#3.4213이 출력되게 되는데 이때 저 위의 말을 해석해보면 3.42134234의 0.4f만큼이 d이다
print(d)

#함수는 어떤 틀정한 일을 하는 명령어들을 묶어놓은 것이다.

#유용한 명령어들 : count,find, join
a="hobby"
print(a.count('b')) /*.은 ~의라는 뜻으로 'a의 b개수를 세라라는 의미임'*/
print(a.find('b'))/*처음으로 발견된 b의 인덱스 */
find = print(a.find('b'))
find = a.find("b", find+1)/*b의 인덱스 이후 다음 발견된 이후 처음 발견된 b의 인덱스 */

a=",".join("abcd")
print(a)

