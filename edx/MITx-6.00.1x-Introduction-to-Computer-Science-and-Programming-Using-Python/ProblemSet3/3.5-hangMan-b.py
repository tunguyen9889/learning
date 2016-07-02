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
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(
        len(secretWord)) + ' letters long'
    getLetter = ''
    count = 8
    guessedLetters = ''

    while count > 0:
        print '-----------'
        if isWordGuessed(secretWord, getLetter):
            print 'Congratulations, you won!'
            break
        print 'You have ' + str(count) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(getLetter)

        char = raw_input('Please guess a letter: ')
        loChar = char.lower()

        getLetter += loChar
        outString = getGuessedWord(secretWord, getLetter)

        # if the letters are guessed
        if loChar in secretWord:
            if loChar in guessedLetters:  # output to remind repeat input
                print 'Oops! You\'ve already guessed that letter: ' + outString
            else:
                print 'Good guess: ' + outString  # keep the count is not changed

        # if the letters are not guessed
        else:
            if loChar in guessedLetters:
                print 'Oops! You\'ve already guessed that letter: ' + outString
            else:
                print 'Oops! That letter is not in my word: ' + outString
                count -= 1  # record the count as minus one

        guessedLetters += loChar
    if count == 0:
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
