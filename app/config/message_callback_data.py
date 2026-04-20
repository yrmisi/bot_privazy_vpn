from pydantic import BaseModel


class MessageCallbackConfig(BaseModel):
    """Message and callback data config for user."""

    key_unauth_text: str = "hello_unauth_user_text"
    key_unauth_call_data: str = "hello_unauth_user_call_data"
    unauth_rows_size: list[int] = [1]

    key_auth_text: str = "hello_auth_user_text"
    key_auth_call_data: str = "hello_auth_user_call_data"
    auth_rows_size: list[int] = [1, 2, 2, 1]

    key_echo_text: str = "message_echo"
