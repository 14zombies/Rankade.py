# RankadeResponse.py

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Optional


@dataclass(frozen=True)
class RankadeResponse(object):
    success: Optional[Mapping[str, Any]] = None
    errors: Optional[List[Dict[str, Any]]] = None
