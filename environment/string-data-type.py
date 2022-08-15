mystring=" this is a string"
print(mystring)
print(type(mystring))
print(mystring + " is of the data type" + str(type(mystring)))

friststring="water"
secondstring="fall"
thirdstring= friststring + secondstring
print(thirdstring)

name = input("what is your name ?")
print(name)

colour = input("what is your favourate colour?")
animal = input("what is your favourate animal?")
print("{}, you like a {} {}!".format(name,colour,animal))