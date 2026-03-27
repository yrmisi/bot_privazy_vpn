from .base import BotBaseError


class UserNotFoundError(BotBaseError):
    """Bot user not found"""

    def __init__(self, message: str = "User not found, message sent on behalf of the chat") -> None:
        self.message = message
        super().__init__(self.message)
