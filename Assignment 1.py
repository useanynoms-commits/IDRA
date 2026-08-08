# Arithmetic Operations Program

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
else:
    division = "Undefined (division by zero)"
    floor_division = "Undefined (division by zero)"
    modulus = "Undefined (division by zero)"

exponentiation = num1 ** num2

print("\n" + "="*50)
print("ARITHMETIC OPERATIONS RESULTS")
print("")
print(f"First Number:  {num1}")
print(f"Second Number: {num2}")
print(f"Addition (+):              {addition}")
print(f"Subtraction (-):           {subtraction}")
print(f"Multiplication (*):        {multiplication}")
print(f"Division (/):              {division}")
print(f"Floor Division (//):       {floor_division}")
print(f"Modulus (%):               {modulus}")
print(f"Exponentiation (**):       {exponentiation}")
