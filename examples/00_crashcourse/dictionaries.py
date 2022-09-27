dict1 = {}
print("Empty Dictionary: ")
print(dict1)

dict2 = {1: 'Hero', 2: 'For', 3: 'Heroes'}
print("\nDictionary with the use of Integer Keys: ")
print(dict2)

dict3 = {'Name': 'Hero', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(dict3)

dict4 = dict({1: 'Hero', 2: 'For', 3: 'Heroes'})
print("\nDictionary with the use of dict(): ")
print(dict4)

dict5 = dict([(1, 'Heroes'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(dict5)