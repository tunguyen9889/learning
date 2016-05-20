def even_the_last(array):
    if array:
        return sum(array[::2]) * array[-1]
    return 0

if __name__ == '__main__':
    assert even_the_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_the_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_the_last([6]) == 36, "(6)*6=36"
    assert even_the_last([]) == 0, "An empty array = 0"
