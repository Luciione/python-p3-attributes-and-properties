import io
import sys
from person import Person

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person".'''
        eve = Person("Eve", "Admin")
        assert type(eve) == Person
        
    def test_name_not_empty(self):
        '''prints "Name must be a string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person("", "Admin")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    # ... other test methods ...
