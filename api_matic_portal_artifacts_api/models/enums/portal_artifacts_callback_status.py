from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PortalArtifactsCallbackStatus(str, Enum):
    """Final status of a Portal Artifacts generation request, sent in the callback notification."""

    GENERATION_COMPLETED = "GenerationCompleted"
    """Generation completed. ``link`` contains the download URL."""

    VALIDATION_ERROR = "ValidationError"
    """The build input is not valid. See ``errors`` for details."""

    SUBSCRIPTION_ERROR = "SubscriptionError"
    """The build input requests features that your subscription does not include. See ``errors`` for details."""

    INTERNAL_SERVER_ERROR = "InternalServerError"
    """Generation failed due to an unexpected error or did not finish within 25 minutes."""

    __str__ = str.__str__


PortalArtifactsCallbackStatusOrStr: TypeAlias = Annotated[
    PortalArtifactsCallbackStatus | str, open_enum_validator(PortalArtifactsCallbackStatus)
]
