# from django.db import models

import json, requests, abc, sys

class BaseWSClient(object):
    
    def __init__(self, url_base, token):
        self.url_base = url_base
        self.token = token
        self.params = {}
        self.resource = None
        self.response_format = None
    
    def add_param(self, key, value):
        self.params[key] = value

    def get_content_json(self, content):
        return json.loads(content)

class MyABC(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def createUser(self):
        pass


class MoodleWSClient(BaseWSClient, MyABC):

    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "0b0c9af5bd3eba5a6fccbc3d1594376f"
        url_base = 'http://localhost:8080/moodle/webservice/rest/server.php'
        response_format = 'json'

        super(MoodleWSClient, self).__init__(url_base, token)
        self.response_format = response_format

        self.add_param('wstoken', self.token)
        self.add_param('moodlewsrestformat', self.response_format)

    def createUser(self, username, password, firstname, lastname, email):
        """Cria um novo usuário no Moodle.

        Args:
            username: Login do usuário que será criado.
            password: Senha do usuário.
            firstname: Primeiro nome do novo usuário.
            lastname: Último nome do novo usuário.
            email: E-mail do novo usuário.
        Returns:
            404: Página não encontrada
            ID do usuário no Moodle.
        Raises:
            TypeError: if n is not a number.
            ValueError: if n is negative.

        """
        self.resource = 'core_user_create_users'
        
        self.add_param('wsfunction', self.resource)
        self.add_param('users[0][username]', username)
        self.add_param('users[0][password]', password)
        self.add_param('users[0][createpassword]', 1)
        self.add_param('users[0][firstname]', firstname)
        self.add_param('users[0][lastname]', lastname)
        self.add_param('users[0][email]', email)

        # try:
        #    response = requests.post(self.url_base, data=self.get_data())
        #    content = self.get_content_json(response.content)
        #     if(response.status_code == 200 & self.requestException(content) == False):
        #         print({ 'request': False, 'error': False, 'data': content[0] })
        #     elif (response.status_code == 200):
        #         print({ 'request': False, 'error': True, 'data': content })
        #     else:
        #         print({ 'request': True, 'code': response.status_code })
        # except:
        #     print(sys.exc_info()[0])
        #     return sys.exc_info()[0]
    
    def request_exception(self, data):
        if 'exception' in data.keys():
            return False
        else:
            return True


class SuapWSClient(BaseWSClient):
    
    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "0b0c9af5bd3eba5a6fccbc3d1594376f"
        url_base = 'http://localhost:8080/moodle/webservice/rest/server.php'
        response_format = 'json'

        super(SuapWSClient, self).__init__(url_base, token)
        self.response_format = response_format

    def createUser(self):
        return 1
    