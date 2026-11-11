from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate

router = APIRouter()

class RoleChecker:
    """Classe para validar se o utilizador possui o papel (role) necessário."""
    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: User = Depends(deps.get_current_user)):
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Acesso negado. Permissão insuficiente."
            )

# Instância de verificação para rotas exclusivas de Admin
allow_admin = RoleChecker(["admin"])

@router.get("/me", response_model=UserResponse)
def read_user_me(current_user: User = Depends(deps.get_current_user)):
    """Retorna os dados do utilizador autenticado."""
    return current_user

@router.get("/", response_model=List[UserResponse], dependencies=[Depends(allow_admin)])
def read_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(deps.get_db)
):
    """Lista todos os utilizadores (Acesso exclusivo para Admin)."""
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.put("/{user_id}", response_model=UserResponse, dependencies=[Depends(allow_admin)])
def update_user(
    user_id: int,
    user_in: UserUpdate,
    db: Session = Depends(deps.get_db)
):
    """Atualiza dados e papel de um utilizador (Acesso exclusivo para Admin)."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilizador não encontrado."
        )
    
    update_data = user_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)
        
    db.commit()
    db.refresh(user)
    return user