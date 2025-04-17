

class Animal(object):
    def __init__(self,age) -> None:
        self._years = age
        self._name = None
    
    def get_age(self):
        return self._years
    def get_name(self):
        return self._name
    
    def set_age(self,new_age):
        self._years = new_age
    def set_name(self, new_name = ""):
        self._name = new_name
        
    def __str__(self) -> str:
        return "Animal:"+str(self._name)+":"+str(self._years)


rabbit = Animal(90)
rabbit.set_name("shubham")
print(rabbit)