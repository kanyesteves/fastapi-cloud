from fastapi.security import OAuth2PasswordBearer
from services.userService import UserService
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from utils.libs import Libs
from jose import jwt, JWTError
import secrets

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
service = UserService()

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class AuthService:
    def __init__(self):
        self.lib = Libs()

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, username: str, password: str):
        user = service.getUserByName(username)
        if not user:
            return False        
        if not self.lib.check_password(password, user.password):
            return False
        return user

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            user = service.getUserByName(username)
            if user is None:
                raise credentials_exception
        except JWTError as e:
            print(f"Erro ao decodificar o JWT: {str(e)}")
            raise credentials_exception
        return user

        

