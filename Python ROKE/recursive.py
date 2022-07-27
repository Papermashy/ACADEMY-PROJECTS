
# A recursive function to get the factorial of a number
def fctrl(n):
    if n>1:
        return n*fctrl(n-1)
    else:
        return n

print (fctrl(5))