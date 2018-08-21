from django.test import TestCase

from .models import Base
from .models import Moodle

class BaseModelTests(TestCase):
    
    # def setUp(self):
    #     base = Base('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')

    def teste_de_sanidade(self):
        """
        Teste se o objeto está se comportando como deveria.
        """
        base = Base('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')
        self.assertEqual(base.getUrlBase(), 'http://localhost:8000')
        self.assertEqual(base.getToken(), 'abcdefghijlmnopqrstuvxz')
        self.assertEqual(base.getResource(), 'get_users')

class MoodleModelTests(TestCase):

    def teste_de_sanidade(self):
        """
        Teste se o objeto está se comportando como deveria.
        """
        moodle = Moodle('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')
        self.assertEqual(moodle.getUrlBase(), 'http://localhost:8000')
        self.assertEqual(moodle.getToken(), 'abcdefghijlmnopqrstuvxz')
        self.assertEqual(moodle.getResource(), 'get_users')