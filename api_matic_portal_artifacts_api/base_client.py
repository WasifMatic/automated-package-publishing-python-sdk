from __future__ import annotations

from typing import Generic

from .core import RawClientT
from .server.environment import Environment, validate_environment
from .server.server import Server
from .server.server_config import ProductionConfig, ServerConfig, TestingConfig

DEFAULT_TIMEOUT = 30.0


class BaseApiMaticPortalArtifactsApiClient(Generic[RawClientT]):
    _raw_client: RawClientT

    def __init__(
        self, *, environment: Environment = "production", base_url: str | None = None, timeout: float = DEFAULT_TIMEOUT
    ) -> None:
        if not timeout > 0:
            raise ValueError(f"timeout must be greater than 0; got {timeout!r}")
        self._server = Server(
            validate_environment(environment),
            (
                ServerConfig(production=ProductionConfig(base_url=base_url), testing=TestingConfig(base_url=base_url))
                if base_url is not None
                else ServerConfig()
            ),
        )
