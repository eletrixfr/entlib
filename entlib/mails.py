#entlib
# Licensed under the GPL 2.0 license

import requests
from .exceptions import *
from .logs import Logs
class SendMail:
    """
    A class for sending emails through the ENT.

    Attributes:
    - ent: An instance of the ENT class to manage the session.
    - body: The content of the email to be sent.
    - subject: The subject of the email.
    - to: A list of email (UUID) recipients.

    Methods:
    - send(): Sends the email with the specified content, subject, and recipients.
    """
    def __init__(self,ent,body,subject,to=["to"]):
        '''Initializes the SendMail instance.'''

        self.ent = ent
        self.body = body
        self.subject = subject
        self.to = to
    def send(self):
        '''Send the mail'''
        x =self.ent.session.post(f"{self.ent.url}/conversation/send")
        Logs.info("[ENTLIB/conversation/send] Sending mail to "+str(self.to))
        r = self.ent.session.post(
            f'{self.ent.url}/conversation/send#/inbox',
            json={"body": self.body, "cc": [], "cci": [], "subject": self.subject, "to": self.to}
        )
        print(r.text)
class Mail():
    """
    A class for retrieving emails from the ENT.

    Attributes:
    - ent: An instance of the ENT class to manage the session.

    Methods:
    - get_mail_list(): Retrieves a list of emails, with the option to filter by unread status.
    - get_mail_data(): Retrieves detailed data for a specific email by ID.
    """
    def __init__(self,ent):
        self.ent = ent
    def get_mail_list(self,unread=True):
       X = self.ent.session.get(f"{self.ent.url}/conversation/list/inbox?page=0&unread="+str(unread))
       if X.status_code != 200:
           raise ENTLoginException("Login failed")
       messages = X.json()
       return messages
    def get_mail_data(self,id):
        '''Fetches detailed data for an email by its ID. Use get_mail_list() to get the ID.'''

        x = self.ent.session.get(f"{self.ent.url}/conversation/message/"+str(id))
        if x.status_code != 200:
            raise ENTLoginException("Login failed")
        
        return x.json()