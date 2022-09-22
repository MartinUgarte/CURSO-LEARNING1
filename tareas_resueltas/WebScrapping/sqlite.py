import sqlite3
from sqlite3 import Error
from novela import Novel

class SqliteStorage:

    def __init__(self, db_name):
        self.database = db_name

        sql_novels_table = """ CREATE TABLE IF NOT EXISTS novels (
                                            id integer PRIMARY KEY,
                                            URL integer,
                                            title text NOT NULL,
                                            author text,
                                            genres text,
                                            summary text,
                                            text text
                                        ); """

        # create a database connection
        conn = self.create_connection(self.database)

        # create tables
        if conn is not None:
            # create projects table
            self.create_table(conn, sql_novels_table)

        else:
            print("Error! cannot create the database connection.")
            return
        
        self.conn = conn       
    
    def close(self):
        self.conn.close()

    def add_novel(self, novel):
        novel_tuple = (novel.url, novel.title, novel.author, novel.genres, novel.summary, novel.text)
        novel_id = self.create_novel(self.conn, novel_tuple)

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def __enter__(self):
        return self
  
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.close()

    def create_novel(self, conn, novel):
        """
        Create a new novel into the novel table
        :param conn:
        :param novel:
        :return: novel id
        """
        sql = ''' INSERT INTO novels(URL,title,author,genres,summary,text)
                VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, novel)
        conn.commit()
        return cur.lastrowid

    def cursor(self):
        return self.conn.cursor()

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
