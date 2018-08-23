# from django.db import models

import json, requests, abc

class Base(object):
    
    def __init__(self, urlBase, token):
        # super(Base, self).__init__()
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

    def createUser(self):
        self.setResource('core_user_create_users')
        
        self.addData('wstoken', self.getToken())
        self.addData('wsfunction', self.getResource())
        self.addData('users[0][username]', 'ptest')
        self.addData('users[0][password]', 'ptest')
        self.addData('users[0][createpassword]', 1)
        self.addData('users[0][firstname]', 'Python')
        self.addData('users[0][lastname]', 'Test')
        self.addData('users[0][email]', 'ptest@example.com')

        response = requests.post(self.getUrlBase(), data=self.getData())
    


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
    