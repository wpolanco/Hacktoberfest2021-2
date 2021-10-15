#Python Program to Check if a number is prime or not
def check_prime(n):    
  if n > 1:
    for i in range(2, n):
      if (n % i) == 0:           
          return True
          break
  else:
    return "Input number must be greater than 1"
n = int(input("Enter the number to check if it is Prime: "))
if check_prime(n):
  print(n, "is not a Prime Number.")
else:
  print(n, "is a Prime Number")
