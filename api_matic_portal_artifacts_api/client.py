from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.internal import Internal
from .apis.portal_artifacts_generation_async import PortalArtifactsGenerationAsync
from .apis.public import Public
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseApiMaticPortalArtifactsApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    no_auth,
    param,
)
from .server.environment import Environment


class ApiMaticPortalArtifactsApiClient(BaseApiMaticPortalArtifactsApiClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        authorization: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "ApiMaticPortalArtifactsApiClient/3.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "3.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            authorization=ApiKeyHeaderScheme("Authorization", authorization) if authorization is not None else no_auth
        )

    @cached_property
    def portal_artifacts_generation_async(self) -> PortalArtifactsGenerationAsync:
        return PortalArtifactsGenerationAsync(self._raw_client, self._server, self._auth)

    @cached_property
    def internal(self) -> Internal:
        return Internal(self._raw_client, self._server, self._auth)

    @cached_property
    def public(self) -> Public:
        return Public(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = ApiMaticPortalArtifactsApiClient
