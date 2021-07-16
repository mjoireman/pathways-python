
from datetime import datetime
from io import DEFAULT_BUFFER_SIZE
import requests
from requests.auth import HTTPBasicAuth
import json 
from dateutil import parser
import pytz
import os

ME_SERVICE = '/api/authentication/token?isLongToken=true'
DEFAULT_BASE_URL = 'https://api.vdotp4p.com'


class Credentials:
    def __init__(self, user_name: str, password: str, base_url: str):
        self.username = user_name
        self.password = password
        self.base_url = base_url
        self.token = None
        self.token_expiration = None
    
    def __eq__(self, obj):
        return self.password == obj.password and \
               self.username == obj.username and \
               self.base_url == obj.base_url

    def __repr__(self):
        return ("Credentials(username='{username}', "
                "password='***', "
                "base_url='{base_url}')").format(username=self.username,
                                                 password=self.password,
                                                 base_url=self.base_url)
    
    def get_token(self) -> str:
        if not self._is_valid():
            self._update_token()
        return self.token

    def _update_token(self) -> None:
        endpoint = f'{self.base_url}/{ME_SERVICE}'
        response = requests.post(endpoint, auth=HTTPBasicAuth(self.username, self.password), verify=False)
        token = response.json()
        self.token = token['accessToken']
        self.token_expiration = parser.parse(token['expiry'])

    def _is_valid(self) -> bool:
        if self.token_expiration is None or datetime.now(pytz.utc) > self.token_expiration:
            return False
        return True
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as read_file:
            data = json.load(read_file)
            base_url = data['base_url'] if 'base_url' in data else DEFAULT_BASE_URL
            return cls(
                data['username'],
                data['password'],
                base_url)
    
    @classmethod
    def from_env(cls):
        user_name = os.environ['P4P_USERNAME']
        password = os.environ['P4P_PASSWORD']
        base_url = os.environ['P4P_BASE_URL'] if 'P4P_BASE_URL' in os.environ else DEFAULT_BASE_URL
        if user_name and password:
            return cls(user_name, password, base_url)
        return None
            
    
    