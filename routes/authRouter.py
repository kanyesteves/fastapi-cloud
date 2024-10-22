from services.userService import UserService
from services.authService import AuthService
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter(prefix='/auth', tags=['Auth Endpoint'])
user_service = UserService()
auth_service = AuthService()
    
@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=auth_service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(
        data={"sub": user}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}