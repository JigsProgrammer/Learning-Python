
#integer (int) tutorial; returns a value
first = input("First: ")
second = input("Second: ")
sum = int(first) + int(second)
print(sum)

#now with float; decimal
first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum is " + str(sum))

    #another way to write this previous one is
first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum is " + str(sum)) #string is those within ""