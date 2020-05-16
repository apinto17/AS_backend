  
from rest_framework.exceptions import APIException


class LoginException(APIException):
    status_code = 401
    default_detail = "Invalid username/password."
    default_code = "invalid"


