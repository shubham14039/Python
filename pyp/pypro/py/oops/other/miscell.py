
# Coordinate clss
import math
class Coordinate:
    # Special dunder methods
    def __init__(self,x,y,z) -> None:
        self.x = x 
        self.y = y
        self.z = z
    
    @classmethod   
    def origin(cls) -> tuple:
        return (0,0,0)
    
    def distance(self, other):
        return math.sqrt(
            (other.x - self.x)**2 +
            (other.y - self.y)**2 +
            (other.z - self.z)**2
        )
    


# 2-Dimensional coordinate class 
class twoDcoordinate(Coordinate):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, z=0)
    
    @classmethod
    def origin(cls) -> tuple:
        return (0,0)

    

# Circle class
class circle(twoDcoordinate):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
    
    def radius(self,other):
        dist = self.distance(other)
        return round(dist,2)
    
    def area(self,other):
        radii = self.radius(other)
        ar = 3.14*(radii**2)
        return round(ar,2)
    
    def perimeter(self,other):
        per = 2*3.14*(self.radius(other))
        return round(per,2)
    
    def equation(self,other):
        var = "x²+y²"
        cons = (self.radius(other)**2)+((self.x)**2)+((self.y)**2)
        varconx, varcony = (self.x)*2, (self.y)*2
        return (f"The equation of circle with centre {(self.x,self.y)} is: {var+"+"+str(cons)+"-"+(str(varconx)+"x"+"-"+str(varcony)+"y")}")
        # The equation does not take the initial signs of the x and y coordinate of the circle. 


cir = circle(2,4)
pt = twoDcoordinate(6,7)
# print(circle.equation(cir,pt))
# print(cir)
print(type(Coordinate))





# pointa = twoDcoordinate(2,4)
# pointb = twoDcoordinate(6,7)
# pointc = twoDcoordinate(8,2)
# print(twoDcoordinate.area(pointa,pointb,pointc))
# print(twoDcoordinate.distance(pointb,pointa))
# print(coordinate.origin())
    