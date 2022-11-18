# Function needed add, subtract,multiply and division
# Print options to the user
# Ask for value
# Call the functions
# Loop until the user exits

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")


def subtract(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")


def multiply(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")


def division(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")


while True:
    print("A , Addition")
    print("B , Subtraction")
    print("C , Multiplication")
    print("D , Division")
    print("E , Exit")

    choice = input('Input Your Choice: ')

    if choice == "A" or choice == "a":
        print('Addition')
        a = int(input('Please input first number: '))
        b = int(input('Please input second number: '))
        add(a, b)

    elif choice == "B" or choice == "b":
        print('Subtraction')
        a = int(input('Please input first number: '))
        b = int(input('Please input second number: '))
        subtract(a, b)

    elif choice == "C" or choice == "c":
        print('Multiplication')
        a = int(input('Please input first number: '))
        b = int(input('Please input second number: '))
        multiply(a, b)

    elif choice == "D" or choice == "d":
        print('Division')
        a = int(input('Please input first number: '))
        b = int(input('Please input second number: '))
        division(a, b)

    elif choice == "E" or choice == "e":
        print('Program ended')
        quit()
