from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProblemDetailsError(SdkBaseModel):
    """Error details in the Problem Details format (RFC 7807)."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """A URI reference that identifies the problem type."""

    title: Optional[str] = UNSET
    """A short summary of the problem type."""

    status: Optional[int] = UNSET
    """The HTTP status code."""

    detail: Optional[str] = UNSET
    """An explanation specific to this occurrence of the problem."""

    instance: Optional[str] = UNSET
    """The request path where the problem occurred."""

    errors: Optional[dict[str, Any]] = UNSET
    """Error messages grouped by the field or part of the request they relate to."""


class ProblemDetailsErrorDict(TypedDict):
    type_: NotRequired[str]
    title: NotRequired[str]
    status: NotRequired[int]
    detail: NotRequired[str]
    instance: NotRequired[str]
    errors: NotRequired[dict[str, Any]]
