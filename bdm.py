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
    add_book = [book_title, book_author, book_genre, book_status])

book_add = add_book