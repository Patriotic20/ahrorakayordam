from fastapi import HTTPException, status



class UserNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="User Not Found",
            headers={"WWW-Authenticate": "Bearer"}
        )


class CredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

class InvalidRoleException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Role",
            headers={"WWW-Authenticate": "Bearer"}
        )
