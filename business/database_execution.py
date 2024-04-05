import mysql.connector


class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, data=None):
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_dict(self, query, fetchall=True):
        self.cursor.execute(query)
        columns = [col[0] for col in self.cursor.description]
        if fetchall:
            result = self.cursor.fetchall()
            return [dict(zip(columns, row)) for row in result]
        else:
            result = self.cursor.fetchone()
            return dict(zip(columns, result)) if result else None

    def close_connecor(self):
        self.cursor.close()
        self.connection.close()