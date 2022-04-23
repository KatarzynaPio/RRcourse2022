# Ad 1

def Fibonacci(n):
    """Function returns nth Fibonacci number"""
   
    # Check if input is correct
    if n < 0:
        print("Incorrect input")
 
    # if n is 0 the fibonacci number is 0
    elif n == 0:
        return 0
 
    # if n is 1 or 2 the fibonacci number is 1
    elif n == 1 or n == 2:
        return 1
    
    # if n is greater than 2 fibonacci number is calucalted by recursion
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 

def largestFibNumber(n: int|float) -> int:
    """Return the largest Fibonacci number smaller than n"""
    i = 0 # first possible Fibonacci number

    # increment i until the Fibonacci number for i is greater than n
    while Fibonacci(i) < n : 
        i += 1
    return i-1 

# Ad 2
def reverse_digit(number: int) -> int:
    """Return number in the opposite order"""
    return int(str(number)[::-1]) # reverse digits in number converted to string

