"""TMSX SDK exception hierarchy.

The TMSX API signals failures via an `Error` envelope inside an HTTP 200 response,
not via HTTP status codes. The SDK translates that envelope into language-native
exceptions so callers can `try/except` like any other Python library.
"""

from __future__ import annotations


class TMSXError(Exception):
    """Base class for all TMSX SDK errors.

    Attributes:
        code: Application-level error code from `Error.ErrorCode`, or `None` for
            transport-level failures.
        message: Human-readable error message from `Error.ErrorMessage`, or the
            transport error message.
        transaction_id: Echoed `TransactionID` from the failed request, if known —
            useful for support tickets and log correlation.
    """

    def __init__(
        self,
        message: str,
        *,
        code: str | None = None,
        transaction_id: str | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.transaction_id = transaction_id

    def __str__(self) -> str:
        parts: list[str] = []
        if self.code:
            parts.append(f"[ErrorCode={self.code}]")
        parts.append(self.message)
        if self.transaction_id:
            parts.append(f"(TransactionID={self.transaction_id})")
        return " ".join(parts)


class TMSXAuthError(TMSXError):
    """Raised when the API rejects authentication (ErrorCode 105)."""


class TMSXValidationError(TMSXError):
    """Raised when the API reports a malformed or invalid request (ErrorCode 101-103)."""


class TMSXClientError(TMSXError):
    """Raised for transport-level or unexpected errors (network, timeout, parse failure)."""


def from_error_code(
    code: str | None, message: str, *, transaction_id: str | None = None
) -> TMSXError:
    """Construct the most-specific exception class for an `Error.ErrorCode`.

    See `https://github.com/tourmind-com/tmsx-platform/blob/main/AUTH.md` for the error-code table.
    """
    if code in {"101", "102", "103"}:
        return TMSXValidationError(message, code=code, transaction_id=transaction_id)
    if code == "105":
        return TMSXAuthError(message, code=code, transaction_id=transaction_id)
    return TMSXError(message, code=code, transaction_id=transaction_id)
