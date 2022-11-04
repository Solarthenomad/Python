#mod1 py module
class Cal(self,first,second):
    def __init__(self, first,second) :
        self.first = first
        self.second = second
    def dataset(self, first,second):
        self.first = first
        self.second =second
    def add(self):
        result = self.first+self.second
        return result
    
if __name__=="__main__":
    print(add(1,2))
    print(add(5,8))