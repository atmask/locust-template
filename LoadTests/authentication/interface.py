
from abc import abstractmethod
from locust import HttpUser

class IAuthUser(HttpUser):
    '''Extends HTTPUser. This provides us with a client that is an instance of an HTTPSession for preserving authentication'''

    def __init__(self, username, password, environment):
        self.username =username
        self.password = password
        super().__init__(environment)

    def on_start(self):
        self.login()

    @abstractmethod
    def login(self):
        '''Login the user in through the auth mechanism'''
