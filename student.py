import datetime

map_ = {
    'UG': 'Uganda',
    'KE': 'Kenya',
    'NG': 'Nigeria',
    'TZ': 'Tanzania'
}

class Student(object):
    #declaring a variable Id with a value zero which is an instance  variable
    Id = 0  
    #Create an empty dictionary attendace that stores the attendance of the students                                                    
    attendance = {}                                            

    def __init__(self, fname, lname, cc='KE'):
        #Increment the Student Id everytime this class is called so that everyone has a unique Id
        Student.Id = Student.Id + 1                            

        self.unique_id = Student.Id
        self.fname = fname
        self.lname = lname
        self.country = map_[cc]


    def attend_class(self, **kwargs):
        '''
        defaualt values:
            loc = 'Hogwarts'
            date = 'today'
            teacher = 'Alex'
        '''

        loc = kwargs.get('loc', 'Hogwarts')
        date = kwargs.get('date', datetime.date.today())
        teacher = kwargs.get('teacher', 'Alex')

        if date not in Student.attendance.keys(): 
         #Check if each date is in the attendance list, if not, add both the current date and the full name of the student                                 
            Student.attendance[date] = [self.fname + " " + self.lname]
        else:
            full_name = self.fname +  " " + self.lname
            if full_name not in Student.attendance[date]:
                Student.attendance[date].append(full_name)

    @staticmethod
    def attendance_list(date):
        if date not in Student.attendance.keys(): 
          #Print the records for the current date, if none, then no  attendance                                
            print("No Attendance today!")
        else:
            the_attendance_list = Student.attendance[date]

            print("Attendance on: " + str(date))
            for student in the_attendance_list:
                print(student)