x = int(input("Give an integer x: "))
y = int(input("Give an integer y: "))
z = int(input("Give an integer z: "))

if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    if x < z and y < z:
        print("z is the largest odd integer!")
    elif x < y:
        print("y is the largest odd integer!")
    else:
        print("x is the largest odd integer!")

elif x % 2 != 0 and y % 2 != 0:
    if x < y:
        print("y is the largest odd integer!")
    else:
        print("x is the largest odd integer!")
    print("z is an even integer")

elif y % 2 != 0 and z % 2 != 0:
    if y < z:
        print("z is the largest odd integer!")
    else:
        print("y is the largest odd integer!")
    print("x is an even integer")

elif x % 2 != 0 and z % 2 != 0:
    if x < z:
        print("z is the largest odd integer!")
    else:
        print("x is the largest odd integer!")
    print("y is an even integer")

elif x % 2 != 0 and (y % 2 == 0 and z % 2 == 0):
    print("Only x is an odd integer! The other two numbers are even!!")

elif y % 2 != 0 and (x % 2 == 0 and z % 2 == 0):
    print("Only y is an odd integer! The other two numbers are even!!")

elif z % 2 != 0 and (x % 2 == 0 and y % 2 == 0):
    print("Only z is an odd integer! The other two numbers are even!!")

else:
    print("All the numbers are even!")
