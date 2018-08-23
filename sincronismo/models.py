# from django.db import models

import json, requests, abc, sys

class Base(object):
    
    def __init__(self, urlBase, token):
        self._urlBase = urlBase
        self._token = token
        self._data = {}
    
    def getUrlBase(self):
        return self._urlBase
    
    def setUrlBase(self, urlBase):
        self._urlBase = urlBase

    def getToken(self):
        return self._token
    
    def setToken(self, token):
        self._token = token

    def getResource(self):
        return self._resource
    
    def setResource(self, resource):
        self._resource = resource

    def getResponseFormat(self):
        return self._responseFormat
    
    def setResponseFormat(self, responseFormat):
        self._responseFormat = responseFormat

    def getData(self):
        return self._data
    
    def addData(self, key, value):
        self._data[key] = value

    def getContentJson(self, content):
        return json.loads(content)

class MyABC(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def createUser(self):
        pass


class Moodle(Base, MyABC):

    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "0b0c9af5bd3eba5a6fccbc3d1594376f"
        urlBase = 'http://localhost:8080/moodle/webservice/rest/server.php'
        responseFormat = 'json'

        super(Moodle, self).__init__(urlBase, token)
        self.setResponseFormat(responseFormat)

        self.addData('wstoken', self.getToken())
        self.addData('moodlewsrestformat', self.getResponseFormat())

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
        self.setResource('core_user_create_users')
        
        self.addData('wsfunction', self.getResource())
        self.addData('users[0][username]', username)
        self.addData('users[0][password]', password)
        self.addData('users[0][createpassword]', 1)
        self.addData('users[0][firstname]', firstname)
        self.addData('users[0][lastname]', lastname)
        self.addData('users[0][email]', email)

        try:
            response = requests.post(self.getUrlBase(), data=self.getData())
            content = self.getContentJson(response.content)
            if(response.status_code == 200 & self.requestException(content) == False):
                print({ 'request': False, 'error': False, 'data': content[0] })
            elif (response.status_code == 200):
                print({ 'request': False, 'error': True, 'data': content })
            else:
                print({ 'request': True, 'code': response.status_code })
        except:
            print(sys.exc_info()[0])
            return sys.exc_info()[0]
    
    def requestException(self, data):
        if 'exception' in data.keys():
            return False
        else:
            return True


class Suap(Base):
    
    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "0b0c9af5bd3eba5a6fccbc3d1594376f"
        urlBase = 'http://localhost:8080/moodle/webservice/rest/server.php'
        responseFormat = 'json'

        super(Suap, self).__init__(urlBase, token)
        self.setResponseFormat(responseFormat)

    def createUser(self):
        return 1
    