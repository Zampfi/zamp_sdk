import os
from enum import Enum

from zamp_public_workflow_sdk.actions_hub.constants import ExecutionMode as AHExecutionMode


class ExecutionMode(str, Enum):
    SYNC = "SYNC"
    ASYNC = "ASYNC"
    INLINE = "INLINE"


_SDK_TO_AH_MODE = {
    ExecutionMode.SYNC: AHExecutionMode.TEMPORAL_SYNC,
    ExecutionMode.ASYNC: AHExecutionMode.TEMPORAL_ASYNC,
    ExecutionMode.INLINE: AHExecutionMode.INLINE,
}


def resolve_execution_mode(mode: ExecutionMode | None) -> AHExecutionMode | None:
    """Map SDK execution mode to ActionsHub execution mode.

    If INSIDE_SANDBOX=true, always returns MODAL regardless of what the caller passed.
    """
    import pprint
    print("[resolve_execution_mode] environment variables:")
    pprint.pprint(dict(os.environ))

    if os.environ.get("INSIDE_SANDBOX") == "true":
        chosen = AHExecutionMode.MODAL
    elif mode is None:
        chosen = None
    else:
        chosen = _SDK_TO_AH_MODE[mode]

    print(f"[resolve_execution_mode] chosen mode: {chosen!r}")
    return chosen
