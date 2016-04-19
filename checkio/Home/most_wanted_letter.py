# CheckIO - Home Challenge 4 : The Most Wanted Letter
# http://checkio.org

# You are given a text, which contains different english letters
# and punctuation symbols.
# You should find the most frequent letter in the text.
# The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter,
# so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols, digits and whitespaces,
# only letters.
# If you have two or more letters with the same frequency, then
# return the letter which comes first in the latin alphabet.
# For example -- "one" contains "o", "n", "e" only once for each,
# thus we choose "e".
# Input: A text for analysis as a string (unicode for py2.7).
# Output: The most frequent letter in lower case as a string.
# Precondition: The password contains only ASCII symbols. 0 < len(text) ≤ 105


from collections import Counter
import re


# Using lambda for shortest solution
# checkio = lambda t: max('abcdefghijklmnopqrstuvwxyz', key = t.lower().count)

def checkio(text):
    text = re.sub("[^a-zA-Z]", "", text).lower()
    char_count = dict(Counter(text).items())
    most = 0
    main_char = ''
    for c in char_count.keys():
        if char_count.get(c) > most:
            most = char_count.get(c)
            main_char = c
    return main_char


if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
