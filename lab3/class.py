#1 get_string
class get_String:
    def __init__(self):
        self.string=''
    def getstr(self):
        self.string=str(input())
    def printup(self):
        print(self.string.upper())

ans=get_String()
ans.getstr()
ans.printup() 

#2 shape,square
class shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class square(shape):
    def __init__(self, side_length):
        super().__init__
        self.side_length = side_length
        
    def area(self):
        return self.side_length*self.side_length
    
square = square(5)
print(square.area())
shape = shape()
print(shape.area())

#3 rectangle
class rectangle(shape):
    def __init__(self, length, width):
        super().__init__
        self.length = length
        self.width = width
    def area (self):
        return(self.length * self.width)

rectangle = rectangle(5, 4)
print(rectangle.area())
shape=shape()
print(shape.area())

#4 point
import math
class Point:
    def __init__(self, x, y, movedx, movedy):
        self.x = x
        self.y = y
        self.movedx = movedx
        self.movedy = movedy  
    def show(self):
        return( self.x, self.y)
    def move(self):
        self.movedx = self.movedx + self.x
        self.movedy = self.movedy + self.y
        return(self.movedx,self.movedy)
    def dist(self):
        return(math.sqrt((self.x - self.movedx)**2 + (self.y - self.movedy)**2))


point = Point(1, 2, 3, 3)
print(point.show())
print(point.move())
print(point.dist())
        
#5 bank_account     
class bank_account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def dep(self, amount):
        if(amount>=0):
             self.balance = self.balance + amount
             return(self.balance)
        else:
            return("amount is less than 0")
    def wd(self, amount):
        if amount>=0 and amount <=self.balance:
            self.balance=self.balance-amount
            return(self.balance)
        else:
            return("amount is greater than balance")
account = bank_account("Daniyar", 1000000)
print(account.dep(500000))
print(account.wd(800000))


#6 prime numbers
def prime_num(x):
    a=0
    if(x==0 or x==1):
        return False
    for i in range(2,x):
        if x%i==0:
            a=a+1
    if a==0:
        return True
    else:
        return False
        
list_nums = [int(s) for s in input().split()]
primes = list(filter(lambda x:prime_num(x), list_nums))
for i in range(len(primes)):
    print(primes[i], end=' ')

        
        
