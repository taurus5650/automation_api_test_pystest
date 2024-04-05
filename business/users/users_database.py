from urllib.parse import urljoin

from configurations import FakeDBConfig
from ..database_execution import DatabaseConnector


class BooksDatabase (DatabaseConnector):


    def connector(self):
        return DatabaseConnector(
            host=FakeDBConfig.HOST,
            user=FakeDBConfig.USER,
            password=FakeDBConfig.PASSWORD,
            database=FakeDBConfig.DATABASE
        )
    def get_books_id(self, id):
        mysql = f"""
        SELECT * FROM fake_user_tab WHERE %(id) ;
        """
        return self.connector().fetch_dict(mysql, fetchall=True)