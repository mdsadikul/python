from abc import ABC, abstractmethod

class Father(ABC):
    n1=200
    n2=300

    @abstractmethod
    def add (self):
        print(self.n2+self.n1)

    def sub (self):
        print(self.n2-self.n1)


#Child class MUST redefine the method
class son(Father):
    def add (self):
        print(self.n2+self.n1)

obj = son()

obj.add()
obj.sub()