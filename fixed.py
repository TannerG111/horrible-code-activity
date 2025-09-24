def add(num1,num2):
    """
    Returns the addition of num1 and num2
    :param num1: first number
    :param num2: second number
    :return: The result of the addition of num1 and num2
    """
    return num1+num2

def subtract(num1,num2):
    """
    Returns the subtraction of num1 and num2
    :param num1: first number
    :param num2: second number
    :return: The result of the subtraction of num2 from num1
    """
    return num1-num2

def multiply(num1,num2):
    """
    Returns the multiplication of num1 and num2
    :param num1: first number
    :param num2: second number
    :return: The result of num1 multiplied by num2
    """
    return num1*num2

def divide(num1,num2):
    """
    Returns the division of num1 and num2
    :param num1: first number
    :param num2: second number
    :return: The result of num1 divided by num2
    """
    return num1/num2

def main():
    operation = input("Choose an operation: (add / subtract / multiply / divide / off): ")
    while operation != "off":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if operation == "add":
            print(add(num1,num2))
        elif operation == "subtract":
            print(subtract(num1,num2))
        elif operation == "multiply":
            print(multiply(num1,num2))
        elif operation == "divide":
            print(divide(num1,num2))
        elif operation == "off":
            return
        operation = input("Choose an operation: (add / subtract / multiply / divide / off): ")



if __name__=="__main__":
    main()