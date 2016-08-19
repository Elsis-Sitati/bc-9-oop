from datetime import date
from student import Student

# Create at least 10 students

s1 = Student('Kevin', 'Chiteri')
s2 = Student('Allan', 'M.', 'UG')
s3 = Student('Elsis', 'Sitati')
s4 = Student('Jane', 'Kugo')
s5 = Student('Beth', 'Wanjiku')
s6 = Student('Rehema', 'Wachira')
s7 = Student('Innocent', 'Kateba')
s8 = Student('Mike', 'Dean')
s9 = Student('Steve', 'Njoro')
s10 = Student('Lucious', 'Lyon')


print(s1.id)
print(s2.id)
print(s3.id)

# Make at least 5 students attend class
today = str(date.today())
print(s3.attend_class(location='Dojo', date='2016-08-05', teacher='Mururi'))
print(s7.attend_class(location='Valhalla', date=today, teacher='Maxwell'))
print(s4.attend_class(location='Lionden', date='2016-08-14', teacher='Ned'))
# make a student have default values
print(s1.attend_class())
print(s8.attend_class(location='Ovaloffice', date=today, teacher='Frankie'))
    

# You should be able to print the list of students who attend class on a particular day
print()
print(Student.get_attendance_list())
print()
