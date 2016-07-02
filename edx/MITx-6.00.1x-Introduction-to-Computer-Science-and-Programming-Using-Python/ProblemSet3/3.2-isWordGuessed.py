def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    if lettersGuessed == []:
        return False

    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count +=1

    if count == len(secretWord):
        return True
    else:
        return False

isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
