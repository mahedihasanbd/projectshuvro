#####Calculator######
#1. ADD
#2. Subtract
#3. Multiply
#4. Divide

print("Select an operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("1. MULTIPLY")
print("1. DIVIDE")
operation = input()
if operation == "1":
    numb1 = input("enter the first number")
    numb2 = input("enter the second  number")
    print("The sum is" + str(int(numb1) + int(numb2)))
elif operation == "2":
    numb1 = input("enter the first number")
    numb2 = input("enter the second  number")
    print("The sum is" + str(int(numb1) - int(numb2)))
elif operation == "3":
    numb1 = input("enter the first number")
    numb2 = input("enter the second  number")
    print("The sum is" + str(input(numb1) * int(numb2)))
elif operation == "4":
    numb1 = input("enter the first number")
    numb2 = input("enter the second  number")
    print("The sum is" + str(int(numb1) / int(numb2)))
else:
    print("invalid entry")

