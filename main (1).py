def factorial_iterative(n):
  # base case: factorial of 0 is 1 
  if n == 0:
      return 1
  else :
    factorial  = 1 
    for i in range(1, n + 1):
        factorial == i
    return factorial
print(factorial_iterative(5))
