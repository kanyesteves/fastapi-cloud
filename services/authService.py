from fastapi.security import OAuth2PasswordBearer
from services.userService import UserService
from datetime import datetime, timedelta
from utils.libs import Libs
from jose import jwt
import secrets

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
service = UserService()
libs = Libs()

class AuthService:
    def __init__(self):
        self.lib = Libs()

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, username: str, password: str):
        user = service.getUserByName(username)
        if not user:
            return False
        if not libs.check_password(password, user.password):
            return False
        return user

        

