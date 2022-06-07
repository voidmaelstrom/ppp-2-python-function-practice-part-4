# Find the maximum of three numbers.
def max_num(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest

# Test Run
res = max_num(2, 4, 7)
print("Largest Number: ", res)

# Multiply all the numbers in a list.
def mult_list(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total

# Test Run    
print(mult_list((10, 6, 5, -4, 7)))

# Reverse a string.
def rev_string(input_string):
  new_string = ''
  for character in input_string:
    new_string = character + new_string
  return new_string

# Test Run
print(rev_string(".tnaem I tahw si sihT"))

# Check whether a number falls in a given range.
def num_within(num, start_num, end_num):
    if num in range(start_num, end_num):
        return True
    else :
        return False

# Test Run
print(num_within(20, 15, 40))
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# Output Pascal's triangle
from math import factorial

def pascal(numRows):
  for i in range(numRows):
  # loop to get leading spaces
    for j in range(numRows-i+1):
      print(end=" ")
    # loop to get elements of row i
    for j in range(i+1):
      # nCr = n!/((n-r)!*r!)
      print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    # print each row in a new line
    print("\n")

# Test Run
pascal(3)
pascal(10)
