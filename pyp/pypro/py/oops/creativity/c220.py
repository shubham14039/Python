# Write a python program that inputs a polynomial in standard algebraic notation and outputs the first derivative of that polynomial

class Derivative:
    def __init__(self, polynomial) -> None:
        self._equation = polynomial
        
    def __str__(self) -> str:
        return f"The given polynomial is: {self._equation} "


x = Derivative("r**2")
print(x)