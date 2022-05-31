#ARGS AND KWARGS

#args
# def diff(*num):
#     sum = 0

#     for n in num:
#         sum = sum - n


#     print('Sum:', sum)    


# diff(-4, 2)    

#  OR

def adder (*num):

    sum = num[0] - num[1]
    print('diff:', sum)

adder(4,2)    

    #OR

def add(*numb):
    sum = 0

    for n in numb:
        sum = sum - n

    print('Sum:', sum)   #'Key:' , value  

add(3,9,6,10)    



#KWARGS

def intro(**data):
    print('\nData tyoe of argument:', type(data))
    
    for key, value in data.items():
        print('{} : {}'.format(key, value) )


intro(Firstname= 'Rhema', Lastname = 'Shama', Age= 14, Email= 'olamide@gmail.com')  
intro(Firstname= 'Mide', Lastname = 'Odoko', Age= 20, Email= 'mide@gmail.com')  

#CLASSES AND OBJECTS(Contd)

# class point():
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#         self.coords = (self.x,self.y)
#         print('first point')

#     def __add__(self,p): 
#         return point(self.x+p.x, self.y+p.y)   
#     def __sub__(self,p): 
#         return point(self.x-p.x, self.y-p.y)   
#     def __mul__(self,p): 
#         return point(self.x*p.x + self.y*p.y)   
#     def __gt__(self,p): 
#         return point(self.x>p.x , self.y>p.y)

#     def length(self): 
#         import math
#         return math.squt(self.x**2 + self.y**2)  

#     # def __it__(self, p)    
#     def __str__(self):
#         return "(" + str(self.x)  + '.' + str(self.y) + ')'  

# p1 = point(3,4)
# p2 = point(3,2)
# p3 = point(1,3)
# p4 = point(1,3)
# p5 = point(5,9)
# p6 = p3 + p4
# p7 = p3 - p4
# p8 = p3*p2


# print(p6)
# print(p7)
# print(p8)
# print(p6,p7,p8)
# print(p2 >p5)
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
        print("first point")
    def _add_(self, p):
        return Point(self.x+p.x, self.y+p.y)
    def _sub_(self, p):
        return Point(self.x-p.x, self.y-p.y)
    def _mul_(self, p):
        return Point(self.x*p.x + self.y*p.y)
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    def _gt_(self, p):
        # return (self.x > p.x , self.y>p.y)
        return self.length() > p.length()

    def _lt_(self, p):
        # return (self.x < p.x , self.y<p.y)
        return self.length() < p.length()
    def _le_(self, p):
        # return (self.x <= p.x , self.y<=p.y)
        return self.length() <= p.length()


    def _str_(self):
        return "(" + str(self.x) + '.' + str(self.y) + ')'
p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = p1 + p2
p6 = p3 - p1
p7 = p4*p3
print(p5, p6, p7)
print(p1 > p3)
print(p1 < p3)
print(p1 <= p2)


