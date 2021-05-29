import time
import math
print('''
         For Sum type 1  
         For Subtraction type 2
         For multiplication 3
         For quotient type 3
         For remainder type 4
         ''')
ip = int(input("Enter Yoour Selection:"))
start = time.time()
if ip == 1 :
  a = int(input("Enter 1st No. :"))
  b = int(input("Enter 2nd No. :"))
  sum = a+b
  print("Sum is :",sum)
elif ip == 2 :
  a = int(input("Enter 1st No. :"))
  b = int(input("Enter 2nd No. :"))
  diff = a - b
  print("Difference is :",diff)
elif ip == 3 :
  a = int(input("Enter 1st No. :"))
  b = int(input("Enter 2nd No. :"))
  mult = a * b
  print("Multiplication is :",diff)
elif ip == 4 :
  a = int(input("Enter 1st No. :"))
  b = int(input("Enter 2nd No. :"))
  quo = a % b
  print("Quotient is :",quo)
elif ip == 5 :
  a = int(input("Enter 1st No. :"))
  b = int(input("Enter 2nd No. :"))
  remain = a / b
  print("Remainder is :",remain)
else :
  print("Invalid Input")
end  = time.time()
print("Time taken:",end-start)
