import unittest
from notes_application import NotesApplication


class TestNotesApplication(unittest.TestCase):
    # testing to see if it creates objects
    def test_if_object_is_instance(self):
        x = NotesApplication('AuthorName')
        self.assertIsInstance(x, NotesApplication)

    # testing to see if it returns the right auther
    def test_if_auther_is_registred(self):
        y = NotesApplication("Kimani")
        self.assertEqual(y.author, 'Kimani')

    # test to see if it creates list
    def test_if_it_creates_list(self):
        author = NotesApplication('Rehema')
        author.create('The Notebook')
        self.assertIn('The Notebook', author.list())

    # test to see if second parameter is a list
    def test_if_parameter_is_a_list(self):
        author = 'Rehema Mkazi'
        notes_list = [
            "I dont think there is a better learning environment than andela"]
        note_application = NotesApplication(author, notes_list)
        self.assertEqual(type(noteApp.notes), list,
                         msg='Second argument should be a list.')
        with self.assertRaises(TypeError):
            author = 'Another Author'
            notes_list = ''
            note_application = NotesApplication(author, notes_list)

    # test to see if create method is called with one argument
    def test_if_create_method_is called_with_one_argument(self):
        with self.assertRaises(TypeError):
            note_application = NotesApplication(
                'Ronaldo', ['I am better than Messi ', 'Ozil made me shine'])
            note_application.create('')

    # test to confirm constructor takes in two arguments
    def test_if_only_one_argument_in_constructor(self):
        with self.assertRaises(TypeError):
            author = 'Prof Nandaa'
            note_application = NotesApplication(author)

    # test to ensure that the object is instantiated with arguments
    def test_if_constructor_has_arguments(self):
        with self.assertRaises(TypeError):
            note_application = NotesApplication()
    # test to see it deletes
    def test_if_note_is_deleted(self):
        author = 'Elsis'
        notes_list = ['I am testing this']
        note_application = NotesApplication(author, notes_list)
        note_application.create('Arsenal is cool')
        self.assertEqual(note_application.delete(
            0), 'Successful Deletion!', msg="Deletion Failed!")


if __name__ == "__main__":
    unittest.main()
