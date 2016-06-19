vowels = ['a', 'e', 'i', 'o', 'u']


def count_vowels(s):
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print "Number of vowels: " + str(count)
