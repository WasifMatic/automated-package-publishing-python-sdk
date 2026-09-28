<!-- Generated file — do not edit; regenerated with the SDK. -->

# Internal — operations

Accessor: `client.internal` · Source: `api_matic_portal_artifacts_api/apis/internal.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.internal.download_portal_artifacts_build_file

- **Route**: `GET /portal-artifacts/{id}/build/download`
- **Auth**: `authorization`
- **Signature**: `def download_portal_artifacts_build_file(id_: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DownloadPortalArtifactsBuildFileErrorBody]`
- **Error**: `DownloadPortalArtifactsBuildFileErrorBody` — **Case A (typed)**
- **Error arms**: `ProblemDetails` [400] · `UnauthorizedResponse` [401] · `InternalServerErrorResponse` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DownloadPortalArtifactsBuildFileErrorBody` | `api_matic_portal_artifacts_api/errors/download_portal_artifacts_build_file_error.py` |
| `ProblemDetails` | `api_matic_portal_artifacts_api/models/problem_details.py` |
| `UnauthorizedResponse` | `api_matic_portal_artifacts_api/models/unauthorized_response.py` |
| `InternalServerErrorResponse` | `api_matic_portal_artifacts_api/models/internal_server_error_response.py` |

