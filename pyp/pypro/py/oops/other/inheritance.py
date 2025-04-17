class Animal:
    def __init__(self, age) -> None:
        self._years = age
        self._name = None
    
    
    def __str__(self) -> str:
        return "animal:" + str(self._name) + ":" + str(self._years)
# Implemeanting getttrs and setters:
    # Getters are very simple methods that return the data attributes
    # So question is why to use getters when we can acess the data attributes direcly - One reason behind this approach is "Encapsulation". Encapsulation is one of the core principles of python classes, which means keeping the internal details of an object hidden and contrilling acess to them. 
    
      
    def get_age(self):
        return self._years
    
    def get_name(self):
        return self._name
    
    # Setters are methods that set the data attributes
    # Setters does not return anything, they just assign a new value

 



myanimal = Animal(9)

print(myanimal.get_age())


# print(myanimal.get_age) 
# # This will return something like this: <bound method Animal.get_age of <__main__.Animal object at 0x10029db80>>  and this means that we are dealing with bound methods. Bound methods in python are methods accociated with instance to a class, and we are getting this because it has not been called yet. To call it we have to include parenthesis "()" at the end of the methods we are calling 