from __future__ import annotations

from typing import Any
from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.portal_artifacts_callback_status import PortalArtifactsCallbackStatusOrStr


class PortalArtifactsCallbackPayload(SdkBaseModel):
    """Notification sent to the callback URL when a Portal Artifacts generation request finishes."""

    id: UUID
    """Unique identifier of the generation request."""

    status: PortalArtifactsCallbackStatusOrStr
    """Final status of a Portal Artifacts generation request, sent in the callback notification."""

    link: Optional[str] = UNSET
    """URL to download the generated artifacts. Present only when ``status`` is ``GenerationCompleted``."""

    errors: Optional[dict[str, Any]] = UNSET
    """Error messages grouped by the part of the build input they relate to. Present only when generation did not
    complete."""


class PortalArtifactsCallbackPayloadDict(TypedDict):
    id: UUID
    status: PortalArtifactsCallbackStatusOrStr
    link: NotRequired[str]
    errors: NotRequired[dict[str, Any]]
