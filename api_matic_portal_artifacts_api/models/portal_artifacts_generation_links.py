from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PortalArtifactsGenerationLinks(SdkBaseModel):
    """Links to check the status of a generation request and download its artifacts."""

    status: str
    """URL to check the status of the generation request."""

    download: str
    """URL to download the generated artifacts once generation completes."""


class PortalArtifactsGenerationLinksDict(TypedDict):
    status: str
    download: str
