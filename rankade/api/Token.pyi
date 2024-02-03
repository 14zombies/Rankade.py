"""
This type stub file was generated by pyright.
"""

import logging
from dataclasses import dataclass
from typing import List, Optional

logger: logging.Logger = ...
@dataclass(kw_only=True, slots=True)
class Token:
    """
    JWT Object

    """
    token: str
    algorithms: Optional[List[str]] = ...
    def __post_init__(self) -> None:
        ...

    @property
    def bearer(self) -> str:
        """For use with authorisation returns "Bearer" + token."""
        ...

    @property
    def is_invalid(self) -> bool:
        """Checks whether the token is invalid or not. By checking if the token can be decoded then checks the expiry date."""
        ...



