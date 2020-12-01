import csv, getpass, sys
from time import sleep
from os import system, name
from tabulate import tabulate


def reg_login():
    try:
        users_data_file = open("users_data.csv", 'r')
        users_data_file.close()
    except FileNotFoundError:
        users_data = open("users_data.csv", 'w', newline='')
        users_data_writer = csv.writer(users_data, delimiter=',')
        users_data_writer.writerow(['Username', 'Password'])
        print("Please create an account.")
        uname = input("Please choose an username\n:: ")
        pword = getpass.getpass("Please choose a password for your account\n:: ")
        record = [uname, pword]
        users_data_writer.writerow(record)
        lib_file_name = uname + ".csv"
        lib_file = open(lib_file_name, 'w', newline='')
        lib_file_writer = csv.writer(lib_file, delimiter=',')
        lib_file_writer.writerow(['Title','Author','Genre','Status'])
        lib_file.close()


def existing_up():
    global unames, pwords, users_data_reader, users_data_file
    users_data_file = open("users_data.csv", 'r')
    users_data_reader = csv.reader(users_data_file)
    #users_data_writer = csv.writer(users_data_file)
    unames = []
    pwords = []
    for row in users_data_reader:
        unames.append(row[0])
        pwords.append(row[1])
    users_data_file.close()


def user_reg():
    users_data_file = open("users_data.csv", 'a+', newline = '')
    users_data_writer = csv.writer(users_data_file)
    print("Please create an account.")
    uname = input("Please choose an username\n:: ")
    while uname in unames:
        print("Please select a different username.")
        uname = input("Please choose an username\n:: ")
    pword = getpass.getpass("Please choose a password for your account\n:: ")
    record = [uname, pword]
    users_data_writer.writerow(record)
    users_data_file.close()
    lib_file_name = uname + ".csv"
    lib_file = open(lib_file_name, 'w', newline = '') 
    lib_file_writer = csv.writer(lib_file, delimiter=',')
    lib_file_writer.writerow(['title','author','genre','status'])
    lib_file.close()
    existing_up()
    print("================== successful ==================")


def login():
    global name_of_user
    print("================== login ==================")
    attempts = 0
    while attempts < 3:
        attempts += 1
        print("Enter your login details below.")
        uname = input("Please enter your username\n:: ")
        if uname in unames:
            pword = getpass.getpass("Please enter your password\n:: ")
            if pword == pwords[unames.index(uname)]:
                name_of_user = uname
                print("================== successful ==================")
                print("Welcome!")
                break
            else:
                print("Wrong password. Please try again.")
        else:
            print("Wrong username.")
    else:
        print("3 unsuccessful attempts to login. Please try again later.")
        sys.exit()


def add_book():
    file_user = open(user_file_name, 'a', newline = '')
    file_user_writer = csv.writer(file_user, delimiter = ',')
    book_title = input("Name of book: ")
    book_author = input("Name of author: ")
    book_genre = input("Genre of the book: ")
    book_status_num = input("Enter your choice:\n1. Read 2. Reading 3. To-Be Read\nstatus: ")
    book_status = ''
    while True:
        if book_status_num == '1':
            book_status = 'read'
            break
        elif book_status_num == '2':
            book_status = 'reading'
            break
        elif book_status_num == '3':
            book_status = 'to-be-read'
            break
        else:
            print("Enter valid number.")
            book_status_num == 'not-set'
    add_book = [(book_title.lower()).replace(" ", ""), (book_author.lower()).replace(" ", ""), (book_genre.lower()).replace(" ", ""), book_status.lower()]
    file_user_writer.writerow(add_book)
    file_user.close()


def search_book(search_book):
    global book_exists, update_row
    file_user = open(user_file_name, 'r')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    for row in file_user_reader:
        if search_book == row[0]:
            print(row)
            update_row = row
            book_exists = True
            break
    else:
        print("No such book found in library.")
        book_exists = False
    file_user.close()


def search_multiple():
    search_by = int(input("Search by:\n0. Exit 1.Author 2.Genre 3.Status: "))
    file_user = open(user_file_name, 'r')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    reqd_books = []
    if search_by == 0:
        return
    elif search_by == 1:
        all_of_author = input("Enter name of author to search for: ")
        for book in file_user_reader:
            if book[1] == all_of_author.lower():
                reqd_books.append(book)
    elif search_by == 2:
        all_of_genre =  input("Enter genre to search for: ")
        for book in file_user_reader:
            if book[2] == all_of_genre.lower():
                reqd_books.append(book)
    elif search_by == 3:
        all_of_status =  input("Enter status to search for: ")
        for book in file_user_reader:
            if book[3] == all_of_status.lower():
                reqd_books.append(book)
    else:
        print("Invalid choice.")
        return
    print(tabulate(reqd_books, headers = ['title','author','genre','status'], tablefmt='pretty'))
    file_user.close()


