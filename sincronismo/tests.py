from django.test import TestCase

from .models import Base
from .models import Moodle

class BaseModelTests(TestCase):
    
    # def setUp(self):
    #     base = Base('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')

    def teste_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        base = Base('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')
        self.assertEqual(base.getUrlBase(), 'http://localhost:8000')
        self.assertEqual(base.getToken(), 'abcdefghijlmnopqrstuvxz')
        self.assertEqual(base.getResource(), 'get_users')

class MoodleModelTests(TestCase):

    def teste_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        model = Moodle('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')
        self.assertEqual(model.getUrlBase(), 'http://localhost:8000')
        self.assertEqual(model.getToken(), 'abcdefghijlmnopqrstuvxz')
        self.assertEqual(model.getResource(), 'get_users')

class SuapModelTests(TestCase):
    
    def teste_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        model = Moodle('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')
        self.assertEqual(model.getUrlBase(), 'http://localhost:8000')
        self.assertEqual(model.getToken(), 'abcdefghijlmnopqrstuvxz')
        self.assertEqual(model.getResource(), 'get_users')