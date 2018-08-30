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
        self.response = { 'status': 404, 'exception': False, 'data': {} }
    
    def add_param(self, key, value):
        """ Adiciona um novo parâmetro para ser usado na requisição.
        
        Args:
            key: Parametro.
            value: Valor do parâmetro.
        """
        self.params[key] = value    
    
    def send_post(self):
        """ Envia uma requisição do tipo POST. """
        request = requests.post(self.url_base, data=self.params)
        self.request_status = request.status_code
        self.request_content = request.content
    
    def send_get(self):
        """ Envia uma requisição do tipo GET. """
        request = requests.get(self.url_base, data=self.params)
        self.request_status = request.status_code
        self.request_content = request.content

    def request_content_json(self):
        """ Callback da requisição requisição no formato JSON. """
        return json.loads(self.request_content)


class MyABC(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def create_user(self):
        pass

    @abc.abstractmethod
    def find_user(self, field):
        pass

    @abc.abstractmethod
    def check_exception_callback(self, data):
        """ Verifica se a requisicão gerou alguma exception.

        Args:
            data: Dicionário de dados com retorno da requisição.

        Returns:
            Boolean: True para excption e False para sucesso.
        """
        pass

    @abc.abstractmethod
    def get_response(self):
        """ Retorna resposta da requisição no formato JSON.

        json: Status: Código http de resposta.
              Exception: Se existe exception na requisição.
              Data: Dados gerados pela requisição.
        """
        pass


class MoodleWSClient(BaseWSClient, MyABC):

    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "0b0c9af5bd3eba5a6fccbc3d1594376f"
        url_base = 'http://localhost:8080/moodle/webservice/rest/server.php'
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
            Boolean: True para excption e False para sucesso.
        """
        data = self.request_content_json()
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

    def get_response(self):
        """ Retorna resposta da requisição no formato JSON.

        json: Status: Código http de resposta.
              Exception: Se existe exception na requisição.
              Data: Dados gerados pela requisição.
        """
        if self.request_status == 200:
            self.response['status'] = self.request_status
            self.response['exception'] = self.check_exception_callback()
            self.response['data'] = self.request_content_json()
        else:
            pass
            # self.response['status'] = self.request_status
        
        return json.dumps(self.response)

    def create_user(self, username, password, firstname, lastname, email):
        """Cria um novo usuário no Moodle.

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
        Raises:

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
    
    def find_user(self, username):
        self.request_resource = 'core_user_get_users_by_field'
        self.add_param('wsfunction', self.request_resource)
        self.add_param('field', 'username')
        self.add_param('values[0]', username)
        
        #try:
        self.send_get()
        return self.get_response()
        #except:
        #    return sys.exc_info()[0]


class SuapWSClient(BaseWSClient):
    
    def __init__(self):
        pass
