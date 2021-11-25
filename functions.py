def is_even(n):
    if n%2==0:
        return True
    else:return False
    
#is_even(10)

def is_perfect(n):
    s=0
    for num in range(1,n//2+1):
        if n%num==0:
            s+=num
    if s==n:
        return True
    else:return False
    
    
def perfect_range(lw,up):
    for num in range(lw,up+1):
        if is_perfect(num):
            print(num,end=" ")
            
            
def is_palindrome(st):
    if st==st[::-1]:
        return True
    else:return False
    
