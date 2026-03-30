from enum import StrEnum

POLL_INITIAL_INTERVAL_SECONDS = 1.0
POLL_MAX_INTERVAL_SECONDS = 30.0
POLL_TIMEOUT_SECONDS = 600.0


class ActionStatus(StrEnum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"
    TERMINATED = "TERMINATED"
    TIMED_OUT = "TIMED_OUT"


SUCCESS_STATUSES = frozenset({ActionStatus.COMPLETED})
TERMINAL_FAILURE_STATUSES = frozenset(
    {
        ActionStatus.FAILED,
        ActionStatus.CANCELED,
        ActionStatus.TERMINATED,
        ActionStatus.TIMED_OUT,
    }
)
IN_PROGRESS_STATUSES = frozenset({ActionStatus.RUNNING})
