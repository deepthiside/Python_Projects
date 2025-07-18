from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-": subtract,
    "*" : multiply,
    "/": division,
}
def calculator():


    first_number= float(input("Enter the First Number: "))
    should_accumulate = True
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        ask_operation= input("Enter the operation: ")
        second_operation= float(input("Enter the Second Number: "))
        answer = (operations[ask_operation](first_number,second_operation))
        print(f"{first_number} {ask_operation} {second_operation} = {answer} ")
        again = input(" type y if you want to continue with previous result or start a new calculation: ")
        if again == "y":
            first_number = answer
        else:
            should_accumulate = True
            print("\n"*20)
            print(logo)
            calculator()

calculator()