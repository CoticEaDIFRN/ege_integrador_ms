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
        response = self.model.create_user('ptest', 'ptest', 'python', 'test', 'aaa@aaa.com')
        r_json = self.model.request_content_json()

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['username'], 'ptest')

    def test_create_user_exception(self):
        """
        Testa falha criação de usuário no moodle.
        """
        response = self.model.create_user('admin', 'ptest', 'python', 'test', 'aaa@aaa.com')
        r_json = self.model.request_content_json()

        self.assertTrue(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json['exception'], 'invalid_parameter_exception')
    
    def test_find_user(self):
        """
        Testa busca de usuário no moodle.
        """
        response = self.model.find_user('ptest')
        r_json = self.model.request_content_json()

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['username'], 'ptest')
        self.assertEqual(r_json[0]['firstname'], 'python')

    def test_find_user_no_exist(self):
        """
        Testa falha na busca de usuário no moodle.
        """
        response = self.model.find_user('naoexiste')
        r_json = self.model.request_content_json()

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json, [])

    def test_create_courses(self):
        model = MoodleWSClient()
        response = model.create_course('fullname', 'shortname', 'categoryid')
        self.assertEqual(response, '{"status": 200, "exception": false, "data": [{"id": 5, "shortname": "curso1"}]}')


class SuapWSClientModelTests(TestCase):
    
    def test_init(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        pass