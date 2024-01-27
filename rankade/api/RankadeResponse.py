# rankade.api.RankadeResponse.py
from dataclasses import dataclass
from typing import Any, MutableMapping, Optional


@dataclass(slots=True)
class RankadeResponse(object):
    """First response from server, should never leave the Api class and be surfaced to user of the package."""

    success: Optional[MutableMapping[str, Any]] = None
    errors: Optional[MutableMapping[str, Any]] = None
