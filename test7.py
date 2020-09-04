# Python program to print prime factors
import math
# prime
def func():
   n = input("Input a number: ")
   n = int(n)
   # no of even divisibility
   while n % 2 == 0:
      print (2),
      n = n / 2
   # n reduces to become odd
   for i in range(3,int(math.sqrt(n))+1,2):
      # while i divides n
      while n % i== 0:
         print (i)
         n = n / i
   # if n is a prime
   if n > 2:
      print (n)

if __name__ == "__main__":
    func();