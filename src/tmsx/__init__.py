"""TMSX — Python SDK for the Tourmind TMS hotel API.

Top-level package. The public surface is in `tmsx.hotel`.
"""

from tmsx.exceptions import (
    TMSXAuthError,
    TMSXClientError,
    TMSXError,
    TMSXValidationError,
)

__all__ = [
    "TMSXAuthError",
    "TMSXClientError",
    "TMSXError",
    "TMSXValidationError",
]

__version__ = "0.1.0"
