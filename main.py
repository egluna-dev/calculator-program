from art import logo

# sum function
def add(n1, n2):
  return n1 + n2

# Subtraction function
def subtract(n1, n2):
  return n1 - n2

# Multiplication function
def multiply(n1, n2):
  return n1 * n2

# Division function
def divide(n1, n2):
  return n1 / n2

operations_dictionary = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?\n"))
      
  for symbol in operations_dictionary:
    print(symbol)
  
  program_on = True
  
  while program_on:
    operation_symbol = input("Please pick an operation from the line above:\n")
    operation_selected = operations_dictionary[operation_symbol]
    num2 = float(input("What is the next number?\n"))
    answer = operation_selected(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}\n")
  
    continue_program = input("Please type 'y' to continue calculation or 'n' to start a new calculation.\n")
  
    if continue_program == "y":
      num1 = answer
    elif continue_program == "n":
      program_on = False
      calculator()

calculator()
    
  