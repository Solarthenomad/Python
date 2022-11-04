from hello import add

add(1,2)
add(3,4)

#근데 내가 찾을 모듈이 같은 폴더 안에 없으면 어떡하지? 다른 폴더에 있는 모듈을 가져올 때는 import sys를 쓴다. 
import sys
sys.path.append("C:\\python")
import dictionary
##import sys

##sys.path.append("내가 찾을 파일이 속한 폴더")
##import 내가 찾을 파일
#import 