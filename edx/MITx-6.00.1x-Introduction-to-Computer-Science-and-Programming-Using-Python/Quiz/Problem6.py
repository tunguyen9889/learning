def flatten(aList):
    """
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    """
    result = []
    for el in aList:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


print flatten([[], []])
print flatten([[1], [1]])
print flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]]])
