import io
import sys
from dog import Dog

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog".'''
        fido = Dog("Fido", "Labrador")
        assert type(fido) == Dog
        
    def test_name_not_empty(self):
        '''prints "Name must be a string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="", breed="Labrador")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    # ... other test methods ...
