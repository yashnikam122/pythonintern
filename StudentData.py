'''1.	You are helping a teacher create a student attendance list 
for a class. Write a program that can: 
i) Track the attendance by adding students who are present to the list.
ii) Remove students who are absent from the list.
iii)Count how many students are present today 
iv) Add a list of students who were late and find 
out if any of them are in the attendance list.'''
 
attendentList=[] #list
print("\n---  student attendance list  Menu ---")
print("1.add student in attendentList to present ")
print("2. Remove a student in attendentList")
print("3. Count student in attendentList")
print('''4.students who were late find out if 
      any of them are in the attendance list''')
print("5. Exit")
while True:
      choice=int(input("enter your Choice"))
      
      if choice == 1:
            studentName=input("enter Student name to Mark are present")
            attendentList.append(studentName)
            print(studentName,"mark to present")
      elif choice == 2:
            studentName=input("enter Student name to Mark are apsent")
            for studentName in attendentList:
                  if studentName in attendentList:
                        attendentList.remove(studentName)
                        print(studentName,"mark as apsent")
                        break
                  else:
                        print(studentName,"not mark to present")
                        continue
                  
      elif choice == 3:
            countTotalStudent=len(attendentList)
            print(countTotalStudent," number of Student are Present")
            
      elif choice == 4:
            lateStudentName=input("enter student Name those are late")
            for lateStudentName in attendentList:
                  if lateStudentName:
                        print(lateStudentName, "is in the attendance list (was late).")
                        break
                  else:
                         print (lateStudentName ," is not in the attendance list.")

      else:
            print("invalid")
                        
            

      