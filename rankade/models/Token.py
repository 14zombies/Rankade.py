# Token.py

import logging
from dataclasses import dataclass, field
from typing import Optional
import jwt
from .Base import RankadeObject


@dataclass
class Token(RankadeObject):

    token: str
    _api: Optional["Api"] = field(default=None, init=False)  # type: ignore

    @property
    def _bearer(self):
        return "Bearer {}".format(self.token)

    @property
    def is_invalid(self) -> bool:
        if self.token is None:
            return True
        try:
            jwt.decode(self.token, options={
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
