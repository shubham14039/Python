# Write a python program that inputs a polynomial in standard algebraic notation and outputs the first derivative of the polynomial

class Polynomial: 
    def __init__(self, equation) -> None:
        '''
        Initialize the polynomial in the form of a list.
        For example:
        3x°5 + 4x°4 + 6x°3 + 7x°2 + 8x is represented as:
        [[3,5],[4,4],[6,3],[7,2],[8,1]]
        And we dont have to write the constant values (Those doesnt matter anyways)
        '''
        self._equation = equation
    
    def __str__(self) -> str:
        '''
        Returns the actual polynomial in the form of a list
        '''
        return f"The polynomial is: {self._equation}"
    
    def list_of_derivatives(self):
        '''
        Returns the derivative of the polynomial.
        '''
        for i in self._equation:
            i[0] = i[0]*i[1]
            i[1] = i[1]-1
        return self._equation
        
    def derivative(self):
        '''
        Returns a function in its original form
        '''
        list = []
        result = self.list_of_derivatives()
        for i in result:
            list.append(f"{i[0]}x°{i[1]}")
        return (f"The first derivative of the polynomial is: {" + ".join(list)}")
            



pol = Polynomial([[3,5],[4,4],[6,3],[7,2],[8,1]])
print(pol.derivative())

