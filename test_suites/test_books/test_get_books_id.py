from http import HTTPStatus

import allure

from business.books.books_api import BooksAPI
from logger import Logger


class TestCase:
    logger = Logger.setup_logger()
    booksAPI = BooksAPI()


    @allure.title("[P0][Negative] Invalid id")
    def test_get_books_validId_p0(self):
        Id = 5
        Title = "Book 5"
        Description = "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n"
        PageCount = 500

        res = self.booksAPI.books_id(
            id=Id,
        )

        assert res.status_code == HTTPStatus.OK

        resp = res.json()
        assert resp["id"] == Id
        assert resp["title"] == Title
        assert resp["description"] == Description
        assert resp["pageCount"] == PageCount

    @allure.title("[P3][Negative] Without symbol hash ")
    def test_get_books_url_withHash_p3(self):
        Id = "#"
        ExpectedId = [1, 2, 3, 4, 5]
        ExpectedTitle = ["Book 1", "Book 2", "Book 3", "Book 4", "Book 5"]
        PauseId = 5


        res = self.booksAPI.books_id(
            id=Id,
        )

        assert res.status_code == HTTPStatus.OK

        resp = res.json()

        for idx, resp_result in enumerate(resp):
            self.logger.debug(f"DebugId: {resp_result['id']}")
            assert resp_result['id'] == ExpectedId[idx]
            assert resp_result['title'] == ExpectedTitle[idx]
            if resp_result['id'] == PauseId:
                break