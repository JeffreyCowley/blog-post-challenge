import sqlite3
from sqlite3 import Error
import logging
import re


class BlogPostApp:

    def __init__(self):
        self.conn = None
        self.log = logging.getLogger(__name__)

    def setup_logging(self, file, level_in='WARNING', formatter='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        if not self.log.hasHandlers():
            log_handler = logging.FileHandler(file)

            level = re.match('^(CRITICAL|ERROR|WARNING|INFO|DEBUG|NOTSET)$', level_in.upper())
            if level is not None:
                self.log.setLevel(level.string)

            log_handler.setFormatter(logging.Formatter(formatter))
            self.log.addHandler(log_handler)

    def connect_database(self, file):
        """ create a database connection to the SQLite database specified by file """
        try:
            self.conn = sqlite3.connect(file)
            self.log.info(f'connected to database {file}')
        except Error as connection_error:
            self.log.error(f'{connection_error}')
            self.conn = None

    def get_all_entries(self):
        """return all entries from the database"""
        try:
            with self.conn:
                get_cursor = self.conn.cursor()
                get_cursor.execute(f"""SELECT post_id, title, body FROM posts ORDER BY post_id;""")
                result = get_cursor.fetchall();

                if result is not None:
                    for row in result:
                        self.log.debug(f'Entry: {row[0]}, Title: {row[1]}, Body: {row[2]}')
                else:
                    self.log.warning(f'No entries found.')
        except Error as get_error:
            self.log.error(f'{get_error}')

        return result

    def set_entry(self, title, body):
        """add a new entry to the database"""
        try:
            with self.conn:
                set_cursor = self.conn.cursor()
                set_cursor.execute(f"""INSERT INTO posts(title, body) values (?,?)""", (title, body))
                self.log.debug(f' Set entry = {set_cursor.lastrowid}')
                return set_cursor.lastrowid
        except Error as set_error:
            self.log.error(f'{set_error}')

        return None

    def get_entry(self, entry):
        """return the selected entry from the database"""
        try:
            with self.conn:
                get_cursor = self.conn.cursor()
                get_cursor.execute(f"""SELECT post_id, title, body FROM posts WHERE post_id =?;""", (entry,))
                result = get_cursor.fetchone()
                if result:
                    self.log.debug(f'Entry: {result[0]}, Title: {result[1]}, Body: {result[2]}')
                else:
                    self.log.warning(f'No entry matching \'{entry}\'.')
        except Error as get_error:
            self.log.error(f'{get_error}')

        return result
