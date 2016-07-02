def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    import string
    alphabet = string.ascii_lowercase
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in alphabet:
            alphabet = alphabet.replace(lettersGuessed[i], "")
    return alphabet

getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
