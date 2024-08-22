# pip install python-dotenv
from dotenv import load_dotenv
import os
import pytest


def test_auth():
    load_dotenv()
    #username="admin"
    #password="password123"
    username: str | None = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    print(username, password)
