import sqlite3
from .migration import update_database

class DataCursor:
    def __init__(self, connection: sqlite3.Connection):
        self._cursor = connection.cursor()
        self._in_transaction = False
        self._active = False

    def __enter__(self):
        self._active = True
        return self
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if (self._in_transaction):
            if (exc_type is not None):
                self.rollback()
            else:
                self.commit()
        self._active = False

    def _check_state(self):
        if not self._active:
            raise IOError('Not active')

    def begin_transaction(self):
        self._check_state()
        if self._in_transaction:
            return
        self._cursor.execute('BEGIN TRANSACTION;')
        self._in_transaction = False        

    def commit(self):
        self._check_state()
        if not self._in_transaction:
            return
        self._cursor.execute('COMMIT;')
        self._in_transaction = False        

    def rollback(self):
        self._check_state()
        if not self._in_transaction:
            return
        self._cursor.execute('ROLLBACK;')
        self._in_transaction = False        
        
    def select(self, table, columns:list[str], where:str|None=None, order:list[str]|None=None, args:dict|None=None, max_rows:int|None=None, skip_rows:int|None=None):
        self._check_state()
        SQL = f"SELECT {', '.join(columns)} FROM {table}"
        if where is not None:
            SQL = f"{SQL} WHERE {where}"
        if order is not None:
            SQL = f"{SQL} ORDER BY {', '.join(order)}"

        if max_rows is not None:
            SQL = f"{SQL} LIMIT {max_rows}"
        if skip_rows is not None:
            SQL = f"{SQL} OFFSET {skip_rows}"
 
        print(SQL)

        result = self._cursor.execute(SQL) if args is None else self._cursor.execute(SQL, args).fetchall()

        def arr_to_dict(arr):
            d = {}
            for i in range(len(columns)):
                d[columns[i]] = arr[i]
            return d

        return [arr_to_dict(r) for r in result]

    def select_single(self, table:str, columns:list[str], where:str|None=None, order:list[str]|None=None, args:dict|None=None):
        result = self.select(table,columns,where,order,args,1)
        if len(result) != 1:
            return None
        return result[0]

class DatabaseClient:
    def __init__(self, path):
        self._connection = sqlite3.connect(path)
    def get_cursor(self):
        return DataCursor(self._connection)


db_name=None
def innitialise_database(settings):
    #update_database(settings)
    global db_name
    db_name = "development.db"  #settings['databaseName']

def get_cursor():
    db = DatabaseClient(db_name)
    return db.get_cursor()