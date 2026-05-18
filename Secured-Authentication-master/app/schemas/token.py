from pydantic import BaseModel, SecretStr


class TokenRefreshRequest(BaseModel):
    refresh_token: SecretStr


class TokenExchangeResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class StandardActionResponse(BaseModel):
    detail: str
