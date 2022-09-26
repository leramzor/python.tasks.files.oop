import math
class Shape:
    def __init__(self, side_a):
        self.side_a=side_a
    def perimetr(self):
        return self.side_a+self.side_a
    def area(self):
        return self.side*self.side_a
class Rectangle(Shape):
    def __init__(self,side_a, side_b):
        super(Rectangle,self).__init__(side_a)
        #Shape.__init__(side_a)
        self.side_b=side_b
    def perimetr(self):
        return (self.side_a+self.side_b)*2
    def area(self):
        return self.side_a*self.side_b
recTangleArea=Rectangle(5,2).area()
recTanglePerimetr=Rectangle(5,2).perimetr()
print(recTangleArea)
print(recTanglePerimetr)  