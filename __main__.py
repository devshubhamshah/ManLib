import csv, reg_login

reg_login.reg_login()
reg_login.existing_up()
reg_login.login()
user_file_name = reg_login.name_user + '.csv'
file_user = open(user_file_name, 'a+')
file_user_writer = csv.writer(file_user, delimiter = ',')
file_user_reader = csv.reader(file_user)

def add_book(file_user_writer):
    book_title = input("Name of book: ")
    book_author = input("Name of author: ")
    #book_pages = input("Number of pages: ")
    book_genre = input("Genre of the book: ")
    book_status = input("Enter your choice:\n1. Read 2. Reading 3. To-Be Read")
    while book_status == 'not-set':
        if book_status == '1':
            book_status = 'Read'
        elif book_status == '2':
            book_status = 'Reading'
        elif book_status == '3':
            book_status = 'To-Be Read'
        else:
            print("Enter valid number.")
            book_status = 'not-set'
    add_book = [book_title, book_author, book_genre, book_status]
    file_user_writer.writerow(add_book)

def del_book(mod_book):
    #delete = input("Name of the book to be deleted: ")
    records = []
    for row in file_user_reader:
        if row[0] == mod_book:
            pass
        else:
            records.append(row)
    file_user_writer.writerow(records)

def edit_book():
    del_book(mod_book)
    add_book()

def search_book():
    for row in file_user_reader:
        
    

    

    