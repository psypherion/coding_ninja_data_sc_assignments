import time
ip = int(input("Enter a no:"))
start = time.time()
def palindrome(ip):
  t = ip
  rev_num = 0
  while ip > 0:
    rem = ip%10
    rev_num = (rev_num*10) + rem
    ip = ip//10
  if rev_num == t :
    return "Palindrome Number"
  else :
    return "Not a palinrome."
print(palindrome(ip))
end = time.time()
print("Runtime : ", end - start)
