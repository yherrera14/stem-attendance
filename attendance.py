__author__ = 'student'
# Comments look like this
import time
import pickle

present = [] # creates an empty list called present

with open('students.p', 'rb') as p_file:  #opens and closes the file without having to actually close it every time
        roster = pickle.load(p_file) 
        
while True:
    try:
        s_id = input('Scan student id or enter Q to quit: ') # asks for id number
        if s_id in ['q', 'Q']: #if lowercase or uppercase "q" is entered
            mark_absent = input('Mark missing students absent? (y/[n]) ') # asks if students any students are missing
            if mark_absent in ['y', 'Y']: #if lowercase or uppercase "y" is entered
                for key, data in roster.items():
                    if data['name'] not in present: # if name of student was not added to the list "present" 
                        roster[key]['absent'].append(time.strftime("%m/%d")) # then the student's name is added to the list "absent" with the date
                with open('students.p', 'wb') as p_file:
                    pickle.dump(roster, p_file) 
            break # ends the loop

        else:
            present.append(roster[s_id]['name'])
            roster[s_id]['present'].append(time.strftime("%m/%d at %I/%M")) # adds the name of student and date/time tot he list "present
            print('%s checked in on %s' % (roster[s_id]['name'], time.strftime("%m/%d at %I:%M"))) #spits out the name of the student and the dateand time
    except KeyError:
        print("Invalid ID number") #when an invalid input is typed, it recognizes the mistake and spits out "Invalid ID number"
