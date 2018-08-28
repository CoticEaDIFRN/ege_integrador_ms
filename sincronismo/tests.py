from django.test import TestCase

from .models import BaseWSClient
from .models import MoodleWSClient
from .models import SuapWSClient

import json, requests

class BaseModelTests(TestCase):
    
    # def setUp(self):
    #     base = Base('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')

    def test_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        base = BaseWSClient('http://localhost:8000', 'abcdefghijlmnopqrstuvxz')
        self.assertEqual(base.url_base, 'http://localhost:8000')
        self.assertEqual(base.token, 'abcdefghijlmnopqrstuvxz')
    
    def test_resource(self):
        """
        Verifica se o objeto tem o comportamento esperado quando atribuido
        algum recurso a ele.
        """
        base = BaseWSClient('http://localhost', 'test')
        base.resource = 'get_users'
        self.assertEqual(base.resource, 'get_users')
    
    def test_response_format(self):
        """
        Verifica se o objeto tem o comportamento esperado quando atribuido
        algum formato de resposta a ele.
        """
        base = BaseWSClient('http://localhost', 'test')
        base.response_format = 'json'
        self.assertEqual(base.response_format, 'json')

    def test_data(self):
        """
        Verifica se o objeto tem o comportamento esperado quando atribuido
        algum valor ao dicionario data.
        """
        base = BaseWSClient('http://localhost', 'test')
        self.assertEqual(base.params, {})
        
        base.add_param('param1', 10)
        self.assertEqual(base.params, {'param1': 10})

        base.add_param('param2', 'test')
        self.assertEqual(base.params, {'param1': 10, 'param2': 'test'})
        

class MoodleModelTests(TestCase):

    def teste_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        model = MoodleWSClient()
        self.assertEqual(model.url_base, 'http://localhost:8080/moodle/webservice/rest/server.php')
        self.assertEqual(model.token, '0b0c9af5bd3eba5a6fccbc3d1594376f')
        self.assertEqual(model.response_format, 'json')
    
    def teste_criacao_de_usuario(self):
        """
        Testa criação de usuário no moodle.
        """
        model = MoodleWSClient()
        model.create_user('ptest', 'ptest', 'python', 'test', 'aaa@aaa.com')

class SuapModelTests(TestCase):
    
    def teste_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        model = SuapWSClient()
        self.assertEqual(model.url_base, 'http://localhost:8080/moodle/webservice/rest/server.php')
        self.assertEqual(model.token, '0b0c9af5bd3eba5a6fccbc3d1594376f')
        self.assertEqual(model.response_format, 'json')