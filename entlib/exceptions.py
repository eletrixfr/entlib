# Exceptions

class ENTException(Exception):
    pass

class ENTLoginException(ENTException):
    pass
class InvalidInputError(ENTException):
    pass

# API errors

class ENTAPIException(ENTException):
    pass