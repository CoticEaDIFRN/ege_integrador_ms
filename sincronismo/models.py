# from django.db import models

import json, requests, abc, sys

class BaseWSClient(object):
    
    def __init__(self, url_base, token):
        self.url_base = url_base
        self.token = token
        self.params = {}
        self.request_resource = None
        self.request_format = None
        self.request_status = None
        self.request_content = None
        self.request_json = None
        self.response = { 'status': 404, 'exception': False, 'data': None }
    
    def add_param(self, key, value):
        """ Adiciona um novo parâmetro para ser usado na requisição.
        
        Args:
            key: Parâmetro.
            value: Valor do parâmetro.
        """
        self.params[key] = value
    
    def send_post(self):
        """ Envia uma requisição do tipo POST. """
        request = requests.post(self.url_base, data=self.params)
        self.request_status = request.status_code
        self.request_content = request.content
        self.request_json = request.json()

    def send_put(self):
        """ Envia uma requisição do tipo PUT. """
        request = requests.put(self.url_base, params=self.params)
        self.request_status = request.status_code
        self.request_content = request.content
        self.request_json = request.json()
    
    def send_get(self):
        """ Envia uma requisição do tipo GET. """
        request = requests.get(self.url_base, params=self.params)
        self.request_status = request.status_code
        self.request_content = request.content
        self.request_json = request.json()


