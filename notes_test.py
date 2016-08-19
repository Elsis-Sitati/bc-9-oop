import unittest
from notes_application import NotesApplication

class TestNotesApplication(unittest.TestCase):
	# testing to see if it creates objects
	def test_if_object_is_instance(self): 
		x = NotesApplication('AuthorName')
		self.assertIsInstance(x, NotesApplication)

    # testing to see if it returns the right auther
	def test_if_auther_is_registred(self):
		y = NotesApplication ("Kimani")
		self.assertEqual(y.author, 'Kimani')



if __name__ == "__main__":
	unittest.main()