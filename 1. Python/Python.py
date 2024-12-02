# Python basics question

'''01. Find the sum of list elements '''
from random import randint
array = []
[array.append(randint(0, 10)) for _ in range(5)]
print("List : ",array)

s = sum(array)
print("Sum of array : ", s)

'''02. Largest element in the list '''
from random import randint
array = []
[array.append(randint(0, 10)) for _ in range(5)]
print("List : ",array)

array.sort()
print("Largest element from given array : ", array[-1])

'''03. Remove Duplicates in a list '''
from random import randint
array = []
[array.append(randint(0, 10)) for _ in range(10)]
print("List : ",array)

arr = []
for i in array:
    if i in arr:
        pass

    else:
        arr.append(i)
print(arr, array)

'''04. Check if all elements in a list are unique '''
from random import randint
array = []
[array.append(randint(0, 10)) for _ in range(4)]
print("List : ",array)

arr = set(array)

if sum(arr) == sum(array):
    print("Unique")

else:
    print("Repeated")

'''05. Program to reverse list '''
from random import randint
array = []
[array.append(randint(0, 10)) for _ in range(4)]
print("List : ",array)

print("Reverse list : ", array[::-1])

'''06. Count no of odd n even numbers in a list '''
from random import randint
array = []
[array.append(randint(0, 10)) for _ in range(4)]
print("List : ",array)
odd, even = 0, 0
for i in array:
    if i%2 == 0:
        even += 1
    
    else:
        odd += 1

print(f"Odd numbers : {odd}\nEven numbers : {even}")

'''07. Check if a list is subset of another list '''
from random import randint
array1, array2 = [], []
[[array1.append(randint(0, 10)), array2.append(randint(0, 10))] for _ in range(4)]
print(f"List1 : {array1}\nList2 : {array2}")

if set(array1).issubset(set(array2)):
    print("List1 is a subset of List2")
elif set(array2).issubset(set(array1)):
    print("List2 is a subset of List1")
else:
    print("List1 and List2 are disjoint sets")

'''08. Max diff btw two consecutive elements in a list '''
from random import randint
array = []
[array.append(randint(0, 10)) for _ in range(4)]
print("List : ",array)
max = 0
for i in range(len(array)-1):
    if (array[i] - array[i+1]) > max:
        max = array[i] - array[i+1]
print("Max diff : ", max)

'''09. Merge Multiple dictionaries'''
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = dict1 | dict2
print(merged_dict)

'''10. Find words frequency in a sentence '''
string = input("Enter any string : ")
frequency = {}
for letter in string:
    if letter.isalpha():
        frequency[letter] = frequency.get(letter, 0) + 1
print("Frequency of letters : ", frequency)
