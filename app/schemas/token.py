from pydantic import BaseModel
from typing import Optional

# Resposta devolvida no endpoint de Login/Refresh
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

# Dados contidos dentro do Payload do Token JWT
class TokenPayload(BaseModel):
    sub: Optional[str] = None
    type: Optional[str] = None