from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, SecretStr


class UserCreate(BaseModel):
    email: EmailStr
    password: SecretStr = Field(min_length=8, max_length=128)


class UserRegistrationResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    is_superuser: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }
