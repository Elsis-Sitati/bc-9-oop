class NotesApplication(object):


	def __init__(self, author, notes=[]):
		self.author = author
		self.notes = notes
    
    # take parameter note_content and adds new note data to the list  notes

	def create(self, notes_content):
		self.notes.append(notes_content)


	def list(self):
		for i, j in enumerate(self.notes):
			line  = str(i) + "\n"
			line += j + "\n"
			line += "By " + self.author + "\n\n"
			print(line)

	def search(self, search_text):
		for i,j in enumerate(self.notes):
			if j.find(search_text) != -1:
				result  = "Showing results for '" + search_text + "'\n"
				result += "Note ID: " + str(i) + "\n"
				result += j + "\n"
				result += "By " + self.author
				print(result)

	def get(self, note_id):
		return self.notes[note_id]

	def delete(self, note_id):
		self.notes.pop(note_id)

	def edit(self, note_id, new_content):
		self.notes[note_id] = new_content



