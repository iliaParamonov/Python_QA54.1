def run():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        operator = input("Enter Action operator (+,-,*,/): ")
        result = pars(a, b, operator)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except ZeroDivisionError:
        print("Cannot divide by zero")

run()