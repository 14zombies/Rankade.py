# rankade.api.Token.py
import logging
from dataclasses import dataclass, field
from typing import List, Optional

import jwt

logger = logging.getLogger(__name__)


@dataclass(kw_only=True, slots=True)
class Token:
    """
    JWT Object

    """

    token: str
    """JWT string"""
    algorithms: Optional[List[str]] = field(default=None)
    """List of JWA Algorithms to use in JWT decoding.
    See [rfc7518 section-3.1](https://datatracker.ietf.org/doc/html/rfc7518#section-3.1)
    for a full list. "HS256" by default."""

    def __post_init__(self):
        if self.algorithms is None:
            self.algorithms = ["HS256"]

    @property
    def bearer(self) -> str:
        """For use with authorisation returns "Bearer" + token."""
        return f"Bearer {self.token}"

    @property
    def is_invalid(self) -> bool:
        """Checks whether the token is invalid or not. By checking if the token can be decoded then checks the expiry date."""
        try:
            jwt.decode(self.token, options={"verify_signature": False, "verify_exp": True}, algorithms=self.algorithms)  # pyright: ignore[reportUnknownMemberType] #
            logger.info("🎟 Token is valid")
            return False
        except jwt.ExpiredSignatureError:
            logger.info("☠️ Token is expired")
            return True
        except jwt.PyJWTError as exp:
            logger.critical(f"⛔️ Token error - {exp}")
            return True
