#!/usr/bin/env python3
""" Creating An authentication class in Flask
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require file
        """
        return (False)

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
