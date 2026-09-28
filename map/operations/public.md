<!-- Generated file — do not edit; regenerated with the SDK. -->

# Public — operations

Accessor: `client.public` · Source: `api_matic_portal_artifacts_api/apis/public.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.public.download_generated_portal_artifacts

- **Route**: `GET /portal-artifacts/{id}/download`
- **Auth**: `authorization`
- **Signature**: `def download_generated_portal_artifacts(id_: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DownloadGeneratedPortalArtifactsErrorBody]`
- **Error**: `DownloadGeneratedPortalArtifactsErrorBody` — **Case A (typed)**
- **Error arms**: `ProblemDetails` [400] · `UnauthorizedResponse` [401] · `InternalServerErrorResponse` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DownloadGeneratedPortalArtifactsErrorBody` | `api_matic_portal_artifacts_api/errors/download_generated_portal_artifacts_error.py` |
| `ProblemDetails` | `api_matic_portal_artifacts_api/models/problem_details.py` |
| `UnauthorizedResponse` | `api_matic_portal_artifacts_api/models/unauthorized_response.py` |
| `InternalServerErrorResponse` | `api_matic_portal_artifacts_api/models/internal_server_error_response.py` |

### client.public.generate_portal_artifacts_async

- **Route**: `POST /portal-artifacts`
- **Auth**: `authorization`
- **Signature**: `def generate_portal_artifacts_async(file: FileInput, *, x_api_matic_callback_url: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `file`
- **Params**: `x_api_matic_callback_url` — header `X-APIMatic-CallbackUrl` · `file` — multipart file
- **Returns (parsed)**: `PortalArtifactsGenerationAsyncResponse`
- **Returns (raw)**: `ApiResult[PortalArtifactsGenerationAsyncResponse, GeneratePortalArtifactsAsyncErrorBody]`
- **Error**: `GeneratePortalArtifactsAsyncErrorBody` — **Case A (typed)**
- **Error arms**: `ProblemDetails` [400, 403] · `UnauthorizedResponse` [401] · `InternalServerErrorResponse` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PortalArtifactsGenerationAsyncResponse` | `api_matic_portal_artifacts_api/models/portal_artifacts_generation_async_response.py` |
| `GeneratePortalArtifactsAsyncErrorBody` | `api_matic_portal_artifacts_api/errors/generate_portal_artifacts_async_error.py` |
| `ProblemDetails` | `api_matic_portal_artifacts_api/models/problem_details.py` |
| `UnauthorizedResponse` | `api_matic_portal_artifacts_api/models/unauthorized_response.py` |
| `InternalServerErrorResponse` | `api_matic_portal_artifacts_api/models/internal_server_error_response.py` |

### client.public.get_portal_artifacts_generation_status

- **Route**: `GET /portal-artifacts/{id}/status`
- **Auth**: `authorization`
- **Signature**: `def get_portal_artifacts_generation_status(id_: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `PortalArtifactsGenerationStatusResponse`
- **Returns (raw)**: `ApiResult[PortalArtifactsGenerationStatusResponse, GetPortalArtifactsGenerationStatusErrorBody]`
- **Error**: `GetPortalArtifactsGenerationStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ProblemDetails` [400] · `UnauthorizedResponse` [401] · `InternalServerErrorResponse` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PortalArtifactsGenerationStatusResponse` | `api_matic_portal_artifacts_api/models/portal_artifacts_generation_status_response.py` |
| `GetPortalArtifactsGenerationStatusErrorBody` | `api_matic_portal_artifacts_api/errors/get_portal_artifacts_generation_status_error.py` |
| `ProblemDetails` | `api_matic_portal_artifacts_api/models/problem_details.py` |
| `UnauthorizedResponse` | `api_matic_portal_artifacts_api/models/unauthorized_response.py` |
| `InternalServerErrorResponse` | `api_matic_portal_artifacts_api/models/internal_server_error_response.py` |

