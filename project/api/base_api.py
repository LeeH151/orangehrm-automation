'''import requests
from project.utils.config import API_BASE

class BaseAPI:
    """API helper base class"""
    def __init__(self):
        self.base_url = API_BASE
        self.headers = {
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}", headers=self.headers)

    def post(self, endpoint, payload):
        return requests.post(f"{self.base_url}{endpoint}", json=payload, headers=self.headers)

    def put(self, endpoint, payload):
        return requests.put(f"{self.base_url}{endpoint}", json=payload, headers=self.headers)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)
'''
import requests
from project.utils.config import API_BASE

class BaseAPI:
    def __init__(self, token=None):
        self.base_url = f"{API_BASE}/api/v2"
        self.headers = {
            "Content-Type": "application/json"
        }
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}", headers=self.headers)

    def post(self, endpoint, payload):
        return requests.post(f"{self.base_url}{endpoint}", json=payload, headers=self.headers)

    def put(self, endpoint, payload):
        return requests.put(f"{self.base_url}{endpoint}", json=payload, headers=self.headers)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)

    # ✅ Helper lấy danh sách nhân viên
    def get_employees(self):
        res = self.get("/pim/employees")
        if res.status_code == 200:
            data = res.json().get("data", [])
            return data
        else:
            raise Exception(f"Failed to get employees: {res.status_code} - {res.text}")
