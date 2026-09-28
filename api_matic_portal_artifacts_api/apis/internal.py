from __future__ import annotations

from uuid import UUID

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    empty_response,
    param,
)
from ..errors.download_portal_artifacts_build_file_error import (
    DownloadPortalArtifactsBuildFileErrorBody,
    download_portal_artifacts_build_file_error_mapper,
)
from ..server.server import Server


class Internal:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InternalWithRawResponse(client, server, auth)

    def download_portal_artifacts_build_file(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Download the build file that was uploaded for a Portal Artifacts generation request. Available to admin users
        only.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The uploaded build zip file.

        Raises:
            ApiError: Bad Request. The ``id`` is not a valid UUID, or no build file exists for it. Unauthorized. The
                Auth key is missing or invalid, or the user is not an admin. Internal Server Error ``error`` is
                ``ProblemDetails | UnauthorizedResponse | InternalServerErrorResponse | RawError``."""
        return self._with_raw_response.download_portal_artifacts_build_file(
            id_, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> InternalWithRawResponse:
        return self._with_raw_response


class AsyncInternal:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInternalWithRawResponse(client, server, auth)

    async def download_portal_artifacts_build_file(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Download the build file that was uploaded for a Portal Artifacts generation request. Available to admin users
        only.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The uploaded build zip file.

        Raises:
            ApiError: Bad Request. The ``id`` is not a valid UUID, or no build file exists for it. Unauthorized. The
                Auth key is missing or invalid, or the user is not an admin. Internal Server Error ``error`` is
                ``ProblemDetails | UnauthorizedResponse | InternalServerErrorResponse | RawError``."""
        return (
            await self._with_raw_response.download_portal_artifacts_build_file(id_, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInternalWithRawResponse:
        return self._with_raw_response


class InternalWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def download_portal_artifacts_build_file(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DownloadPortalArtifactsBuildFileErrorBody]:
        """Download the build file that was uploaded for a Portal Artifacts generation request. Available to admin users
        only.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/portal-artifacts/{id}/build/download"),
            path_params=[param[UUID]("id", id_)],
            auth_scheme=self._auth.authorization,
            decoder=empty_response,
            error_mapper=download_portal_artifacts_build_file_error_mapper,
            request_options=request_options,
        )


class AsyncInternalWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def download_portal_artifacts_build_file(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DownloadPortalArtifactsBuildFileErrorBody]:
        """Download the build file that was uploaded for a Portal Artifacts generation request. Available to admin users
        only.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/portal-artifacts/{id}/build/download"),
            path_params=[param[UUID]("id", id_)],
            auth_scheme=self._auth.authorization,
            decoder=async_empty_response,
            error_mapper=download_portal_artifacts_build_file_error_mapper,
            request_options=request_options,
        )
