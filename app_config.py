import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:5002/getAToken")

SCOPE = ["User.Read"]

# Flask-Session config
SESSION_TYPE = "filesystem"

# Flask secret key
SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
