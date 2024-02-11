#1
def square_generator(N):
    for i in range(1,N+1):
        yield i**2

N = 6
square_gen = square_generator(N)

for i in square_gen:
    print(i,end=' ') 
    
#2
def even_generator(N):
    for i in range(0,N):
        if(i%2==0):
            yield i
          
N=int(input())
even_gen = even_generator(N)

for i in even_gen:
    print(i,end = ', ')
     
#3  
def generator(N):
    for i in range(0,N):
        if(i%3==0 and i%4 == 0):
            yield i

N = int(input())
gen = generator(N)
for i in gen:
    print(i,end=' ')
  
#4
def squaregen(ab):
    for i in range(ab[0],ab[1]+1):
        yield (i**2)   

ab = [int(i) for i in input().split()]
sq = squaregen(ab)
for square in sq:
    print(square,end = ' ')
 
#5
def generator(N):
    for i in range(N,-1,-1):
        yield i   

N = int(input())
gener = generator(N)
for i in gener:
    print(i,end=' ')






