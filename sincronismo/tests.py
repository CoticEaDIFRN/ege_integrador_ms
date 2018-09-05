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
        self.assertEqual(self.model.request_format, 'json')
        self.assertEqual(self.model.url_base, 'http://localhost:8080/moodle/webservice/rest/server.php')
        self.assertEqual(self.model.token, '0b0c9af5bd3eba5a6fccbc3d1594376f')
    
    def test_create_user(self):
        """
        Testa criação de usuário no moodle.
        """
        self.model.create_user('ptest', 'ptest', 'python', 'test', 'aaa@aaa.com')
        r_json = self.model.request_content_json()

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['username'], 'ptest')
    
    def test_create_user_exception(self):
        """
        Testa falha criação de usuário no moodle.
        """
        self.model.create_user('admin', 'ptest', 'python', 'test', 'aaa@aaa.com')
        r_json = self.model.request_content_json()

        self.assertTrue(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json['exception'], 'invalid_parameter_exception')
    
    def test_update_user(self):
        """
        Testa atualização de usuário no moodle.
        """
        self.model.update_user(2, None, 'Unit', 'Test')
        r_json = self.model.request_content_json()
        
        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertIsNone(r_json)
        
    def test_find_user(self):
        """
        Testa busca de usuário no moodle.
        """
        self.model.find_user('ptest')
        r_json = self.model.request_content_json()

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['username'], 'ptest')
        self.assertEqual(r_json[0]['firstname'], 'python')

    def test_find_user_no_exist(self):
        """
        Testa falha na busca de usuário no moodle.
        """
        self.model.find_user('naoexiste')
        r_json = self.model.request_content_json()

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json, [])
    
    def test_create_course(self):
        self.model.create_course('Curso 1', 'curso1', 1)
        r_json = self.model.request_content_json()
        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['categoryid'], 1)
        self.assertEqual(r_json[0]['shortname'], 'curso1')
        
    
    def test_create_category(self):
        self.model.create_category( 1, 'Categoria 1', 'Teste da criação da Categoria 1')
        r_json = self.model.request_content_json()
        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['name'], 'Categoria 1')
    

class SuapWSClientModelTests(TestCase):
    
    def test_init(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        pass