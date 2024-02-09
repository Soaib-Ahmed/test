class Book:
    def __init__(self,id,name,quantity):
        self.id=id
        self.name=name
        self.quantity=quantity
        
class User:
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password
        self.borrowBooks=[]
        self.returnedBooks=[]

class Library:
    def __init__(self,name):
        self.name=name
        self.users=[]
        self.books=[]

    def add_book(self,id,name,quantity):
        book=Book(id,name,quantity)
        self.books.append(book)
        print(f"{book.name} added succecsfully")

    def add_user(self,id,name,password):
        user=User(id,name,password)
        self.users.append(user)
        return user
    def borrow_Book(self,user,token):
        for book in self.books:
            if book.name==token:
                if book in user.borrowBooks:
                    print("Already borrowed!\n")
                    return
                elif book.quantity==0:
                    print("NO copy Available!\n")
                    return
                else:
                    user.borrowBooks.append(book)
                    book.quantity-=1
                    print("Borrowed book successfull\n")
                    return
            
            
        print(f"Not found any book with name {token}!\n")
    
    def return_Book(self,user,token):
        for book in self.books:
            if book.name==token:
                if book in user.borrowBooks:
                    book.quantity+=1
                    user.returnedBooks.append(book)
                    user.borrowBooks.remove(book)
                    print("Returned book successfull")
                elif book.quantity==0:
                    print("NO copy Available!\n")
                    return
        print(f"Not found any book with name {token}!\n")

seaum=Library("Seaum Library")
admin=seaum.add_user(102,'admin','admin')
abir=seaum.add_user(33,'seaum',123)
cpbook=seaum.add_book(334,'cpbook',5)

current_user=admin

while True:
    if current_user == None:
        print('No user found\n')

        op=input("login ro reg (L/R):")

        if(op)=="L":
            id=int(input('Enter the id:'))
            password=input("Enter the Pass:")

            match=False
            for user in seaum.users:
                if user.id==id and user.password==password:
                    current_user=user
                    match=True
                    break
            if match==False:
                print("No user Found!\n")

        elif op=='R':
            id=int(input("Enter id: "))
            name=input("Enter the name:")
            password=input("Enter the Pass:")

            for user in seaum.users:
                if user.id==id:
                    print("All ready reg\n")
            user=seaum.add_user(id,name,password)
            current_user=user

    else:
        print(f"Welcome Back {current_user.name}!\n")
        if current_user.name=="admin":
            print("Options\n")
            print("1. Add Book")
            print("2. Add User")
            print("3. Show All Books")
            print("4. Logout")

            ch=int(input("Enter Opiton: "))
            
            if ch==1:
                id=int(input("Enter the Book Id: "))
                name=input("Enter the book name:")
                quan=int(input("Enter book Qunatity:"))

                seaum.add_book(id,name,quan)

            elif ch==3:

                for book in seaum.books:
                    print(f"{book.id}\t{book.name}\t{book.quantity}")
                    #print("\n")
            elif ch==4:
                current_user=None
        else:
            print("Options\n")
            print("1. Borrow Book")
            print("2. Return Book")
            print("3. Show Borrowed Books")
            print("4. Show History")
            print("5. Logout\n")

            ch=int(input("Enter Opiton: "))

            if ch==1:
                name=input("Enter book name: ")
                seaum.borrow_Book(current_user,name)
            elif ch==2:
                name=input("Enter book name: ")
                seaum.return_Book(current_user,name)
            elif ch==3:
                print("\nBorrowed Books:\n")
                for book in current_user.borrowBooks:
                    print(f"{book.id}\t{book.name}\t{book.quantity}")
                print("\n")
            elif ch==4:
                print("\nYour History\n")
                for book in current_user.returnedBooks:
                    print(f"{book.id}\t{book.name}\t{book.quantity}")
                print("\n")
            elif ch==5:
                current_user=None

            



