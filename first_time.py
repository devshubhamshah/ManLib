import csv, new_user

users_data = open("users_data.csv", 'w')
users_data_writer = csv.writer(users_data, delimiter=',')
users_data_writer.writerow(['Username', 'Password'])

new_user.user_reg()