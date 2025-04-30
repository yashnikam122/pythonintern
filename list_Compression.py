numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newEvenElementlist=[]
for number in numbers:
      if number % 2 == 0:
            newEvenElementlist.append(number)
      else:
            continue

print(newEvenElementlist)