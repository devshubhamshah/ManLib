import csv, getpass

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
    global unames, pwords, users_data_writer, users_data_reader
    users_data_file = open("users_data.csv", 'r')
    users_data_reader = csv.reader(users_data_file)
    users_data_writer = csv.writer(users_data_file)
    unames = []
    pwords = []

    for row in users_data_reader:
        unames.append(row[0])
        pwords.append(row[1])

def user_reg():
    print("Please create an account.")
    uname = input("Please choose an username\n:: ")
    while uname in unames:
        print("Please select a different username.")
        uname = input("Please choose an username\n:: ")
    pword = getpass.getpass("Please choose a password for your account\n:: ")
    record = [uname, pword]
    users_data_writer.writerow(record)

    lib_file_name = uname + ".csv"
    lib_file = open(lib_file_name, 'w')
    lib_file_writer = csv.writer(lib_file, delimiter=',')
    lib_file_writer.writerow(['Title','Author','Genre','Status'])
    lib_file.close()

def login():
    print("================== login ==================")
    attempts = 0
    while attempts <= 3:
        attempts += 1
        print("Enter your login details below.")
        uname = input("Please enter your username\n:: ")
        if uname in unames:
            pword = getpass.getpass("Please enter your password\n:: ")
            if pword == pwords[unames.index(uname)]:
                global name_of_user
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
            book_status = 'Read'
            break
        elif book_status_num == '2':
            book_status = 'Reading'
            break
        elif book_status_num == '3':
            book_status = 'To-Be Read'
            break
        else:
            print("Enter valid number.")
            book_status_num == 'not-set'
    add_book = [book_title, book_author, book_genre, book_status]
    file_user_writer.writerow(add_book)
    file_user.close()

def search_book(search_book):
    global book_exists
    file_user = open(user_file_name, 'r')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    for row in file_user_reader:
        if search_book == row[0]:
            print(row)
            book_exists = True
            break
    else:
        print("No such book found!")
        book_exists = False
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
   # del_book(mod_book)
   # if book_exists:
   #     add_book()
    search_book(mod_book)
    if book_exists:
        to_update = int(input("0.Exit 1.Author 2.Genre 3.Status: "))
        file_user = open(user_file_name, 'r', newline = '')
        file_user_reader = csv.reader(file_user, delimiter = ',')
        for book in file_user_reader:
            if book[0] == mod_book:
                row = book
            
        if to_update == 0:
            return
        elif to_update == 1:
            new_auth = input("new author name: ")
            row[1] = new_auth
            print(row)
            return row
            
        elif to_update == 2:
            pass
        elif to_update == 3:
            pass
        file_user.close()

def data_print():
    file_user = open(user_file_name, 'r', newline = '')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    data = []
    for row in file_user_reader:
        data.append(row)
    header = data.pop(0)
    def fixed(text,length):
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + ' ' * length)[:length]
        return text
    print('#'*100)
    print('', end = ' ')
    for col in header:
        print(fixed(col,30), end = ' ')
    print()
    print('#'*100)
    for row in data:
        print('', end = ' ')
        for col in row:
            print(fixed(col,30), end = ' ')
        print()
    print('#'*100)
    file_user.close()

print("================== MANLIB ==================")
reg_login()
existing_up()
name_of_user = ''
login()
user_file_name = name_of_user + '.csv'

book_exists = ''

while True:
    try:
        print("==================")
        crud = int(input("Please select:\n\t0. Exit\n\t1. Create\n\t2. Search\n\t3. Update\n\t4. Delete\n\t5. Whole data\nchoice: "))
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
            file_user = open(user_file_name, 'a', newline = '')
            file_user_writer = csv.writer(file_user, delimiter = ',')
            file_user_writer.writerow(update_book(book_to_update))
            file_user.close()
            del_book(book_to_update)
        elif crud == 4:
            book_to_delete = input("Enter name of book to delete: ")
            del_book(book_to_delete)
        elif crud == 5:
            data_print()
        else:
            print("Invalid choice.")
            print("==================")
    except:
        print("Invalid choice.")
    