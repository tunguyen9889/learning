def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter_dict = {}
    diff_dict = {}

    for key, value in d1.items():
        if key in d2.keys():
            # keys are shared
            inter_dict[key] = f(value, d2[key])
        else:
            # d1 contains a key not found in d2.
            # add this to diff_dict
            diff_dict[key] = value

    for key, value in d2.items():
        if key not in d1.keys():
            # d2 contains a key not found in d1.
            # add this to diff_dict
            diff_dict[key] = value

    return (inter_dict, diff_dict)


print dict_interdiff({}, {})
print dict_interdiff({1: 1}, {1: 1})
print dict_interdiff({0: 0, 2: 5, 5: 2}, {0: 0, 2: 5})
print dict_interdiff({1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}, {9: 1, 5: 3, 6: 3, 7: 4})
