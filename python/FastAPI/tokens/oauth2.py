from jose import JWTError, jwt
from settings import keys, config
from datetime import UTC, datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(tz=UTC) + timedelta(minutes=keys.ACCESS_TOKEN_TIME)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, keys.AUTH_KEY, algorithm=keys.ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, keys.AUTH_KEY, algorithms=keys.ALGORITHM)
        id = payload.get("user_id")

        if id is None:
            raise credential_exception
        token_data = config.TokenData(id = id)

    except JWTError:
        raise credential_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
                                        status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail = "Could not validate credentials",
                                        headers={"WWW-Authenticate": "Bearer"}
                                        )

    return verify_access_token(token, credential_exception)
