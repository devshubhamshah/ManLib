# books data manipulation
import csv

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
    global add_book
    add_book = [book_title, book_author, book_genre, book_status]

book_add = add_book

def del_book():
    delete = input("Name of the book to be deleted:")
    


# def update_book(mod_book):
#    # del_book(mod_book)
#    # if book_exists:
#    #     add_book()
#     global new_row
#     #new_row = list(new_row)
#     search_book(mod_book)
#     if book_exists:
#         with open(user_file_name, 'a+', newline='') as file_user:
#             file_user = open(user_file_name, 'r', newline = '')
#             file_user_reader = csv.reader(file_user, delimiter = ',')
#             file_user_writer = csv.writer(file_user, delimiter = ',')
#             for book in file_user_reader:
#                 print(book)
#                 if book[0] == mod_book:
#                    #updated_row.append(book)
#                     print("row done")
#                     for sec in book:
#                         new_row.append(sec)
#                     print(new_row)
#                     print(type(new_row))
#                     #new_row = list(new_row) #par new row str hai
#                     #print(updated_row)
#                     break
#             to_update = int(input("0.Exit 1.Title 2.Author 3.Genre 4.Status: "))        
#             if to_update == 0:
#                 return
#             elif to_update == 1:
#                 new_title = input("new title: ")
#                 new_row[0]= new_title
#                 #print(updated_row)
#                 file_user_writer.writerow(new_row)
#                 #file_user.close()
#                 return
#             elif to_update == 2:
#                 new_auth = input("new author name: ")
#                 new_row[1] = new_auth
#                 #print(updated_row)
#                 file_user_writer.writerow(new_row)
#                 #file_user.close()
#                 return
#             elif to_update == 3:
#                 new_genre = input("new genre: ")
#                 new_row[2] = new_genre
#                 #print(updated_row)
#                 file_user_writer.writerow(new_row)
#                 #file_user.close()
#                 return
#             elif to_update == 4:
#                 new_book_status_num = input("Enter your choice:\n1. Read 2. Reading 3. To-Be Read\nstatus: ")
#                 while True:
#                     if new_book_status_num == '1':
#                         book_status = 'Read'
#                         break
#                     elif new_book_status_num == '2':
#                         book_status = 'Reading'
#                         break
#                     elif new_book_status_num == '3':
#                         book_status = 'To-Be Read'
#                         break
#                     else:
#                         print("Enter valid number.")
#                         new_book_status_num == 'not-set'
#                 new_row[3] = book_status
#                 #print(updated_row)
#                 file_user_writer.writerow(new_row)
#                 #file_user.close()
#                 return

