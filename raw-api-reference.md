# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [ApiMaticPortalArtifactsApiClient](api_matic_portal_artifacts_api/client.py)

## PortalArtifactsGenerationAsync

> Source: [PortalArtifactsGenerationAsync](api_matic_portal_artifacts_api/apis/portal_artifacts_generation_async.py)

<details>
<summary><code>def download_generated_portal_artifacts(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DownloadGeneratedPortalArtifactsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Download the generated Portal Artifacts as a zip file. The zip file contains:

1. `sdk/<language>.zip`: the SDK for each configured language
2. `code-samples/<language>.json`: the code samples catalog for each configured language
3. `docs/<language>.json`: the getting started guide for each configured language
4. `plugin.zip`: the context plugin, only when the build input declares one

The artifacts are available only after generation completes. Until then, this endpoint returns `400`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.portal_artifacts_generation_async.with_raw_response.download_generated_portal_artifacts(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadGeneratedPortalArtifactsErrorBody
```

**Async**

```python
result = await async_client.portal_artifacts_generation_async.with_raw_response.download_generated_portal_artifacts(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadGeneratedPortalArtifactsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>UUID</code> | The `id` returned by **Generate Portal Artifacts Async**. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_matic_portal_artifacts_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_matic_portal_artifacts_api/core/results.py)&#91;None, [DownloadGeneratedPortalArtifactsErrorBody](api_matic_portal_artifacts_api/errors/download_generated_portal_artifacts_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DownloadGeneratedPortalArtifactsErrorBody](api_matic_portal_artifacts_api/errors/download_generated_portal_artifacts_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ProblemDetails](api_matic_portal_artifacts_api/models/problem_details.py)</code> |
| 401 | <code>[UnauthorizedResponse](api_matic_portal_artifacts_api/models/unauthorized_response.py)</code> |
| 500 | <code>[InternalServerErrorResponse](api_matic_portal_artifacts_api/models/internal_server_error_response.py)</code> |
| anything unmapped | <code>[RawError](api_matic_portal_artifacts_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_portal_artifacts_build_file(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DownloadPortalArtifactsBuildFileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Download the build file that was uploaded for a Portal Artifacts generation request. Available to admin users only.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.portal_artifacts_generation_async.with_raw_response.download_portal_artifacts_build_file(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadPortalArtifactsBuildFileErrorBody
```

**Async**

```python
result = await async_client.portal_artifacts_generation_async.with_raw_response.download_portal_artifacts_build_file(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadPortalArtifactsBuildFileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>UUID</code> | The `id` returned by **Generate Portal Artifacts Async**. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_matic_portal_artifacts_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_matic_portal_artifacts_api/core/results.py)&#91;None, [DownloadPortalArtifactsBuildFileErrorBody](api_matic_portal_artifacts_api/errors/download_portal_artifacts_build_file_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DownloadPortalArtifactsBuildFileErrorBody](api_matic_portal_artifacts_api/errors/download_portal_artifacts_build_file_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ProblemDetails](api_matic_portal_artifacts_api/models/problem_details.py)</code> |
| 401 | <code>[UnauthorizedResponse](api_matic_portal_artifacts_api/models/unauthorized_response.py)</code> |
| 500 | <code>[InternalServerErrorResponse](api_matic_portal_artifacts_api/models/internal_server_error_response.py)</code> |
| anything unmapped | <code>[RawError](api_matic_portal_artifacts_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_portal_artifacts_async(file: FileInput, *, x_api_matic_callback_url: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PortalArtifactsGenerationAsyncResponse, GeneratePortalArtifactsAsyncErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Start an asynchronous generation of Portal Artifacts by uploading a Portal Build Input. The build input is your build directory (containing the `apimatic.json` file, your API specification and your content) compressed into a zip file.

For every language configured in the build input, the generated artifacts include:

1. An SDK
2. A code samples catalog
3. A getting started guide

A context plugin is also generated when the build input declares one.

The request returns immediately with an `id` and links to check the status and download the artifacts. Generation must finish within 25 minutes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.portal_artifacts_generation_async.with_raw_response.generate_portal_artifacts_async(
    Path("path/to/file.bin"), x_api_matic_callback_url="https://example.com/portal-artifacts-callback"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortalArtifactsGenerationAsyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GeneratePortalArtifactsAsyncErrorBody
```

**Async**

```python
result = await async_client.portal_artifacts_generation_async.with_raw_response.generate_portal_artifacts_async(
    Path("path/to/file.bin"), x_api_matic_callback_url="https://example.com/portal-artifacts-callback"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortalArtifactsGenerationAsyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GeneratePortalArtifactsAsyncErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>file</code> | <code>FileInput</code> | The Portal Build Input as a zip file (maximum 20 MB). The zip file must contain the build directory, including the `apimatic.json` file. |
| <code>x_api_matic_callback_url</code> | <code>str \| None</code> | Optional absolute HTTP or HTTPS URL. When provided, the server sends a `POST` request to this URL once generation finishes, with the generation status and, on success, the download link.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_matic_portal_artifacts_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_matic_portal_artifacts_api/core/results.py)&#91;[PortalArtifactsGenerationAsyncResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_async_response.py), [GeneratePortalArtifactsAsyncErrorBody](api_matic_portal_artifacts_api/errors/generate_portal_artifacts_async_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PortalArtifactsGenerationAsyncResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_async_response.py)</code> -- Generation request accepted. Use the returned links to check the status and download the artifacts.

**On `Failure`**: `error` is <code>[GeneratePortalArtifactsAsyncErrorBody](api_matic_portal_artifacts_api/errors/generate_portal_artifacts_async_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403 | <code>[ProblemDetails](api_matic_portal_artifacts_api/models/problem_details.py)</code> |
| 401 | <code>[UnauthorizedResponse](api_matic_portal_artifacts_api/models/unauthorized_response.py)</code> |
| 500 | <code>[InternalServerErrorResponse](api_matic_portal_artifacts_api/models/internal_server_error_response.py)</code> |
| anything unmapped | <code>[RawError](api_matic_portal_artifacts_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_portal_artifacts_generation_status(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PortalArtifactsGenerationStatusResponse, GetPortalArtifactsGenerationStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the status of a Portal Artifacts generation request.

While generation is running or after it has failed, this endpoint returns `200` with the current status. Once generation completes, it returns a `302` redirect to the download endpoint. HTTP clients that follow redirects automatically will receive the artifacts zip file directly.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.portal_artifacts_generation_async.with_raw_response.get_portal_artifacts_generation_status(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortalArtifactsGenerationStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPortalArtifactsGenerationStatusErrorBody
```

**Async**

```python
result = await async_client.portal_artifacts_generation_async.with_raw_response.get_portal_artifacts_generation_status(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortalArtifactsGenerationStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPortalArtifactsGenerationStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>UUID</code> | The `id` returned by **Generate Portal Artifacts Async**. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_matic_portal_artifacts_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_matic_portal_artifacts_api/core/results.py)&#91;[PortalArtifactsGenerationStatusResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_status_response.py), [GetPortalArtifactsGenerationStatusErrorBody](api_matic_portal_artifacts_api/errors/get_portal_artifacts_generation_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PortalArtifactsGenerationStatusResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_status_response.py)</code> -- Generation is in progress or has failed.

**On `Failure`**: `error` is <code>[GetPortalArtifactsGenerationStatusErrorBody](api_matic_portal_artifacts_api/errors/get_portal_artifacts_generation_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ProblemDetails](api_matic_portal_artifacts_api/models/problem_details.py)</code> |
| 401 | <code>[UnauthorizedResponse](api_matic_portal_artifacts_api/models/unauthorized_response.py)</code> |
| 500 | <code>[InternalServerErrorResponse](api_matic_portal_artifacts_api/models/internal_server_error_response.py)</code> |
| anything unmapped | <code>[RawError](api_matic_portal_artifacts_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Internal

> Source: [Internal](api_matic_portal_artifacts_api/apis/internal.py)

<details>
<summary><code>def download_portal_artifacts_build_file(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DownloadPortalArtifactsBuildFileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Download the build file that was uploaded for a Portal Artifacts generation request. Available to admin users only.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.internal.with_raw_response.download_portal_artifacts_build_file(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadPortalArtifactsBuildFileErrorBody
```

**Async**

```python
result = await async_client.internal.with_raw_response.download_portal_artifacts_build_file(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadPortalArtifactsBuildFileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>UUID</code> | The `id` returned by **Generate Portal Artifacts Async**. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_matic_portal_artifacts_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_matic_portal_artifacts_api/core/results.py)&#91;None, [DownloadPortalArtifactsBuildFileErrorBody](api_matic_portal_artifacts_api/errors/download_portal_artifacts_build_file_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DownloadPortalArtifactsBuildFileErrorBody](api_matic_portal_artifacts_api/errors/download_portal_artifacts_build_file_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ProblemDetails](api_matic_portal_artifacts_api/models/problem_details.py)</code> |
| 401 | <code>[UnauthorizedResponse](api_matic_portal_artifacts_api/models/unauthorized_response.py)</code> |
| 500 | <code>[InternalServerErrorResponse](api_matic_portal_artifacts_api/models/internal_server_error_response.py)</code> |
| anything unmapped | <code>[RawError](api_matic_portal_artifacts_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Public

> Source: [Public](api_matic_portal_artifacts_api/apis/public.py)

<details>
<summary><code>def download_generated_portal_artifacts(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DownloadGeneratedPortalArtifactsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Download the generated Portal Artifacts as a zip file. The zip file contains:

1. `sdk/<language>.zip`: the SDK for each configured language
2. `code-samples/<language>.json`: the code samples catalog for each configured language
3. `docs/<language>.json`: the getting started guide for each configured language
4. `plugin.zip`: the context plugin, only when the build input declares one

The artifacts are available only after generation completes. Until then, this endpoint returns `400`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.public.with_raw_response.download_generated_portal_artifacts(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadGeneratedPortalArtifactsErrorBody
```

**Async**

```python
result = await async_client.public.with_raw_response.download_generated_portal_artifacts(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadGeneratedPortalArtifactsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>UUID</code> | The `id` returned by **Generate Portal Artifacts Async**. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_matic_portal_artifacts_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_matic_portal_artifacts_api/core/results.py)&#91;None, [DownloadGeneratedPortalArtifactsErrorBody](api_matic_portal_artifacts_api/errors/download_generated_portal_artifacts_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DownloadGeneratedPortalArtifactsErrorBody](api_matic_portal_artifacts_api/errors/download_generated_portal_artifacts_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ProblemDetails](api_matic_portal_artifacts_api/models/problem_details.py)</code> |
| 401 | <code>[UnauthorizedResponse](api_matic_portal_artifacts_api/models/unauthorized_response.py)</code> |
| 500 | <code>[InternalServerErrorResponse](api_matic_portal_artifacts_api/models/internal_server_error_response.py)</code> |
| anything unmapped | <code>[RawError](api_matic_portal_artifacts_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_portal_artifacts_async(file: FileInput, *, x_api_matic_callback_url: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PortalArtifactsGenerationAsyncResponse, GeneratePortalArtifactsAsyncErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Start an asynchronous generation of Portal Artifacts by uploading a Portal Build Input. The build input is your build directory (containing the `apimatic.json` file, your API specification and your content) compressed into a zip file.

For every language configured in the build input, the generated artifacts include:

1. An SDK
2. A code samples catalog
3. A getting started guide

A context plugin is also generated when the build input declares one.

The request returns immediately with an `id` and links to check the status and download the artifacts. Generation must finish within 25 minutes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.public.with_raw_response.generate_portal_artifacts_async(
    Path("path/to/file.bin"), x_api_matic_callback_url="https://example.com/portal-artifacts-callback"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortalArtifactsGenerationAsyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GeneratePortalArtifactsAsyncErrorBody
```

**Async**

```python
result = await async_client.public.with_raw_response.generate_portal_artifacts_async(
    Path("path/to/file.bin"), x_api_matic_callback_url="https://example.com/portal-artifacts-callback"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortalArtifactsGenerationAsyncResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GeneratePortalArtifactsAsyncErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>file</code> | <code>FileInput</code> | The Portal Build Input as a zip file (maximum 20 MB). The zip file must contain the build directory, including the `apimatic.json` file. |
| <code>x_api_matic_callback_url</code> | <code>str \| None</code> | Optional absolute HTTP or HTTPS URL. When provided, the server sends a `POST` request to this URL once generation finishes, with the generation status and, on success, the download link.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_matic_portal_artifacts_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_matic_portal_artifacts_api/core/results.py)&#91;[PortalArtifactsGenerationAsyncResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_async_response.py), [GeneratePortalArtifactsAsyncErrorBody](api_matic_portal_artifacts_api/errors/generate_portal_artifacts_async_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PortalArtifactsGenerationAsyncResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_async_response.py)</code> -- Generation request accepted. Use the returned links to check the status and download the artifacts.

**On `Failure`**: `error` is <code>[GeneratePortalArtifactsAsyncErrorBody](api_matic_portal_artifacts_api/errors/generate_portal_artifacts_async_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403 | <code>[ProblemDetails](api_matic_portal_artifacts_api/models/problem_details.py)</code> |
| 401 | <code>[UnauthorizedResponse](api_matic_portal_artifacts_api/models/unauthorized_response.py)</code> |
| 500 | <code>[InternalServerErrorResponse](api_matic_portal_artifacts_api/models/internal_server_error_response.py)</code> |
| anything unmapped | <code>[RawError](api_matic_portal_artifacts_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_portal_artifacts_generation_status(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PortalArtifactsGenerationStatusResponse, GetPortalArtifactsGenerationStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the status of a Portal Artifacts generation request.

While generation is running or after it has failed, this endpoint returns `200` with the current status. Once generation completes, it returns a `302` redirect to the download endpoint. HTTP clients that follow redirects automatically will receive the artifacts zip file directly.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.public.with_raw_response.get_portal_artifacts_generation_status(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortalArtifactsGenerationStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPortalArtifactsGenerationStatusErrorBody
```

**Async**

```python
result = await async_client.public.with_raw_response.get_portal_artifacts_generation_status(
    UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PortalArtifactsGenerationStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPortalArtifactsGenerationStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id_</code> | <code>UUID</code> | The `id` returned by **Generate Portal Artifacts Async**. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_matic_portal_artifacts_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_matic_portal_artifacts_api/core/results.py)&#91;[PortalArtifactsGenerationStatusResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_status_response.py), [GetPortalArtifactsGenerationStatusErrorBody](api_matic_portal_artifacts_api/errors/get_portal_artifacts_generation_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PortalArtifactsGenerationStatusResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_status_response.py)</code> -- Generation is in progress or has failed.

**On `Failure`**: `error` is <code>[GetPortalArtifactsGenerationStatusErrorBody](api_matic_portal_artifacts_api/errors/get_portal_artifacts_generation_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ProblemDetails](api_matic_portal_artifacts_api/models/problem_details.py)</code> |
| 401 | <code>[UnauthorizedResponse](api_matic_portal_artifacts_api/models/unauthorized_response.py)</code> |
| 500 | <code>[InternalServerErrorResponse](api_matic_portal_artifacts_api/models/internal_server_error_response.py)</code> |
| anything unmapped | <code>[RawError](api_matic_portal_artifacts_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

