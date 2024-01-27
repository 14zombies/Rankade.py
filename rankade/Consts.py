# rankade.consts.py
"""Any magic strings to go here."""
DEFAULT_BASE_URL = "https://api.rankade.com/public/api/1/"
"""Rankade server URL."""
BOT_ID = "bot"
"""Bot users have an ID of "bot"."""
GHOST_PREFIX = "*"
"""Ghost players have a display name prefixed with "*"."""
ERROR_STATUS = [400, 401, 403, 404, 429, 500]
"""All Error HTTP Status"""
RANKADE_ERROR_PREFIX = "R"
"""If Rankade server returns 400, 404, or 500, it should also return an error code beginning with "R"."""
MATCH_ERROR_STATUS = [202, 400]
"""Match validation errors will return either 202 or 400 HTTP status code."""
MATHC_ERROR_PREFIX = "M"
"""Match validation errors will return an error code beginning with "M"."""
AUTH_ERROR_STATUS = [401, 403]
"""Authentication errors will return either 202 or 400 HTTP status."""
AUTH_ERROR_PREFIX = "A"
"""Authentication errors will return an error code beginning with "A"."""
QUOTA_ERROR_STATUS = [202, 429]
"""Quota validation errors will return either 202 or 429 HTTP status."""
QUOTA_ERROR_PREFIX = "Q"
"""Quota errors will return an error code beginning with "Q"."""
