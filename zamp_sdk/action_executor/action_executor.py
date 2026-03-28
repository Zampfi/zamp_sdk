from datetime import timedelta
from typing import Any

from zamp_public_workflow_sdk.actions_hub import ActionsHub
from zamp_public_workflow_sdk.actions_hub.models.core_models import RetryPolicy

from zamp_sdk.action_executor.execution_mode import ExecutionMode, resolve_execution_mode


class ActionExecutor:
    """Static entry point for executing actions via the Zamp platform.

    Usage:
        result = await ActionExecutor.execute("action_name", params)
    """

    @staticmethod
    async def execute(
        action_name: str,
        params: Any,
        *,
        summary: str | None = None,
        return_type: type | None = None,
        execution_mode: ExecutionMode | None = None,
        action_retry_policy: RetryPolicy | None = None,
        action_start_to_close_timeout: timedelta | None = None,
    ) -> Any:
        ah_mode = resolve_execution_mode(execution_mode)
        return await ActionsHub.execute_action(
            action_name,
            params,
            summary=summary,
            return_type=return_type,
            inject_zamp_metadata_context=True,
            execution_mode=ah_mode,
            action_retry_policy=action_retry_policy,
            action_start_to_close_timeout=action_start_to_close_timeout,
        )
