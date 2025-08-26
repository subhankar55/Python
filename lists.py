marks = [89,90,34,67,"Math"]

print(marks)

print(marks[1])
print(marks[-1]) # count from back
print(marks[0:2]) # create a list with index [0,2) i.e. 2 is exluded and will print it.

for score in marks:
    print(score)
marks.append(99) # can add new value from back

print(marks)

marks.insert(1,65) # can add new value at any index

print(marks)

print(len(marks)) # print the length of the list

marks.clear() # empty the list
print(marks)