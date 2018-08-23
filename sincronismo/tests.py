from django.test import TestCase

from .models import Base
from .models import Moodle
from .models import Suap

import json, requests

class BaseModelTests(TestCase):
    
    # def setUp(self):
    #     base = Base('http://localhost:8000', 'abcdefghijlmnopqrstuvxz', 'get_users')

    def test_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        base = Base('http://localhost:8000', 'abcdefghijlmnopqrstuvxz')
        self.assertEqual(base.getUrlBase(), 'http://localhost:8000')
        self.assertEqual(base.getToken(), 'abcdefghijlmnopqrstuvxz')
    
    def test_resource(self):
        """
        Verifica se o objeto tem o comportamento esperado quando atribuido
        algum recurso a ele.
        """
        base = Base('http://localhost', 'test')
        base.setResource('get_users')
        self.assertEqual(base.getResource(), 'get_users')
    
    def test_responseFormat(self):
        """
        Verifica se o objeto tem o comportamento esperado quando atribuido
        algum formato de resposta a ele.
        """
        base = Base('http://localhost', 'test')
        base.setResponseFormat('json')
        self.assertEqual(base.getResponseFormat(), 'json')

    def test_data(self):
        """
        Verifica se o objeto tem o comportamento esperado quando atribuido
        algum valor ao dicionario data.
        """
        base = Base('http://localhost', 'test')
        self.assertEqual(base.getData(), {})
        
        base.addData('param1', 10)
        self.assertEqual(base.getData(), {'param1': 10})

        base.addData('param2', 'test')
        self.assertEqual(base.getData(), {'param1': 10, 'param2': 'test'})
        

class MoodleModelTests(TestCase):

    def teste_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        model = Moodle()
        self.assertEqual(model.getUrlBase(), 'http://localhost:8080/moodle/webservice/rest/server.php')
        self.assertEqual(model.getToken(), '0b0c9af5bd3eba5a6fccbc3d1594376f')
        self.assertEqual(model.getResponseFormat(), 'json')
    
    def teste_criacao_de_usuario(self):
        """
        Testa criação de usuário no moodle.
        """
        model = Moodle()
        model.createUser()

class SuapModelTests(TestCase):
    
    def teste_de_sanidade(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        model = Suap()
        self.assertEqual(model.getUrlBase(), 'http://localhost:8080/moodle/webservice/rest/server.php')
        self.assertEqual(model.getToken(), '0b0c9af5bd3eba5a6fccbc3d1594376f')
        self.assertEqual(model.getResponseFormat(), 'json')