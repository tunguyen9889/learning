num_dict = {
    0: (' _ ', '| |', '|_|'),
    1: ('   ', '  |', '  |'),
    2: (' _ ', ' _|', '|_ '),
    3: (' _ ', ' _|', ' _|'),
    4: ('   ', '|_|', '  |'),
    5: (' _ ', '|_ ', ' _|'),
    6: (' _ ', '|_ ', '|_|'),
    7: (' _ ', '  |', '  |'),
    8: (' _ ', '|_|', '|_|'),
    9: (' _ ', '|_|', ' _|')
}

while True:
    try:
        number_raw = int(raw_input("Please input a number: "))
        break
    except ValueError:
        print("This is not a number! Try again.")

output = [str(), str(), str()]

for row in range(3):
    for digit in str(number_raw):
        output[row] += num_dict[int(digit)][row]
    print output[row]
