import json
catalog = []
def add_book():
    try:
        title = input("Enter the name of the book. ")
        author = input("Enter the author of the book. ")
        genre = input("Enter the genre of the book. ")

        if(title.strip() == " " or author.strip()== " " or genre.strip() == " "  ):
            print("Title, Author and Genre cannot be empty.")
            return

        price = float(input("Enter the price: "))
        copies= int(input("Enter the number of copies: "))

        if(price <=0 or copies<0):
            print(" Please enter valid price and number of copies.")
            return

        book = {
            "id" : len(catalog)+1,
            "title" : title,
            "author" : author,
            "genre" : genre,
            "price" : price,
            "copies" : copies
        }

        catalog.append(book)
        print("Book added successfully.")

    except ValueError:
        print("Please enter valid details.")

def view_catalog():
    if(len(catalog)==0):
        print("Nothing to print.")
        return
    print("-"*50)
    for book in catalog:
        print(f"""id     : {book["id"]},
title  : {book["title"]},
author : {book["author"]},
genre  : {book["genre"]},
price  : {book["price"]},
copies : {book["copies"]}""")
    print("-"*50)

def search_catalog():
    id = int(input("Enter the id of the book: "))

    for book in catalog:
        if(book["id"]==id):
             
             print(f"""id     : {book["id"]},
             title  : {book["title"]},
             author : {book["author"]},
             genre  : {book["genre"]},
             price  : {book["price"]},
             copies : {book["copies"]}""")
        else:
            print("No Book found.")

def update_catalog():
    id = int(input("Enter the id: "))

    for book in catalog:
            if(book["id"]==id):
                book["price"] = float(input("Enter new price: "))
                book["copies"] = int(input("enter new copies: "))
                print("Book updated successfully")
                print(
                        book["id"],
                        book["title"],
                        book["author"],
                        book["genre"],
                        book["price"],
                        book["copies"]
                                    )
            else:
                print("Book not Found!")
                
def delete():
    id = int(input("Enter the id: "))
    for book in catalog:
        if(book["id"]==id):
            catalog.remove(book)
            print("book removed")
        else:
            print("book not found")

def save_cat():
     with open("book.json", "w", encoding= "utf-8") as f:
          json.dump(catalog, f, indent = 4)
          print("Book saved sucessfully")

def load_cat():
    with open("book.json", "r", encoding= "utf-8") as f:
        loaded_book = json.load(f)

        print(f" Books loaded : {loaded_book}")


while True:
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Save")
    print("7. Load")
    print("8. Exit")

    choice = int(input("Enter the choice: "))


    if(choice==1):
        add_book()
    elif(choice==2):
        view_catalog()
    elif(choice==3):
        search_catalog()
    elif(choice==4):
        update_catalog()
    elif(choice==5):
        delete()
    elif(choice==6):
        save_cat()
    elif(choice==7):
        load_cat()
    elif(choice==8):
        print("Bye!")
        break
    else:
        print("invalid Choice")

    








    
