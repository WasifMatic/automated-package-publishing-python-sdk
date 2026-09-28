from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.portal_artifacts_generation_status import PortalArtifactsGenerationStatusOrStr


class PortalArtifactsGenerationStatusResponse(SdkBaseModel):
    """Current status of a Portal Artifacts generation request."""

    status: PortalArtifactsGenerationStatusOrStr
    """Status of a Portal Artifacts generation request."""

    errors: Optional[dict[str, Any]] = UNSET
    """Error messages grouped by the part of the build input they relate to. Returned only when ``status`` is
    ``ValidationError`` or ``SubscriptionError``."""


class PortalArtifactsGenerationStatusResponseDict(TypedDict):
    status: PortalArtifactsGenerationStatusOrStr
    errors: NotRequired[dict[str, Any]]
