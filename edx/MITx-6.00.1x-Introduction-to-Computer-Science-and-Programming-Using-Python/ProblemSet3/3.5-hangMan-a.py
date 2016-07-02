def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    import string
    alphabet = string.ascii_lowercase
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    print '-------------'
    count = 8
    getLetter = ''
    print 'You have ' + str(count) + 'guesses left.'
    print "Available letters: " + str(alphabet)
    getLetterList = ''
    while 0 <= count <=8:
        char = raw_input('Please guess a letter: ')
        lowerChar = char.lower()
        getLetter += lowerChar

        outString = getGuessedWord(secretWord, getLetter)
        leftLetters = getAvailableLetters(getLetter)
        result = isWordGuessed(char, secretWord)

        if result == True:
            if char in getLetterList:
                print 'Oops! You\'ve already guessed that letter: ' + outString
            else:
                print 'Good guess: ' + outString
                getLetterList += getLetter
            print '-------------'

            if outString == secretWord:
                print 'Congratulations, you won!'
                break

            print 'You have ' + str(count) + ' guesses left.'
            print 'Available letters: ' + getAvailableLetters(outString)
        else:
            if char in getLetterList:
                print 'Oops! You\'ve already guessed that letter: ' + outString
                print '-------------'
                print 'You have ' + str(count) + ' guesses left.'
                print 'Available letters: ' + leftLetters
            else:
                print 'Oops! That letter is not in my word: ' + outString
                getLetterList += getLetter
                print '-------------'
                if count != 1:
                    count -= 1
                    print 'You have ' + str(count) + ' guesses left.'
                    print 'Available letters: ' + leftLetters
                else:
                    print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
                    break
