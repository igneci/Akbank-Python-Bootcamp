f = open ("books.txt","a+")
f.close()
class Library:
    def __init__ (self,book,author,date,number):
        self.book=book
        self.author=author
        self.date=date
        self.number=number
        w = open ("books.txt","a+")
        w.write(f'book_name:{self.book},author:{self.author},date:{self.date},pages:{self.number}\n')
        w.close()
    def list_books():
        read = open ("books.txt","r")
        data=read.readlines()
        if(len(data)>=0):
            for i in range(len(data)):
                book_name=data[i].split(",")[0].split(":")[1]
                author=data[i].split(",")[1].split(":")[1]
                print(f'Book: {book_name}, Author: {author}')
    def remove_books(book):
        global check
        check=False
        with open("books.txt", "r") as f:
            lines = f.readlines()
        with open("books.txt", "w") as f:
            for line in lines:
                if line.split(",")[0].split(":")[1] != book:
                    f.write(line)
                else:
                    check=True
        return check
ans=True
while ans:
    print("""
*** MENU ***
1) List Books
2) Add Books
3) Remove Books
q) Quit""")
    ans=input("Enter your choice (1-4): ")
    if ans=="1":
      Library.list_books()
    elif ans=="2":
      _book=input("Enter the book title: ")
      _author=input("Enter the author: ")
      _date=input("Enter the release year: ")
      _number=input("Enter the number of pages: ")
      Library(_book,_author,_date,_number)
      print("\nAdd Books Successful")
    elif ans=="3":
        _remove=input("Enter the book title to remove: ")
        if(Library.remove_books(_remove)):
            print("\nRemove Books Successful")
        else:
            print("\nRemove Books Error")
    elif ans=="q":
      ans = None
    else:
       print("\nNot Valid Choice Try Again")
        