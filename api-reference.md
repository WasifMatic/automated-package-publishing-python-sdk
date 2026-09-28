# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [ApiMaticPortalArtifactsApiClient](api_matic_portal_artifacts_api/client.py)

## PortalArtifactsGenerationAsync

> Source: [PortalArtifactsGenerationAsync](api_matic_portal_artifacts_api/apis/portal_artifacts_generation_async.py)

<details>
<summary><code>def download_generated_portal_artifacts(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.portal_artifacts_generation_async.download_generated_portal_artifacts(
        UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadGeneratedPortalArtifactsErrorBody
```

**Async**

```python
try:
    await async_client.portal_artifacts_generation_async.download_generated_portal_artifacts(
        UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadGeneratedPortalArtifactsErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](api_matic_portal_artifacts_api/core/exceptions.py)&#91;[DownloadGeneratedPortalArtifactsErrorBody](api_matic_portal_artifacts_api/errors/download_generated_portal_artifacts_error.py)&#93;</code>

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
<summary><code>def download_portal_artifacts_build_file(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.portal_artifacts_generation_async.download_portal_artifacts_build_file(
        UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadPortalArtifactsBuildFileErrorBody
```

**Async**

```python
try:
    await async_client.portal_artifacts_generation_async.download_portal_artifacts_build_file(
        UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadPortalArtifactsBuildFileErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](api_matic_portal_artifacts_api/core/exceptions.py)&#91;[DownloadPortalArtifactsBuildFileErrorBody](api_matic_portal_artifacts_api/errors/download_portal_artifacts_build_file_error.py)&#93;</code>

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
<summary><code>def generate_portal_artifacts_async(file: FileInput, *, x_api_matic_callback_url: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PortalArtifactsGenerationAsyncResponse</code></summary>

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
try:
    response = client.portal_artifacts_generation_async.generate_portal_artifacts_async(
        Path("path/to/file.bin"), x_api_matic_callback_url="https://example.com/portal-artifacts-callback"
    )
    # TODO: Handle 'response' of type PortalArtifactsGenerationAsyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePortalArtifactsAsyncErrorBody
```

**Async**

```python
try:
    response = await async_client.portal_artifacts_generation_async.generate_portal_artifacts_async(
        Path("path/to/file.bin"), x_api_matic_callback_url="https://example.com/portal-artifacts-callback"
    )
    # TODO: Handle 'response' of type PortalArtifactsGenerationAsyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePortalArtifactsAsyncErrorBody
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

**OnSuccess**: <code>[PortalArtifactsGenerationAsyncResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_async_response.py)</code> -- Generation request accepted. Use the returned links to check the status and download the artifacts.

**OnError**: <code>[ApiError](api_matic_portal_artifacts_api/core/exceptions.py)&#91;[GeneratePortalArtifactsAsyncErrorBody](api_matic_portal_artifacts_api/errors/generate_portal_artifacts_async_error.py)&#93;</code>

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
<summary><code>def get_portal_artifacts_generation_status(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> PortalArtifactsGenerationStatusResponse</code></summary>

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
try:
    response = client.portal_artifacts_generation_async.get_portal_artifacts_generation_status(
        UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
    )
    # TODO: Handle 'response' of type PortalArtifactsGenerationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPortalArtifactsGenerationStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.portal_artifacts_generation_async.get_portal_artifacts_generation_status(
        UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
    )
    # TODO: Handle 'response' of type PortalArtifactsGenerationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPortalArtifactsGenerationStatusErrorBody
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

**OnSuccess**: <code>[PortalArtifactsGenerationStatusResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_status_response.py)</code> -- Generation is in progress or has failed.

**OnError**: <code>[ApiError](api_matic_portal_artifacts_api/core/exceptions.py)&#91;[GetPortalArtifactsGenerationStatusErrorBody](api_matic_portal_artifacts_api/errors/get_portal_artifacts_generation_status_error.py)&#93;</code>

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
<summary><code>def download_portal_artifacts_build_file(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.internal.download_portal_artifacts_build_file(UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadPortalArtifactsBuildFileErrorBody
```

**Async**

```python
try:
    await async_client.internal.download_portal_artifacts_build_file(UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadPortalArtifactsBuildFileErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](api_matic_portal_artifacts_api/core/exceptions.py)&#91;[DownloadPortalArtifactsBuildFileErrorBody](api_matic_portal_artifacts_api/errors/download_portal_artifacts_build_file_error.py)&#93;</code>

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
<summary><code>def download_generated_portal_artifacts(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.public.download_generated_portal_artifacts(UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadGeneratedPortalArtifactsErrorBody
```

**Async**

```python
try:
    await async_client.public.download_generated_portal_artifacts(UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47"))
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadGeneratedPortalArtifactsErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](api_matic_portal_artifacts_api/core/exceptions.py)&#91;[DownloadGeneratedPortalArtifactsErrorBody](api_matic_portal_artifacts_api/errors/download_generated_portal_artifacts_error.py)&#93;</code>

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
<summary><code>def generate_portal_artifacts_async(file: FileInput, *, x_api_matic_callback_url: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PortalArtifactsGenerationAsyncResponse</code></summary>

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
try:
    response = client.public.generate_portal_artifacts_async(
        Path("path/to/file.bin"), x_api_matic_callback_url="https://example.com/portal-artifacts-callback"
    )
    # TODO: Handle 'response' of type PortalArtifactsGenerationAsyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePortalArtifactsAsyncErrorBody
```

**Async**

```python
try:
    response = await async_client.public.generate_portal_artifacts_async(
        Path("path/to/file.bin"), x_api_matic_callback_url="https://example.com/portal-artifacts-callback"
    )
    # TODO: Handle 'response' of type PortalArtifactsGenerationAsyncResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePortalArtifactsAsyncErrorBody
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

**OnSuccess**: <code>[PortalArtifactsGenerationAsyncResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_async_response.py)</code> -- Generation request accepted. Use the returned links to check the status and download the artifacts.

**OnError**: <code>[ApiError](api_matic_portal_artifacts_api/core/exceptions.py)&#91;[GeneratePortalArtifactsAsyncErrorBody](api_matic_portal_artifacts_api/errors/generate_portal_artifacts_async_error.py)&#93;</code>

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
<summary><code>def get_portal_artifacts_generation_status(id_: UUID, *, request_options: RequestOptionsOrDict | None = None) -> PortalArtifactsGenerationStatusResponse</code></summary>

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
try:
    response = client.public.get_portal_artifacts_generation_status(UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47"))
    # TODO: Handle 'response' of type PortalArtifactsGenerationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPortalArtifactsGenerationStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.public.get_portal_artifacts_generation_status(
        UUID("019992a4-5c3e-7b21-9f0a-3d6e8c1b2a47")
    )
    # TODO: Handle 'response' of type PortalArtifactsGenerationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPortalArtifactsGenerationStatusErrorBody
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

**OnSuccess**: <code>[PortalArtifactsGenerationStatusResponse](api_matic_portal_artifacts_api/models/portal_artifacts_generation_status_response.py)</code> -- Generation is in progress or has failed.

**OnError**: <code>[ApiError](api_matic_portal_artifacts_api/core/exceptions.py)&#91;[GetPortalArtifactsGenerationStatusErrorBody](api_matic_portal_artifacts_api/errors/get_portal_artifacts_generation_status_error.py)&#93;</code>

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

