#ChatGPT_ComplexNos Algorithm
#Created by Cephas Cardozo

#Functions_Defined
def add_complex(a, b):
    return a + b

def subtract_complex(a, b):
    return a - b

def multiply_complex(a, b):
    return a * b

def divide_complex(a, b):
    return a / b

def get_complex_number_from_input():
    real_part = float(input("Enter the real part of the complex number: "))
    imaginary_part = float(input("Enter the imaginary part of the complex number: "))
    return complex(real_part, imaginary_part)

#Conditionals
if __name__ == "__main__":
    print("Enter the first complex number:")
    complex_num1 = get_complex_number_from_input()

    print("\nEnter the second complex number:")
    complex_num2 = get_complex_number_from_input()
    print("\nPerforming operations on complex numbers:")

    # Addition
    result_add = add_complex(complex_num1, complex_num2)
    print(f"Addition: {result_add}")

    # Subtraction
    result_subtract = subtract_complex(complex_num1, complex_num2)
    print(f"Subtraction: {result_subtract}")

    # Multiplication
    result_multiply = multiply_complex(complex_num1, complex_num2)
    print(f"Multiplication: {result_multiply}")
