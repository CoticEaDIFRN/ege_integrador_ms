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
    
    def test_create_user(self):
        """
        Testa criação de usuário no moodle.
        """
        self.model.create_user('ptest', 'ptest', 'python', 'test', 'aaa@aaa.com')
        r_json = self.model.request_json

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['username'], 'ptest')
    
    def test_create_user_exception(self):
        """
        Testa falha criação de usuário no moodle.
        """
        self.model.create_user('admin', 'ptest', 'python', 'test', 'aaa@aaa.com')
        r_json = self.model.request_json

        self.assertTrue(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json['exception'], 'invalid_parameter_exception')
    
    def test_update_user(self):
        """
        Testa atualização de usuário no moodle.
        """
        self.model.update_user(2, None, 'Unit', 'Test')
        r_json = self.model.request_json
        
        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertIsNone(r_json)

    def test_update_user_no_exist(self):
        """
        Testa atualização de usuário que não existe no moodle.
        """
        self.model.update_user(7000, None, 'Unit', 'Test')
        r_json = self.model.request_json
        
        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertIsNone(r_json)
        
    def test_find_user(self):
        """
        Testa busca de usuário no moodle.
        """
        self.model.find_user('ptest')
        r_json = self.model.request_json

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['username'], 'ptest')
        self.assertEqual(r_json[0]['firstname'], 'python')

    def test_find_user_no_exist(self):
        """
        Testa falha na busca de usuário no moodle.
        """
        self.model.find_user('naoexiste')
        r_json = self.model.request_json

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json, [])
    
    def test_enrol_user(self):
        """
        Associa usuário a um curso do moodle.
        """
        self.model.enrol_user(2, 2, 3)
        r_json = self.model.request_json

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertIsNone(r_json)

    def test_enrol_user_no_exist(self):
        """
        Associa usuário a um curso do moodle.
        """
        self.model.enrol_user(7000, 2, 3)
        r_json = self.model.request_json

        self.assertTrue(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json['exception'], 'coding_exception')
        self.assertEqual(r_json['errorcode'], 'codingerror')

    def test_enrol_user_course_no_exist(self):
        """
        Associa usuário a um curso do moodle.
        """
        self.model.enrol_user(2, 7000, 3)
        r_json = self.model.request_json

        self.assertTrue(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json['exception'], 'invalid_parameter_exception')
        self.assertEqual(r_json['errorcode'], 'invalidparameter')
    
    def test_enrol_user_role_no_exist(self):
        """
        Associa usuário a um curso do moodle.
        """
        self.model.enrol_user(2, 2, 30000)
        r_json = self.model.request_json

        self.assertTrue(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json['exception'], 'moodle_exception')
        self.assertEqual(r_json['errorcode'], 'wsusercannotassign')
    
    def test_get_enrolled_users_in_course(self):
        """
        Retorna lista de usuários associados curso do moodle.
        """
        self.model.get_enrolled_users_in_course(2)
        r_json = self.model.request_json

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['id'], 2)

    def test_get_enrolled_users_in_course_no_exist(self):
        """
        Retorna lista de usuários associados curso do moodle.
        """
        self.model.get_enrolled_users_in_course(20000)
        r_json = self.model.request_json

        self.assertTrue(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json['exception'], 'dml_missing_record_exception')
        self.assertEqual(r_json['errorcode'], 'invalidrecord')

    def test_create_course(self):
        self.model.create_course('Curso_1', 'curso1', 1)
        r_json = self.model.request_json

        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['categoryid'], 1)
        self.assertEqual(r_json[0]['shortname'], 'curso1')
        
    
    def test_create_category(self):
        self.model.create_category( 1, 'Categoria 1', 'Teste da criação da Categoria 1')
        r_json = self.model.request_json
        
        self.assertFalse(self.model.response['exception'])
        self.assertEqual(self.model.response['status'], 200)
        self.assertEqual(r_json[0]['name'], 'Categoria 1')
    

class SuapWSClientModelTests(TestCase):
    
    def test_init(self):
        """
        Verifica se o objeto tem o comportamento padrão esperado.
        """
        pass