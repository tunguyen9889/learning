def nfruits(dictionary, string):
    string = sorted(string)
    for idx, char in enumerate(string):
        # Update the fruit Python ate
        dictionary[char] -= 1
        # update others he bought, skip this on the last step
        if idx < len(string) - 1:
            for key in dictionary:
                if key != char:
                    dictionary[key] += 1
    return dictionary[max(dictionary, key=dictionary.get)]

print nfruits({'Y': 7, 'I': 5, 'S': 9, 'K': 6, 'N': 9}, 'KSNYS')
