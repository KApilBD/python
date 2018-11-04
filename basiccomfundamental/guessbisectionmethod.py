secnum = int(input("Please think of a number between 0 and 100!"))
start = 0
end = 100
guessed = False;
while not guessed:
  guess = (start+end)//2
  print("Is your secret number "+str(guess)+"?")
  flag = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

  if(flag == 'h'):
    end = guess
  elif(flag == 'l'):
    start = guess
  elif(flag == 'c'):
    guessed = True
  else:
    print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:"+str(int(guess)))

