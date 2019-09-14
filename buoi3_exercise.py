import numpy as np

A = np.array([["", "2213e", "31"], ["tâm1", "5553e", "31"]])

def clean_data(row, empty, too_long, chang_phone,change_salary):
    empty(row)
    too_long(row)
    chang_phone(row)
    change_salary(row)

def convert_emty(row):
    if row[0]=='':
        row[0]= 'John'

def too_long(row):
    if len(row[0])>25:
        row[0]=row[0][:25]
# test
row=['hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhlallalal', '03301k', 11]
too_long(row)
print(row)
#def chang_phone_zero(row):


#def change_pre(row):

#def change_salary_end(row):

#def change_salary_valid(row):
