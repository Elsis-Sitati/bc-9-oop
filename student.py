map_ = {
    'KE': 'Kenya',
    'NG': 'Nigeria',
    'UG': 'Uganda',
    'TZ': 'Tanzania'
}

class Student(object): #inheritance

    count = 0
    
    def __init__(self, fname, lname, cc='KE'):
        # generate sequential unique ID
        Student.count += 1
        self.__id = Student.count # fake private
        self.fname = fname
        self.lname = lname
        self.country = map_[cc]

   def attend_class(self, **kwargs):
		'''
		defaualt values:
			loc = 'Hogwarts'
			date = 'current_date'
			teacher = 'Alex'
		'''
		if not kwargs['loc']:
			loc = 'Hogwarts'
		else:
			loc = kwargs['loc']

		if not kwargs['teacher']:
			teacher = 'Hogwarts'
		else:
			teacher = kwargs['teacher']

		if not kwargs['date']:
			date = datetime.date.today()
		else:
			date = kwargs['date']


