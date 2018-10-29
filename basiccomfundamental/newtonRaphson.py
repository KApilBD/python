

x = float(input("Enter any number: "))

epsilon = 0.1
guess = x/2.0

while abs(guess*guess-x) >= epsilon :
    guess = guess - (((guess**2)-x)/(2*guess)) #Newton-Raphson equation
    
print(str(guess) +" is square root of: "+ str(x))