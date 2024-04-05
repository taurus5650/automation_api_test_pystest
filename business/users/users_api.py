from urllib.parse import urljoin

from configurations import FakeRestAPIConfig
from ..api_request import APIRequest


class UsersAPI (APIRequest):
    BASE_URL = FakeRestAPIConfig.URL

    USERS = "/api/v1/Users"

    def __init__(self, waitingTime=5):
        super().__init__(waiting_time=waitingTime)

    def postUsers(self, id: int, userName: str, password: str):
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json; v=1.0"
        }
        body = {
            "id": id,
            "userName": userName,
            "password": password
        }
        return self._send_request(
            method="POST",
            url=urljoin(self.BASE_URL, self.USERS),
            headers=headers,
            json=body
        )

    def getUsers(self, id: int):

        return self._send_request(
            method="GET",
            url=urljoin(self.BASE_URL, self.USERS + f"/{id}"),
        )