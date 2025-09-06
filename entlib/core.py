#entlib
#Licensed under the gpl 2.0

import requests
from .exceptions import *
from .logs import Logs

# generate fake user agent
import fake_useragent

USER_AGENT = fake_useragent.UserAgent().random
Logs.info(f"[ENTLIB/core] Welcome! \n This is in a work in progress state, so expect bugs and errors \n Feel free to contribute to the project on github : https://github.com/eletrixfr/entlib")
Logs.info(f"[ENTLIB/core/init] User agent: {USER_AGENT}")


class ENT:
    """
    Base class for interacting with the ENT account.

    Attributes:
    - username: The username (email) for the ENT account.
    - password: The password for the ENT account.
    - url: The URL of the ENT.

    Methods:
    - login(): Logs into the ENT account with the provided credentials.
    - who_ami(): Fetches the user data in JSON format.
    """
    def __init__(self, username, password,url):
        '''Initializes the ENT instance.'''
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": USER_AGENT
        })
        self.username = username
        self.password = password
        self.url = url
        self.whoami = None
        xsrf_token = "nothing"
        self.login()

    def login(self):
        '''Login to your ENT account'''
        Logs.info(f"[ENTLIB/auth/login] Logging in as {self.username[ : 5]}...")
        response = self.session.post(f"{self.url}/auth/login", data={
            "email": self.username,
            "password": self.password,
            "callBack": self.url,
            "details": ""
        })

        if response.status_code != 200:
            raise ENTLoginException("Login failed")
        self.session.cookies.update(response.cookies)
        self.xsrf_token = self.session.cookies.get("XSRF-TOKEN")
        # update the header with the xsrf token
        self.session.headers.update({
            "X-XSRF-TOKEN": self.xsrf_token
        })
        self.whoami_json = self.who_ami()
        Logs.info("[ENTLIB/auth/login] Logged in successfully")
        

    def who_ami(self):
        '''Get your user data (JSON)'''
        response = self.session.get(f"{self.url}/auth/oauth2/userinfo")
        return response.json()
    def get_myself_data(self):
        '''Idk why'''
        X = self.who_ami()
        self.whoami = X
        return X




