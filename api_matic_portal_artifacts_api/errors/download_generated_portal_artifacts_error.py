from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.internal_server_error_response import InternalServerErrorResponse
from ..models.problem_details import ProblemDetails
from ..models.unauthorized_response import UnauthorizedResponse

DownloadGeneratedPortalArtifactsErrorBody: TypeAlias = (
    ProblemDetails | UnauthorizedResponse | InternalServerErrorResponse | RawError
)


@dataclass(frozen=True, slots=True)
class _DownloadGeneratedPortalArtifactsError:
    def map(self, status_code: int, content: bytes) -> DownloadGeneratedPortalArtifactsErrorBody:
        match status_code:
            case 400:
                return decode_json[ProblemDetails](content)
            case 401:
                return decode_json[UnauthorizedResponse](content)
            case 500:
                return decode_json[InternalServerErrorResponse](content)
            case _:
                return RawError(status_code, content)


download_generated_portal_artifacts_error_mapper: Final[
    ErrorMapper[DownloadGeneratedPortalArtifactsErrorBody]
] = _DownloadGeneratedPortalArtifactsError()
