import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):
    def setUp(self):
        '''
        set up will run before every test
        '''
        self.new_user = User(id = 1, fullname = "Gitu Mbugua", username = "gitu", email = "gitu@testing.com", password_hash = "password")

    def test_instance(self):
        '''
        test case to check if new instance is created
        '''
        self.assertTrue(isinstance(self.new_user, User))

    def test_password_setter(self):
        '''
        test to check if password is being hashed
        '''
        self.assertTrue(self.new_user.password_hash is not None)

