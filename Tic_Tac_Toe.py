import sys

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
except (IndexError, ValueError):
    print("Please provide two valid numbers.")
    sys.exit(1)

result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")

