from project.api.base_api import BaseAPI
from project.utils.config import ADMIN_USER, ADMIN_PASS

class AuthAPI(BaseAPI):
    def login(self):
        # OrangeHRM demo may not expose token endpoint publicly; this is a placeholder
        # If your target has token endpoint, implement payload accordingly.
        path = '/oauth/issueToken'
        payload = {
            'client_id': ADMIN_USER,
            'client_secret': ADMIN_PASS,
            'grant_type': 'password'
        }
        resp = self.post(path, json=payload)
        if resp.status_code in (200, 201):
            return resp.json()
        return resp