from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UnauthorizedResponse(SdkBaseModel):
    """Error returned when the request is not authorized."""

    message: Optional[str] = UNSET
    """A message describing the error."""


class UnauthorizedResponseDict(TypedDict):
    message: NotRequired[str]
