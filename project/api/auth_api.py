'''
import requests
from project.utils.config import API_BASE, ADMIN_USER, ADMIN_PASS

class AuthAPI:
    """Authentication helper"""
    def get_token(self):
        payload = {
            "client_id": ADMIN_USER,
            "client_secret": ADMIN_PASS,
            "grant_type": "password"
        }
        response = requests.post(f"{API_BASE}/oauth/issueToken", json=payload)
        if response.status_code == 200:
            return response.json().get("access_token")
        else:
            raise Exception(f"Login failed: {response.status_code} - {response.text}")
'''
import requests
from project.utils.config import API_BASE, CLIENT_ID, CLIENT_SECRET, ADMIN_USER, ADMIN_PASS

class AuthAPI:
    def get_token(self):
        """
        Lấy access token từ OAuth client (demo online)
        """
        url = f"{API_BASE}/oauth/issueToken"
        payload = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "password",
            "username": ADMIN_USER,
            "password": ADMIN_PASS
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            token = response.json().get("access_token")
            return token
        else:
            raise Exception(f"Login failed: {response.status_code} - {response.text}")
