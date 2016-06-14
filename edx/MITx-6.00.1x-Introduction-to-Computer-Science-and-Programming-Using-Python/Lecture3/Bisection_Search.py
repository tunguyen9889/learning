print "Please think of a number between 0 and 100!"
low = 0
high = 100
guessed = False

while not guessed:
    secret = (low + high)/2
    print "Is your secret number " + str(secret) + "?"

    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if ans == 'h':
        high = secret
    elif ans == 'l':
        low = secret
    elif ans == 'c':
        print "Game over. Your secret number was: " + str(secret)
        break
    else:
        print "Sorry, I did not understand your input."
