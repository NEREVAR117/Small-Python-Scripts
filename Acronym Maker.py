# Creates an acronym

string = input('Please enter a series of words: ')

list = string.split()

output = ''

for x in list:
    for y in (x[0]):
        output += y

print(output.upper())


# Second method (much more efficient)

string = input('Please enter a series of words: ').upper().split()

for word in string:
    print(word[0], end='')