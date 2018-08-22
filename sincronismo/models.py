# from django.db import models

import json, requests

class Base(object):
    
    def __init__(self, urlBase, token, resource):
        self._urlBase = urlBase
        self._token = token
        self._resource = resource
    
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

class Moodle(Base):

    def __init__(self, urlBase, token, resource):
        super(Moodle, self).__init__(urlBase, token, resource)

class Suap(Base):
    
    def __init__(self, urlBase, token, resource):
        super(Suap, self).__init__(urlBase, token, resource)
    