from fastapi.security import OAuth2PasswordBearer
from services.userService import UserService
from datetime import datetime, timedelta
from utils.libs import Libs
from jose import jwt
import secrets

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
service = UserService()

class AuthService:
    def __init__(self):
        self.lib = Libs()
        self.SECRET_KEY = secrets.token_hex(32)
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, username: str, password: str):
        user = service.getUserByName(username)
        if not user:
            return False        
        if not self.lib.check_password(password, user.password):
            return False
        return user

        

