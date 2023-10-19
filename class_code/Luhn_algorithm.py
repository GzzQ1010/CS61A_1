def check_digits(n):
    digit=1
    while n >10:
        n//=10
        digit+=1
    if digit==16:
            return True
    else:
        return False

def coded_number(n):
     for i in range(16):
          last=n%10
          n//=10
          if i%2==0:
               last*=2
               if last>=10:
                    last= last%10+last//10
                
               