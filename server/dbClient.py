import sqlite3;

class DataCursor:
    def __init__(self, connection: sqlite3.Connection):
        self._cursor = connection.cursor()
        self._transaction = 0
        
class DatabaseClient:
    def __init__(self, path):
        self._connection = sqlite3.connect(path)
