
def calculate(expression):
    """Evaluate math expression safely"""
    try:
        # Replace × and ÷ with * and /
        expression = expression.replace("×", "*").replace("÷", "/")
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except:
        return " Invalid expression!"

def main():
    print("=== Dynamic Calculator ===")
    print("Use +  -  *  /  and ( ) in expressions")
    print("You can also use × and ÷")
    print("Type 'exit' to quit\n")

    while True:
        expr = input("Enter expression: ")

        if expr.lower() == "exit":
            print("Calculator closed.")
            break

        print("Result =", calculate(expr), "\n")

# Run program
if __name__ == "__main__":
    main()
