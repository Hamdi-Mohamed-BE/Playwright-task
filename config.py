import os
from dotenv import load_dotenv

# load env file
load_dotenv(verbose=True)

# base settings class to be shared throughout the app
class Settings:
    # --- Base section ---
    USER_ID: str = os.environ.get("USER_ID")
    PASS: str = os.environ.get("PASS")
    DEBUG: bool = bool(int(os.environ.get("DEBUG" , True)))


settings = Settings()


if __name__ == "__main__":
    print(settings.USER_ID)
    print(settings.PASS)
    print(settings.DEBUG)