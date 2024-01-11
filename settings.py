import os

from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "djsfjfd")

print(JWT_SECRET)
