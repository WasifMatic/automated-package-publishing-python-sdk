from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PortalArtifactsGenerationStatus(str, Enum):
    """Status of a Portal Artifacts generation request."""

    IN_PROGRESS = "InProgress"
    """Generation is queued or running."""

    FAILED = "Failed"
    """Generation failed due to an unexpected error."""

    VALIDATION_ERROR = "ValidationError"
    """The build input is not valid. See ``errors`` for details."""

    SUBSCRIPTION_ERROR = "SubscriptionError"
    """The build input requests features that your subscription does not include. See ``errors`` for details."""

    __str__ = str.__str__


PortalArtifactsGenerationStatusOrStr: TypeAlias = Annotated[
    PortalArtifactsGenerationStatus | str, open_enum_validator(PortalArtifactsGenerationStatus)
]
