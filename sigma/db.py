from __future__ import annotations
from pydantic import BaseModel, Base64UrlBytes, Field
from uuid import uuid4


class Data(BaseModel):
    users: dict[str, User] = Field(default_factory=dict)


class User(BaseModel):
    name: str
    password: str
    images: list[str]
    keywords: dict[str, int] = Field(default_factory=dict)
    id: str = Field(default_factory=lambda: str(uuid4()))
