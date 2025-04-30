'''3.	You have a tuple with several mixed values (strings, numbers).
Write a program that: 
i) Counts how many times a specific element appears in the tuple.
ii)Checks if a particular value exists in the tuple.
iii)Extracts a slice of the tuple from index 1 to  
Iv) Converts the tuple to a list, adds a new value,
and then converts it back to a tuple.'''

tuple1=("bhupendra",100,"nandulal",100,"patil",35)
print("tuple element is:",tuple1)

print("100 is appear in",tuple1.count(100),"time in tuple")
sliceElement=tuple1[1:]
print("slicing the element is:-",sliceElement)

list1=list(tuple1) ##list()
print(list1)
list1.append(10) ##add append

tuple1=tuple(list1)

print(tuple1)