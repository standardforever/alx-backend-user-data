#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar

""" Creating An authentication class in Flask
"""


class Auth():
    """ Authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require file
        """
        if (path is None or excluded_paths is None or excluded_paths == []):
            return (True)
        elif (path in excluded_paths or path + '/' in excluded_paths):
            return (False)
        return (True)

    def authorization_header(self, request=None) -> str:
        """ Responsible for authorization_header
        """
        authorization = request.__dict__.get("headers").get("Authorization")
        if (request is None or authorization is None):
            return (None)
        return (authorization)

    def current_user(self, request=None) -> TypeVar('User'):
        """ It Returns the current User
        """
        return (None)
