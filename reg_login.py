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
    print("login")
    for attempts in range(3):
        print("Enter your login details below.")
        uname = input("Please enter your username\n:: ")
        if uname in unames:
            pword = getpass.getpass("Please enter your password\n:: ")
            if pword == pwords[unames.index(uname)]:
                print("Login Successful.")
                break
            else:
                print("Wrong password. Please try again.")
        else:
            print("Wrong username.")
    else:
        print("3 unsuccessful attempts to login. Please try again later.")