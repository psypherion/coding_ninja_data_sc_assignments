ip = int(input("Enter a no:"))
rev_num = 0
while ip > 0:
  rem = ip%10
  rev_num = (rev_num*10) + rem
  ip = ip//10
print(rev_num)
