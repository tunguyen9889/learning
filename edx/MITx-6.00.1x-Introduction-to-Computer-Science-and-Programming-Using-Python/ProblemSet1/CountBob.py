s = 'azcbobobegghakl'


def count_bobs(string, substring):
    str_length = len(string)
    sstr_length = len(substring)
    count = 0
    for i in xrange(0, str_length - sstr_length + 1):
        if string[i:i + sstr_length] == substring:
            count += 1
    print "Number of times bob occurs is: " + str(count)

count_bobs(s, 'bob')
