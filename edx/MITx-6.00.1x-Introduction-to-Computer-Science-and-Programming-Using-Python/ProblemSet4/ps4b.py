from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#


def isValidWordInHand(word, hand):
    """
    Returns True if word is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)

    """
    flag = True
    handCopy = hand.copy()
    for letter in word:
        if letter in handCopy:
            handCopy[letter] -= 1
        else:
            return False
    for i in handCopy.values():
        if i < 0:
            flag = False
    return flag


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    score = 0
    maxScore = 0

    bestWord = None
    for word in wordList:
        if isValidWordInHand(word, hand) == True:
            score = getWordScore(word, n)
            if score > maxScore:
                maxScore = score
                bestWord = word
    return bestWord


def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total = 0
    handCopy = hand.copy()
    bestWord = compChooseWord(handCopy, wordList, n)
    while bestWord != None:
        print 'Current Hand: ',
        displayHand(handCopy)
        total += getWordScore(bestWord, n)
        print '\"' + bestWord + '\" earned ' + \
              str(getWordScore(bestWord, n)) + ' points. Total: ' + str(
            total) + ' points'
        handCopy = updateHand(handCopy, bestWord)
        bestWord = compChooseWord(handCopy, wordList, n)

    if bestWord == None:
        if sum(handCopy.values()) != 0:
            print 'Current Hand: ',
            displayHand(handCopy)
            print 'Total score: ' + str(total) + ' points.'
        else:
            print 'Total score: ' + str(total) + ' points.'


#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    isFirst = True
    n = HAND_SIZE
    while 1:
        choice = raw_input(
            "Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choice == 'e':
            break
        elif choice != 'r' and choice != 'n':
            print "Invalid command.\n"
        elif isFirst and choice is 'r':
            print "You have not played a hand yet. Please play a new hand first!\n"
        else:
            isFirst = False
            while 1:
                choice2 = raw_input(
                    "Enter u to have yourself play, c to have the computer play: ")
                if choice2 == 'c':
                    if choice == 'n':
                        hand = dealHand(n)
                    compPlayHand(hand, wordList, n)
                    break
                elif choice2 == 'u':
                    if choice == 'n':
                        hand = dealHand(n)
                    playHand(hand, wordList, n)
                    break
                else:
                    print "Invalid command.\n"


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
