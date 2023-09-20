# program to print 1 to 20 numbers in a pyramid usinf for loop
def number_pyramid(number):
    for i in range(1, number+1):
        for j in range(i):
            print(i , end=" ")
        print("\n")


print(number_pyramid(20))