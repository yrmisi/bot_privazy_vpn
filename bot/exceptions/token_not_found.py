from .base import BotBaseError


class TokenNotFound(BotBaseError):
    """Token not found."""

    def __init__(self, message: str = "Bot token not found in env file") -> None:
        self.message = message
        super().__init__(self.message)
