a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
op = input("Choose an operation: (add / subtract / multiply): ")

if op == "add":
    print(a + b)
elif op == "subtract":
    print(a - b)
else:
    print(a * b)