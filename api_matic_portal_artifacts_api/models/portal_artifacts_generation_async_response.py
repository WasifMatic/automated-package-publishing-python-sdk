from __future__ import annotations

from uuid import UUID

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .portal_artifacts_generation_links import PortalArtifactsGenerationLinks, PortalArtifactsGenerationLinksDict


class PortalArtifactsGenerationAsyncResponse(SdkBaseModel):
    """Details of an accepted Portal Artifacts generation request."""

    id: UUID
    """Unique identifier of the generation request."""

    links: PortalArtifactsGenerationLinks
    """Links to check the status of a generation request and download its artifacts."""


class PortalArtifactsGenerationAsyncResponseDict(TypedDict):
    id: UUID
    links: PortalArtifactsGenerationLinksDict
