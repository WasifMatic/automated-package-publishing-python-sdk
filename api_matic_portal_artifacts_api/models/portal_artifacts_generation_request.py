from __future__ import annotations

from typing_extensions import TypedDict

from ..core import FileResponse, SdkBaseModel


class PortalArtifactsGenerationRequest(SdkBaseModel):
    """Multipart form data for a Portal Artifacts generation request."""

    file: FileResponse
    """The Portal Build Input as a zip file (maximum 20 MB). The zip file must contain the build directory, including
    the ``apimatic.json`` file."""


class PortalArtifactsGenerationRequestDict(TypedDict):
    file: FileResponse
