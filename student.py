from datetime import date


map_ = {
    'KE': 'Kenya',
    'NG': 'Nigeria',
    'UG': 'Uganda',
    'TZ': 'Tanzania'
}


class Student(object): #inheritance

	# class properties
    count = 0
    attended_today = []
    
    def __init__(self, fname, lname, cc='KE'):
        # generate sequential unique ID
        Student.count += 1
        self.__id = Student.count # fake private
        self.fname = fname
        self.lname = lname
        self.country = map_[cc]

	def attend_class(self, **kwargs):
		'''
           	default values:
            location  = 'Hogwarts'
            date      = current_date
            teacher   = 'Alex'
        '''
        # declare variables to hold whataver value is gotten at a certain key
        # if no value is gotten the default value is asssigned to the variable
        location = kwargs.get('location', 'Hogwarts')
        what_day = kwargs.get('date', date.today())
        teacher  = kwargs.get('teacher', 'Alex')
        sentence  = self.fname + ' attended class taught by ' + teacher + ' at ' + location + ' on ' + str(what_day)
        # first make full_name to be an empty string
        full_name = ''
        # condition for it the day in arguments is the same as todays day
        # if they match then append the full names to the empty attendee_today list declared above
        if str(what_day) == str(date.today()):
            full_name = self.fname + ' ' + self.lname
            Student.todays_attended_today.append(full_name)
        return sentence

    @staticmethod
    def get_attendance_list():
        '''
            Method should generate a list of people who attended class in that day
        '''
        # declarea variable came_today that stores people who came today from attended_today list
        came_today = Student.attended_today
        sentence = "\n".join(came_today)
        return sentence
    
    
    


