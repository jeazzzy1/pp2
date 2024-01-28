#example 1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#example 2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#example 3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#example 4
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#example 5
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

