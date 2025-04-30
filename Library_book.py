'''Imagine you're managing a library, and you have a list of book titles.
Write a program that allows you to: i) Add a new book title to the list 
ii) Remove a book from the list. 
iii) Find out if a specific book is available in the library
iv) Sort the list alphabetically 
v) Display the number of books in the library.'''


books=[1984, "Dune", "IT", "Emma"]

print("\n--- Library Menu ---")
print("1. Add a new book")
print("2. Remove a book")
print("3. Search for a book")
print("4. Sort books alphabetically")
print("5. Count total books")
print("6. Show all books")
print("7. Exit")



while True:
    choice=int(input("enter your choice"))
    if choice == 1:
        book=input("enter to Book Title TO add")
        books.append(book)
        print(book,"added to the library.")
        
    elif choice == 2:
        book = input("Enter book title to remove: ")
        if book in books:
            books.remove(book)
            print(book,"remove to the library.")
        else:
            print(book," not found in the library")
            
    elif choice==3:
        book=input("enter to Book Title TO search") 
        if book in books:
            print(book,"is available in  Library")   
        else:
            print(book," not found in the library")
    elif choice==4:
        books.sort()
        print("Books sorted alphabetically.")
    elif choice==5:
        print(len(books),"Total Number OF Books In Library")

    elif choice==6:
        for book in books:
            print(book,"\t")
        break    
    else:
        print("invalid input")
        