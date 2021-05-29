import time
ip = int(input("Enter a no:"))
start = time.time()
def sum_even_odd(ip):
  sum_even = 0
  sum_odd = 0
  while ip > 0:
    rem = ip % 10
    ip = ip // 10
    if rem % 2 == 0 :
      sum_even = sum_even + rem
    elif rem % 2 != 0 :
      sum_odd = sum_odd + rem
  print("Sum of the Odd terms is :", sum_odd)
  print("Sum of the Even terms is :", sum_even)
end = time.time()
print(sum_even_odd(ip))
print("Runtime : ", end - start)
