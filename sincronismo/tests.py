from django.test import TestCase

from .models import BaseWSClient
from .models import MoodleWSClient
from .models import SuapWSClient

import json, requests

class BaseWSClientModelTests(TestCase):
    
    def setUp(self):
        self.base = BaseWSClient('http://localhost:8000', 'abcdefghijlmnopqrstuvxz')
        self.base.add_param('param1', 10)
        self.base.add_param('param2', 'test')

    def test_init(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        self.assertEqual(self.base.url_base, 'http://localhost:8000')
        self.assertEqual(self.base.token, 'abcdefghijlmnopqrstuvxz')

    def test_add_param(self):
        """
        Verifica se o objeto tem o comportamento esperado quando atribuido
        algum valor ao dicionario data.
        """
        
        self.assertEqual(self.base.params, {'param1': 10, 'param2': 'test'})

    def test_resource(self):
        """
        Verifica se o objeto tem o comportamento esperado quando atribuido
        algum recurso a ele.
        """
        self.base.resource = 'get_users'
        self.assertEqual(self.base.resource, 'get_users')
        

class MoodleWSClientModelTests(TestCase):

    def setUp(self):
        self.model = MoodleWSClient()

    def test_init(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        self.assertEqual(model.request_format, 'json')
    
    def test_create_user(self):
        """
        Testa criação de usuário no moodle.
        """
        model = MoodleWSClient()
        response = model.create_user('ptest', 'ptest', 'python', 'test', 'aaa@aaa.com')
        self.assertEqual(response, '{"status": 200, "exception": false, "data": [{"id": 31, "username": "ptest"}]}')

    def test_create_courses(self):
        model = MoodleWSClient()
        response = model.create_course('Ptest','ptest','1')
        self.assertEqual(response, '{"status": 200, "exception": false, "data"}')

class SuapWSClientModelTests(TestCase):
    
    def test_init(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        pass