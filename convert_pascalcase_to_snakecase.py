def to_underscore(string):
    res = ''
    res = res + string[0].lower()

    for i in range(1, len(string)):
        if string[i].isupper():
            res = res + '_' + string[i].lower()
        else:
            res = res + string[i]

    return res

print(to_underscore(input("Enter PascalCase string: ")))