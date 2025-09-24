
def add_or_subtract(a, b, o):
    """
    adds or subtracts numbers
    """
    if o == "add":
        return a + b
    else:
        return a - b
def multiply(a,b):
    """
    multiplies numbers
    """
    return_value = 0
    i = 0
    while i < b:
        return_value = return_value + a
        i = i + 1
    return return_value
def divide(a,b):
    """
    divides numbers
    """
    return a/b
def power(a,b):
    """
    powers numbers
    """
    return a ** b
def main():
    # get the input
    o = input("Choose an operation: (add / subtract / multiply / divide / off): ")
    # loop until user inputs 'off'
    while o != "off":
        # get first number
        a = int(input("Enter first number: "))
        # get second number
        b = int(input("Enter second number: "))
        # if input was add then add
        if o == "add":
            # add the numbers and print result
            print(add_or_subtract(a,b,o))
        # if input was subtract then subtract
        elif o == "subtract":
            # subtract the numbers and print result
            print(add_or_subtract(a,b,o))
        # if input was multiply then multiply
        elif o == "multiply":
            print(multiply(a,b))
            # multiply the values and print the result
        # if user put in divide then divide the numbers
        elif o == "divide":
            print(divide(a,b)) # divide the input and output return value
        # turn off when user inputs off
        elif o == "off":
            return # exit
        o = input("pick an function: (add / subtract / multiply / divide / off): ") # check if user wants to do another operation
if __name__=="__main__":
    main()