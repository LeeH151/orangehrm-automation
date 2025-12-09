import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost/orangehrm-5.8/web/index.php")
TIMEOUT = int(os.getenv("TIMEOUT", 60000))
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
DELAY_MS = int(os.getenv("DELAY_MS", 1000))  # default 1 giây
