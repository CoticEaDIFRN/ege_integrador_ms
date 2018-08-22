# from django.db import models

import json, requests

class Base(object):
    
    def __init__(self, urlBase, token):
        # super(Base, self).__init__()
        self._urlBase = urlBase
        self._token = token
    
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


class Moodle(Base):

    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "0b0c9af5bd3eba5a6fccbc3d1594376f"
        urlBase = 'http://localhost:8080/moodle/webservice/rest/server.php'
        responseFormat = 'json'

        super(Moodle, self).__init__(urlBase, token)
        self.setResponseFormat(responseFormat)


class Suap(Base):
    
    def __init__(self):
        # TODO Colocar em arquivo de configuração da app
        token = "0b0c9af5bd3eba5a6fccbc3d1594376f"
        urlBase = 'http://localhost:8080/moodle/webservice/rest/server.php'
        responseFormat = 'json'

        super(Suap, self).__init__(urlBase, token)
        self.setResponseFormat(responseFormat)

    