from dataclasses import dataclass


@dataclass
class UserAnswer:
    """
    Dataclass representing user answer with keyboard data.
    """

    text: str
    call_data: list[dict[str, str]]
    rows_size: list[int] | None
