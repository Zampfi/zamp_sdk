# zamp_sdk

Customer-facing SDK for executing actions on the [Zamp](https://zamp.com) platform.

## Requirements

- Python >= 3.12

## Installation

```bash
pip install zamp_sdk
```

Or with Poetry:

```bash
poetry add zamp_sdk
```

## Quick Start

```python
from zamp_sdk import ActionExecutor, ExecutionMode

result = await ActionExecutor.execute(
    "my_action",
    {"key": "value"},
    execution_mode=ExecutionMode.SYNC,
)
```

## API Reference

### `ActionExecutor`

Static entry point for executing actions on the Zamp platform.

#### `ActionExecutor.execute`

```python
await ActionExecutor.execute(
    action_name: str,
    params: Any,
    *,
    summary: str | None = None,
    return_type: type | None = None,
    execution_mode: ExecutionMode | None = None,
    action_retry_policy: RetryPolicy | None = None,
    action_start_to_close_timeout: timedelta | None = None,
) -> Any
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `action_name` | `str` | Name of the action to execute. |
| `params` | `Any` | Input parameters passed to the action. |
| `summary` | `str \| None` | Optional human-readable description of the execution. |
| `return_type` | `type \| None` | Expected return type; used for deserialisation. |
| `execution_mode` | `ExecutionMode \| None` | How the action should be executed (see below). Defaults to the platform default when `None`. |
| `action_retry_policy` | `RetryPolicy \| None` | Custom retry policy for the action. |
| `action_start_to_close_timeout` | `timedelta \| None` | Maximum time allowed for the action to complete. |

### `ExecutionMode`

Controls how an action is dispatched.

| Value | Description |
|-------|-------------|
| `ExecutionMode.SYNC` | Execute synchronously via Temporal and wait for the result. |
| `ExecutionMode.ASYNC` | Dispatch asynchronously via Temporal and return immediately. |
| `ExecutionMode.INLINE` | Execute inline in the current process without Temporal. |

> **Note:** When the environment variable `INSIDE_SANDBOX=true` is set, all executions are automatically routed through `MODAL` mode regardless of the value passed to `execution_mode`.

## Examples

### Synchronous execution

```python
from zamp_sdk import ActionExecutor, ExecutionMode

result = await ActionExecutor.execute(
    "send_invoice",
    {"invoice_id": "inv_123"},
    summary="Send invoice inv_123 to customer",
    execution_mode=ExecutionMode.SYNC,
)
```

### Asynchronous execution with timeout

```python
from datetime import timedelta
from zamp_sdk import ActionExecutor, ExecutionMode

await ActionExecutor.execute(
    "generate_report",
    {"report_type": "monthly"},
    execution_mode=ExecutionMode.ASYNC,
    action_start_to_close_timeout=timedelta(minutes=10),
)
```

### Inline execution (no Temporal)

```python
from zamp_sdk import ActionExecutor, ExecutionMode

result = await ActionExecutor.execute(
    "validate_data",
    {"data": [1, 2, 3]},
    execution_mode=ExecutionMode.INLINE,
)
```

## Development

Install development dependencies:

```bash
poetry install --with dev
```

Run tests:

```bash
pytest
```

Lint and format:

```bash
ruff check .
ruff format .
```

Type-check:

```bash
mypy zamp_sdk
```

## License

MIT — see [LICENSE](LICENSE) for details.