def del_book(mod_book):
    search_book(mod_book)
    file_user = open(user_file_name, 'r')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    if book_exists:
        records = []
        for row in file_user_reader:
            if row[0] == mod_book:
                continue
            else:
                records.append(row)
        file_user.close()
        file_user = open(user_file_name, 'w', newline = '')
        file_user_writer = csv.writer(file_user, delimiter = ',')
        file_user_writer.writerows(records)
        file_user.close()
    

def update_book(mod_book):
    del_book(mod_book)
    if book_exists:
        file_user = open(user_file_name, 'a', newline='')
        file_user_writer = csv.writer(file_user, delimiter = ',')
        to_update = int(input("0.Exit 1.Title 2.Author 3.Genre 4.Status: "))
        if to_update == 0:
            return
        elif to_update == 1:
            new_title = input("Enter new title: ")
            update_row[0] = new_title.lower()
            file_user_writer.writerow(update_row)
            file_user.close()
        elif to_update == 2:
            new_author = input("Enter new author: ")
            update_row[1] = new_author.lower()
            print(update_row)
            file_user_writer.writerow(update_row)
            file_user.close()
        elif to_update == 3:
            new_genre = input("Enter new genre: ")
            update_row[2] = new_genre
            file_user_writer.writerow(update_row)
            file_user.close()
        elif to_update == 4:
            book_status_num = input("Enter your choice:\n1. Read 2. Reading 3. To-Be Read\nstatus: ")
            while True:
                if book_status_num == '1':
                    book_status = 'read'
                    break
                elif book_status_num == '2':
                    book_status = 'reading'
                    break
                elif book_status_num == '3':
                    book_status = 'to-be-read'
                    break
                else:
                    print("Enter valid number.")
                    book_status_num == 'not-set'
            update_row[3] = book_status
            file_user_writer.writerow(update_row)
            file_user.close()
        else:
            print("invalid choice")
            return                    


def update_complete(mod_book):
    del_book(mod_book)
    add_book()


def data_print():
    file_user = open(user_file_name, 'r', newline = '')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    data = []
    for row in file_user_reader:
        data.append(row)
    header = data.pop(0)
    print(tabulate(data, header, tablefmt = "pretty"))
    file_user.close()


def welcome():
    print("================== MANLIB ==================")
    reg_login()
    existing_up()
    cred = ' '
    while True:
        cred = int(input("0. Exit 1.Login 2.New account: "))
        if cred == 0:
            print("So long!")
            sys.exit()
        elif cred == 1:
            login()
            global user_file_name, name_of_user
            user_file_name = name_of_user + '.csv'         
            break
        elif cred == 2:
            user_reg()
            print("Please login after creating account.")


def clear():
        # for windows 
    if name == 'nt': 
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def progress():
    loaded = 0
    total = 100
    while loaded <= 100:
        clear()
        print("================== MANLIB ==================")
        print(loaded,"%")
        bar = str("[" + "="*loaded + "-"*(total - loaded) + "]")
        print(bar)
        sleep(1)
        loaded += 10
    else:
        clear()
        return


def splash_screen():
    print("================== MANLIB ==================")
    progress()
    clear()


clear()
user_file_name = ' '
name_of_user = ''
splash_screen()
welcome()
book_exists = ''
update_row = []


while True:
    try:
        print("==================")
        print("\n")
        crud = int(input("Please select:\n\t0. Exit\n\t1. Create\n\t2. Search\n\t3. Update\n\t4. Delete\n\t5. Search Multiple\n\t6. Update entire record\n\t7. Entire library\nchoice: "))
        if crud == 0:
            print("So long..!\n==================")
            break
        elif crud == 1:
            add_book()
        elif crud == 2:
            book_to_search = input("Enter name of book to search for: ")
            search_book(book_to_search)
        elif crud == 3:
            book_to_update = input("Enter name of book to update: ")
            update_book(book_to_update)
        elif crud == 4:
            book_to_delete = input("Enter name of book to delete: ")
            del_book(book_to_delete)
        elif crud == 5:
            search_multiple()
        elif crud == 6:
            book_to_update = input("Enter name of book to update: ")
            update_complete(book_to_update)
        elif crud == 7:
            data_print()
        else:
            print("Invalid choice.")
            print("==================")
    except Exception as e:
        print("error: {}".format(e))
        print("except Invalid choice.")
    finally:
        print("\n")
        