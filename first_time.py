import csv

def first_time():
    users_data = open("users_data.csv", 'w')
    users_data_writer = csv.writer(users_data, delimiter=',')
    users_data_writer.writerow(['Username', 'Password'])
    #reg_login.user_reg()

first_time()