class MyABC(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def create_user(self):
        """ Cria um novo usuário """
        pass

    @abc.abstractmethod
    def find_user(self, field):
        """ Busca um usuário """
        pass

    @abc.abstractmethod
    def update_user(self):
        """ Atualiza um usuário """
        pass

    @abc.abstractmethod
    def enrol_user(self):
        """ Associa um usuário a uma curso """
        pass

    @abc.abstractmethod
    def create_course(self):
        """ Cria um novo curso """
        pass

    @abc.abstractmethod
    def find_course(self):
        """ Busca um curso """
        pass
    
    @abc.abstractmethod
    def update_course(self):
        """ Atualiza um curso """
        pass

    @abc.abstractmethod
    def create_category(self):
        """ Cria um nova categoria """
        pass

    @abc.abstractmethod
    def find_category(self):
        """ Busca uma categoria """
        pass

    @abc.abstractmethod
    def update_category(self):
        """ Atualiza um categoria """
        pass

    @abc.abstractmethod
    def check_exception_callback(self, data):
        """ Verifica se a requisicão gerou alguma exception. """
        pass


class MoodleWSClient(BaseWSClient, MyABC):

    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "d34003902dcde0571356b513d4a1a03d"
        url_base = 'http://localhost/moodle/webservice/rest/server.php'
        request_format = 'json'

        super(MoodleWSClient, self).__init__(url_base, token)
        self.request_format = request_format
        self.add_param('wstoken', self.token)
        self.add_param('moodlewsrestformat', self.request_format)

    def check_exception_callback(self):
        """ Verifica se a requisição gerou alguma exception.

        Args:
            data: Dicionário de dados com retorno da requisição.

        Returns:
            Boolean: True para exception e False para sucesso.
        """
        data = self.request_json
        if isinstance(data, dict):
            if 'exception' in data.keys():
                return True
            else:
                return False
        elif isinstance(data, list):
            if 'exception' in data[0].keys():
                return True
            else:
                return False
        else:
            return False

    def get_response(self):
        """ Retorna resposta da requisição no formato JSON.

        json: Status: Código http de resposta.
              Exception: Se existe exception na requisição.
              Data: Dados gerados pela requisição.
        """
        if self.request_status == 200:
            self.response['status'] = self.request_status
            self.response['exception'] = self.check_exception_callback()
            self.response['data'] = self.request_json
        else:
            self.response['status'] = self.request_status
        
        return json.dumps(self.response)

    def create_user(self, username, password, firstname, lastname, email):
        """
        Cria um novo usuário no Moodle.

        Args:
            username: Login do usuário que será criado.
            password: Senha do usuário.
            firstname: Primeiro nome do novo usuário.
            lastname: Último nome do novo usuário.
            email: E-mail do novo usuário.

        Returns:
            json: Status: Código http de resposta.
                  Exception: Se existe exception na requisição.
                  Data: Dados gerados pela requisição.

        """
        self.request_resource = 'core_user_create_users'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('users[0][username]', username)
        self.add_param('users[0][password]', password)
        self.add_param('users[0][createpassword]', 1)
        self.add_param('users[0][firstname]', firstname)
        self.add_param('users[0][lastname]', lastname)
        self.add_param('users[0][email]', email)

        try:
            self.send_post()
            return self.get_response()
        except:
            return sys.exc_info()[0]
    
    def update_user(self, user_id, username=None, firstname=None, lastname=None, email=None):
        """
        Atualiza um usuário no Moodle.

        Args
            user_id: Id do usuário que será atualizado.
            username: Novo login do usuário.
            firstname: Novo primeiro nome do usuário.
            lastname: Novo último nome do usuário.
            email: Novo e-mail do usuário.

        Returns:
            json: Status: Código http de resposta.
                  Exception: Se existe exception na requisição.
                  Data: Dados gerados pela requisição.

        """
        self.request_resource = 'core_user_update_users'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('users[0][id]', user_id)
        
        if username is not None:
            self.add_param('users[0][username]', username)
        if firstname is not None:
            self.add_param('users[0][firstname]', firstname)
        if lastname is not None:
            self.add_param('users[0][lastname]', lastname)
        if email is not None:
            self.add_param('users[0][email]', email)

        try:
            self.send_put()
            return self.get_response()
        except:
           return sys.exc_info()[0]

    def find_user(self, username):
        """
        Busca um usuário no Moodle.

        Args:
            username: Login do usuário.

        Returns:
            json: Status: Código http de resposta.
                  Exception: Se existe exception na requisição.
                  Data: Dados gerados pela requisição.

        """
        self.request_resource = 'core_user_get_users_by_field'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('field', 'username')
        self.add_param('values[0]', username)

        try:
            self.send_get()
            return self.get_response()
        except:
           return sys.exc_info()[0]
    
    def enrol_user(self, user_id, course_id, role_id):
        self.request_resource = 'enrol_manual_enrol_users'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('enrolments[0][courseid]', course_id)
        self.add_param('enrolments[0][roleid]', role_id)
        self.add_param('enrolments[0][userid]', user_id)

        try:
            self.send_post()
            return self.get_response()
        except:
           return sys.exc_info()[0]

    def get_enrolled_users_in_course(self, course_id):
        self.request_resource = 'core_enrol_get_enrolled_users'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('courseid', course_id)

        try:
            self.send_get()
            return self.get_response()
        except:
           return sys.exc_info()[0]

    def create_course(self, fullname, shortname, categoryid):
        self.request_resource = 'core_course_create_courses'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('courses[0][fullname]', fullname)
        self.add_param('courses[0][shortname]', shortname)
        self.add_param('courses[0][categoryid]', categoryid)
        
        try:
            self.send_post()
            return self.get_response()
        except:
            return sys.exc_info()[0]

    def find_course(self, shortname ):
        self.request_resource = 'core_course_get_courses_by_field'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('field', 'shortname')
        self.add_param('values[0]', shortname)

        try:
            self.send_get()
            return self.get_response()
        except:
           return sys.exc_info()[0]

    def update_course(self, course_id, fullname=None, shortname=None, category_id=None):
        self.request_resource = 'core_course_update_courses'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('courses[0][id]', course_id)
        
        if fullname is not None:
            self.add_param('courses[0][fullname]', fullname)
        if shortname is not None:
            self.add_param('courses[0][shortname]', shortname)
        if category_id is not None:
            self.add_param('courses[0][categoryid]', category_id)

        try:
            self.send_put()
            return self.get_response()
        except:
           return sys.exc_info()[0]

    def create_category(self, name, description):
        
        self.request_resource = 'core_course_create_categories'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('categories[0][name]', name)
        self.add_param('categories[0][description]', description)

        try:
            self.send_post()
            return self.get_response()
        except:
            return sys.exc_info()[0]

    def find_category(self, name ):
        self.request_resource = 'core_course_get_categories'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('field', 'name')
        self.add_param('values[0]', name)

        try:
            self.send_get()
            return self.get_response()
        except:
           return sys.exc_info()[0]

    def update_category(self, category_id, name=None, description=None):
        self.request_resource = 'core_course_update_categories'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('categories[0][id]', category_id)
        
        if name is not None:
            self.add_param('categories[0][name]', name)
        if description is not None:
            self.add_param('categories[0][description]', description)

        try:
            self.send_put()
            return self.get_response()
        except:
           return sys.exc_info()[0]


class SuapWSClient(BaseWSClient):
    
    def __init__(self):
        pass

    