class Library:
    def __init__(self,BookList):
        self.BookList=BookList

    def print_list(self):
        for book in self.BookList:
            print("*",book)

    def request(self,a):
        if a in self.BookList:
            print(f"This book {a} is availabe. Please return it within 30 days")
            self.BookList.remove(a)
        else:
            print(f"The request book {a} is not available")
    def returnbook(self,a):
        print("Thanks for the book {a}")
        self.BookList.append(a)
class Student():
    def borrowbook(self):
        a=input("Please Enter the name of book you want you borrow: ")
        return a
    def returnbook(self):
        a=input("Please Enter the name of book you want you Return or donate: ")
        return a


if __name__ == "__main__":
    book=Library(["History","Geography","Math"]) 
    student=Student()
    wellcome='''---------Welcome to Central Libary---------
    Press The folloing Keys for operation
    1. Show the List of Books
    2. Borrow a Book
    3. Return/donate a Book
    q. To exit'''    
    while True:
        print(wellcome)
        a=input("   ")
        if a=="1":
            book.print_list()
        elif a=="2":
            book.request(student.borrowbook())
        elif a=="3":
            book.returnbook(student.returnbook())
        elif a=="q":
            break

        else:   
            print("Invailed Entry")     



