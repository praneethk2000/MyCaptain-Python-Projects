

import operator
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] = d[key] + 1
    a = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
    print (a)


string = input("Please enter a string: ")

most_frequent(string)
