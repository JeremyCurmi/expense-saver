from .config import Settings
from .security import AuthManager

settings = Settings()
auth = AuthManager(settings.ACCESS_TOKEN_EXPIRE_MINUTES,
                   settings.SECRET_KEY
                   )