"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Any, MutableMapping, Optional

"""
This type stub file was generated by pyright.
"""
@dataclass(slots=True)
class RankadeResponse:
    """First response from server, should never leave the Api class and be surfaced to user of the package."""
    success: Optional[MutableMapping[str, Any]] = ...
    errors: Optional[MutableMapping[str, Any]] = ...


