
#def fiboo(a=10):
i = 0
first = 1
second = 1
while i < 10 :
  if i<=1:
     fib = 1
  else:
     fib = first + second
     first = second
     second = fib
  i +=1
  print(fib)
    
    
  
#Recursive
  
def fibbo(x):
    if x == 0 or x==1:
        return 1
    return fibbo(x-1)+fibbo(x-2)

i=0 
while i<10:
    print(fibbo(i))
    i+=1
