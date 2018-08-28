# from django.db import models

import json, requests, abc, sys

class BaseWSClient(object):
    
    def __init__(self, url_base, token):
        self.url_base = url_base
        self.token = token
        self.params = {}
        self.resource = None
        self.request_format = None
        self.request_status = None
        self.request_content = None
        self.response = None
    
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
    
    def request_content_json(self):
        """ Callback da requisição requisição no formato JSON. """
        return json.loads(self.request_content)


class MyABC(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def create_user(self):
        pass

    @abc.abstractmethod
    def check_exception_callback(self, data):
        """ Verifica se a requisicão gerou alguma exception.

        Args:
            data: Dados de retorno da requisição.

        Returns:
            Boolean: True para excption e False para sucesso.
        """
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

    def check_exception_callback(self, data):
        """ Verifica se a requisição gerou alguma exception.

        Args:
            data: Dados de retorno da requisição.

        Returns:
            Boolean: True para excption e False para sucesso.
        """
        if 'exception' in data.keys():
            return True
        else:
            return False
            
    def create_user(self, username, password, firstname, lastname, email):
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

        try:
            self.send_post()
            print(self.request_status)
            print(self.request_content)
            print(self.request_content_json())
            # response = requests.post(self.url_base, data=self.params)
            # self.send_post()
            # if self.status_request() == 200:
            #     print(self.callback_json())
            # else:
                
                
                
            # print(self.callback())
            # print(self.check_exception_callback(self.callback_json()))

            # if response.status_code == 200 :
            #     print('ok')
            # else:
            #     print('erro')
            # content = self.get_content_json(response.content)
            # print(response.status_code)
            # print(content)
            # print('aki')
        #     if(response.status_code == 200 & self.requestException(content) == False):
        #         print({ 'request': False, 'error': False, 'data': content[0] })
        #     elif (response.status_code == 200):
        #         print({ 'request': False, 'error': True, 'data': content })
        #     else:
        #         print({ 'request': True, 'code': response.status_code })
        except:
            print(sys.exc_info()[0])
            return sys.exc_info()[0]


class SuapWSClient(BaseWSClient):
    
    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "0b0c9af5bd3eba5a6fccbc3d1594376f"
        url_base = 'http://localhost:8080/moodle/webservice/rest/server.php'
        response_format = 'json'

        super(SuapWSClient, self).__init__(url_base, token)
        self.response_format = response_format

    