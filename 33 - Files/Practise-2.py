while True:
    book = input("Lovely book (press 'enter' for stop): ")

    if not book:
        print("Code was stopped!!!")
        break

    with open("books/books_list.txt", "a") as file:
        file.write(book + "\n")