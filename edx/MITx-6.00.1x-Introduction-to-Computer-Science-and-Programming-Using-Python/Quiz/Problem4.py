def isPalindrome(aString):
    return aString == ''.join(reversed(aString))


print isPalindrome('')
print isPalindrome('hZO')
print isPalindrome('poop')
print isPalindrome('FYOnZZnOYF')
