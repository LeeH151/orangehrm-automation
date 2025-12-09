import requests
from project.utils.config import API_BASE_URL
from project.utils.logger import logger

class BaseAPI:
    def __init__(self):
        self.base = API_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def get(self, path, params=None, headers=None):
        url = f"{self.base}{path}"
        resp = self.session.get(url, params=params, headers=headers)
        logger.info(f'GET {url} -> {resp.status_code}')
        return resp

    def post(self, path, json=None, headers=None):
        url = f"{self.base}{path}"
        resp = self.session.post(url, json=json, headers=headers)
        logger.info(f'POST {url} -> {resp.status_code}')
        return resp

    def put(self, path, json=None, headers=None):
        url = f"{self.base}{path}"
        resp = self.session.put(url, json=json, headers=headers)
        logger.info(f'PUT {url} -> {resp.status_code}')
        return resp

    def delete(self, path, headers=None):
        url = f"{self.base}{path}"
        resp = self.session.delete(url, headers=headers)
        logger.info(f'DELETE {url} -> {resp.status_code}')
        return resp