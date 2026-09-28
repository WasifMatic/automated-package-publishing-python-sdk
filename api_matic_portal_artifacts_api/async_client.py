from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.internal import AsyncInternal
from .apis.portal_artifacts_generation_async import AsyncPortalArtifactsGenerationAsync
from .apis.public import AsyncPublic
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseApiMaticPortalArtifactsApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncApiMaticPortalArtifactsApiClient(BaseApiMaticPortalArtifactsApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        authorization: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "ApiMaticPortalArtifactsApiClient/3.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "3.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            authorization=ApiKeyHeaderScheme("Authorization", authorization) if authorization is not None else no_auth
        )

    @cached_property
    def portal_artifacts_generation_async(self) -> AsyncPortalArtifactsGenerationAsync:
        return AsyncPortalArtifactsGenerationAsync(self._raw_client, self._server, self._auth)

    @cached_property
    def internal(self) -> AsyncInternal:
        return AsyncInternal(self._raw_client, self._server, self._auth)

    @cached_property
    def public(self) -> AsyncPublic:
        return AsyncPublic(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncApiMaticPortalArtifactsApiClient
