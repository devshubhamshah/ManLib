import csv, reg_login

reg_login.reg_login()
reg_login.existing_up()
reg_login.login()
user_file_name = reg_login.name_user + '.csv'
file_user = open(user_file_name, 'a+')
file_user_writer = csv.writer(file_user, delimiter = ',')