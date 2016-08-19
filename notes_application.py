class NotesApplication(object):


	def __init__(self, author, notes=[]):
		self.author = author
		self.notes = notes
    
    
	# This function takes the notes_content argument and appends it to the notes list
	def create(self, notes_content):
		self.notes.append(notes_content)


	def list(self):
		# loop through the notes passed in the initializer function
		for i, j in enumerate(self.notes):
			# getting the index of the item in self.notes
			line  = str(i) + "\n"
			# getting the value of that item in that index in the self.notes
			line += j + "\n"
			line += "By " + self.author + "\n\n"
			print(line)

	def search(self, search_text):
		# loop through the content in self.notes
		for i,j in enumerate(self.notes):
			# There should be at least one value for this operation to follow
			if j.find(search_text) != -1:
				result  = "Showing results for '" + search_text + "'\n"
				# storing the note_id in i
				result += "Note ID: " + str(i) + "\n"
				# storing the string value in j
				result += j + "\n"
				result += "By " + self.author
				print(result)

	# returning the content of the notes using the note_id index
	def get(self, note_id):
		return self.notes[note_id]

	# deleting a note using the note_id as the index
	def delete(self, note_id):
		self.notes.pop(note_id)

	# replacing content of a note at the index specified with new_content
	def edit(self, note_id, new_content):
		self.notes[note_id] = new_content



