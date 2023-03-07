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
        return (False)

    def authorization_header(self, request=None) -> str:
        """ Responsible for authorization_header
        """
        return (None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ It Returns the current User
        """
        return (None)
