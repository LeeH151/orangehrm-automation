from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

load_dotenv(dotenv_path=env_path)

BASE_URL = os.getenv("BASE_URL")
ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")
API_BASE_URL = "http://localhost:8000"
HEADLESS = os.getenv("HEADLESS", "False").lower() in ("true", "1", "yes")


