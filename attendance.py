__author__ = 'student'

import time
from time import localtime,strftime

student_info = {'4401001': 'Christine Adewale',
'44001722': 'Wayne Bertrand',
'4401011' : 'Ariel Casanella',
'4401020' : 'Abhiram Dawar',
'514005' : 'Eliel Esquivel',
'514007' : 'Andrew Fuentes',
'44001790': 'Yahira Herrera',
'44003688': 'Riyakumari Jain',
'15404' : 'Cristina Morocho',
'13249' : 'Nidhi Parekh',
'4401121' : 'Max Quevedo',
'302319' : 'Marianna Said',
'4401094' : 'Sebastian Tapia'}

while True:
    s_id = input('Scan student id: ')
    print('%s checked in - %s' % (student_info[s_id], time.strftime("%I:%M %p")))
