#entlib
# Licensed under the GPL 2.0 license

import requests
from .exceptions import *


class User:
    '''Get user information
    
    Attributes:
    - ent: An instance of the ENT class to manage the session.
    - user_id: The user ID of the user to retrieve information for.

    Methods:
    - get_user_json(): Retrieves the user's JSON data.
    - get_profile_json(): Retrieves the user's profile JSON data.
    - get_name(): Retrieves the user's name.
    - get_id(): Retrieves the user's ID.
    - get_email(): Retrieves the user's email. (if public)
    - get_phone(): Retrieves the user's phone number. (if public)
    - birthday(): Retrieves the user's birthday. (if public)
    - profile_picture(): Retrieves the user's profile picture URL.

    (REWRITE SOON)

    '''
    def __init__(self, ent, user_id):
        '''Initializes the User instance.'''
        self.ent = ent
        self.user_id = user_id
        self.session = ent.session  
        self.userjson = self.get_user_json()
        self.profile_json = self.get_profile_json()
    def get_user_json(self):
        response = self.session.get(f"{self.ent.url}/auth/oauth2/userinfo")  
        if response.status_code != 200:
            raise InvalidInputError("Invalid user id")
        return response.json()
    def get_profile_json(self):

        response = self.session.get(f"{self.ent.url}/userbook/api/person?id={self.user_id}")
        if response.status_code != 200:
            raise InvalidInputError("Invalid user id")
        return response.json()

    def get_name(self):
        '''Get the user's name'''
        X = self.userjson
        return X["firstName"] + " " + X["lastName"]
    def get_id(self):
        '''Get the user's ID'''
        X = self.userjson
        return X["userId"]
    def get_email(self):
        '''Get the user's email'''
        X = self.userjson
        return X["email"]
    def get_phone(self):
        '''Get the user's phone number (return none is the user doesn't have a phone number)'''
        X = self.userjson
        if X["mobile"] == "":
            return None
        return X["mobile"]
    def birthday(self):
        'Return the user birthday'
        X = self.userjson
        return X["birthDate"]
    
    def profile_picture(self):
        X = self.get_user_json
        return f"{self.ent.url}/userbook/avatar/{self.user_id}"