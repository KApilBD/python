

def isPalindrom(x):
    def toString(x):
        x=x.lower()
        ans = ''
        for c in x:
            if c in "qwertyuioplkjhgfdsazxcvbnm":
                ans = ans + c
        return ans
    
    def isPal(x):
        if len(x)<=1:
            return True
        else:
            return x[0]==x[-1] and isPal(x[1:-1])
    return isPal(toString(x))

print(isPalindrom("edvE e,v de"))