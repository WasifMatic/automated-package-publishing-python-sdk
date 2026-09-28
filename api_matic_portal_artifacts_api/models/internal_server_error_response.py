from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InternalServerErrorResponse(SdkBaseModel):
    """Error returned when the server encounters an unexpected error."""

    message: Optional[str] = UNSET
    """A message describing the error."""


class InternalServerErrorResponseDict(TypedDict):
    message: NotRequired[str]
