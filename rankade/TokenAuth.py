# TokenAuth.py

import logging

import jwt

from .RankadeObject import RankadeObject


class TokenAuth(RankadeObject):

    def _set_attributes(self, attributes):
        self._token = attributes.get("token")

    @property
    def token(self):
        return self._token

    def __call__(self, r):
        r.headers['Authorization'] = self._bearer
        return r

    @property
    def _bearer(self):
        return "Bearer {}".format(self.token)

    @property
    def is_invalid(self) -> bool:
        if self.token is None:
            return True
        try:
            jwt.decode(self._token, options={
                       'verify_signature': False}, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            logging.info("Token is expired")
            return True
        except Exception as e:
            logging.critical("Token error – {}".format(e))
            return True
        else:
            logging.info("Token is valid")
            return False
