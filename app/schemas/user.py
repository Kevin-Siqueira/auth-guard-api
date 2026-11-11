from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Propriedades comuns compartilhadas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: Optional[str] = "user"
    is_active: Optional[bool] = True

# Schema para criação de utilizador (requer palavra-passe)
class UserCreate(UserBase):
    password: str

# Schema para atualização de dados do utilizador
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

# Schema de resposta da API (não expõe o hash da palavra-passe)
class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True