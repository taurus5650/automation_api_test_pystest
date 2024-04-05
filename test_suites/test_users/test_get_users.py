
from http import HTTPStatus

import allure

from business.users.users_api import UsersAPI


class TestCase:
    usersAPI = UsersAPI()

    @allure.title("[P0][Positive] Valid id")
    def test_get_users_validId_p0(self):
        Id = 5
        UserName = "User 5"
        Password = "Password5"

        res = self.usersAPI.getUsers(
            id=Id
        )

        assert res.status_code == HTTPStatus.OK

        resp = res.json()
        assert resp["id"] == Id
        assert resp["userName"] == UserName
        assert resp["password"] == Password
