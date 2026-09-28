from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncFileInput,
    AsyncRawClient,
    FileInput,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    file_part,
    json_decoder,
    multipart_body,
    param,
)
from ..errors.download_generated_portal_artifacts_error import (
    DownloadGeneratedPortalArtifactsErrorBody,
    download_generated_portal_artifacts_error_mapper,
)
from ..errors.generate_portal_artifacts_async_error import (
    GeneratePortalArtifactsAsyncErrorBody,
    generate_portal_artifacts_async_error_mapper,
)
from ..errors.get_portal_artifacts_generation_status_error import (
    GetPortalArtifactsGenerationStatusErrorBody,
    get_portal_artifacts_generation_status_error_mapper,
)
from ..models.portal_artifacts_generation_async_response import PortalArtifactsGenerationAsyncResponse
from ..models.portal_artifacts_generation_status_response import PortalArtifactsGenerationStatusResponse
from ..server.server import Server


class Public:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PublicWithRawResponse(client, server, auth)

    def download_generated_portal_artifacts(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Download the generated Portal Artifacts as a zip file. The zip file contains:

        1. ``sdk/<language>.zip``: the SDK for each configured language
        2. ``code-samples/<language>.json``: the code samples catalog for each configured language
        3. ``docs/<language>.json``: the getting started guide for each configured language
        4. ``plugin.zip``: the context plugin, only when the build input declares one

        The artifacts are available only after generation completes. Until then, this endpoint returns ``400``.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The generated Portal Artifacts zip file.

        Raises:
            ApiError: Bad Request. The ``id`` is not a valid UUID, no generation request exists for it, or the artifacts
                are not available yet. Unauthorized. The Auth key is missing or invalid. Internal Server Error ``error``
                is ``ProblemDetails | UnauthorizedResponse | InternalServerErrorResponse | RawError``."""
        return self._with_raw_response.download_generated_portal_artifacts(
            id_, request_options=request_options
        ).unwrap()

    def generate_portal_artifacts_async(
        self,
        file: FileInput,
        *,
        x_api_matic_callback_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PortalArtifactsGenerationAsyncResponse:
        """Start an asynchronous generation of Portal Artifacts by uploading a Portal Build Input. The build input is
        your build directory (containing the ``apimatic.json`` file, your API specification and your content) compressed
        into a zip file.

        For every language configured in the build input, the generated artifacts include:

        1. An SDK
        2. A code samples catalog
        3. A getting started guide

        A context plugin is also generated when the build input declares one.

        The request returns immediately with an ``id`` and links to check the status and download the artifacts.
        Generation must finish within 25 minutes.

        Args:
            file: The Portal Build Input as a zip file (maximum 20 MB). The zip file must contain the build directory,
                including the ``apimatic.json`` file.
            x_api_matic_callback_url: Optional absolute HTTP or HTTPS URL. When provided, the server sends a ``POST``
                request to this URL once generation finishes, with the generation status and, on success, the download
                link.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Generation request accepted. Use the returned links to check the status and download the artifacts.

        Raises:
            ApiError: Bad Request. The build file is missing, empty or not a zip file, or the callback URL is not valid.
                Unauthorized. The Auth key is missing or invalid. Subscription Issue. Your subscription does not include
                portal generation. Internal Server Error ``error`` is ``ProblemDetails | UnauthorizedResponse |
                InternalServerErrorResponse | RawError``."""
        return self._with_raw_response.generate_portal_artifacts_async(
            file, x_api_matic_callback_url=x_api_matic_callback_url, request_options=request_options
        ).unwrap()

    def get_portal_artifacts_generation_status(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> PortalArtifactsGenerationStatusResponse:
        """Get the status of a Portal Artifacts generation request.

        While generation is running or after it has failed, this endpoint returns ``200`` with the current status. Once
        generation completes, it returns a ``302`` redirect to the download endpoint. HTTP clients that follow redirects
        automatically will receive the artifacts zip file directly.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Generation is in progress or has failed.

        Raises:
            ApiError: Bad Request. The ``id`` is not a valid UUID, no generation request exists for it, or the artifacts
                are not available yet. Unauthorized. The Auth key is missing or invalid. Internal Server Error ``error``
                is ``ProblemDetails | UnauthorizedResponse | InternalServerErrorResponse | RawError``."""
        return self._with_raw_response.get_portal_artifacts_generation_status(
            id_, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PublicWithRawResponse:
        return self._with_raw_response


class AsyncPublic:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPublicWithRawResponse(client, server, auth)

    async def download_generated_portal_artifacts(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Download the generated Portal Artifacts as a zip file. The zip file contains:

        1. ``sdk/<language>.zip``: the SDK for each configured language
        2. ``code-samples/<language>.json``: the code samples catalog for each configured language
        3. ``docs/<language>.json``: the getting started guide for each configured language
        4. ``plugin.zip``: the context plugin, only when the build input declares one

        The artifacts are available only after generation completes. Until then, this endpoint returns ``400``.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The generated Portal Artifacts zip file.

        Raises:
            ApiError: Bad Request. The ``id`` is not a valid UUID, no generation request exists for it, or the artifacts
                are not available yet. Unauthorized. The Auth key is missing or invalid. Internal Server Error ``error``
                is ``ProblemDetails | UnauthorizedResponse | InternalServerErrorResponse | RawError``."""
        return (
            await self._with_raw_response.download_generated_portal_artifacts(id_, request_options=request_options)
        ).unwrap()

    async def generate_portal_artifacts_async(
        self,
        file: AsyncFileInput,
        *,
        x_api_matic_callback_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PortalArtifactsGenerationAsyncResponse:
        """Start an asynchronous generation of Portal Artifacts by uploading a Portal Build Input. The build input is
        your build directory (containing the ``apimatic.json`` file, your API specification and your content) compressed
        into a zip file.

        For every language configured in the build input, the generated artifacts include:

        1. An SDK
        2. A code samples catalog
        3. A getting started guide

        A context plugin is also generated when the build input declares one.

        The request returns immediately with an ``id`` and links to check the status and download the artifacts.
        Generation must finish within 25 minutes.

        Args:
            file: The Portal Build Input as a zip file (maximum 20 MB). The zip file must contain the build directory,
                including the ``apimatic.json`` file.
            x_api_matic_callback_url: Optional absolute HTTP or HTTPS URL. When provided, the server sends a ``POST``
                request to this URL once generation finishes, with the generation status and, on success, the download
                link.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Generation request accepted. Use the returned links to check the status and download the artifacts.

        Raises:
            ApiError: Bad Request. The build file is missing, empty or not a zip file, or the callback URL is not valid.
                Unauthorized. The Auth key is missing or invalid. Subscription Issue. Your subscription does not include
                portal generation. Internal Server Error ``error`` is ``ProblemDetails | UnauthorizedResponse |
                InternalServerErrorResponse | RawError``."""
        return (
            await self._with_raw_response.generate_portal_artifacts_async(
                file, x_api_matic_callback_url=x_api_matic_callback_url, request_options=request_options
            )
        ).unwrap()

    async def get_portal_artifacts_generation_status(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> PortalArtifactsGenerationStatusResponse:
        """Get the status of a Portal Artifacts generation request.

        While generation is running or after it has failed, this endpoint returns ``200`` with the current status. Once
        generation completes, it returns a ``302`` redirect to the download endpoint. HTTP clients that follow redirects
        automatically will receive the artifacts zip file directly.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Generation is in progress or has failed.

        Raises:
            ApiError: Bad Request. The ``id`` is not a valid UUID, no generation request exists for it, or the artifacts
                are not available yet. Unauthorized. The Auth key is missing or invalid. Internal Server Error ``error``
                is ``ProblemDetails | UnauthorizedResponse | InternalServerErrorResponse | RawError``."""
        return (
            await self._with_raw_response.get_portal_artifacts_generation_status(id_, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPublicWithRawResponse:
        return self._with_raw_response


class PublicWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def download_generated_portal_artifacts(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DownloadGeneratedPortalArtifactsErrorBody]:
        """Download the generated Portal Artifacts as a zip file. The zip file contains:

        1. ``sdk/<language>.zip``: the SDK for each configured language
        2. ``code-samples/<language>.json``: the code samples catalog for each configured language
        3. ``docs/<language>.json``: the getting started guide for each configured language
        4. ``plugin.zip``: the context plugin, only when the build input declares one

        The artifacts are available only after generation completes. Until then, this endpoint returns ``400``.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/portal-artifacts/{id}/download"),
            path_params=[param[UUID]("id", id_)],
            auth_scheme=self._auth.authorization,
            decoder=empty_response,
            error_mapper=download_generated_portal_artifacts_error_mapper,
            request_options=request_options,
        )

    def generate_portal_artifacts_async(
        self,
        file: FileInput,
        *,
        x_api_matic_callback_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PortalArtifactsGenerationAsyncResponse, GeneratePortalArtifactsAsyncErrorBody]:
        """Start an asynchronous generation of Portal Artifacts by uploading a Portal Build Input. The build input is
        your build directory (containing the ``apimatic.json`` file, your API specification and your content) compressed
        into a zip file.

        For every language configured in the build input, the generated artifacts include:

        1. An SDK
        2. A code samples catalog
        3. A getting started guide

        A context plugin is also generated when the build input declares one.

        The request returns immediately with an ``id`` and links to check the status and download the artifacts.
        Generation must finish within 25 minutes.

        Args:
            file: The Portal Build Input as a zip file (maximum 20 MB). The zip file must contain the build directory,
                including the ``apimatic.json`` file.
            x_api_matic_callback_url: Optional absolute HTTP or HTTPS URL. When provided, the server sends a ``POST``
                request to this URL once generation finishes, with the generation status and, on success, the download
                link.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/portal-artifacts"),
            headers=[
                param[str | None]("X-APIMatic-CallbackUrl", x_api_matic_callback_url),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(file_part("file", file)),
            auth_scheme=self._auth.authorization,
            decoder=json_decoder[PortalArtifactsGenerationAsyncResponse],
            error_mapper=generate_portal_artifacts_async_error_mapper,
            request_options=request_options,
        )

    def get_portal_artifacts_generation_status(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PortalArtifactsGenerationStatusResponse, GetPortalArtifactsGenerationStatusErrorBody]:
        """Get the status of a Portal Artifacts generation request.

        While generation is running or after it has failed, this endpoint returns ``200`` with the current status. Once
        generation completes, it returns a ``302`` redirect to the download endpoint. HTTP clients that follow redirects
        automatically will receive the artifacts zip file directly.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/portal-artifacts/{id}/status"),
            path_params=[param[UUID]("id", id_)],
            auth_scheme=self._auth.authorization,
            decoder=json_decoder[PortalArtifactsGenerationStatusResponse],
            error_mapper=get_portal_artifacts_generation_status_error_mapper,
            request_options=request_options,
        )


class AsyncPublicWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def download_generated_portal_artifacts(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DownloadGeneratedPortalArtifactsErrorBody]:
        """Download the generated Portal Artifacts as a zip file. The zip file contains:

        1. ``sdk/<language>.zip``: the SDK for each configured language
        2. ``code-samples/<language>.json``: the code samples catalog for each configured language
        3. ``docs/<language>.json``: the getting started guide for each configured language
        4. ``plugin.zip``: the context plugin, only when the build input declares one

        The artifacts are available only after generation completes. Until then, this endpoint returns ``400``.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/portal-artifacts/{id}/download"),
            path_params=[param[UUID]("id", id_)],
            auth_scheme=self._auth.authorization,
            decoder=async_empty_response,
            error_mapper=download_generated_portal_artifacts_error_mapper,
            request_options=request_options,
        )

    async def generate_portal_artifacts_async(
        self,
        file: AsyncFileInput,
        *,
        x_api_matic_callback_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PortalArtifactsGenerationAsyncResponse, GeneratePortalArtifactsAsyncErrorBody]:
        """Start an asynchronous generation of Portal Artifacts by uploading a Portal Build Input. The build input is
        your build directory (containing the ``apimatic.json`` file, your API specification and your content) compressed
        into a zip file.

        For every language configured in the build input, the generated artifacts include:

        1. An SDK
        2. A code samples catalog
        3. A getting started guide

        A context plugin is also generated when the build input declares one.

        The request returns immediately with an ``id`` and links to check the status and download the artifacts.
        Generation must finish within 25 minutes.

        Args:
            file: The Portal Build Input as a zip file (maximum 20 MB). The zip file must contain the build directory,
                including the ``apimatic.json`` file.
            x_api_matic_callback_url: Optional absolute HTTP or HTTPS URL. When provided, the server sends a ``POST``
                request to this URL once generation finishes, with the generation status and, on success, the download
                link.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/portal-artifacts"),
            headers=[
                param[str | None]("X-APIMatic-CallbackUrl", x_api_matic_callback_url),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=multipart_body(file_part("file", file)),
            auth_scheme=self._auth.authorization,
            decoder=async_json_decoder[PortalArtifactsGenerationAsyncResponse],
            error_mapper=generate_portal_artifacts_async_error_mapper,
            request_options=request_options,
        )

    async def get_portal_artifacts_generation_status(
        self, id_: UUID, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PortalArtifactsGenerationStatusResponse, GetPortalArtifactsGenerationStatusErrorBody]:
        """Get the status of a Portal Artifacts generation request.

        While generation is running or after it has failed, this endpoint returns ``200`` with the current status. Once
        generation completes, it returns a ``302`` redirect to the download endpoint. HTTP clients that follow redirects
        automatically will receive the artifacts zip file directly.

        Args:
            id_: The ``id`` returned by **Generate Portal Artifacts Async**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/portal-artifacts/{id}/status"),
            path_params=[param[UUID]("id", id_)],
            auth_scheme=self._auth.authorization,
            decoder=async_json_decoder[PortalArtifactsGenerationStatusResponse],
            error_mapper=get_portal_artifacts_generation_status_error_mapper,
            request_options=request_options,
        )
